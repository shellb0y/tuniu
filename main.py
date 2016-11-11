# -*- coding: utf-8 -*-

# import adsl
import service
import app_conf
import log_ex as logger
import requests
import json
import traceback
from time import ctime, sleep

# adsl_service = adsl.Adsl({"name": u"宽带连接",
#                        "username": "057474432953",
#                        "password": "734206"})
# adsl_service.set_adsl()

PLACEORDERINTERVAL = 30

while True:
    partner_order_id = ''
    order_id = ''

    try:
        logger.info('-----------------------')
        logger.info('get tuniu account')
        req = requests.get(app_conf.get_account_tuniu)
        if req.status_code == 200:
            account = req.json()
            logger.debug('account:%s' % json.dumps(account))
            trainService = service.TrainOrderService(json.loads(account['data']), account['id'])

            logger.info('get train data from %s' % app_conf.get_train_order)
            req = requests.get(app_conf.get_train_order)
            resp = req.json()
            logger.debug('response:%s' % resp)

            partner_order_id = resp['order_id']

            logger.info('save train data')
            req = requests.post(app_conf.save_order, data=json.dumps(resp),
                                headers={'Content-Type': 'application/json'})
            order_id = req.text

            if order_id and req.status_code == 200:
                logger.info('save order success')
            else:
                logger.error('save order faild,exit')
                sleep(PLACEORDERINTERVAL)
                continue

            logger.info('prepare the orders data')

            if resp['zw_name'] == u'二等座':
                seatName = u'二等'
            elif resp['zw_name'] == u'一等座':
                seatName = u'一等'
            elif resp['zw_name'] == u'特等座':
                seatName = u'特等'
            elif resp['zw_name'] == u'商务座':
                seatName = u'商务'
            else:
                seatName = resp['zw_name']

            data = {
                'from': resp['from_station'], 'to': resp['to_station'],
                'depart_date': resp['train_date'].replace('00:00:00', ''), 'price': resp['ticket_price'],
                'seatName': seatName,
                'train_number': resp['checi'], 'phone': json.loads(account['data'])['username'],
                'touristList': [
                    {"birthday": resp['passport_se_no'][6:10] + '-' + resp['passport_se_no'][10:12] + '-'
                                 + resp['passport_se_no'][12:14],
                     "name": resp['passenger_name'], "psptId": resp['passport_se_no'], "psptType": 1,
                     "isAdult": 1,
                     "sex": 1}], 'promotionList': []  # '126246' int(resp['passport_se_no'][-2]) % 2
            }

            logger.debug("READY:%s" % data)
            resp = trainService.place_order(data, partner_order_id, [176, 198])
            logger.info('ALL SUCCESS.')

            # logger.info('partner callback 1# begin.')
            # req = requests.get(app_conf.train_order_callback % (partner_order_id, 'true'))
            # resp = req.json()
            # logger.info(resp)

            logger.info('mobilepay callback')
            req = requests.put(app_conf.set_order_status % (order_id, u'下单成功'), data=json.dumps(resp),
                               headers={'Content-Type': 'application/json'})
            logger.info(req.text)

            sleep(PLACEORDERINTERVAL)
        elif req.status_code == 204:
            logger.error('not more tuniu account,sleep 5m')
            sleep(PLACEORDERINTERVAL)
            continue
        else:
            logger.error('get tuniu account falid')
            sleep(PLACEORDERINTERVAL)
            continue

    except Exception, e:
        logger.error(traceback.format_exc())
        if partner_order_id:
            logger.info('partner callback 1# begin.')
            req = requests.get(app_conf.train_order_callback % (partner_order_id, 'false'))
            resp = req.json()
            logger.info(resp)

        if order_id:
            logger.info('mobilepay callback 2#')
            req = requests.put(app_conf.set_order_status % (order_id, u'下单失败'),
                               data=json.dumps({'error': traceback.format_exc()}),
                               headers={'Content-Type': 'application/json'})
            logger.info(req.text)

        sleep(PLACEORDERINTERVAL)
        continue

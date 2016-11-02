# -*- coding: utf-8 -*-

# import adsl
import service
import app_conf
import log_ex as logger
import requests
import json
import traceback
import time

# adsl_service = adsl.Adsl({"name": u"宽带连接",
#                        "username": "057474432953",
#                        "password": "734206"})
# adsl_service.set_adsl()


try:
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
        req = requests.post(app_conf.save_order, data=resp, headers={'Content-Type': 'application/json'})
        order_id = req.text

        if order_id:
            logger.info('save order success')
        else:
            logger.error('save order faild,exit')
            exit()

        logger.info('prepare the orders data')
        data = {
            'from': resp['from_station'], 'to': resp['to_station'],
            'depart_date': resp['train_date'].replace('00:00:00', ''), 'price': resp['ticket_price'], 'seatName': u'二等',
            'train_number': resp['checi'], 'phone': account['userid'],
            'touristList': [
                {"birthday": resp['passport_se_no'][6:10] + '-' + resp['passport_se_no'][10:12] + '-' + resp['passport_se_no'][12:14],
                 "name": resp['passenger_name'], "psptId": resp['passport_se_no'], "psptType": 1,
                 "isAdult": 1,
                 "sex": int(resp['passport_se_no'][-2]) % 2}], 'promotionList': []  # '126246'
        }
        # TODO:支付
        logger.debug("READY:%s",data)
        resp = trainService.place_order(data, [194, 176])
        if resp['success']:
            logger.info('place order success')
        else:
            logger.error('place order faild,callback')

    elif req.status_code == 204:
        logger.error('not more tuniu account,sleep 5m')
        exit()
    else:
        logger.error('get tuniu account falid')
        exit()


except Exception, e:
    logger.error(traceback.format_exc())
    exit()

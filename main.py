# -*- coding: utf-8 -*-

import adsl
import service
import base_data
import log_ex as logger
import requests
import json
import traceback
import time
from time import ctime, sleep
import redis

<<<<<<< HEAD
adsl_service = adsl.Adsl({"name": u"宽带连接".encode("gbk"),
                        "username": "057474432953",
                        "password": "734206"})
=======
# adsl_service = adsl.Adsl({"name": u"宽带连接".encode("gbk"),
#                        "username": "057474432953",
#                        "password": "734206"})
>>>>>>> 985815ee27411dc0a3ff3abe430a16a5e224139f

PLACEORDERINTERVAL = 20
FAILDWAITING = 180

pool = redis.ConnectionPool(host='139.199.65.115', port=6379, db=1, password='melodicdeath')
r = redis.Redis(connection_pool=pool)

while True:
    partner_order_id = ''
    order_id = ''
    currentHour = int(time.strftime('%H',time.localtime(time.time())))

    if currentHour > 22 or currentHour < 7:
        print 'sleep one hour'
        sleep(3600)
        continue
    try:
        logger.info('-----------------------')
        logger.info('get train data from %s' % base_data.get_train_order)
        req = requests.get(base_data.get_train_order)
        resp = ''
        try:
            resp = req.json()
        except Exception, e:
            print req.text
            logger.error('get train data error')
            sleep(5)
            continue

        logger.debug('response:%s' % resp)
        partner_order_id = resp['order_id']

        while True:
            logger.info('save train data')
            resp['pay_channel'] = base_data.payChannel
            resp['target'] = 'tn'
            req = requests.post(base_data.save_order, data=json.dumps(resp),
                                headers={'Content-Type': 'application/json'})
            order_id = req.text

            if order_id and req.status_code == 200:
                logger.info('save order success')
                break
            else:
                logger.error('save order faild,exit')
                sleep(FAILDWAITING)
                continue

        while True:
            logger.info('get tuniu account')
            req = requests.get(base_data.get_account_tuniu)
            if req.status_code == 200:
                account = req.json()
                logger.debug('account:%s' % json.dumps(account))
                break
            elif req.status_code == 204:
                logger.error('not more tuniu account')
                sleep(FAILDWAITING)
                continue
            else:
                logger.error('get tuniu account falid')
                sleep(FAILDWAITING)
                continue

        # adsl_service.reconnect()
        trainService = service.TrainOrderService(json.loads(account['data']), account['id'])
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
        resp = trainService.place_order(data, partner_order_id, [])  # [210]

        # logger.info('partner callback 1# begin.')
        # req = requests.get(base_data.train_order_callback % (partner_order_id, 'true'))
        # resp = req.json()
        # logger.info(resp)

        logger.info('mobilepay callback')
        req = requests.put(base_data.set_order_status % (order_id, u'下单成功'), data=json.dumps(resp),
                           headers={'Content-Type': 'application/json'})
        logger.info(req.text)

        logger.info('put account ordercount')
        req = requests.put(base_data.put_account_ordercount % account['id'])
        logger.info(req.text)

        if base_data.payChannel == 8:
            logger.info('get pc cookie')
            cookie = r.get(account['id'])
            if cookie:
                logger.info('from redis')
            else:
                try:
                    data = requests.get(
                        'http://115.29.79.63:9001/api/Cookie/Get?username=%s&password=%s&bizOrderId=%s&tnOrderId=%s' % (
                            resp['account']['username'], resp['account']['password'], resp['bizOrderId'],
                            resp['tuniu_orderId']
                        ), timeout=10)

                    data = data.json()
                    logger.info('success')

                    if data['Status']:
                        cookie = data['Cookie']
                        r.set(account['id'], cookie)
                        r.expire(account['id'], 4 * 60 * 60)
                    else:
                        if '错误' in data['Message']:
                            logger.info('account cant use,send to server')
                            resp = requests.put(base_data.put_aacount_cantuse % account['id'])
                            logger.info(resp.text)

                except Exception, e:
                    logger.error(e.message)

            req = requests.post(
                'http://op.yikao666.cn/JDTrainOpen/CallBackForTNLock',
                'tnOrderno=%s&userName=%s&password=%s&sessionid=%s&order_id=%s&success=%s&amount=%s&cookie=%s&m_cookie=%s' % (
                    resp['bizOrderId'], resp['account']['username'], resp['account']['password'],
                    resp['account']['sessionid'] + ',' + str(resp['account']['userid']),
                    partner_order_id, 'true', resp['price'], cookie, resp['cookie']),
                headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'})  # account['cookie']
            logger.info(req.text)
<<<<<<< HEAD
=======
        logger.info('ALL SUCCESS.')
        sleep(PLACEORDERINTERVAL)
>>>>>>> 985815ee27411dc0a3ff3abe430a16a5e224139f

    except Exception, e:
        logger.error(traceback.format_exc())
        if order_id:
            logger.info('mobilepay callback 1#')
            try:
                req = requests.put(base_data.set_order_status % (order_id, u'下单失败'),
                                   data=json.dumps({'error': traceback.format_exc()}),
                                   headers={'Content-Type': 'application/json'})
                logger.info(req.text)
            except Exception, e:
                logger.error('mobilepay callback faild')
                sleep(FAILDWAITING)

        if partner_order_id:
            logger.info('partner callback 2# begin.')
            try:
                if base_data.payChannel == 8:
                    req = requests.get(
                        'http://op.yikao666.cn/JDTrainOpen/CallBackForTNLock?order_id=%s&success=false&msg=%s' % (
                            partner_order_id, e.message))
                    logger.info(req.text)
                else:
                    req = requests.get(base_data.train_order_callback % (partner_order_id, 'false', e.message))
                    resp = req.text
                    logger.info(resp)
            except Exception, e:
                logger.error('partner callback faild')
                sleep(FAILDWAITING)

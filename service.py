# -*- coding: utf-8 -*-

import http_handler
import base_data
import json
import log_ex as logger
import requests
import uuid
import datetime
import random
import time
import base64


class TrainOrderService:
    def __init__(self, account, acountid):
        self.partner = base_data.get_partner()
        self.cc = base_data.get_cc()
        self.account = account
        self.accountid= acountid

        logger.info('check session by get user id %s' % account)

        if not account.has_key('sessionid') or not account['sessionid']:
            logger.info('need login')
            self.login()
        account['userid'] = self.get_user_id()
        logger.info('update account data')
        req = requests.put(base_data.put_account % acountid, data=json.dumps(account),
                           headers={'Content-Type': 'application/json'})
        logger.debug('put %s %s' % (req.url, account))
        logger.debug('resp:%s' % req.text)

        if req.text == '1':
            logger.info('update account success')
        else:
            raise ValueError('update account faild')

    def login(self):
        logger.info('login starting...\n1#.get session id')
        begin_session_resp = http_handler.login.begin_session(self.partner, self.cc)
        logger.info('begin session resp:%s' % begin_session_resp)

        if begin_session_resp['success']:
            self.account['sessionid'] = begin_session_resp['data']['sessionId']
            logger.info('get session id success,the id is %s' % self.account['sessionid'])

            logger.info('#2.login')
            login_resp = http_handler.login.login(self.account['sessionid'], self.account['username'],
                                                  self.account['password'], self.partner, self.cc)
            logger.debug('login resp:%s' % login_resp)
            if login_resp['success']:
                logger.info('login success,the sessionid is %s' % self.account['sessionid'])
                return self.account['sessionid']
            else:
                err = '2#.login faild'

                logger.info('account cant use,send to server')
                resp = requests.put(base_data.put_aacount_cantuse % self.accountid)
                logger.info(resp.text)

                logger.error(err)
                raise ValueError(err)
        else:
            err = 'get session id faild'
            logger.error(err)
            raise ValueError(err)

    def get_user_id(self):
        logger.info('get user id starting...')
        resp = http_handler.account.account_info(self.account['sessionid'], self.partner)
        logger.debug('account info:%s' % resp)
        if (resp['success']):
            logger.info('get user id %s' % resp['data']['userProfile']['userId'])
            self.account['userid'] = int(resp['data']['userProfile']['userId'])
            return self.account['userid']
        else:
            err = 'get user id faild'
            logger.error(err)
            raise ValueError(err)

    def get_coupon(self, coupon_id):
        logger.info('looking for coupon %d\n1#.' % coupon_id)
        get_coupon_list_resp = http_handler.coupon.get_coupon_list()
        if get_coupon_list_resp['success']:
            list = filter(lambda c: c['id'] == str(coupon_id), get_coupon_list_resp['data']['list'])
            if list:
                mark = list[0]['mark']
                logger.info('''looking for coupon %d success,the mark is %s.\n2#.get coupon %d''' % (
                    coupon_id, mark, coupon_id))
                get_special_coupon_resp = http_handler.coupon.get_special_coupon(
                    1 and self.account['userid'] or self.get_user_id(),
                    self.account['sessionid'], mark)
                logger.debug('get special coupon resp: %s' % get_special_coupon_resp)
                if get_special_coupon_resp['success']:
                    logger.info('get coupon %d success' % coupon_id)
                    return True
                else:
                    logger.warn('get coupon %d falid' % coupon_id)
                    return False

            else:
                logger.warn('find coupon %d faild' % coupon_id)

    def __lookup_coupon(self, data):
        logger.info('looking for trainticket order coupon that can use ')
        train_order_coupon_resp = http_handler.account.get_account_train_order_can_use_coupon({
            'trainNumber': data['train_number'], 'startStationName': data['from'], 'arrivalStationName': data['to'],
            'departureCityCode': '200',
            'departDate': data['depart_date'], 'adultPrice': data['price']
        }, self.account['sessionid'], self.partner, self.cc)
        # logger.debug('train order coupon resp:%s' % train_order_coupon_resp)

        if train_order_coupon_resp['success'] and train_order_coupon_resp['data']['sortData']:
            coupon = train_order_coupon_resp['data']['sortData'][0]
                #random.randint(0, len(train_order_coupon_resp['data']['sortData'])) - 1]
            logger.info('find it.use %s' % coupon['number'])
            data['promotionList'].append(coupon['number'])
            data['price'] -= coupon['reduction']

            return True
        else:
            logger.error('trainticket order coupon not found')
            return False

    def place_order(self, data, partner_order_id, coupons):
        if coupons:
            if not self.__lookup_coupon(data):
                for id in coupons:
                    self.get_coupon(id)
                self.__lookup_coupon(data)

        logger.info('READY:%s' % data)
        resp = http_handler.train_order.add_order(self.account['sessionid'], self.partner, self.cc, data)
        logger.debug('add order response:%s' % resp)

        if resp['success']:
            termId = str(uuid.uuid1())
            pay_data = {'bizOrderId': resp['data']['orderId'], 'price': data['price']}
            logger.info('add order success.id:%s.submiting...' % pay_data['bizOrderId'])

            resp = http_handler.pay.submit(
                {'userId': self.account['userid'], 'orderId': pay_data['bizOrderId'], 'price': pay_data['price'],
                 'sessionId': self.account['sessionid'],
                 'termId': termId})

            logger.debug('order submit response:%s' % resp)
            if resp['success']:
                pay_data['partner_order_id'] = partner_order_id
                pay_data['tuniu_orderId'] = resp['data']['orderId']
                pay_data['price'] = resp['data']['remainAmount']
                pay_data['account'] = self.account
                pay_data['timeout'] = str(datetime.datetime.now() + datetime.timedelta(minutes=25))
                cookie = 'PageSwitch=2,%s; _tacau=MCwzYTY0MTU4Ni1mZDI3LTQyMWUtZDI3NS1kNGI1ZDEzNDU1ODcs; _tacz2=taccsr=(direct)|tacccn=(none)|taccmd=(none)|taccct=(none)|taccrt=(none); _taca=1477397184786.1477397184786.1477397184786.1; _tacc=1; SERVERID=dnionD; app_imei=%s; ov=1; tuniuuser_id=%d;  TUNIUmuser=%s; sessionId=MQ==; token=%s; appVersion=9.0.0; tuniu_partner=MTU0NDcsMCwsOWIxMTFkNWY3NGQ1NmQ1NjdhNjEyZDQzYjEzYjVlYjI=; deviceType=1; SsoSession=%s; clientType=20; page_flag=; __utma=1.1665134217.1477397186.1477397186.1477397188.2; __utmb=1.4.10.1477397188; __utmc=1; __utmz=1.1477397188.2.2.utmcsr=morecoupon|utmccn=(not set)|utmcmd=couponcenter; _tact=NTExZDJiZTYtNGUxOS05Y2E2LWJlNjEtMTM0ZDMwYmMwNDRh;' % (
                    str(time.time()).replace('.', ''), base_data.get_random_number(), self.account['userid'],
                    self.account['sessionid'],
                    base64.b64encode(base_data.get_random_letter_number()), self.account['sessionid'])

                logger.info(
                    'order submit success,payid:%s,price:%s,confirming...' % (
                        pay_data['tuniu_orderId'], pay_data['price']))

                # --回调优惠券金额
                headers = {'content-type': 'application/json; charset=UTF-8',
                           'User-Agent': 'TuNiuApp/9.0.6/Dalvik/1.6.0 (Linux; U; Android 4.2.2)',
                           'cookie': cookie}
                req = requests.get(
                    'http://m.tuniu.com/userOrder/trainTicketOrderDetailAjax?data=%7B%22orderId%22%3A%22' + str(
                        pay_data['bizOrderId'])
                    + '%22%2C%22orderType%22%3A%2238%22%7D', headers=headers)
                resp = req.json()
                logger.debug('get order deails response:%s' % resp)
                logger.info('callback promotionPrice')
                if resp['success']:
                    req = requests.get('http://op.yikao666.cn/JDTrainOpen/CallBackForTN?'
                                       'order_id=%s&success=true&amount=%s&coupon_price=%s' % (
                                           pay_data['partner_order_id'], pay_data['price'],
                                           resp['data']['promotionPrice']))
                    logger.info('callback promotionPrice:%s' % req.text)
                else:
                    logger.error('get order details faild')
                # 回调优惠券金额--

                if base_data.payChannel == 8:
                    pay_data['cookie'] = cookie
                    return pay_data
                else:
                    resp = http_handler.pay.confirm(
                        {'userId': self.account['userid'], 'orderId': pay_data['tuniu_orderId'],
                         'price': pay_data['price'],
                         'sessionId': self.account['sessionid'],
                         'termId': termId})
                    logger.debug('order confirm response:%s' % resp)

                    if resp['success']:
                        pay_data['finalOrderId'] = resp['data']['finalOrderId']
                        pay_data['url'] = resp['data']['url']
                        logger.info('order confirm success.alipay url:%s\nupload data' % pay_data['url'])

                        return pay_data
                    else:
                        err = 'order confirm faild'
                        logger.error(err)
                        raise ValueError(err)

            else:
                err = 'order submit faild'
                logger.error(err)
                raise ValueError(err)

        else:
            err = 'add order faild'
            logger.error(err)
            raise ValueError(err)

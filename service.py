# -*- coding: utf-8 -*-

import http_handler
import base_data
import json
import log_ex as logger
import requests
import app_conf
import uuid


class TrainOrderService:
    def __init__(self, account, acountid):
        self.partner = base_data.get_partner()
        self.cc = base_data.get_cc()
        self.account = account

        logger.info('check session by get user id %s' % account)

        if not account.has_key('sessionid') or not account['sessionid']:
            logger.info('need login')
            self.login()

        account['userId'] = self.get_user_id()

        logger.info('update account data')
        req = requests.put(app_conf.put_account % acountid, data=json.dumps(account),
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
        logger.debug('train order coupon resp:%s' % train_order_coupon_resp)

        if train_order_coupon_resp['success'] and train_order_coupon_resp['data']['sortData']:
            coupon = train_order_coupon_resp['data']['sortData'][0]
            logger.info('find it.use %s' % coupon['number'])
            data['promotionList'].append(coupon['number'])
            data['price'] -= coupon['reduction']

            return True
        else:
            logger.error('trainticket order coupon not found')
            return False

    def place_order(self, data, coupons):
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
            pay_data = {'bizOrderId': resp['data']['orderId'], 'price': data['price'],}
            logger.info('add order success.id:%s.submiting...' % pay_data['bizOrderId'])

            resp = http_handler.pay.submit(
                {'userId': self.account['userid'], 'orderId': pay_data['bizOrderId'], 'price': pay_data['price'],
                 'sessionId': self.account['sessionid'],
                 'termId': termId})

            logger.debug('order submit response:%s' % resp)
            if resp['success']:
                pay_data['orderId'] = resp['data']['orderId']
                pay_data['price'] = resp['data']['remainAmount']

                logger.info(
                    'order submit success,payid:%s,price:%s,confirming...' % (pay_data['orderId'], pay_data['price']))

                resp = http_handler.pay.confirm(
                    {'userId': self.account['userid'], 'orderId': pay_data['orderId'], 'price': pay_data['price'],
                     'sessionId': self.account['sessionid'],
                     'termId': termId})
                logger.debug('order confirm response:%s' % resp)

                if resp['success']:
                    pay_data['finalOrderId'] = resp['data']['finalOrderId']
                    pay_data['alipay_url'] = resp['data']['url']
                    # pay_data['account'] = self.account
                    logger.info('order confirm success.alipay url:%s\nupload data' % pay_data['alipay_url'])

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

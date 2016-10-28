# -*- coding: utf-8 -*-

import http_handler
import base_data
import json


class TrainOrderService:
    def __init__(self, account):
        self.partner = base_data.get_partner()
        self.cc = base_data.get_cc()
        self.account = account

        print 'check session by get user id %s' % account

        if not account['sessionid']:
            print 'need login'
            self.login()

        self.get_user_id()

    def login(self):
        print 'login starting...\n1#.get session id'
        begin_session_resp = http_handler.login.begin_session(self.partner, self.cc)
        print 'begin session resp:%s', begin_session_resp

        if begin_session_resp['success']:
            self.account['sessionid'] = begin_session_resp['data']['sessionId']
            print 'get session id success,the id is %s' % self.account['sessionid']

            print '#2.login'
            login_resp = http_handler.login.login(self.account['sessionid'], self.account['username'],
                                                  self.account['password'],self.partner,self.cc)
            print 'login resp:%s', login_resp
            if login_resp['success']:
                print 'login success,the sessionid is %s' % self.account['sessionid']
                return self.account['sessionid']
            else:
                err = '2#.login faild'
                print err
                raise ValueError(err)
        else:
            err = 'get session id faild'
            print err
            raise ValueError(err)

    def get_user_id(self):
        print 'get user id starting...'
        resp = http_handler.account.account_info(self.account['sessionid'], self.partner)
        print 'account info:%s', resp
        if (resp['success']):
            print 'get user id %s' % resp['data']['userProfile']['userId']
            self.account['userid'] = int(resp['data']['userProfile']['userId'])
            return self.account['userid']
        else:
            err = 'get user id faild'
            print err
            raise ValueError(err)

    def get_coupon(self, coupon_id):
        print 'looking for coupon %d\n1#.' % coupon_id
        get_coupon_list_resp = http_handler.coupon.get_coupon_list()
        if get_coupon_list_resp['success']:
            list = filter(lambda c: c['id'] == str(coupon_id), get_coupon_list_resp['data']['list'])
            if list:
                mark = list[0]['mark']
                print '''looking for coupon %d success,the mark is %s.\n2#.get coupon %d''' % (coupon_id, mark, coupon_id)
                get_special_coupon_resp = http_handler.coupon.get_special_coupon(
                    1 and self.account['userid'] or self.get_user_id(),
                    self.account['sessionid'], mark)
                print 'get special coupon resp: %s' % get_special_coupon_resp
                if get_special_coupon_resp['success']:
                    print 'get coupon %d success' % coupon_id
                    return True
                else:
                    print 'get coupon %d falid' % coupon_id
                    return False

            else:
                print 'find coupon %d faild' % coupon_id

    def __lookup_coupon(self,data):
        print 'looking for trainticket order coupon that can use '
        train_order_coupon_resp = http_handler.account.get_account_train_order_can_use_coupon({
            'trainNumber': data['train_number'], 'startStationName': data['from'], 'arrivalStationName': data['to'],
            'departureCityCode': '200',
            'departDate': data['depart_date'], 'adultPrice': data['price']
        }, self.account['sessionid'], self.partner, self.cc)
        print 'train order coupon resp:%s' % train_order_coupon_resp

        if train_order_coupon_resp['success'] and train_order_coupon_resp['data']['sortData']:
            coupon = train_order_coupon_resp['data']['sortData'][0]
            print 'find it.use %s' % coupon['number']
            data['promotionList'].append(coupon['number'])
            data['price'] -= coupon['reduction']

            return True
        else:
            print 'trainticket order coupon not found'
            return False

    def place_order(self, data, coupons):
        if coupons:
            if not self.__lookup_coupon(data):
                for id in coupons:
                    self.get_coupon(id)
                self.__lookup_coupon(data)

        print 'READY:%s' % data
        add_order_resp = http_handler.train_order.add_order(self.account['sessionid'], self.partner, self.cc, data)
        print 'add order response:%s', add_order_resp

        if add_order_resp['success']:
            return True
        else:
            return False

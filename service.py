# -*- coding: utf-8 -*-

import http_handler
import base_data
import json


class TrainOrderService:
    def __init__(self, account, coupons):
        self.partner = base_data.get_partner()
        self.cc = base_data.get_cc()
        self.account = account
        self.use_coupon = coupons

    def login(self):
        print '''login starting...
                1#.get session id'''
        begin_session_resp = http_handler.login.begin_session(self.partner, self.cc)
        print 'begin session resp:%s', begin_session_resp

        if begin_session_resp['success']:
            self.account['sessionid'] = begin_session_resp['data']['sessionId']
            print 'get session id success,the id is %s' % self.account['sessionid']

            print '#2.login'
            login_resp = http_handler.login.login(self.account['sessionid'], self.account['username'],
                                                  self.account['password'])
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
            print 'get user id %d' % resp['data']['userProfile']['userId']
            self.account['userid'] = resp['data']['userProfile']['userId']
            return self.account['userid']
        else:
            err = 'get user id faild'
            print err
            raise ValueError(err)

    def get_coupon(self, coupon_id):
        print '''get coupon %d starting...
                 1#. get coupon list''' % coupon_id
        get_coupon_list_resp = http_handler.coupon.get_coupon_list()
        if get_coupon_list_resp['success']:
            list = filter(lambda c: c['id'] == coupon_id, get_coupon_list_resp['data']['list'])
            if list:
                mark = list[0]['mark']
                print '''lookup coupon %d success,the mark is %s.
                        2#.get coupon %d''' % (coupon_id, mark, coupon_id)
                get_special_coupon_resp = http_handler.coupon.get_special_coupon(
                    1 and self.account['userid'] or self.get_user_id(),
                    self.account['sessionid'], mark)
                print 'get special coupon resp: %s' % get_coupon_list_resp
                if get_special_coupon_resp['success']:
                    print 'get coupon %d success' % coupon_id
                    return True
                else:
                    return False

            else:
                err = 'get coupon %d faild' % coupon_id
                print err
                raise ValueError(err)

    def place_order(self, data, coupons):
        promotionList = []
        if coupons:
            for id in coupons:
                self.get_coupon(id)

                # get_account_coupon_resp = http_handler.account.get_account_train_order_can_use_coupon(self.account['userid'],self.account['sessionid'])
                # if get_account_coupon_resp['success']:




        http_handler.train_order.add_order(self.account['sessionid'], self.partner, self.cc, data)

# -*- coding: utf-8 -*-

import http_handler
import base_data
import json


class TrainOrderService:
    def __init__(self, account, train):
        self.partner = base_data.get_partner()
        self.cc = base_data.get_cc()
        self.account = account
        self.train = train

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
            print resp['data']['userProfile']['userId']
        else:
            err = 'get user id faild'
            print err
            raise ValueError(err)

    def get_coupon(self, coupon_id, user_id=None):
        print '''get coupon %d starting...
                 1#. get coupon list''' % coupon_id
        get_coupon_list_resp = http_handler.coupon.get_coupon_list()
        if get_coupon_list_resp['success']:
            list = filter(lambda c: c['id'] == coupon_id, get_coupon_list_resp['data']['list'])
            if list:
                mark = list[0]['mark']
                print '''lookup coupon %d success,the mark is %s.
                        2#.get coupon %d''' % (coupon_id, mark, coupon_id)
                get_special_coupon_resp = http_handler.coupon.get_special_coupon(1 and user_id or self.get_user_id(), self.account['sessionid'],mark)


            else:
                err = 'get coupon %d faild' % coupon_id
                print err
                raise ValueError(err)

    def place_order(self):
        pass

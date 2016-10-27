# -*- coding: utf-8 -*-

import http_handler
import unittest
import base_data
import urllib
import json


class HttpHandlerTestSuit(unittest.TestCase):
    def setUp(self):
        self.partner = base_data.get_partner()
        self.cc = base_data.get_cc()

    def begin_session_test(self):
        print http_handler.login.begin_session(self.partner, self.cc)

    def login_test(self):
        print http_handler.login.login('8ec18aeb6e4c3c6c9422213eeed8a3f3', '13192655251', 'h442278', self.partner,
                                       self.cc)

    def add_order_test(self):
        print http_handler.train_order.add_order('9d37eacbd75fa145f571ac6ffdaf9286', self.partner, self.cc, {
            'from': u'昆山南', 'to': u'西安北', 'depart_date': '2016-11-25', 'coupon': '', 'price': 639, 'seatId': '3',
            'resourceId': '1650320356',
            'train_number': 'G1920', 'phone': '13192655251',
            'touristList': [
                {"birthday": "1974-11-26", "name": "蒋学松", "psptId": "34112519741126147X", "psptType": 1, "isAdult": 1,
                 "sex": 1}], 'promotionList': ['126246']
        })

    def account_info_test(self):
        resp = http_handler.account.account_info('8ec18aeb6e4c3c6c9422213eeed8a3f3', self.partner)
        print resp
        if (resp['success']):
            print resp['data']['userProfile']['userId']

    def get_coupon_list_test(self):
        resp = http_handler.coupon.get_coupon_list()
        print resp

        for l in resp['data']['list']:
            print l

        list = filter(lambda c: c['id'] == '177', resp['data']['list'])
        print list[0]['mark']

    def click_special_coupon_test(self):

        # 190:10 173:5
        resp = http_handler.coupon.click_special_coupon(53652991, '8ec18aeb6e4c3c6c9422213eeed8a3f3', 174)
        print resp

    def get_special_coupon_test(self):
        resp = http_handler.coupon.get_special_coupon(53652991, '8ec18aeb6e4c3c6c9422213eeed8a3f3', 'nzr4wnt9')
        print resp

    def get_account_coupon_test(self):
        resp = http_handler.account.get_account_coupon(53652991, '8ec18aeb6e4c3c6c9422213eeed8a3f3')
        print resp

    def get_account_train_order_can_use_coupon_test(self):
        resp = http_handler.account.get_account_train_order_can_use_coupon({
            'trainNumber': 'K472', 'startStationName': '长沙站', 'arrivalStationName': '北京西站', 'departureCityCode': '1502',
            'departDate': '2016-10-28', 'adultPrice': 343.5, 'seatId': 353438822
        }, '8ec18aeb6e4c3c6c9422213eeed8a3f3', self.partner, self.cc)
        print resp

    def get_train_list_test(self):
        data = {"arrivalCityCode": "2702", "arrivalCityName": u"西安北", "departureCityCode": "1615",
                "departureCityName": u"昆山南",
                "departureDate": "2016-11-25", "deviceNumber": "863175026618021", "sortName": 0, "sortType": 0,
                "start": 0,
                "showAvailableTickets": 0, "limit": 0}
        resp = http_handler.train_order.get_train_list(data)
        print resp

        if resp['success']:
            train = filter(lambda t: t['trainNum'] == 'G1920', resp['data']['rows'])
            print train
            if train:
                seat = filter(lambda t: t['seatName'] == u'二等', train[0]['seatDesc'])
                print seat[0]['resId'], seat[0]['seatId'], seat[0]['price']

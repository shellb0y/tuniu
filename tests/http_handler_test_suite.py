# -*- coding: utf-8 -*-

import http_handler.login
import http_handler.train_order
import unittest
import base_data


class HttpHandlerTestSuit(unittest.TestCase):
    def setUp(self):
        self.partner = base_data.get_partner()
        self.cc = base_data.get_cc()

    def begin_session_test(self):
        print http_handler.login.begin_session(self.partner, self.cc)

    def login_test(self):
        print http_handler.login.login('9d37eacbd75fa145f571ac6ffdaf9286', '13192655251', 'h442278', self.partner,
                                       self.cc)

    def add_order_test(self):
        print http_handler.train_order.add_order('9d37eacbd75fa145f571ac6ffdaf9286', self.partner, self.cc, {
            'from': u'上海虹桥站', 'to': u'北京南站', 'depart_date': '2016-11-30', 'coupon': '', 'price': 543.0,
            'train_number': 'G106','phone':'15974253250'
        })

# encoding:utf-8

import unittest
import base_data


class BaseDataTestSuite(unittest.TestCase):
    def setUp(self):
        self.a=1

    def get_station_test(self):
        print base_data.get_station_code_by_city_name(u'昆山南')
        print base_data.get_station_code_by_city_name(u'西安北')

    def get_station_code_12306(self):
        print base_data.get_station_code_12306(u'长沙')
        print base_data.get_station_code_12306(None)
        print base_data.get_station_code_12306('')
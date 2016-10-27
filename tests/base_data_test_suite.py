# encoding:utf-8

import unittest
import base_data


class BaseDataTestSuite(unittest.TestCase):
    def get_station_test(self):
        print base_data.get_station_code_by_city_name(u'昆山南')
        print base_data.get_station_code_by_city_name(u'西安北')

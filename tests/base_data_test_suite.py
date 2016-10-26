# encoding:utf-8

import unittest




class BaseDataTestSuite(unittest.TestCase):
    def __init__(self):pass

    def get_city_code_test(self):
        self.assertEqual(1, 1)
        # print base_data.get_city_code('北京')
        # print base_data.get_city_code('长沙')
        # print base_data.get_city_code('aaa')
        # print base_data.get_city_code('')

    def get_station_code(self):pass
        # print base_data.get_city_code('北京西')
        # print base_data.get_city_code('长沙南')
        # print base_data.get_city_code('aaa')
        # print base_data.get_city_code('')

def load_tests(loader, tests, pattern):
    test_cases=(BaseDataTestSuite)
    suite = unittest.TestSuite()
    for test_class in test_cases:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    return suite


if __name__ == '__main__':
    unittest.main()
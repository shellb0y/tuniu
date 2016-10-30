# -*- coding: utf-8 -*-
import service
import unittest
import base_data


class ServcieTestSuite(unittest.TestCase):
    def setUp(self):
        self.account = {'userid': 53653289, 'username': '13175001652', 'password': 'k593653',
                        'sessionid': '5e19a0b7c7486b07e4ba49767d1d48c9'}
        self.partner = base_data.get_partner()
        self.cc = base_data.get_cc()
        self.trainOrderService = service.TrainOrderService(self.account)

    def place_order_test(self):
        self.trainOrderService.place_order(
            {
                'from': u'乌鲁木齐南', 'to': u'嘉峪关南', 'depart_date': '2016-11-28', 'price': 334, 'seatName': u'二等',
                'train_number': 'D2714', 'phone': '13192655251',
                'touristList': [
                    {"birthday": "1987-03-03", "name": u"张庆梅", "psptId": "412801198703032610", "psptType": 1,
                     "isAdult": 1,
                     "sex": 1}], 'promotionList': []  # '126246'
            }, [194,176])

if __name__ == '__main__':
    unittest.main()
# -*- coding: utf-8 -*-
import service
import unittest
import base_data
import log_ex


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
                'from': u'温州南', 'to': u'上海虹桥', 'depart_date': '2016-12-05', 'price': 334, 'seatName': u'二等',
                'train_number': 'D2288', 'phone': '13192655251',
                'touristList': [
                    {"birthday": "1985-06-02", "name": u"武仕伟", "psptId": "130129198506021014", "psptType": 1,
                     "isAdult": 1,
                     "sex": 1}], 'promotionList': []  # '126246'
            }, [194,176])


if __name__ == '__main__':
    unittest.main()
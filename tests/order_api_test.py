# -*- coding: utf-8 -*-

import requests
import unittest
import json
import urllib


class OrderApiTest(unittest.TestCase):
    def get_order_test(self):
        req = requests.get('http://op.yikao666.cn/JDTrainOpen/getOrderForTN')
        print req.json()

    def callback_pay_test(self):
        req = requests.get('http://op.yikao666.cn/JDTrainOpen/CallBackForTN?order_id=%s&success=%s&amount=163.5&coupon_price=5' % ('36c2fbd3711947a68408e7b4b50530c8', 'true'))
        resp = req.json()
        self.assertEqual(resp['message'], u'操作成功')

    def put_account_ordercount_test(self):
        put_account_ordercount = 'http://localhost:8000/api/mobilepay/account/ordercount/%s'
        req = requests.put(put_account_ordercount % 1)
        resp = req.text
        self.assertEqual(resp, '1')

    def callback_lock_test(self):
        req = requests.get(
            'http://op.yikao666.cn/JDTrainOpen/CallBackForTNLock?tnOrderno=14966527&userName=13189940634&password=s031161&order_id=%s&success=%s&amount=23.5' % (
                '4c8a4d119fdf4c3197d2f98e3bb4e377', 'true'))
        # resp = req.json()
        # self.assertEqual(resp['message'], u'操作成功')

    def post_order_test(self):
        req = requests.post('http://localhost:8000/api/mobilepay/order', data=
        '{"id":13915,"order_id":"2bcc3e3c7a5b4124879d535cc9d9ac14","train_date":"2016-12-01 00:00:00","checi":"D5484",'
        '"from_station_code":"NUH","to_station_code":"NJH","from_station":"南通","to_station":"南京","zw_code":"O",'
        '"zw_name":"二等座","ticket_type_id":1,"ticket_type_name":"成人票","ticket_price":105.5000,'
        '"passport_se_no":"120101198112292569","passenger_name":"李晶晶","passport_type_se_id":"1",'
        '"passport_name":"二代身份证","status":101,"create_time":"2016-11-01 14:37:30","update_time":null,'
        '"order_user":"tuniu","site_no":null,"pay_price":null,"discount_amount":null,"site_order_no":null,'
        '"refund_amount":null,"loss_amount":null,"last_opt_time":null,'
        '"partner_order_id":null,"status_id":null,"status_name":null,"account_info":null,"coupon_id":null,"get_time":null,'
        '"JdUserInfo":null,"pay_channel":8,"target":"tuniu"}',
                            headers={'Content-Type': 'application/json'})
        self.assertIsNotNone(req.text)

    def set_order_status_test(self):
        req = requests.put(u'http://localhost:8000/api/mobilepay/order/status/10023/' + urllib.quote('下单失败'),
                           data=json.dumps({'error': 'error'}), headers={'Content-Type': 'application/json'})
        self.assertEqual(req.text, '1')

        # req = requests.put(u'http://localhost:8000/api/mobilepay/order/status/10022/下单成功',
        #                    data=json.dumps({'url': 'afdafdafd'}), headers={'Content-Type': 'application/json'})
        # self.assertEqual(req.text, '1')

    def get_account_api_test(self):
        req = requests.get('http://localhost:8000/api/mobilepay/account/tuniu')
        print req.status_code
        print req.json()

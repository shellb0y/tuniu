# encoding:utf-8

import unittest
import hashlib
import base_data
import base64
import requests


class EnDeCryptionTest(unittest.TestCase):
    def md5_test(self):
        req = requests.get(base_data.rsa_encode % '573.0')
        resp = req.text
        print resp
        encodeTotalAmount = resp
        data = 'downPaymentFlag=0&encodeTotalAmount=%s&orderId=14105241&orderType=1&payChannel=9&payMethod=11&userId=53652883' % encodeTotalAmount
        data = data + '&*()%sd76@#$Dfs^YsfUJKDs'
        print data
        print hashlib.md5(data).hexdigest()

# encoding:utf-8

import unittest
import hashlib
import app_conf
import rsa
import base64


class EnDeCryptionTest(unittest.TestCase):
    def md5_test(self):
        encodeTotalAmount = 'JvFsTYKg3GpELtK2SNt/futbdwCwrNDqzJXNYfQ2aIJyCeVigRuBhqH5yJdDEoy+iUUecFx9AEWBGtoBAMQmEB435z93ewHps7FAcZVBVSTE00RO2fVDKughQbLDmBSS0sGziRl6+WfVW1Y0UkCcuK5cTEZsiixpNCK+9V7PqcPJsmw8G5NJpM+myome4Vgi51cF2zZBygqd0winciuYRcctYZ/uRkv+igkhbOfJDnyuZDNa4nSEx2PVfhEaoGDXgTU0+S2iLwLdZK+d7pbdt8ErBqffqwR4fkC6Tx7YalRlckJvyLLF1SiThwGQ9Zii0gXQKYQrhKz97HdWUiK52w=='
        data = 'downPaymentFlag=0&encodeTotalAmount=%s&orderId=14105241&orderType=1&payChannel=9&payMethod=11&userId=53652883' % encodeTotalAmount
        data = data +'&*()%sd76@#$Dfs^YsfUJKDs'
        print data
        print hashlib.md5(data).hexdigest()

    def public_key_encryption_test(self):
        with open('../rsa_public_key_new.pem') as publickfile:
            p = publickfile.read()
            pubkey = rsa.PublicKey.load_pkcs1(p)

        crypto = rsa.encrypt('523.0', pubkey)
        print crypto

# -*- coding: utf-8 -*-

import requests

req = requests.get('http://m.tuniu.com/api/train/product/StationCitys?'
                   'd=%7B%22version%22%3A%223%22%7D&c=%7B%22v%22%3A%228.1.6%22%2C%22ct%22%3A20%2C%22'
                   'dt%22%3A1%2C%22ov%22%3A1%2C%22p%22%3A15447%2C%22cc%22%3A1502%7D')
resp = req.json()
print resp.data.hotCityList
s = '你好'
print '\u5357\u4eac'.decode('raw_unicode_escape')
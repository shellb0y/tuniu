# -*- coding: utf-8 -*-
# s = '你好'
# print '\u5357\u4eac'.decode('raw_unicode_escape')

import datetime
import time

import base_data
from http_handler import login
from my_exception import *

# li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
# for e in [elem for elem in li if (lambda b: b == 'b')(elem)]:
#     print e
#
# print filter(lambda b: b == 'b', li)

# print base_data.get_city_code(u'长沙')
# print base_data.get_station_code(u'北京西')
print time.time()
print datetime.datetime.now().microsecond

# print base_data.get_sid()

try:
    login.begin_session(base_data.get_partner())
except HttpRequestException, e:
    print e

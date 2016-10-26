# -*- coding: utf-8 -*-
# s = '你好'
# print '\u5357\u4eac'.decode('raw_unicode_escape')
import traceback
try:
    raise ValueError('test',{'a':'m'})
except ValueError,e:
    print traceback.format_exc()
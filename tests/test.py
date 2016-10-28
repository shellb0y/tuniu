# -*- coding: utf-8 -*-
# s = '你好'
# print '\u5357\u4eac'.decode('raw_unicode_escape')
import traceback
try:
    raise ValueError('test',{'a':'m'})
except ValueError,e:
    print traceback.format_exc()

print 1 and None or '2'


class test:
    def __init__(self,c):
        self.c=c
        c['a']=1

a={'b':1}
test(a)
print a
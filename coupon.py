# -*- coding: utf-8 -*-
import requests

import adsl



adsl_service = adsl.Adsl({"name": u"宽带连接".encode("gbk"),
                        "username": "057474432953",
                        "password": "734206"})




f = open("account.txt")  # 返回一个文件对象
s = open('success.txt', 'a')
i=0
for line in open("account.txt"):
    i=i+1
    if i%5==0:
        while 1:
            try:
                adsl_service.reconnect()
                break;
            except Exception,e:
                print e.message
                continue
    
    tel = line[0:line.find('-')]
    resp = requests.get(
        'http://dynamic.m.tuniu.com/event/lottery/opeLottery'
        '/lotteryAndSendAjax?tel=%s&actId=1459&mark=wyyyy1107&offCode=&type=1&one=1&p=0' % tel)
    try:
        data = resp.json()
        if data['success']:
            print i,tel,'success'
            s.write(tel+'\n')
        else:
            print i,tel,'faild'
    except Exception,e:
        print e.message

f.close()
s.close()

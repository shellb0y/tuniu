# -*- coding: utf-8 -*-
import requests

# import adsl



# adsl_service = adsl.Adsl({"name": u"宽带连接".encode("gbk"),
#                        "username": "057474432953",
#                        "password": "734206"})

#
# adsl_service.reconnect()

f = open("account.txt")  # 返回一个文件对象
s = open('success.txt', 'a')
for line in open("account.txt"):
    tel = line[0:line.find('-')]
    resp = requests.get(
        'http://dynamic.m.tuniu.com/event/lottery/opeLottery'
        '/lotteryAndSendAjax?tel=%s&actId=1459&mark=wyyyy1107&offCode=&type=1&one=1&p=0' % tel)
    try:
        data = resp.json()
        if data['success']:
            print tel
            s.write(tel)
    except Exception,e:
        print e.message

f.close()
s.close()
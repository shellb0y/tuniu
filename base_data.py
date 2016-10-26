# -*- coding: utf-8 -*-

import requests
import time
import random

print 'get tuniu stations and citys...'
req = requests.get('http://m.tuniu.com/api/train/product/StationCitys?'
                   'd=%7B%22version%22%3A%223%22%7D&c=%7B%22v%22%3A%228.1.6%22%2C%22ct%22%3A20%2C%22'
                   'dt%22%3A1%2C%22ov%22%3A1%2C%22p%22%3A15447%2C%22cc%22%3A1502%7D')
resp = req.json()
TRAINSTAIONLIST = resp['data']['trainStationlist']
print 'complete.'

r = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
     '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

ron=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


def get_city_code(name):
    for k in TRAINSTAIONLIST:
        t = filter(lambda d: d['cityName'] == name, TRAINSTAIONLIST[k])
        if t:
            return t[0]['cityCode']


def get_station_code(name):
    for k in TRAINSTAIONLIST:
        t = filter(lambda d: d['stationName'] == name, TRAINSTAIONLIST[k])
        if t:
            return t[0]['stationId']


def get_sid(parm=str(time.time()).replace('.', '')):
    sub = parm[len(parm) - 8:]
    # print 'parm=',parm,'sub=',sub
    str1 = ''
    for i in range(0, len(sub)):
        j = random.randint(1, 9)
        str1 += str(j)
        parm += str(int(sub[i]) << j)
        # print '#%d:j=%d,a=%s,b=%s' % (i, j,str1,parm)
    return str1 + parm


def get_token(n=16):
    token = []
    for i in range(n):
        token.append(random.choice(r))
    return ''.join(token)

def get_imei(n=15):
    imei = []
    for i in range(n):
        imei.append(random.choice(ron))
    return ''.join(imei)

def get_partner():
    return random.randint(15000,19000)
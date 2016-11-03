# -*- coding: utf-8 -*-

import requests
import time
import random
import json
import re
import log_ex as logger



def get_partner():
    return random.randint(15000, 19000)


def get_cc():
    return random.randint(1500, 2500)


logger.info('get tuniu stations and citys...')

params = {'d': json.dumps({"version": "3"}),
          'c': json.dumps({"v": "8.1.6", "ct": 20, "dt": 1, "ov": 1, "p": get_partner(), "cc": get_cc()})}
req = requests.get('http://m.tuniu.com/api/train/product/StationCitys', params)
resp = req.json()
TRAINSTAIONLIST = resp['data']['trainStationlist']
logger.info('complete.')

logger.info('get 12306 stations and citys...')
req = requests.get('https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8971',
                   verify=False)
STATION = req.text
logger.info('complete.')

r = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
     '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

ron = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


def get_station_code_12306(name):
    pattern = re.compile(ur'\|%s\|\w+?\|' % name)
    match = pattern.findall(STATION)
    if match:
        return match[0].split('|')[2]
    return None


def get_station_code_by_city_name(name):
    for k in TRAINSTAIONLIST:
        t = filter(lambda d: d['cityName'] == name, TRAINSTAIONLIST[k])
        if t:
            return t[0]


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


def get_random_letter_number(n=16):
    token = []
    for i in range(n):
        token.append(random.choice(r))
    return ''.join(token)


def get_random_number(n=15):
    imei = []
    for i in range(n):
        imei.append(random.choice(ron))
    return ''.join(imei)

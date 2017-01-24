# -*- coding: utf-8 -*-

import requests
import base_data
import time
import json
import hashlib
from my_exception import *
import log_ex as logger


# POST https://m.tuniu.com/api/user/auth/beginSession?c=%7B%22v%22%3A%228.1.5%22%2C%22ct%22%3A20%2C%22dt%22%3A1%2C%22ov%22%3A1%2C%22p%22%3A18798%2C%22cc%22%3A2500%7D HTTP/1.1
# User-Agent: TuNiuApp/9.0.1/Dalvik/1.6.0 (Linux; U; Android 4.2.2; Full JellyBean on Mako Build/JDQ39E)
# host: m.tuniu.com
# Content-Type: application/json; charset=UTF-8
# Content-Length: 290
# Connection: Keep-Alive
# Accept-Encoding: gzip
#
# {"sessionId":"0","parameters":{"version":"8.1.5","token":"46571ea36b8ee327","createTime":"Oct 22, 2016 1:48:42 PM","sid":"818394981331210412544400256009122457613312","imei":"353918053384455","lg":"1477144122904","partner":18798,"deviceType":1,"clientType":20,"apiType":1},"activateTimes":0}

# HTTP/1.1 200 OK
# Date: Tue, 25 Oct 2016 12:01:40 GMT
# Server: nginx
# Content-Type: text/html; charset=utf-8
# Transfer-Encoding: chunked
# Cache-Control: no-store,no-control,must-revalidate
# Connection: keep-alive
# {
# 	"success": true,
# 	"errorCode": 710000,
# 	"msg": "OK",
# 	"data": {
# 		"sessionId": "0be5a61a4c796b61ebd4c0df8cf6e861",
# 		"isLogin": 0
# 	}
# }

def begin_session(partner, cc):
    timestamp = time.time()
    lg = str(timestamp).replace('.', '')
    data = {"sessionId": "0",
            "parameters": {"version": "9.0.6", "token": base_data.get_random_letter_number(),
                           "createTime": time.ctime(timestamp),
                           "sid": base_data.get_sid(lg), "imei": base_data.get_random_number(),
                           "lg": lg, "partner": partner, "deviceType": 1, "clientType": 20, "apiType": 1},
            "activateTimes": 0}

    # print data

    c = {"v": "9.0.6", "ct": 20, "dt": 1, "ov": 1, "p": partner, "cc": cc}
    url = 'https://m.tuniu.com/api/user/auth/beginSession?c=%s' % json.dumps(c)
    req = requests.post(url, json=data, headers={'content-type': 'application/json; charset=UTF-8',
                                                 'User-Agent': base_data.get_user_agent()})
    # print url
    logger.debug('POST %s \n%s \n%s' % (req.url, req.headers, data))
    try:
        resp = req.json()
        return resp
    except Exception, e:
        raise HttpRequestException(e, {'function': 'begin_session', 'url': url, 'method': 'post',
                                       'content-type': 'application/json; charset=UTF-8',
                                       'data': data,
                                       'resp_content': req.content})


# GET https://m.tuniu.com/api/user/auth/login?d={"captcha":"","deviceId":"31f432734f0fb42f2bc55352abc1:28","sessionId":"bb3fdf37ef796386b446181279323a64","loginId":"15728532201","password":"f88be3495c9c29561a17c8755b073ebf","isDynamic":0}&c={"v":"9.0.1","ct":20,"dt":1,"ov":1,"p":18798,"cc":1502} HTTP/1.1
# User-Agent: Fiddler
# Host: m.tuniu.com
# Content-Length: 0
#
# HTTP/1.1 200 OK
# Date: Tue, 25 Oct 2016 12:01:40 GMT
# Server: nginx
# Content-Type: text/html; charset=utf-8
# Transfer-Encoding: chunked
# Cache-Control: no-store,no-control,must-revalidate
# Expires: Tue, 25 Oct 2016 12:01:39 GMT
# X-Via: 1.1 shydx35:9 (Cdn Cache Server V2.0)
# Connection: keep-alive
#
# {"success":true,"errorCode":710000,"msg":"OK","data":{"intlCode":"0086","phoneNum":"15728532201","realName":""}}
def login(sessionid, username, password, partner, cc):
    params = {
        'd': json.dumps({"captcha": "", "deviceId": base_data.get_random_letter_number(28),
                         "sessionId": sessionid, "loginId": username,
                         "password": hashlib.md5(password).hexdigest(), "isDynamic": 0}),
        'c': json.dumps({"v": "9.0.6", "ct": 20, "dt": 1, "ov": 1, "p": partner, "cc": cc})}

    req = requests.get('https://m.tuniu.com/api/user/auth/login', params,
                       headers={'content-type': 'application/json; charset=UTF-8',
                                'User-Agent': base_data.get_user_agent()})

    logger.debug('GET %s \n%s' % (req.url, req.headers))
    try:
        resp = req.json()
        return resp
    except Exception, e:
        raise HttpRequestException(e,
                                   {'function': 'login', 'method': 'get', 'url': req.url, 'resp_content': req.content})

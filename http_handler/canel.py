# -*- coding: utf-8 -*-

import requests
import json
import hashlib
import base64
from my_exception import *
import log_ex as logger
import rsa

# GET /onlineBook/onlineBookTrain/trainApplyLossAjax?data=%7B%22orderId%22%3A1005100477%2C%22orderType%22%3A38%2C%22touristIds%22%3A%2210705597%22%7D HTTP/1.1
# Host: m.tuniu.com
# Accept: application/json
# X-Requested-With: XMLHttpRequest
# User-Agent: Mozilla/5.0 (Linux; Android 4.4.2; NX507J Build/KVT49L) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36
# Referer: http://m.tuniu.com/m2015/train/trainTicket/trainTicketOrderDetail?orderId=1005100477&orderType=38&cFrom=0&returnFromPay=0
# Accept-Encoding: gzip,deflate
# Accept-Language: zh-CN,en-US;q=0.8
# Cookie: PageSwitch=2%2C1485920543; _tacau=MCwyNjMzMjgyNS1mNTcxLTdiNzgtNTBlMy01YjNjYmU3MTUzMjIs; _tacz2=taccsr%3D%28direct%29%7Ctacccn%3D%28none%29%7Ctaccmd%3D%28none%29%7Ctaccct%3D%28none%29%7Ctaccrt%3D%28none%29; _tacc=1; _taca=1478144600853.1478144600853.1478158757792.2; app_imei=863175026618021; ov=1; sessionId=Mw==; token=OTRiOTA2NTFmNDU1MDg1Nw==; appVersion=8.1.5; deviceType=1; tuniuuser_id=53652883; tuniuuser_citycode=MjUwMA%3D%3D; TUNIUmuser=a69921200054a3619ca7848bbb27925c; SsoSession=a69921200054a3619ca7848bbb27925c; clientType=20; tuniu_partner=MTg3OTgsMCwsMzdmMzQzMjJjYzBkMzU2YWU1NjE2MzQyYjM0MDMzZDY%3D; __utma=1.441945427.1478144601.1478144601.1478158758.2; __utmb=1.4.10.1478158758; __utmc=1; __utmz=1.1478144601.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); page_flag=; departDate=2016-12-01; departCityCode=217; departCityName=%u6000%u67D4; departStationId=1175883; departStationName=%u6000%u67D4%u5317%u7AD9; destCityCode=200; destCityName=%u5317%u4EAC; destStationId=1175342; destStationName=%u5317%u4EAC%u7AD9; _tact=NDljZDhmNTItNzBhYi0wNjlkLWQwYzYtMGI3ZTcwNTg4ZmJh; _tacb=NjcxNmE0NTItZmExYS00NjMwLTk3YjItYzAxN2E3YjlmMzg3
#
# HTTP/1.1 200 OK
# Date: Thu, 03 Nov 2016 08:04:26 GMT
# Server: nginx
# Content-Type: text/html; charset=utf-8
# Access-Control-Allow-Origin: http://m.tuniu.com,http://dynamic.m.tuniu.com
# Access-Control-Allow-Credentials: true
# Content-Encoding: gzip
# X-Via: 1.1 szhj11:0 (Cdn Cache Server V2.0), 1.1 dianxin45:4 (Cdn Cache Server V2.0)
# Transfer-Encoding: chunked
# Proxy-Connection: Keep-alive
#
# {"success":true,"msg":"\u9000\u7968\u53ef\u80fd\u635f\u59310\u5143\uff0c\u5b9e\u9645\u6838\u6536\u9000\u7968\u8d39\u53ca\u5e94\u9000\u7968\u6b3e\u5c06\u6309\u6700\u7ec8\u4ea4\u6613\u65f6\u95f4\u8ba1\u7b97\u3002","errorCode":130000,"data":{"lossPrice":{"total":0,"details":[{"resMainId":268962594,"touristId":10705597,"loss":0}]}}}
def apply_loss():
    pass


# GET /onlineBook/onlineBookTrain/trainCancelOrderAjax?data=%7B%22orderId%22%3A1005100477%2C%22orderType%22%3A38%2C%22touristIds%22%3A%2210705597%22%7D HTTP/1.1
# Host: m.tuniu.com
# Accept: application/json
# X-Requested-With: XMLHttpRequest
# User-Agent: Mozilla/5.0 (Linux; Android 4.4.2; NX507J Build/KVT49L) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36
# Referer: http://m.tuniu.com/m2015/train/trainTicket/trainTicketOrderDetail?orderId=1005100477&orderType=38&cFrom=0&returnFromPay=0
# Accept-Encoding: gzip,deflate
# Accept-Language: zh-CN,en-US;q=0.8
# Cookie: PageSwitch=2%2C1485920543; _tacau=MCwyNjMzMjgyNS1mNTcxLTdiNzgtNTBlMy01YjNjYmU3MTUzMjIs; _tacz2=taccsr%3D%28direct%29%7Ctacccn%3D%28none%29%7Ctaccmd%3D%28none%29%7Ctaccct%3D%28none%29%7Ctaccrt%3D%28none%29; _tacc=1; _taca=1478144600853.1478144600853.1478158757792.2; app_imei=863175026618021; ov=1; sessionId=Mw==; token=OTRiOTA2NTFmNDU1MDg1Nw==; appVersion=8.1.5; deviceType=1; tuniuuser_id=53652883; tuniuuser_citycode=MjUwMA%3D%3D; TUNIUmuser=a69921200054a3619ca7848bbb27925c; SsoSession=a69921200054a3619ca7848bbb27925c; clientType=20; tuniu_partner=MTg3OTgsMCwsMzdmMzQzMjJjYzBkMzU2YWU1NjE2MzQyYjM0MDMzZDY%3D; __utma=1.441945427.1478144601.1478144601.1478158758.2; __utmb=1.4.10.1478158758; __utmc=1; __utmz=1.1478144601.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); page_flag=; departDate=2016-12-01; departCityCode=217; departCityName=%u6000%u67D4; departStationId=1175883; departStationName=%u6000%u67D4%u5317%u7AD9; destCityCode=200; destCityName=%u5317%u4EAC; destStationId=1175342; destStationName=%u5317%u4EAC%u7AD9; _tact=NDljZDhmNTItNzBhYi0wNjlkLWQwYzYtMGI3ZTcwNTg4ZmJh; _tacb=NjcxNmE0NTItZmExYS00NjMwLTk3YjItYzAxN2E3YjlmMzg3
#
# HTTP/1.1 200 OK
# Date: Thu, 03 Nov 2016 08:05:09 GMT
# Server: nginx
# Content-Type: text/html; charset=utf-8
# Access-Control-Allow-Origin: http://m.tuniu.com,http://dynamic.m.tuniu.com
# Access-Control-Allow-Credentials: true
# Content-Encoding: gzip
# X-Via: 1.1 szhj11:0 (Cdn Cache Server V2.0), 1.1 dianxin45:4 (Cdn Cache Server V2.0)
# Transfer-Encoding: chunked
# Proxy-Connection: Keep-alive
#
# {"success":true,"data":{"success":true,"msg":""}}
def confrim():
    pass
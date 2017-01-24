# -*- coding: utf-8 -*-

import requests
import time
import json
import base_data
import base64
from my_exception import *
import log_ex as logger


# GET http://dynamic.m.tuniu.com/event/couponCenter/MainCenter/SpecialListAjax?tab_id=1 HTTP/1.1
# Host: dynamic.m.tuniu.com
# Connection: keep-alive
# Accept: application/json
# X-Requested-With: XMLHttpRequest
# User-Agent: Mozilla/5.0 (Linux; Android 4.4.2; NX507J Build/KVT49L) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36
# Referer: http://dynamic.m.tuniu.com/event/couponCenter/mainCenter/index?utm_source=morecoupon&utm_medium=couponcenter&q=1005
# Accept-Encoding: gzip,deflate
# Accept-Language: zh-CN,en-US;q=0.8
# Cookie: PageSwitch=2%2C1485172159; SERVERID=dnionD; _tacau=MCw5NTI0OGM4ZS04OTE0LTI0YTktMjQzYS0xOWJjY2M3MDMxZjYs; _tacz2=taccsr%3D%28direct%29%7Ctacccn%3D%28none%29%7Ctaccmd%3D%28none%29%7Ctaccct%3D%28none%29%7Ctaccrt%3D%28none%29; _taca=1477396212293.1477396212293.1477396212293.1; _tacc=1; app_imei=863175026618021; ov=1; tuniuuser_id=53652883; tuniuuser_citycode=MTUwMg%3D%3D; TUNIUmuser=7b42973d419cbe9cce81e0d15923593f; sessionId=MQ==; token=OTRiOTA2NTFmNDU1MDg1Nw==; appVersion=9.0.6; tuniu_partner=MTU0NDcsMCwsOWIxMTFkNWY3NGQ1NmQ1NjdhNjEyZDQzYjEzYjVlYjI=; deviceType=1; SsoSession=7b42973d419cbe9cce81e0d15923593f; clientType=20; page_flag=; __utma=1.1046466050.1477396213.1477396213.1477396718.2; __utmb=1.3.10.1477396718; __utmc=1; __utmz=1.1477396718.2.2.utmcsr=morecoupon|utmccn=(not%20set)|utmcmd=couponcenter; _tact=MWRjZTRhYjYtMmVmMC00NWJjLWIzNTQtODQ3N2E3NDY1M2Zj; _tacb=OGRjMWJkYmEtYzQyZi0yNTRjLWQwZDEtMThiYTA3MzIyZWE3

# HTTP/1.1 200 OK
# Date: Tue, 25 Oct 2016 11:59:27 GMT
# Server: Apache
# Access-Control-Allow-Origin: http://m.tuniu.com,http://dynamic.m.tuniu.com
# Access-Control-Allow-Credentials: true
# cache-control: no-store,no-control,must-revalidate
# expires: Tue, 25 Oct 2016 11:59:26 GMT
# Vary: Accept-Encoding
# Content-Length: 11991
# Content-Type: text/html
# Age: 0
# Connection: keep-alive
# Via: http/1.1 aca-CT-HNHY-226-127 (ACA/2.0)
#
# {"success":true,"errorCode":710000,"msg":"ok","data":{"count":16,"list":[{"id":"174","special_type":"2","name":"国内机票优惠券","amount":"30","discount_tips":"每800减10，最高立减30","stock":"15000","start_time":"2016-07-19 11:59:49","end_time":"2016-11-29 00:00:00","seckill_start_time":"1970-01-01 08:00:00","seckill_end_time":"1970-01-01 08:00:00","get_link":"tuniuapp:\/\/travel\/airlineticket\/home","unget_link":"tuniuapp:\/\/travel\/airlineticket\/home","description":"","style_type":"3","right_type":"1","left_label":"1","left_content":"首单专享","left_img":"http:\/\/m.tuniucdn.com\/fb2\/t1\/G2\/M00\/47\/4F\/Cii-Tle7-emIUmvPAAAY78mcAIAAABnzwP_zh8AABkH205.png","seckill_status":2,"is_over":0,"stock_reduce":7213,"getted_user_num":7787,"getted_per":51,"is_getted":0,"mark":"46wzinyy"},{"id":"173","special_type":"2","name":"火车票优惠券","amount":"10","discount_tips":"每50减5，最高10元","stock":"10000","start_time":"2016-09-05 16:01:12","end_time":"2016-10-29 16:01:14","seckill_start_time":"1970-01-01 08:00:00","seckill_end_time":"1970-01-01 08:00:00","get_link":"tuniuapp:\/\/travel\/trainticket\/home","unget_link":"tuniuapp:\/\/travel\/trainticket\/home","description":"","style_type":"3","right_type":"1","left_label":"1","left_content":"首单专享","left_img":"http:\/\/m.tuniucdn.com\/fb2\/t1\/G2\/M00\/5A\/17\/Cii-T1fNJy6IGJvSAAAl2zGkNfwAACEqQP_aXQAACXz481.png","seckill_status":2,"is_over":0,"stock_reduce":4820,"getted_user_num":5180,"getted_per":51,"is_getted":0,"mark":"zzsq4t5w"},{"id":"152","special_type":"2","name":"国内酒店优惠券","amount":"10","discount_tips":"每订单立减10元","stock":"10000","start_time":"2016-07-20 12:02:32","end_time":"2016-12-01 12:02:36","seckill_start_time":"1970-01-01 08:00:00","seckill_end_time":"1970-01-01 08:00:00","get_link":"http:\/\/m.tuniu.com\/hotel","unget_link":"http:\/\/m.tuniu.com\/hotel","description":"","style_type":"3","right_type":"1","left_label":"1","left_content":"首单专享","left_img":"http:\/\/m.tuniucdn.com\/fb2\/t1\/G2\/M00\/47\/51\/Cii-T1e7-vKIDwRKAAAnMQUOds4AABn0wP_sHcAACdJ057.png","seckill_status":2,"is_over":0,"stock_reduce":2383,"getted_user_num":7617,"getted_per":76,"is_getted":0,"mark":"rt3wSpkp"},{"id":"180","special_type":"2","name":"国内长线优惠券","amount":"100","discount_tips":"每5000减50，最高100","stock":"10000","start_time":"2016-10-13 10:32:20","end_time":"2016-11-15 20:32:30","seckill_start_time":"1970-01-01 08:00:00","seckill_end_time":"1970-01-01 08:00:00","get_link":"http:\/\/m.tuniu.com\/h5\/domestic","unget_link":"http:\/\/m.tuniu.com\/h5\/domestic","description":"","style_type":"2","right_type":"1","left_label":"1","left_content":"","left_img":"http:\/\/m.tuniucdn.com\/fb2\/t1\/G2\/M00\/AB\/A3\/Cii-T1f-8pyIOX0GAAAbJxG1pDMAADUpgP_wnUAABs_012.png","seckill_status":2,"is_over":0,"stock_reduce":7438,"getted_user_num":2562,"getted_per":25,"is_getted":0,"mark":"w4mmiCpk"},{"id":"182","special_type":"2","name":"出境短线优惠券","amount":"100","discount_tips":"每5000减50，最高100","stock":"10000","start_time":"2016-10-13 10:35:43","end_time":"2016-11-15 20:35:45","seckill_start_time":"1970-01-01 08:00:00","seckill_end_time":"1970-01-01 08:00:00","get_link":"http:\/\/m.tuniu.com\/h5\/abroad","unget_link":"http:\/\/m.tuniu.com\/h5\/abroad","description":"","style_type":"2","right_type":"1","left_label":"1","left_content":"","left_img":"http:\/\/m.tuniucdn.com\/fb2\/t1\/G2\/M00\/AB\/A4\/Cii-T1f-83KIdaMUAAA2k91btgoAADUqQP_prkAADar406.png","seckill_status":2,"is_over":0,"stock_reduce":7934,"getted_user_num":2066,"getted_per":20,"is_getted":0,"mark":"4pipuomE"},{"id":"183","special_type":"2","name":"出境长线优惠券","amount":"200","discount_tips":"每5000减50，最高200","stock":"10000","start_time":"2016-10-13 10:35:43","end_time":"2016-11-15 20:35:45","seckill_start_time":"1970-01-01 08:00:00","seckill_end_time":"1970-01-01 08:00:00","get_link":"http:\/\/m.tuniu.com\/h5\/abroad","unget_link":"http:\/\/m.tuniu.com\/h5\/abroad","description":"","style_type":"2","right_type":"1","left_label":"1","left_content":"","left_img":"http:\/\/m.tuniucdn.com\/fb2\/t1\/G2\/M00\/AB\/A4\/Cii-TFf-86OIcv70AAAeyBYLCK0AADUqQP_3WQAAB7g351.png","seckill_status":2,"is_over":0,"stock_reduce":8162,"getted_user_num":1838,"getted_per":18,"is_getted":0,"mark":"s4xssoqF"},{"id":"181","special_type":"2","name":"周边游优惠券","amount":"20","discount_tips":"满500减20","stock":"10000","start_time":"2016-10-10 00:00:00","end_time":"2016-11-15 20:19:36","seckill_start_time":"1970-01-01 08:00:00","seckill_end_time":"1970-01-01 08:00:00","get_link":"http:\/\/m.tuniu.com\/h5\/around","unget_link":"http:\/\/m.tuniu.com\/h5\/around","description":"","style_type":"2","right_type":"1","left_label":"1","left_content":"","left_img":"http:\/\/m.tuniucdn.com\/fb2\/t1\/G2\/M00\/A3\/A9\/Cii-T1f58CqIHkR8AAAYwW72cQUAADMHAFZe2UAABjZ860.png","seckill_status":2,"is_over":0,"stock_reduce":7108,"getted_user_num":2892,"getted_per":28,"is_getted":0,"mark":"k4ouDkst"},{"id":"66","special_type":"2","name":"门票优惠券","amount":"5","discount_tips":"满100减5，最高5元","stock":"83000","start_time":"2016-08-11 10:03:03","end_time":"2016-10-31 18:00:00","seckill_start_time":"1970-01-01 08:00:00","seckill_end_time":"1970-01-01 08:00:00","get_link":"http:\/\/m.tuniu.com\/m2015\/mpChannel\/index","unget_link":"http:\/\/m.tuniu.com\/m2015\/mpChannel\/index","description":"","style_type":"2","right_type":"1","left_label":"1","left_content":"","left_img":"http:\/\/m.tuniucdn.com\/fb2\/t1\/G2\/M00\/47\/55\/Cii-TFe7_ECIHrHLAAAYL8OVUpsAABn2QP3274AABhH425.png","seckill_status":2,"is_over":0,"stock_reduce":29158,"getted_user_num":53842,"getted_per":64,"is_getted":0,"mark":"t1ljjtyQ"},{"id":"186","special_type":"2","name":"当地玩乐优惠券","amount":"5","discount_tips":"每订单立减5元","stock":"10000","start_time":"2016-09-13 15:41:21","end_time":"2016-12-30 15:42:31","seckill_start_time":"1970-01-01 08:00:00","seckill_end_time":"1970-01-01 08:00:00","get_link":"http:\/\/m.tuniu.com\/local\/","unget_link":"http:\/\/m.tuniu.com\/local\/","description":"","style_type":"2","right_type":"1","left_label":"1","left_content":"","left_img":"http:\/\/m.tuniucdn.com\/fb2\/t1\/G2\/M00\/66\/78\/Cii-TlfXrsqIElInAAAshCHKDDsAACWzgP8qvgAACyc614.png","seckill_status":2,"is_over":0,"stock_reduce":9797,"getted_user_num":203,"getted_per":2,"is_getted":0,"mark":"qti4jpxJ"},{"id":"176","special_type":"2","name":"火车票优惠券","amount":"5","discount_tips":"每100减5，最多10元","stock":"10000","start_time":"2016-09-05 16:07:07","end_time":"2016-10-29 16:07:10","seckill_start_time":"1970-01-01 08:00:00","seckill_end_time":"1970-01-01 08:00:00","get_link":"tuniuapp:\/\/travel\/trainticket\/home","unget_link":"tuniuapp:\/\/travel\/trainticket\/home","description":"","style_type":"2","right_type":"1","left_label":"1","left_content":"","left_img":"http:\/\/m.tuniucdn.com\/fb2\/t1\/G2\/M00\/5A\/18\/Cii-T1fNKAmIMQ3CAAAl2zGkNfwAACEqwP2GjwAACXz556.png","seckill_status":2,"is_over":0,"stock_reduce":7374,"getted_user_num":2626,"getted_per":26,"is_getted":0,"mark":"4ktm8jny"},{"id":"178","special_type":"2","name":"国内酒店优惠券","amount":"30","discount_tips":"每100减5，最高30","stock":"10000","start_time":"2016-09-20 13:43:58","end_time":"2016-12-23 13:44:01","seckill_start_time":"1970-01-01 08:00:00","seckill_end_time":"1970-01-01 08:00:00","get_link":"tuniuapp:\/\/travel\/hotel\/home","unget_link":"tuniuapp:\/\/travel\/hotel\/home","description":"","style_type":"2","right_type":"1","left_label":"1","left_content":"","left_img":"http:\/\/m.tuniucdn.com\/fb2\/t1\/G2\/M00\/72\/CC\/Cii-TFfgzeiIWo1nAAAnMQUOds4AACmDwKRVngAACdJ018.png","seckill_status":2,"is_over":0,"stock_reduce":7168,"getted_user_num":2832,"getted_per":28,"is_getted":0,"mark":"m4Axmouo"},{"id":"156","special_type":"2","name":"易到接送机券","amount":"40","discount_tips":"每订单立减40元","stock":"15000","start_time":"2016-07-29 14:29:38","end_time":"2016-10-31 14:29:41","seckill_start_time":"1970-01-01 08:00:00","seckill_end_time":"1970-01-01 08:00:00","get_link":"http:\/\/m.tuniu.com\/m2015\/pick\/index\/exit","unget_link":"http:\/\/m.tuniu.com\/m2015\/pick\/index\/exit","description":"","style_type":"2","right_type":"1","left_label":"1","left_content":"","left_img":"http:\/\/m.tuniucdn.com\/fb2\/t1\/G2\/M00\/47\/50\/Cii-TFe7-j2IQqWMAAAkN9oTFF8AABn0QMAhh0AACRP273.png","seckill_status":2,"is_over":0,"stock_reduce":6617,"getted_user_num":8383,"getted_per":55,"is_getted":0,"mark":"3vjWponi"},{"id":"177","special_type":"2","name":"国际机票优惠券","amount":"60","discount_tips":"满1000减60","stock":"10000","start_time":"2016-08-19 15:48:44","end_time":"2016-10-30 15:48:46","seckill_start_time":"1970-01-01 08:00:00","seckill_end_time":"1970-01-01 08:00:00","get_link":"tuniuapp:\/\/travel\/airlineticket\/home","unget_link":"tuniuapp:\/\/travel\/airlineticket\/home","description":"","style_type":"2","right_type":"1","left_label":"1","left_content":"","left_img":"http:\/\/m.tuniucdn.com\/fb2\/t1\/G2\/M00\/47\/51\/Cii-T1e7-rOIIlmkAAAgZ8Ikph0AABn0wLFk4YAACB_113.png","seckill_status":2,"is_over":0,"stock_reduce":8293,"getted_user_num":1707,"getted_per":17,"is_getted":0,"mark":"ziv49zsz"},{"id":"184","special_type":"2","name":"国际酒店优惠券","amount":"60","discount_tips":"每300减10，最高60","stock":"10000","start_time":"2016-09-20 13:43:58","end_time":"2016-11-17 13:44:01","seckill_start_time":"1970-01-01 08:00:00","seckill_end_time":"1970-01-01 08:00:00","get_link":"tuniuapp:\/\/travel\/hotel\/home","unget_link":"tuniuapp:\/\/travel\/hotel\/home","description":"","style_type":"2","right_type":"1","left_label":"1","left_content":"","left_img":"http:\/\/m.tuniucdn.com\/fb2\/t1\/G2\/M00\/7A\/8D\/Cii-T1fk9NCIGNAzAAAYyozfntEAACttQFD29sAABji416.png","seckill_status":2,"is_over":0,"stock_reduce":9383,"getted_user_num":617,"getted_per":6,"is_getted":0,"mark":"4mrGstpl"},{"id":"162","special_type":"2","name":"汽车票满减券","amount":"10","discount_tips":"每100减5，最高立减10","stock":"15000","start_time":"2016-07-19 11:07:20","end_time":"2016-10-30 00:00:00","seckill_start_time":"1970-01-01 08:00:00","seckill_end_time":"1970-01-01 08:00:00","get_link":"http:\/\/dynamic.m.tuniu.com\/coach","unget_link":"http:\/\/dynamic.m.tuniu.com\/coach","description":"","style_type":"2","right_type":"1","left_label":"1","left_content":"","left_img":"http:\/\/m.tuniucdn.com\/fb2\/t1\/G2\/M00\/47\/50\/Cii-TFe7-n6IKLmBAAAW7DXra3gAABn0gNmqdsAABcE134.png","seckill_status":2,"is_over":0,"stock_reduce":8533,"getted_user_num":6467,"getted_per":43,"is_getted":0,"mark":"3ckikswt"},{"id":"168","special_type":"2","name":"国内租车券","amount":"15","discount_tips":"满300减15","stock":"5000","start_time":"2016-10-19 13:31:10","end_time":"2016-12-30 13:31:16","seckill_start_time":"1970-01-01 08:00:00","seckill_end_time":"1970-01-01 08:00:00","get_link":"http:\/\/m.tuniu.com\/car\/","unget_link":"http:\/\/m.tuniu.com\/car\/","description":"","style_type":"2","right_type":"1","left_label":"1","left_content":"","left_img":"http:\/\/m.tuniucdn.com\/fb2\/t1\/G2\/M00\/B7\/0F\/Cii-TFgHBaGIXpe5AAAar9zHZjMAADhSAL73_sAABrH504.png","seckill_status":2,"is_over":0,"stock_reduce":2526,"getted_user_num":2474,"getted_per":49,"is_getted":0,"mark":"4mknvvu0"}]}}
def get_coupon_list():
    req = requests.get('http://dynamic.m.tuniu.com/event/couponCenter/MainCenter/SpecialListAjax?tab_id=9')
    logger.debug('GET %s \n%s' % (req.url, req.headers))
    try:
        return req.json()
    except Exception, e:
        raise HttpRequestException(e, {'function': 'get_coupon_list', 'method': 'get', 'url': req.url,
                                       'resp_content': req.content})


# GET http://dynamic.m.tuniu.com/event/common/getClickStaticsAjax?data=%7B%22mark%22%3A%22%E9%A2%86%E5%88%B8%E4%B8%AD%E5%BF%83_1_188%22%7D HTTP/1.1
# GET http: //dynamic.m.tuniu.com/event/couponCenter/MainCenter/getSpecialAjax?tab_id=1&mark=roji4Csq&tel=&q=1005 HTTP/1.1
# Host: dynamic.m.tuniu.com
# Connection: keep-alive
# Accept: application/json
# Origin: http://m.tuniu.com
# User-Agent: Mozilla/5.0 (Linux; Android 4.4.2; NX507J Build/KVT49L) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36
# Referer: http://m.tuniu.com/event/couponCenter/mainCenter/index?utm_source=morecoupon&utm_medium=couponcenter&q=1005
# Accept-Encoding: gzip,deflate
# Accept-Language: zh-CN,en-US;q=0.8
# Cookie: PageSwitch=2%2C1485173132; _tacau=MCwzYTY0MTU4Ni1mZDI3LTQyMWUtZDI3NS1kNGI1ZDEzNDU1ODcs; _tacz2=taccsr%3D%28direct%29%7Ctacccn%3D%28none%29%7Ctaccmd%3D%28none%29%7Ctaccct%3D%28none%29%7Ctaccrt%3D%28none%29; _taca=1477397184786.1477397184786.1477397184786.1; _tacc=1; SERVERID=dnionD; app_imei=863175026618021; ov=1; tuniuuser_id=53652883; tuniuuser_citycode=MTUwMg%3D%3D; TUNIUmuser=5076786a935835ceee9235bd41678fb4; sessionId=MQ==; token=OTRiOTA2NTFmNDU1MDg1Nw==; appVersion=9.0.6; tuniu_partner=MTU0NDcsMCwsOWIxMTFkNWY3NGQ1NmQ1NjdhNjEyZDQzYjEzYjVlYjI=; deviceType=1; SsoSession=5076786a935835ceee9235bd41678fb4; clientType=20; page_flag=; __utma=1.1665134217.1477397186.1477397186.1477397188.2; __utmb=1.4.10.1477397188; __utmc=1; __utmz=1.1477397188.2.2.utmcsr=morecoupon|utmccn=(not%20set)|utmcmd=couponcenter; _tact=NTExZDJiZTYtNGUxOS05Y2E2LWJlNjEtMTM0ZDMwYmMwNDRh; _tacb=NTFiZjQ2ZjgtZWZmNi1iYzUzLWFkNmQtZGQwMTZkZGQ4ZmU1
# X-Requested-With: com.tuniu.app.ui

# HTTP/1.1 200 OK
# Date: Wed, 26 Oct 2016 03:34:30 GMT
# Server: Apache
# Access-Control-Allow-Origin: http://m.tuniu.com
# Access-Control-Allow-Credentials: true
# cache-control: no-store,no-control,must-revalidate
# expires: Wed, 26 Oct 2016 03:34:29 GMT
# Vary: Accept-Encoding
# Content-Length: 16
# Content-Type: text/html
# Age: 0
# Connection: keep-alive
# Via: http/1.1 aca-CT-HNHY-226-127 (ACA/2.0)
#
# {"success":true}
def click_special_coupon(userid, sessionid, id):
    '''not need'''
    headers = {'content-type': 'application/json; charset=UTF-8',
               'User-Agent': base_data.get_user_agent(),
               'Origin': 'http://m.tuniu.com',
               'Referer': 'http://m.tuniu.com/event/couponCenter/mainCenter/index?utm_source=morecoupon&utm_medium=couponcenter&q=1005',
               'X-Requested-With': 'com.tuniu.app.ui',
               'Cookie': 'PageSwitch=2,%s; _tacau=MCwzYTY0MTU4Ni1mZDI3LTQyMWUtZDI3NS1kNGI1ZDEzNDU1ODcs; _tacz2=taccsr=(direct)|tacccn=(none)|taccmd=(none)|taccct=(none)|taccrt=(none); _taca=1477397184786.1477397184786.1477397184786.1; _tacc=1; SERVERID=dnionD; app_imei=%s; ov=1; tuniuuser_id=%d;  TUNIUmuser=%s; sessionId=MQ==; token=%s; appVersion=9.0.6; tuniu_partner=MTU0NDcsMCwsOWIxMTFkNWY3NGQ1NmQ1NjdhNjEyZDQzYjEzYjVlYjI=; deviceType=1; SsoSession=%s; clientType=20; page_flag=; __utma=1.1665134217.1477397186.1477397186.1477397188.2; __utmb=1.4.10.1477397188; __utmc=1; __utmz=1.1477397188.2.2.utmcsr=morecoupon|utmccn=(not set)|utmcmd=couponcenter; _tact=NTExZDJiZTYtNGUxOS05Y2E2LWJlNjEtMTM0ZDMwYmMwNDRh; _tacb=NTFiZjQ2ZjgtZWZmNi1iYzUzLWFkNmQtZGQwMTZkZGQ4ZmU1' % (
                   str(time.time()).replace('.', ''), base_data.get_random_number(), userid, sessionid,
                   base64.b64encode(base_data.get_random_letter_number()),sessionid)
               }
    # tuniuuser_citycode=MTUwMg%3D%3D;

    req = requests.get(
        'http://dynamic.m.tuniu.com/event/common/getClickStaticsAjax?data={"mark":"领券中心_1_%d"}' % id,
        headers=headers)
    try:
        return req.json()
    except Exception, e:
        raise HttpRequestException(e, {'function': 'click_special_coupon', 'method': 'get', 'url': req.url,
                                       'headers': headers,
                                       'resp_content': req.content})


# GET http://dynamic.m.tuniu.com/event/couponCenter/MainCenter/getSpecialAjax?tab_id=1&mark=4ymvx6kv&tel=&q=1005 HTTP/1.1
# Host: dynamic.m.tuniu.com
# Connection: keep-alive
# Accept: application/json
# X-Requested-With: XMLHttpRequest
# User-Agent: Mozilla/5.0 (Linux; Android 4.4.2; NX507J Build/KVT49L) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36
# Referer: http://dynamic.m.tuniu.com/event/couponCenter/mainCenter/index?utm_source=morecoupon&utm_medium=couponcenter&q=1005
# Accept-Encoding: gzip,deflate
# Accept-Language: zh-CN,en-US;q=0.8
# Cookie: PageSwitch=2%2C1485173132; _tacau=MCwzYTY0MTU4Ni1mZDI3LTQyMWUtZDI3NS1kNGI1ZDEzNDU1ODcs; _tacz2=taccsr%3D%28direct%29%7Ctacccn%3D%28none%29%7Ctaccmd%3D%28none%29%7Ctaccct%3D%28none%29%7Ctaccrt%3D%28none%29; _taca=1477397184786.1477397184786.1477397184786.1; _tacc=1; SERVERID=dnionD; app_imei=863175026618021; ov=1; tuniuuser_id=53652883; tuniuuser_citycode=MTUwMg%3D%3D; TUNIUmuser=7b42973d419cbe9cce81e0d15923593f; sessionId=MQ==; token=OTRiOTA2NTFmNDU1MDg1Nw==; appVersion=9.0.6; tuniu_partner=MTU0NDcsMCwsOWIxMTFkNWY3NGQ1NmQ1NjdhNjEyZDQzYjEzYjVlYjI=; deviceType=1; SsoSession=7b42973d419cbe9cce81e0d15923593f; clientType=20; page_flag=; __utma=1.1665134217.1477397186.1477397186.1477397188.2; __utmb=1.11.10.1477397188; __utmc=1; __utmz=1.1477397188.2.2.utmcsr=morecoupon|utmccn=(not%20set)|utmcmd=couponcenter; _tact=NTExZDJiZTYtNGUxOS05Y2E2LWJlNjEtMTM0ZDMwYmMwNDRh; _tacb=NTFiZjQ2ZjgtZWZmNi1iYzUzLWFkNmQtZGQwMTZkZGQ4ZmU1

# HTTP/1.1 200 OK
# Date: Tue, 25 Oct 2016 12:22:24 GMT
# Server: Apache
# Access-Control-Allow-Origin: http://m.tuniu.com,http://dynamic.m.tuniu.com
# Access-Control-Allow-Credentials: true
# cache-control: no-store,no-control,must-revalidate
# expires: Tue, 25 Oct 2016 12:22:23 GMT
# Vary: Accept-Encoding
# Content-Length: 56
# Content-Type: text/html
# Age: 2
# Connection: keep-alive
# Via: http/1.1 aca-CT-HNHY-226-127 (ACA/2.0)
#
# {"success":true,"errorCode":710000,"msg":"ok","data":[]}
def get_special_coupon(userid, sessionid, mark):
    headers = {'content-type': 'application/json; charset=UTF-8',
               'User-Agent': base_data.get_user_agent(),
               'Origin': 'http://m.tuniu.com',
               'Referer': 'http://m.tuniu.com/event/couponCenter/mainCenter/index?utm_source=morecoupon&utm_medium=couponcenter&q=1005',
               'X-Requested-With': 'com.tuniu.app.ui',
               'Cookie': 'PageSwitch=2,%s; _tacau=MCwzYTY0MTU4Ni1mZDI3LTQyMWUtZDI3NS1kNGI1ZDEzNDU1ODcs; _tacz2=taccsr=(direct)|tacccn=(none)|taccmd=(none)|taccct=(none)|taccrt=(none); _taca=1477397184786.1477397184786.1477397184786.1; _tacc=1; SERVERID=dnionD; app_imei=%s; ov=1; tuniuuser_id=%d;  TUNIUmuser=%s; sessionId=MQ==; token=%s; appVersion=9.0.6; tuniu_partner=MTU0NDcsMCwsOWIxMTFkNWY3NGQ1NmQ1NjdhNjEyZDQzYjEzYjVlYjI=; deviceType=1; SsoSession=%s; clientType=20; page_flag=; __utma=1.1665134217.1477397186.1477397186.1477397188.2; __utmb=1.4.10.1477397188; __utmc=1; __utmz=1.1477397188.2.2.utmcsr=morecoupon|utmccn=(not set)|utmcmd=couponcenter; _tact=NTExZDJiZTYtNGUxOS05Y2E2LWJlNjEtMTM0ZDMwYmMwNDRh; _tacb=NTFiZjQ2ZjgtZWZmNi1iYzUzLWFkNmQtZGQwMTZkZGQ4ZmU1' % (
                   str(time.time()).replace('.', ''), base_data.get_random_number(), userid, sessionid,
                   base64.b64encode(base_data.get_random_letter_number()), sessionid)
               }

    req = requests.get(
        'http://dynamic.m.tuniu.com/event/couponCenter/MainCenter/getSpecialAjax?tab_id=9&mark=%s&tel=&q=1005' % mark,
        headers=headers)
    logger.debug('GET %s \n%s' % (req.url, req.headers))
    try:
        return req.json()
    except Exception, e:
        raise HttpRequestException(e, {'function': 'click_special_coupon', 'method': 'get', 'url': req.url,
                                       'headers': headers,
                                       'resp_content': req.content})


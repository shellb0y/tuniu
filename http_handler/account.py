# -*- coding: utf-8 -*-
import base_data
import requests
import json
import time
import base64
from my_exception import *
import log_ex as logger


# GET https://m.tuniu.com/iapi/appserver/view/myAccountInfoV400?{"sessionID":"7b42973d419cbe9cce81e0d15923593f","r":"1477394962287","partner":15447,"clientType":20,"deviceType":1,"version":"8.1.6","_currentCityCode":"1502"} HTTP/1.1
#
# {"success":true,"msg":"success","errorCode":"710000","data":{"nickName":"8095327390","star":0,"starDesc":"注册会员","toSignOrdersCount":0,"toTravelOrdersCount":0,"toCommentOrdersCount":0,"favoriteCount":0,"couponValue":0,"travelCouponValue":0,"cashValue":0,"userProfile":{"phoneNumber":"15974253250","tel_country_id":40,"intl_code":"0086","email":"","sex":"9","marry":2,"birthday":"1980-01-01","idCardType":"0","baseHeardImg":"","cityId":"0","provinceId":"0","userName":"8095327390","nickName":"8095327390","userId":"58221448","realName":"","idCardNumber":"","largeAvatarUrl":"http:\/\/img4.tuniucdn.com\/site\/m2015\/images\/member\/vipform\/default.png","smallAvatarUrl":"http:\/\/img4.tuniucdn.com\/site\/m2015\/images\/member\/vipform\/default.png","provinceName":"","cityName":"","intl_tel":"008615974253250","level":0,"levelDescription":"注册会员","levelIcon":"https:\/\/img1.tuniucdn.com\/site\/wap\/img\/member\/level-2015-4\/level_0.png","additionalAddress":""},"travelCouponH5Url":"http:\/\/m.tuniu.com\/userCoupon\/travelCoupon","couponH5Url":"http:\/\/m.tuniu.com\/userCoupon\/coupon","cashH5Url":"http:\/\/m.tuniu.com\/userCash\/index"}}
def account_info(sessionid, partner):
    req = requests.get('https://m.tuniu.com/iapi/appserver/view/myAccountInfoV400?%s' % base64.b64encode(json.dumps(
        {"sessionID": sessionid, "r": time.time(), "partner": partner, "clientType": 20,
         "deviceType": 1, "version": "9.0.6"})), headers={'content-type': 'application/json; charset=UTF-8',
                                                          'User-Agent': base_data.get_user_agent()})  # "_currentCityCode": "1502"
    logger.debug('GET %s \n%s' % (req.url, req.headers))
    try:
        return json.loads(base64.b64decode(req.content))
    except Exception, e:
        raise HttpRequestException(e, {'function': 'account_info', 'method': 'get', 'url': req.url,
                                       'resp_content': req.content})


# GET http://dynamic.m.tuniu.com/japi/members/coupons/getCanUse?d=%7B%22page%22%3A1%2C%22limit%22%3A10%2C%22codeType%22%3A0%7D HTTP/1.1
# Host: dynamic.m.tuniu.com
# Connection: keep-alive
# Accept: application/json
# X-Requested-With: XMLHttpRequest
# User-Agent: Mozilla/5.0 (Linux; Android 4.4.2; NX507J Build/KVT49L) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36
# Referer: http://dynamic.m.tuniu.com/m2015/user/couponCodeV2
# Accept-Encoding: gzip,deflate
# Accept-Language: zh-CN,en-US;q=0.8
# Cookie: PageSwitch=2%2C1485312343; SERVERID=dnionA; _tacau=MCwxM2E5Y2VmYy00NzkxLWZmN2UtZDE4MS0xN2YyZTk5ODI5YzMs; _tacz2=taccsr%3D%28direct%29%7Ctacccn%3D%28none%29%7Ctaccmd%3D%28none%29%7Ctaccct%3D%28none%29%7Ctaccrt%3D%28none%29; _tacc=1; __utma=1.936861788.1477536396.1477536405.1477540316.3; __utmc=1; __utmz=1.1477536405.2.2.utmcsr=morecoupon|utmccn=(not%20set)|utmcmd=couponcenter; app_imei=863175026618021; from_url=%2FAPP%2Fandroid%2F%E9%95%BF%E6%B2%99%2F%E4%BC%9A%E5%91%98%2F%E4%BC%9A%E5%91%98%E4%B8%AD%E5%BF%83; ov=1; tuniuuser_id=53652991; tuniuuser_citycode=MTUwMg%3D%3D; TUNIUmuser=92cd6c593f3c81ba16414783a2c5fa8f; sessionId=NA==; token=OTRiOTA2NTFmNDU1MDg1Nw==; appVersion=8.1.6; tuniu_partner=MTU0NDcsMCwsOWIxMTFkNWY3NGQ1NmQ1NjdhNjEyZDQzYjEzYjVlYjI=; deviceType=1; SsoSession=92cd6c593f3c81ba16414783a2c5fa8f; clientType=20; page_flag=; _tact=N2Y3YWM0YjktYTJmNS00YmI1LTgzYTEtOGJmYTZjNDRhNzMw; _taca=1477536394951.1477540315879.1477549959409.3; _tacb=ZDQyNGJmYTEtOGUwNS04NTg0LWY0MTgtOGFhM2VlMWNlNzhj

# HTTP/1.1 200 OK
# Server: openresty/1.9.7.3
# Date: Thu, 27 Oct 2016 06:31:48 GMT
# Content-Type: application/json;charset=UTF-8
# Vary: Accept-Encoding
# Accept-Charset: big5, big5-hkscs, cesu-8, euc-jp, euc-kr, gb18030, gb2312, gbk, ibm-thai, ibm00858, ibm01140, ibm01141, ibm01142, ibm01143, ibm01144, ibm01145, ibm01146, ibm01147, ibm01148, ibm01149, ibm037, ibm1026, ibm1047, ibm273, ibm277, ibm278, ibm280, ibm284, ibm285, ibm290, ibm297, ibm420, ibm424, ibm437, ibm500, ibm775, ibm850, ibm852, ibm855, ibm857, ibm860, ibm861, ibm862, ibm863, ibm864, ibm865, ibm866, ibm868, ibm869, ibm870, ibm871, ibm918, iso-2022-cn, iso-2022-jp, iso-2022-jp-2, iso-2022-kr, iso-8859-1, iso-8859-13, iso-8859-15, iso-8859-2, iso-8859-3, iso-8859-4, iso-8859-5, iso-8859-6, iso-8859-7, iso-8859-8, iso-8859-9, jis_x0201, jis_x0212-1990, koi8-r, koi8-u, shift_jis, tis-620, us-ascii, utf-16, utf-16be, utf-16le, utf-32, utf-32be, utf-32le, utf-8, windows-1250, windows-1251, windows-1252, windows-1253, windows-1254, windows-1255, windows-1256, windows-1257, windows-1258, windows-31j, x-big5-hkscs-2001, x-big5-solaris, x-compound_text, x-euc-jp-linux, x-euc-tw, x-eucjp-open, x-ibm1006, x-ibm1025, x-ibm1046, x-ibm1097, x-ibm1098, x-ibm1112, x-ibm1122, x-ibm1123, x-ibm1124, x-ibm1364, x-ibm1381, x-ibm1383, x-ibm300, x-ibm33722, x-ibm737, x-ibm833, x-ibm834, x-ibm856, x-ibm874, x-ibm875, x-ibm921, x-ibm922, x-ibm930, x-ibm933, x-ibm935, x-ibm937, x-ibm939, x-ibm942, x-ibm942c, x-ibm943, x-ibm943c, x-ibm948, x-ibm949, x-ibm949c, x-ibm950, x-ibm964, x-ibm970, x-iscii91, x-iso-2022-cn-cns, x-iso-2022-cn-gb, x-iso-8859-11, x-jis0208, x-jisautodetect, x-johab, x-macarabic, x-maccentraleurope, x-maccroatian, x-maccyrillic, x-macdingbat, x-macgreek, x-machebrew, x-maciceland, x-macroman, x-macromania, x-macsymbol, x-macthai, x-macturkish, x-macukraine, x-ms932_0213, x-ms950-hkscs, x-ms950-hkscs-xp, x-mswin-936, x-pck, x-sjis_0213, x-utf-16le-bom, x-utf-32be-bom, x-utf-32le-bom, x-windows-50220, x-windows-50221, x-windows-874, x-windows-949, x-windows-950, x-windows-iso2022jp
# Age: 0
# Connection: keep-alive
# Via: http/1.1 aca-CT-HNHY-226-127 (ACA/2.0)
# Content-Length: 8138
#
# {"success":true,"msg":"success","errorCode":710000,"data":{"count":5,"list":[{"discountTitle":"65","codeType":3,"translatedFaceValue":"60元","codeState":2,"maxType":1,"maxDiscount":60,"topicUrl":"tuniuapp://travel/airlineticket/home","codeId":"9851I113","promotionName":"[券中心]国际机票60元优惠券","themeName":"会员专享（机票）","promotionRules":["每1000元立减60元"],"faceValue":"65","webShow":"1.该优惠用于APP预订国际机票（仅含票面价），最高可享受60元优惠，详细规则请至“途牛旅游APP-我的-优惠券”中查看。<br />2. 一个用户只可参与一次活动，限国际机票使用，且一次性使用，不拆分，不转赠，不提现，不与其他优惠券红包同时使用。<br />3. 使用名额有限，使用有效期以实际领取时提示的有效期为准，过期失效。<br />4. 本活动仅限最新版本用户参加。<br />5. 若发现参加活动用户存在不正当方式（包括但不限于恶意套现、机器作弊等），途牛旅游网有权在不事先通知情况下禁止其参与活动，取消优惠券使用资格并收回。<br />6. 参与活动订单若产生退票，则不退还优惠券，优惠金额收回，优惠金额优先从税费中抵扣，抵扣不完再从票价中扣除。<br />7. 在法律允许的范围内，途牛旅游网可能对活动的规则/条款作出适当修改或调整。<br />8. 若您参与活动，视为同意以上活动规则，本次活动的最终解释权归途牛旅游网所有。","clctType":"1","translatedRule":["每满1000元减60元(最多60元)"],"discountRule":"满1000元可用","effectiveDate":"2016-10-27至2016-11-11"},{"discountTitle":"30","codeType":3,"translatedFaceValue":"30元","codeState":2,"maxType":1,"maxDiscount":30,"topicUrl":"tuniuapp://travel/airlineticket/home","codeId":"EA121K14","promotionName":"[券中心]国内机票30元优惠券","themeName":"机票优惠券(会员)","promotionRules":["每800元立减10元"],"faceValue":"30","webShow":"1.该优惠用于APP预订机票（仅含票面价），最高可享受30元优惠，详细规则请至“途牛旅游APP-我的-优惠券”中查看。<br />2. 一个用户只可参与一次活动，限机票使用，且一次性使用，不拆分，不转赠，不提现，不与其他优惠券红包同时使用。<br />3. 使用名额有限，使用有效期以实际领取时提示的有效期为准，过期失效。<br />4. 本活动仅限最新版本用户参加。<br />5. 若发现参加活动用户存在不正当方式（包括但不限于恶意套现、机器作弊等），途牛旅游网有权在不事先通知情况下禁止其参与活动，取消优惠券使用资格并收回。<br />6. 参与活动订单若产生退票，则不退还优惠券，优惠金额收回，优惠金额优先从税费中抵扣，抵扣不完再从票价中扣除。<br />7. 在法律允许的范围内，途牛旅游网可能对活动的规则/条款作出适当修改或调整。<br />8. 若您参与活动，视为同意以上活动规则，本次活动的最终解释权归途牛旅游网所有。","clctType":"1","translatedRule":["每满800元减10元(最多30元)"],"discountRule":"每800元立减10元","effectiveDate":"2016-10-27至2016-11-11"},{"discountTitle":"20","codeType":3,"translatedFaceValue":"20元","codeState":2,"maxType":1,"maxDiscount":20,"topicUrl":"","codeId":"54K20F3I","promotionName":"注册用户专享红包（周边自驾）","themeName":"注册用户专享红包8期","promotionRules":["每500元立减20元"],"faceValue":"20","webShow":"1. 优惠券只适用于途牛网站注册用户（即在途牛旅游网注册但未有下单的用户），在途牛旅游预定周边自驾旅游线路产品使用,每满500减20，最高20。<br />2. 一个用户只可参与一次活动，且一次性使用，不拆分，不转赠，不提现，不与其他优惠券红包同时使用。<br />3. 8月31日后，已支付订单若产生退改，优惠券不予退还。<br />4. 若发现参加活动用户存在不正当方式（包括但不限于恶意套现、机器作弊等），途牛旅游网有权在不事先通知情况下禁止其参与活动，取消优惠券使用资格并收回。<br />5. 在法律允许的范围内，途牛旅游网可能对活动的规则/条款作出适当修改或调整。若您参与活动，视为同意以上活动规则，本次活动的最终解释权归途牛旅游网所有.<br />","clctType":"1","translatedRule":["每满500元减20元(最多20元)"],"discountRule":"满500元可用","effectiveDate":"2016-10-11至2016-11-16"},{"discountTitle":"10","codeType":3,"translatedFaceValue":"10元","codeState":2,"maxType":1,"maxDiscount":10,"topicUrl":"tuniuapp://travel/trainticket/home","codeId":"1ZJ8981Z","promotionName":"【领券中心】火车票优惠券10元-首单","themeName":"火车票优惠券第7期","promotionRules":["每50元立减5元"],"faceValue":"10","webShow":"1.火车票优惠券仅限在途牛旅游APP最新版本使用；<br />2.单笔订单只能使用一张火车票优惠券，最高可减10元，详细规则请至“途牛旅游APP-我的-优惠券”中查看；<br />3.火车票优惠券使用有效期以实际领取时提示的有效期为准，过期失效；<br />4.火车票优惠券仅能一次性使用，不转赠、不提现；<br />5.优惠券不能与其他优惠活动（包括但不限于银行优惠活动、会员优惠活动、新用户立减活动等）同时享用；<br />6.一个会员账号一个手机设备最多只能使用6次火车票红包（30天内，包括在其他渠道领取的途牛火车票红包）；<br />7.使用火车票优惠券购票成功的订单，若发生退改签，火车票优惠券不予退还，退票手续费将从实际支付金额中扣除；若购票失败，火车票优惠券予以退还；<br />8.参加活动的用户若存在不正当行为（包括但不限于恶意套现、机器作弊等），途牛旅游网在法律允许的范围内保留对本次活动的变更权，包括但不限于取消参与资格、取消所获得的奖励、暂停或取消本次活动等；<br />9.火车票优惠券使用规则的最终解释权归途牛旅游网所有。","clctType":"1","translatedRule":["每满50元减5元(最多10元)"],"discountRule":"每50元立减5元","effectiveDate":"2016-10-27至2016-11-26"},{"discountTitle":"10","codeType":3,"translatedFaceValue":"10元","codeState":2,"maxType":1,"maxDiscount":10,"topicUrl":"tuniuapp://travel/trainticket/home","codeId":"7PJL83DS","promotionName":"火车票10元券-新用户","themeName":"火车票第9期优惠券","promotionRules":["每10元立减5元"],"faceValue":"10","webShow":"1.火车票优惠券仅限在途牛旅游APP最新版本使用；<br />2.单笔订单只能使用一张火车票优惠券，最高可减10元，详细规则请至“途牛旅游APP-我的-优惠券”中查看；<br />3.火车票优惠券使用有效期以实际领取时提示的有效期为准，过期失效；<br />4.火车票优惠券仅能一次性使用，不转赠、不提现；<br />5.优惠券不能与其他优惠活动（包括但不限于银行优惠活动、会员优惠活动、新用户立减活动等）同时享用；<br />6.一个会员账号一个手机设备最多只能使用6次火车票红包（30天内，包括在其他渠道领取的途牛火车票红包）；<br />7.使用火车票优惠券购票成功的订单，若发生退改签，火车票优惠券不予退还，退票手续费将从实际支付金额中扣除；若购票失败，火车票优惠券予以退还；<br />8.参加活动的用户若存在不正当行为（包括但不限于恶意套现、机器作弊等），途牛旅游网在法律允许的范围内保留对本次活动的变更权，包括但不限于取消参与资格、取消所获得的奖励、暂停或取消本次活动等；<br />9.火车票优惠券使用规则的最终解释权归途牛旅游网所有。","clctType":"1","translatedRule":["每满10元减5元(最多10元)"],"discountRule":"每10元立减5元","effectiveDate":"2016-10-26至2016-11-10"}]}}
def get_account_coupon(userid, sessionid):
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
        'http://dynamic.m.tuniu.com/japi/members/coupons/getCanUse?d=%7B%22page%22%3A1%2C%22limit%22%3A20%2C%22codeType%22%3A0%7D',
        headers=headers)

    logger.debug('GET %s \n%s' % (req.url, req.headers))

    try:
        return req.json()
    except Exception, e:
        raise HttpRequestException(e, {'function': 'get_account_coupon', 'method': 'get', 'url': req.url,
                                       'headers': headers,
                                       'resp_content': req.content})


# GET http://m.tuniu.com/api/train/order/getMyCoupons?d=%7B%22trainNumber%22%3A%22K472%22%2C%22startStationName%22%3A%22%E9%95%BF%E6%B2%99%E7%AB%99%22%2C%22sessionId%22%3A%2292cd6c593f3c81ba16414783a2c5fa8f%22%2C%22arrivalStationName%22%3A%22%E5%8C%97%E4%BA%AC%E8%A5%BF%E7%AB%99%22%2C%22departureCityCode%22%3A%221502%22%2C%22departDate%22%3A%222016-10-28%22%2C%22adultPrice%22%3A343.5%2C%22insurancePrice%22%3A20%2C%22seatId%22%3A353438822%2C%22childCount%22%3A0%2C%22adultCount%22%3A1%2C%22absId%22%3A0%7D&c=%7B%22v%22%3A%228.1.6%22%2C%22ct%22%3A20%2C%22dt%22%3A1%2C%22ov%22%3A1%2C%22p%22%3A15447%2C%22cc%22%3A1502%7D HTTP/1.1
# sid: edb19a25-386c-40e4-bd61-84897965a9b1
# User-Agent: TuNiuApp/8.1.6/Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX507J Build/KVT49L)
# host: m.tuniu.com
# Connection: Keep-Alive
# Accept-Encoding: gzip

# HTTP/1.1 200 OK
# Date: Thu, 27 Oct 2016 06:38:54 GMT
# Server: nginx
# Content-Type: text/html; charset=utf-8
# X-Via: 1.1 szhj11:4 (Cdn Cache Server V2.0), 1.1 shydx35:7 (Cdn Cache Server V2.0)
# Connection: keep-alive
# Content-Length: 10621
#
# {"success":true,"errorCode":710000,"msg":"OK","data":{"sortData":[{"type":1,"number":"126246","title":"活动名称","name":"【领券中心】火车票优惠券10元-首单","remark":"优惠码活动","usageRules":"1.火车票优惠券仅限在途牛旅游APP最新版本使用；\\r\\n2.单笔订单只能使用一张火车票优惠券，最高可减10元，详细规则请至“途牛旅游APP-我的-优惠券”中查看；\\r\\n3.火车票优惠券使用有效期以实际领取时提示的有效期为准，过期失效；\\r\\n4.火车票优惠券仅能一次性使用，不转赠、不提现；\\r\\n5.优惠券不能与其他优惠活动（包括但不限于银行优惠活动、会员优惠活动、新用户立减活动等）同时享用；\\r\\n6.一个会员账号一个手机设备最多只能使用6次火车票红包（30天内，包括在其他渠道领取的途牛火车票红包）；\\r\\n7.使用火车票优惠券购票成功的订单，若发生退改签，火车票优惠券不予退还，退票手续费将从实际支付金额中扣除；若购票失败，火车票优惠券予以退还；\\r\\n8.参加活动的用户若存在不正当行为（包括但不限于恶意套现、机器作弊等），途牛旅游网在法律允许的范围内保留对本次活动的变更权，包括但不限于取消参与资格、取消所获得的奖励、暂停或取消本次活动等；\\r\\n9.火车票优惠券使用规则的最终解释权归途牛旅游网所有。","webUsageRules":"1.火车票优惠券仅限在途牛旅游APP最新版本使用；<br \/>2.单笔订单只能使用一张火车票优惠券，最高可减10元，详细规则请至“途牛旅游APP-我的-优惠券”中查看；<br \/>3.火车票优惠券使用有效期以实际领取时提示的有效期为准，过期失效；<br \/>4.火车票优惠券仅能一次性使用，不转赠、不提现；<br \/>5.优惠券不能与其他优惠活动（包括但不限于银行优惠活动、会员优惠活动、新用户立减活动等）同时享用；<br \/>6.一个会员账号一个手机设备最多只能使用6次火车票红包（30天内，包括在其他渠道领取的途牛火车票红包）；<br \/>7.使用火车票优惠券购票成功的订单，若发生退改签，火车票优惠券不予退还，退票手续费将从实际支付金额中扣除；若购票失败，火车票优惠券予以退还；<br \/>8.参加活动的用户若存在不正当行为（包括但不限于恶意套现、机器作弊等），途牛旅游网在法律允许的范围内保留对本次活动的变更权，包括但不限于取消参与资格、取消所获得的奖励、暂停或取消本次活动等；<br \/>9.火车票优惠券使用规则的最终解释权归途牛旅游网所有。","beginDate":"2016-08-31","endDate":"2016-12-31","expireDays":65,"reduction":10},{"type":1,"number":"129308","title":"活动名称","name":"火车票10元券-新用户","remark":"优惠码活动","usageRules":"1.火车票优惠券仅限在途牛旅游APP最新版本使用；\\r\\n2.单笔订单只能使用一张火车票优惠券，最高可减10元，详细规则请至“途牛旅游APP-我的-优惠券”中查看；\\r\\n3.火车票优惠券使用有效期以实际领取时提示的有效期为准，过期失效；\\r\\n4.火车票优惠券仅能一次性使用，不转赠、不提现；\\r\\n5.优惠券不能与其他优惠活动（包括但不限于银行优惠活动、会员优惠活动、新用户立减活动等）同时享用；\\r\\n6.一个会员账号一个手机设备最多只能使用6次火车票红包（30天内，包括在其他渠道领取的途牛火车票红包）；\\r\\n7.使用火车票优惠券购票成功的订单，若发生退改签，火车票优惠券不予退还，退票手续费将从实际支付金额中扣除；若购票失败，火车票优惠券予以退还；\\r\\n8.参加活动的用户若存在不正当行为（包括但不限于恶意套现、机器作弊等），途牛旅游网在法律允许的范围内保留对本次活动的变更权，包括但不限于取消参与资格、取消所获得的奖励、暂停或取消本次活动等；\\r\\n9.火车票优惠券使用规则的最终解释权归途牛旅游网所有。","webUsageRules":"1.火车票优惠券仅限在途牛旅游APP最新版本使用；<br \/>2.单笔订单只能使用一张火车票优惠券，最高可减10元，详细规则请至“途牛旅游APP-我的-优惠券”中查看；<br \/>3.火车票优惠券使用有效期以实际领取时提示的有效期为准，过期失效；<br \/>4.火车票优惠券仅能一次性使用，不转赠、不提现；<br \/>5.优惠券不能与其他优惠活动（包括但不限于银行优惠活动、会员优惠活动、新用户立减活动等）同时享用；<br \/>6.一个会员账号一个手机设备最多只能使用6次火车票红包（30天内，包括在其他渠道领取的途牛火车票红包）；<br \/>7.使用火车票优惠券购票成功的订单，若发生退改签，火车票优惠券不予退还，退票手续费将从实际支付金额中扣除；若购票失败，火车票优惠券予以退还；<br \/>8.参加活动的用户若存在不正当行为（包括但不限于恶意套现、机器作弊等），途牛旅游网在法律允许的范围内保留对本次活动的变更权，包括但不限于取消参与资格、取消所获得的奖励、暂停或取消本次活动等；<br \/>9.火车票优惠券使用规则的最终解释权归途牛旅游网所有。","beginDate":"2016-10-19","endDate":"2016-12-31","expireDays":65,"reduction":10}],"invalidData":[],"bindCouponUrl":"http:\/\/dynamic.m.tuniu.com\/m2015\/user\/couponCode"}}
def get_account_train_order_can_use_coupon(order, sessionid, partner, cc):
    headers = {'User-Agent': base_data.get_user_agent()}
    params = {'d': json.dumps(
        {"trainNumber": order['trainNumber'], "startStationName": order['startStationName'], "sessionId": sessionid,
         "arrivalStationName": order['arrivalStationName'], "departureCityCode": order['departureCityCode'],
         "departDate": order['departDate'],
         "adultPrice": order['adultPrice'], "insurancePrice": 0, "childCount": 0,
         "adultCount": 1,
         "absId": 0}), 'c': json.dumps({"v": "9.0.6", "ct": 20, "dt": 1, "ov": 1, "p": partner, "cc": cc})}
    # "seatId": order['seatId'],
    req = requests.get(
        'http://m.tuniu.com/api/train/order/getMyCoupons', params=params, headers=headers)

    logger.debug('GET %s \n%s' % (req.url, req.headers))

    try:
        return req.json()
    except Exception, e:
        raise HttpRequestException(e, {'function': 'get_account_coupon', 'method': 'get', 'url': req.url,
                                       'headers': headers,
                                       'resp_content': req.content})

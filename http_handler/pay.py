# -*- coding: utf-8 -*-

import requests
import json
import hashlib
import base64
from my_exception import *
import log_ex as logger
import rsa
import base_data


# POST /fmp-web/app/order/submit HTTP/1.1
# Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4
# baseParams: eyJmaW5nZXJQcmludCI6IiIsInNlc3Npb25JZCI6ImE2OTkyMTIwMDA1NGEzNjE5Y2E3ODQ4YmJiMjc5MjVjIiwidGVybUFwcFZlcnNpb24iOiIxLjMuOSIsInRlcm1TeXNWZXJzaW9uIjoiNC40LjIiLCJ0ZXJtTW9kZWwiOiJudWJpYSBOWDUwN0oiLCJhcHBUeXBlIjoyLCJwbGF0Zm9ybUlkIjoxLCJuZXR3b3JrIjoiV0lGSSIsInRlcm1JZCI6IjFiOTA4OGNiLTRiZGMtNGVmMy1hZjM5LTQ2OTEzNGQ0YmM0NCJ9
# {"fingerPrint":"","sessionId":"a69921200054a3619ca7848bbb27925c","termAppVersion":"1.3.9","termSysVersion":"4.4.2","termModel":"nubia NX507J","appType":2,"platformId":1,"network":"WIFI","termId":"1b9088cb-4bdc-4ef3-af39-469134d4bc44"}
# Content-Type: application/x-www-form-urlencoded; charset=UTF-8
# User-Agent: Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX507J Build/KVT49L)
# Host: jr.tuniu.com
# Connection: Keep-Alive
# Accept-Encoding: gzip
# Content-Length: 408
#
# eyJiaXpJZCI6MzgsImJpek9yZGVySWQiOiIxMDA1MDk1NDEwIiwiZW5jb2RlVG90YWxBbW91bnQiOiJCbEwxcy9WVStvOGptZWVEVG5tWkNqd3VjSlF3Mm50TTk2VHhrallMaFhPMTdhaGlpRGpwWnIvVUVNT1FnMm9vRHZoK1QwQm1vK3dzXG5XYlF3aUhVUHlhbXF6M0tpeW1jVmdBaHE1czk2ajhTTHFRNk43NUlYS1BiMmk5NTNJY1FRMWxkeTkrZU1EZ2JIR1g5NEhMK1dNQzMrXG5UVUJ3OU43MkswbjN1b0JNa2UwXHUwMDNkXG4iLCJzaWduIjoiM2JkZjNkZWUyZjY1YTA0YzQwNTQ5MmU1ODMyNjcyYjciLCJ1c2VySWQiOiI1MzY1Mjg4MyJ9
# {"bizId":38,"bizOrderId":"1005095410","encodeTotalAmount":"BlL1s/VU+o8jmeeDTnmZCjwucJQw2ntM96TxkjYLhXO17ahiiDjpZr/UEMOQg2ooDvh+T0Bmo+ws\nWbQwiHUPyamqz3KiymcVgAhq5s96j8SLqQ6N75IXKPb2i953IcQQ1ldy9+eMDgbHGX94HL+WMC3+\nTUBw9N72K0n3uoBMke0\u003d\n","sign":"3bdf3dee2f65a04c405492e5832672b7","userId":"53652883"}

#
# HTTP/1.1 200 OK
# Server: Apache-Coyote/1.1
# Access-Control-Allow-Origin: *
# Content-Type: application/json;charset=UTF-8
# Date: Thu, 03 Nov 2016 03:43:00 GMT
# Transfer-Encoding: chunked
# Connection: Keep-alive
#
# eyJzdWNjZXNzIjp0cnVlLCJtc2ciOm51bGwsImVycm9yQ29kZSI6MCwiZGF0YSI6eyJpc1NwbGl0T3JkZXIiOmZhbHNlLCJzcGxpdE1pblNpbmdsZUFtb3VudCI6bnVsbCwicmVtYWluQW1vdW50IjoiNTczLjAiLCJvcmRlcklkIjoiMTQxMDUyNDEiLCJwYXlTcGxpdERlc2MiOiLliIbmrKHph5Hpop3lsI/kuo42LjAw5YWD5LiN6IO95Lqr5Y+X6YCU54mb6ZKx5YyF56uL5YeP5LyY5oOgIiwicGF5TG9hbkRlc2MiOiLpppbku5jph5Hpop3lsI/kuo42LjAw5YWD5LiN6IO95Lqr5Y+X6YCU54mb6ZKx5YyF56uL5YeP5LyY5oOgIiwidXNlckF2YWlsYWJsZUNhcmRMaXN0IjpbXSwicGF5V2F5TGlzdCI6W3sicGF5TWV0aG9kIjozLCJtZXRob2RDb2RlIjoxMCwibWV0aG9kTmFtZSI6IumAlOeJm+mSseWMhSIsIm1ldGhvZERlc2MiOiLlpKfpop3orqLljZXmm7Tkvr/mjbcg5pyJ5py65Lya6LWi5Y+WMzAwMOWFg+Wkp+WlliIsImRlc2NGb250UmdiIjoiI2VlMjIyMiIsInBheUNoYW5uZWwiOjIxLCJjaGFubmVsQWN0aXZpdHkiOiLnq4vlh481LjAw5YWDIiwiaXNBY3Rpdml0eSI6dHJ1ZSwidG90YWxCYWxhbmNlIjoiMCIsImF2YWlsYWJsZUJhbGFuY2UiOiIwIiwicmFuayI6MSwibm90VmFsaWREZXNjIjoiIiwidmFsaWQiOnRydWUsInVzZUJhbmsiOnRydWUsIm5vZGVUeXBlIjoxLCJvdGhlcldheUxpc3QiOltdLCJpc0xhcmdlUGF5IjpmYWxzZX0seyJwYXlNZXRob2QiOjMsIm1ldGhvZENvZGUiOjUsIm1ldGhvZE5hbWUiOiLpk7booYzljaHmlK/ku5giLCJtZXRob2REZXNjIjoi5YKo6JOE5Y2hL+S/oeeUqOWNoeaUr+S7mCDmnInmnLrkvJrotaLlj5YzMDAw5YWD5aSn5aWWIiwiZGVzY0ZvbnRSZ2IiOiIjZWUyMjIyIiwicGF5Q2hhbm5lbCI6MCwiY2hhbm5lbEFjdGl2aXR5IjoiIiwiaXNBY3Rpdml0eSI6ZmFsc2UsInRvdGFsQmFsYW5jZSI6IjAiLCJhdmFpbGFibGVCYWxhbmNlIjoiMCIsInJhbmsiOjIsIm5vdFZhbGlkRGVzYyI6IiIsInZhbGlkIjp0cnVlLCJ1c2VCYW5rIjp0cnVlLCJub2RlVHlwZSI6MSwib3RoZXJXYXlMaXN0IjpbXSwiaXNMYXJnZVBheSI6ZmFsc2V9LHsicGF5TWV0aG9kIjoxMSwibWV0aG9kQ29kZSI6MywibWV0aG9kTmFtZSI6IuW+ruS/oeaUr+S7mCIsIm1ldGhvZERlc2MiOiLlronlhajkvr/mjbciLCJwYXlDaGFubmVsIjoxMiwiY2hhbm5lbEFjdGl2aXR5IjoiIiwiaXNBY3Rpdml0eSI6ZmFsc2UsInRvdGFsQmFsYW5jZSI6IjAiLCJhdmFpbGFibGVCYWxhbmNlIjoiMCIsInJhbmsiOjMsIm5vdFZhbGlkRGVzYyI6IiIsInZhbGlkIjp0cnVlLCJ1c2VCYW5rIjpmYWxzZSwibm9kZVR5cGUiOjEsIm90aGVyV2F5TGlzdCI6W10sImlzTGFyZ2VQYXkiOmZhbHNlfSx7InBheU1ldGhvZCI6MTEsIm1ldGhvZENvZGUiOjIsIm1ldGhvZE5hbWUiOiLmlK/ku5jlrp3mlK/ku5giLCJtZXRob2REZXNjIjoiIiwicGF5Q2hhbm5lbCI6OSwiY2hhbm5lbEFjdGl2aXR5IjoiIiwiaXNBY3Rpdml0eSI6ZmFsc2UsInRvdGFsQmFsYW5jZSI6IjAiLCJhdmFpbGFibGVCYWxhbmNlIjoiMCIsInJhbmsiOjUsIm5vdFZhbGlkRGVzYyI6IiIsInZhbGlkIjp0cnVlLCJ1c2VCYW5rIjpmYWxzZSwibm9kZVR5cGUiOjEsIm90aGVyV2F5TGlzdCI6W10sImlzTGFyZ2VQYXkiOmZhbHNlfSx7InBheU1ldGhvZCI6MTEsIm1ldGhvZENvZGUiOjQsIm1ldGhvZE5hbWUiOiLpk7bogZTmlK/ku5giLCJtZXRob2REZXNjIjoi5Y+v5Y+C5Yqg6ZO26IGU5rS75YqoIiwicGF5Q2hhbm5lbCI6MTAsImNoYW5uZWxBY3Rpdml0eSI6IiIsImlzQWN0aXZpdHkiOmZhbHNlLCJ0b3RhbEJhbGFuY2UiOiIwIiwiYXZhaWxhYmxlQmFsYW5jZSI6IjAiLCJyYW5rIjo2LCJub3RWYWxpZERlc2MiOiIiLCJ2YWxpZCI6dHJ1ZSwidXNlQmFuayI6ZmFsc2UsIm5vZGVUeXBlIjoxLCJvdGhlcldheUxpc3QiOltdLCJpc0xhcmdlUGF5IjpmYWxzZX1dLCJsYXJnZVBheUluZm8iOm51bGwsInNtYWxsUGF5SW5mbyI6bnVsbCwiY3JlZGl0SW5mbyI6eyJzdXBwb3J0SW5zdGFsbWVudCI6ZmFsc2UsInBhaWREZXNjIjpudWxsLCJsaW5rVXJsIjpudWxsLCJvcGVuU3RhdHVzIjpudWxsLCJidXR0b25Db250ZW50IjpudWxsLCJidXR0b25EZXNjIjpudWxsLCJzZWxlY3RVc2VGbGFnIjpmYWxzZSwiYXZhaVF1b3RhRGVzYyI6bnVsbCwiY3VyckJpelR5cGUiOm51bGwsImN1cnJUZXJtIjpudWxsLCJjdXJyVGVybURlc2MiOm51bGwsImN1cnJQZXJpb2REZXNjIjpudWxsLCJjdXJyTmVlZERvd25wYXltZW50IjpudWxsLCJhY3Rpdml0eUZsYWciOjAsImljb25VcmwiOm51bGwsImNyZWRpdE5hbWUiOm51bGwsInBsYW5zIjpbXSwicGF5Q2hhbm5lbCI6bnVsbCwicGF5TWV0aG9kIjpudWxsLCJhY3RJbWdVcmwiOm51bGwsImFjdGl2aXR5RGVzYyI6bnVsbH0sImNhc2hpZXJUeXBlIjoxLCJwbWZDYXJkTGlzdCI6W10sInBtZkFkZENhcmQiOnsiZW5hYmxlQWRkIjpmYWxzZSwicGF5Q2hhbm5lbCI6bnVsbCwicGF5TWV0aG9kIjpudWxsfSwicmVzdFNlY29uZHMiOiIxNzk0Iiwib3JkZXJOYW1lIjoi5Zu95YaF54Gr6L2m56WoIn19
# {"success":true,"msg":null,"errorCode":0,"data":{"isSplitOrder":false,"splitMinSingleAmount":null,"remainAmount":"573.0","orderId":"14105241","paySplitDesc":"分次金额小于6.00元不能享受途牛钱包立减优惠","payLoanDesc":"首付金额小于6.00元不能享受途牛钱包立减优惠","userAvailableCardList":[],"payWayList":[{"payMethod":3,"methodCode":10,"methodName":"途牛钱包","methodDesc":"大额订单更便捷 有机会赢取3000元大奖","descFontRgb":"#ee2222","payChannel":21,"channelActivity":"立减5.00元","isActivity":true,"totalBalance":"0","availableBalance":"0","rank":1,"notValidDesc":"","valid":true,"useBank":true,"nodeType":1,"otherWayList":[],"isLargePay":false},{"payMethod":3,"methodCode":5,"methodName":"银行卡支付","methodDesc":"储蓄卡/信用卡支付 有机会赢取3000元大奖","descFontRgb":"#ee2222","payChannel":0,"channelActivity":"","isActivity":false,"totalBalance":"0","availableBalance":"0","rank":2,"notValidDesc":"","valid":true,"useBank":true,"nodeType":1,"otherWayList":[],"isLargePay":false},{"payMethod":11,"methodCode":3,"methodName":"微信支付","methodDesc":"安全便捷","payChannel":12,"channelActivity":"","isActivity":false,"totalBalance":"0","availableBalance":"0","rank":3,"notValidDesc":"","valid":true,"useBank":false,"nodeType":1,"otherWayList":[],"isLargePay":false},{"payMethod":11,"methodCode":2,"methodName":"支付宝支付","methodDesc":"","payChannel":9,"channelActivity":"","isActivity":false,"totalBalance":"0","availableBalance":"0","rank":5,"notValidDesc":"","valid":true,"useBank":false,"nodeType":1,"otherWayList":[],"isLargePay":false},{"payMethod":11,"methodCode":4,"methodName":"银联支付","methodDesc":"可参加银联活动","payChannel":10,"channelActivity":"","isActivity":false,"totalBalance":"0","availableBalance":"0","rank":6,"notValidDesc":"","valid":true,"useBank":false,"nodeType":1,"otherWayList":[],"isLargePay":false}],"largePayInfo":null,"smallPayInfo":null,"creditInfo":{"supportInstalment":false,"paidDesc":null,"linkUrl":null,"openStatus":null,"buttonContent":null,"buttonDesc":null,"selectUseFlag":false,"avaiQuotaDesc":null,"currBizType":null,"currTerm":null,"currTermDesc":null,"currPeriodDesc":null,"currNeedDownpayment":null,"activityFlag":0,"iconUrl":null,"creditName":null,"plans":[],"payChannel":null,"payMethod":null,"actImgUrl":null,"activityDesc":null},"cashierType":1,"pmfCardList":[],"pmfAddCard":{"enableAdd":false,"payChannel":null,"payMethod":null},"restSeconds":"1794","orderName":"国内火车票"}}

def submit(parms):
    headers = {'User-Agent': 'TuNiuApp/9.0.6/Dalvik/1.6.0 (Linux; U; Android 4.2.2)',
               'baseParams': base64.b64encode(json.dumps({"fingerPrint": "", "sessionId": parms['sessionId'],
                                                          "termAppVersion": "1.3.9", "termSysVersion": "4.4.2",
                                                          "termModel": "",
                                                          "appType": 2, "platformId": 1, "network": "WIFI",
                                                          "termId": parms['termId']}))}

    url = 'https://jr.tuniu.com/fmp-web/app/order/submit'
    data = {"bizId": 38, "bizOrderId": parms['orderId'], "encodeTotalAmount": rsa.encode(parms['price']), "sign": "",
            "userId": parms['userId']}
    data['sign'] = hashlib.md5(('bizId=38&bizOrderId=%s&encodeTotalAmount=%s&userId=%d' % (
        data['bizOrderId'], data['encodeTotalAmount'], data['userId'])) + '&*()%sd76@#$Dfs^YsfUJKDs').hexdigest()

    base64_data = base64.b64encode(json.dumps(data))
    req = requests.post(url, data=base64_data, headers=headers)

    logger.debug('POST %s\n%s\n%s\n%s' % (req.url, json.dumps(headers), data, base64_data))
    try:
        resp = json.loads(base64.b64decode(req.text))
        return resp
    except Exception, e:
        raise HttpRequestException(e, {'function': 'order_submit', 'method': 'post', 'url': req.url,
                                       'headers': headers, 'data': data,
                                       'resp_content': req.content})


# POST /fmp-web/pay/confirm HTTP/1.1
# Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4
# baseParams: eyJmaW5nZXJQcmludCI6IiIsInNlc3Npb25JZCI6ImE2OTkyMTIwMDA1NGEzNjE5Y2E3ODQ4YmJiMjc5MjVjIiwidGVybUFwcFZlcnNpb24iOiIxLjMuOSIsInRlcm1TeXNWZXJzaW9uIjoiNC40LjIiLCJ0ZXJtTW9kZWwiOiJudWJpYSBOWDUwN0oiLCJhcHBUeXBlIjoyLCJwbGF0Zm9ybUlkIjoxLCJuZXR3b3JrIjoiV0lGSSIsInRlcm1JZCI6IjFiOTA4OGNiLTRiZGMtNGVmMy1hZjM5LTQ2OTEzNGQ0YmM0NCJ9
# Content-Type: application/x-www-form-urlencoded; charset=UTF-8
# User-Agent: Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX507J Build/KVT49L)
# Host: jr.tuniu.com
# Connection: Keep-Alive
# Accept-Encoding: gzip
# Content-Length: 472
#
# eyJkb3duUGF5bWVudEZsYWciOjAsImVuY29kZVRvdGFsQW1vdW50IjoiZFVESXRSL2dKZkxsallzSkUvT0VTNTJ6aWRoTnd3TXZuMkF3VHNrUU9NcE9iSFJKOGVsQnRhcmNXc3VSQ1FMRi9EQjYxTURHZ21yQVxueXFLbTduci9xbHJWSlFOVzljUEkrT3E2aTRrTTE4OGNvQU16bXZZK0xNKzRKUHp4elJCUThyV1JyNmdwV2k5RnZVa21jNFdNakdTQ1xucVorbDBhOENPOHptRmV1M2dGNFx1MDAzZFxuIiwib3JkZXJJZCI6IjE0MTA1MjQxIiwib3JkZXJUeXBlIjoxLCJwYXlDaGFubmVsIjo5LCJwYXlNZXRob2QiOjExLCJzaWduIjoiYjkxNjBmYTM3N2U1ZmJhYTcwYmViMWI4ODRiNDVlNDgiLCJ1c2VySWQiOiI1MzY1Mjg4MyJ9
# {"downPaymentFlag":0,"encodeTotalAmount":"dUDItR/gJfLljYsJE/OES52zidhNwwMvn2AwTskQOMpObHRJ8elBtarcWsuRCQLF/DB61MDGgmrA\nyqKm7nr/qlrVJQNW9cPI+Oq6i4kM188coAMzmvY+LM+4JPzxzRBQ8rWRr6gpWi9FvUkmc4WMjGSC\nqZ+l0a8CO8zmFeu3gF4\u003d\n","orderId":"14105241","orderType":1,"payChannel":9,"payMethod":11,"sign":"b9160fa377e5fbaa70beb1b884b45e48","userId":"53652883"}

# HTTP/1.1 200 OK
# Server: Apache-Coyote/1.1
# Access-Control-Allow-Origin: *
# Content-Type: application/json;charset=UTF-8
# Date: Thu, 03 Nov 2016 03:44:53 GMT
# Transfer-Encoding: chunked
# Connection: Keep-alive
#
# eyJzdWNjZXNzIjp0cnVlLCJtc2ciOiLmk43kvZzmiJDlip8iLCJlcnJvckNvZGUiOjAsImRhdGEiOnsicmVxdWVzdCI6bnVsbCwib3JkZXJUeXBlIjoyLCJmaW5hbE9yZGVySWQiOjY5NTIzODUsInVybCI6Il9pbnB1dF9jaGFyc2V0PXV0Zi04JmJvZHk9JUU4JUFFJUEyJUU1JThEJTk1JUU1JThGJUI3JUVGJUJDJTlBMTAwNTA5NTQxMCZpdF9iX3BheT0yOG0mbm90aWZ5X3VybD1odHRwJTNBJTJGJTJGY2FzaGllci50dW5pdS5jb20lMkZhbGlwYXklMkZhcHBwYXlOb3RpZnkmb3V0X3RyYWRlX25vPTAwMzgwMDAwNjk1MjM4NTExMDkwNjI0MjQwMDU3MzAwJnBhcnRuZXI9MjA4ODcwMTc4MTQyMTY4MyZwYXltZW50X3R5cGU9MSZzZWxsZXJfaWQ9eGlvbmdmYW5nJTQwdHVuaXUuY29tJnNlcnZpY2U9bW9iaWxlLnNlY3VyaXR5cGF5LnBheSZzaWduPWN5bTV1Y1BDbXRFV28xQm1QUWJPVlBXTzFrVEFkVE1OSEg4bXJVdVpGYVVIZVRyVGUyOUx3cVBySFVVcmZvUVAwNFo3Z0JPZGlGbUh3cHphVUtyYUljSVFWNTElMkI2VEI2QktYZzVKWlN5cEE4S2ZOb29TZ21pUG9RRzhpaDQyNDUzVEJncmNFJTJCRUhSQXR0SXp4SEpqUUdxQ0pZM2xFSmZEd0R5d2IwY0lqTXMlM0Qmc2lnbl90eXBlPVJTQSZzdWJqZWN0PSVFOSU4MCU5NCVFNyU4OSU5QiVFNiU5NyU4NSVFNiVCOCVCOCVFNyVCRCU5MSZ0b3RhbF9mZWU9NTczLjAwIn19
# {"success":true,"msg":"操作成功","errorCode":0,"data":{"request":null,"orderType":2,"finalOrderId":6952385,"url":"_input_charset=utf-8&body=%E8%AE%A2%E5%8D%95%E5%8F%B7%EF%BC%9A1005095410&it_b_pay=28m&notify_url=http%3A%2F%2Fcashier.tuniu.com%2Falipay%2FapppayNotify&out_trade_no=00380000695238511090624240057300&partner=2088701781421683&payment_type=1&seller_id=xiongfang%40tuniu.com&service=mobile.securitypay.pay&sign=cym5ucPCmtEWo1BmPQbOVPWO1kTAdTMNHH8mrUuZFaUHeTrTe29LwqPrHUUrfoQP04Z7gBOdiFmHwpzaUKraIcIQV51%2B6TB6BKXg5JZSypA8KfNooSgmiPoQG8ih42453TBgrcE%2BEHRAttIzxHJjQGqCJY3lEJfDwDywb0cIjMs%3D&sign_type=RSA&subject=%E9%80%94%E7%89%9B%E6%97%85%E6%B8%B8%E7%BD%91&total_fee=573.00"}}
def confirm(parms):
    headers = {'User-Agent': base_data.get_user_agent(),
               'baseParams': base64.b64encode(json.dumps({"fingerPrint": "", "sessionId": parms['sessionId'],
                                                          "termAppVersion": "1.4.0", "termSysVersion": "4.4.2",
                                                          "majorAppVersion": "9.0.0",
                                                          "termModel": "",
                                                          "appType": 2, "platformId": 1, "network": "WIFI",
                                                          "termId": parms['termId']})),
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}

    url = 'https://jr.tuniu.com/fmp-web/pay/confirm'
    data = {"downPaymentFlag": 0, "encodeTotalAmount": rsa.encode(parms['price']), "orderId": parms['orderId'],
            "orderType": 1, "payChannel": base_data.payChannel, "payMethod": 11, "sign": "", "userId": parms['userId']}

    sign_data = 'downPaymentFlag=0&encodeTotalAmount=%s&orderId=%s&orderType=1&payChannel=%d&payMethod=11&userId=%d' % (
        data['encodeTotalAmount'], data['orderId'], base_data.payChannel, data['userId'])
    sign_data = sign_data + '&*()%sd76@#$Dfs^YsfUJKDs'
    data['sign'] = hashlib.md5(sign_data).hexdigest()
    base64_data = base64.b64encode(json.dumps(data))
    req = requests.post(url, data=base64_data, headers=headers)

    logger.debug('POST %s\n%s\n%s\n%s' % (req.url, json.dumps(headers), data, base64_data))
    try:
        resp = json.loads(base64.b64decode(req.text))
        return resp
    except Exception, e:
        raise HttpRequestException(e, {'function': 'pay_confirm', 'method': 'post', 'url': req.url,
                                       'headers': headers, 'data': data,
                                       'resp_content': req.content})

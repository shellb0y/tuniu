# -*- coding: utf-8 -*-

import base_data
import requests
import json
from my_exception import *
import time
import log_ex as logger


# GET http://m.tuniu.com/api/train/order/AddOrder?d=%7B%22zipCode%22%3A%22%22%2C%22address%22%3A%22%22%2C%22verificationCode%22%3A%22%22%2C%22travelCouponId%22%3A%22%22%2C%22arrivalCityCode%22%3A%22200%22%2C%22arrivalCityName%22%3A%22%E5%8C%97%E4%BA%AC%22%2C%22arrivalStationName%22%3A%22%E5%8C%97%E4%BA%AC%E5%8D%97%E7%AB%99%22%2C%22arrivalStations%22%3A%221175341%22%2C%22trainNumber%22%3A%22G106%22%2C%22contactList%22%3A%7B%22appellation%22%3A%22%22%2C%22email%22%3A%22%22%2C%22name%22%3A%22%22%2C%22phone%22%3A%22%22%2C%22tel%22%3A%2213192655251%22%7D%2C%22departDate%22%3A%222016-10-27%22%2C%22departureCityCode%22%3A%222500%22%2C%22departureCityName%22%3A%22%E4%B8%8A%E6%B5%B7%22%2C%22departureStationName%22%3A%22%E4%B8%8A%E6%B5%B7%E8%99%B9%E6%A1%A5%E7%AB%99%22%2C%22departureStations%22%3A%221175076%22%2C%22deviceNumber%22%3A%22863175026618021%22%2C%22trainId%22%3A%2216106%22%2C%22touristList%22%3A%5B%7B%22birthday%22%3A%221995-09-14%22%2C%22name%22%3A%22%E5%BC%A0%E5%BD%A7%E8%B1%AA%22%2C%22psptId%22%3A%22510802199509140039%22%2C%22psptType%22%3A1%2C%22isAdult%22%3A1%2C%22sex%22%3A1%7D%5D%2C%22telNum%22%3A%22%22%2C%22sessionId%22%3A%227b42973d419cbe9cce81e0d15923593f%22%2C%22seatId%22%3A%223%22%2C%22resourceId%22%3A%22353754990%22%2C%22receiverName%22%3A%22%22%2C%22promotionList%22%3A%5B%22129308%22%5D%2C%22rate%22%3A0%2C%22adultPrice%22%3A543.0%2C%22isTransferToDispatchTicket%22%3A0%2C%22isExcess%22%3A0%2C%22isDispatchTicket%22%3A0%2C%22isCouponValuable%22%3A0%2C%22insuranceResourceId%22%3A0%2C%22insurancePrice%22%3A0%2C%22childCount%22%3A0%2C%22ministryRailwaysId%22%3A0%2C%22travelCouponUseValue%22%3A0%2C%22useTrainUniquePromotion%22%3Afalse%2C%22adultCount%22%3A1%2C%22acceptStandingTicket%22%3Afalse%7D&c=%7B%22v%22%3A%228.1.6%22%2C%22ct%22%3A20%2C%22dt%22%3A1%2C%22ov%22%3A1%2C%22p%22%3A15447%2C%22cc%22%3A1502%7D HTTP/1.1
# sid: 8f38d376-fd65-46a4-9075-375f4f63a170
# User-Agent: TuNiuApp/8.1.6/Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX507J Build/KVT49L)
# host: m.tuniu.com
# Connection: Keep-Alive
# Accept-Encoding: gzip

# HTTP/1.1 200 OK
# Date: Wed, 26 Oct 2016 03:39:58 GMT
# Server: nginx
# Content-Type: text/html; charset=utf-8
# Set-Cookie: tuniuuser_citycode=MTUwMg%3D%3D; expires=Wed, 09-Nov-2016 03:39:57 GMT; Max-Age=1209600; path=/; domain=.tuniu.com
# Set-Cookie: tuniu_partner=MjAwLDAsLDMyM2RhZTNmNzMxY2RkNGEyYWExNWQ2NzgxOTJjN2Ji; expires=Wed, 09-Nov-2016 03:39:58 GMT; Max-Age=1209600; path=/; domain=.tuniu.com
# X-Via: 1.1 szhj11:5 (Cdn Cache Server V2.0), 1.1 shydx35:7 (Cdn Cache Server V2.0)
# Connection: keep-alive
# Content-Length: 386
#
# {"success":true,"errorCode":710000,"msg":"OK","data":{"success":true,"orderId":1004932858,"productType":18,"orderType":38,"noticeInfo":"订单提交成功，正在为您占座，请不要离开当前页面。。。","orderDetailUrl":"http:\/\/m.tuniu.com\/u\/order\/1004932858?orderType=38","errorCode":200}}
def add_order(sessionid, partner, cc, data):
    from_ = base_data.get_station_code_by_city_name(data['from'])
    to_ = base_data.get_station_code_by_city_name(data['to'])

    if from_ is None:
        raise ValueError('cannot find from station')
    if to_ is None:
        raise ValueError('cannot find to station')

    logger.info('looking for train %s' % data['train_number'])
    get_train_list_resp = get_train_list(
        {"arrivalCityCode": to_['cityCode'], "arrivalCityName": data['to'], "departureCityCode": from_['cityCode'],
         "departureCityName": data['from'],
         "departureDate": data['depart_date'], "deviceNumber": base_data.get_random_number(), "sortName": 0,
         "sortType": 0,
         "start": 0,
         "showAvailableTickets": 0, "limit": 0})

    train = filter(lambda t: t['trainNum'] == data['train_number'], get_train_list_resp['data']['rows'])
    if train:
        logger.info('find train %s success,looking for seat %s' % (data['train_number'], data['seatName']))
        seat = filter(lambda t: t['seatName'] == data['seatName'], train[0]['seatDesc'])
        if seat:
            logger.info('seat lookup %s success,order place starting...' % data['seatName'])
            params = {'d': json.dumps(
                {"zipCode": "", "address": "", "verificationCode": "", "travelCouponId": "",
                 "arrivalCityCode": to_['cityCode'],
                 "arrivalCityName": data['to'], "arrivalStationName": to_['stationName'],
                 "arrivalStations": to_['stationId'],
                 "trainNumber": data['train_number'],
                 "contactList": {"appellation": "", "email": "", "name": "", "phone": "", "tel": data['phone']},
                 "departDate": data['depart_date'], "departureCityCode": from_['cityCode'],
                 "departureCityName": data['from'],
                 "departureStationName": from_['stationName'], "departureStations": from_['stationId'],
                 "deviceNumber": base_data.get_random_number(),
                 "trainId": train[0]['trainId'], "touristList": data['touristList'],
                 "telNum": "", "sessionId": sessionid, "seatId": seat[0]['seatId'],
                 "promotionList": data['promotionList'],
                 "resourceId": seat[0]['resId'], "receiverName": "",
                 "rate": 0,
                 "adultPrice": data['price'],
                 "isTransferToDispatchTicket": 0, "isExcess": 0, "isDispatchTicket": 0, "isCouponValuable": 0,
                 "insuranceResourceId": 0, "insurancePrice": 0, "childCount": 0, "ministryRailwaysId": 0,
                 "travelCouponUseValue": 0, "useTrainUniquePromotion": False, "adultCount": 1,
                 "acceptStandingTicket": False}),
                'c': json.dumps({"v": "8.1.6", "ct": 20, "dt": 1, "ov": 1, "p": partner, "cc": cc})}

            req = requests.get('http://m.tuniu.com/api/train/order/AddOrder', params)
            logger.debug('GET %s' % req.url)
            try:
                resp = req.json()
                return resp
            except Exception, e:
                raise HttpRequestException(e, {'function': 'addorder', 'method': 'get', 'url': req.url,
                                               'resp_content': req.content})
        else:
            raise ValueError('cant find trainNum %s,seat %s' % (data['train_number'], data['seatName']))
    else:
        raise ValueError('cant find trainNum %s' % data['train_number'])


# POST http://m.tuniu.com/api/train/product/ticketListWithFresh?c=%7B%22v%22%3A%228.1.6%22%2C%22ct%22%3A20%2C%22dt%22%3A1%2C%22ov%22%3A1%2C%22p%22%3A15447%2C%22cc%22%3A1502%7D HTTP/1.1
# sid: 96e920da-8fa6-4e6b-9f65-66457465ca71
# User-Agent: TuNiuApp/8.1.6/Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX507J Build/KVT49L)
# host: m.tuniu.com
# Content-Type: application/json; charset=UTF-8
# Content-Length: 241
# Connection: Keep-Alive
# Accept-Encoding: gzip
#
# {"arrivalCityCode":"200","arrivalCityName":"北京","departureCityCode":"1502","departureCityName":"长沙","departureDate":"2016-10-28","deviceNumber":"863175026618021","sortName":0,"sortType":0,"start":0,"showAvailableTickets":0,"limit":0}
# HTTP/1.1 200 OK
# Date: Tue, 25 Oct 2016 09:18:17 GMT
# Server: nginx
# Content-Type: text/html; charset=utf-8
# X-Via: 1.1 shshx18:3 (Cdn Cache Server V2.0), 1.1 shydx35:7 (Cdn Cache Server V2.0)
# Connection: keep-alive
# Content-Length: 20021
#
# {"success":true,"errorCode":710000,"msg":"OK","data":{"remark":"","memo":"","expire":false,"freshUrl":"","departureDate":"2016-11-23","count":16,"rows":[{"trainId":16401,"trainNum":"G401","trainType":"G-高铁","trainTypeCode":0,"trainTypeName":"高铁","departStationName":"北京西站","departStationCode":"1175343","destStationName":"长沙南站","destStationCode":"1176886","departureCityCode":200,"arrivalCityCode":1502,"departureCityName":"北京西","arrivalCityName":"长沙南","departDepartTime":"07:05","destArriveTime":"13:58","duration":"6时53分","durationDay":1,"departStationType":"始发","departStationTypeCode":0,"destStationType":"过路","destStationTypeCode":2,"saleStatus":"在售","saleStatusId":0,"leftNumber":454,"seat":"二等","price":649,"promotionPrice":649,"resId":454,"seatDesc":[{"leftNumber":3,"seatId":0,"seatName":"商务","price":2050,"promotionPrice":2050,"resId":354712719},{"leftNumber":0,"seatId":2,"seatName":"一等","price":1038,"promotionPrice":1038,"resId":354712720},{"leftNumber":454,"seatId":3,"seatName":"二等","price":649,"promotionPrice":649,"resId":354712721}],"memoDay":null,"memoHour":"","canGrap":true,"oneLeftNumber":0},{"trainId":16501,"trainNum":"G501","trainType":"G-高铁","trainTypeCode":0,"trainTypeName":"高铁","departStationName":"北京西站","departStationCode":"1175343","destStationName":"长沙南站","destStationCode":"1176886","departureCityCode":200,"arrivalCityCode":1502,"departureCityName":"北京西","arrivalCityName":"长沙南","departDepartTime":"07:10","destArriveTime":"14:10","duration":"7时0分","durationDay":1,"departStationType":"始发","departStationTypeCode":0,"destStationType":"终点","destStationTypeCode":1,"saleStatus":"在售","saleStatusId":0,"leftNumber":815,"seat":"二等","price":649,"promotionPrice":649,"resId":815,"seatDesc":[{"leftNumber":26,"seatId":0,"seatName":"商务","price":2050,"promotionPrice":2050,"resId":356182618},{"leftNumber":142,"seatId":2,"seatName":"一等","price":1038,"promotionPrice":1038,"resId":356182620},{"leftNumber":815,"seatId":3,"seatName":"二等","price":649,"promotionPrice":649,"resId":356182621}],"memoDay":null,"memoHour":"","canGrap":true,"oneLeftNumber":1},{"trainId":16529,"trainNum":"G529","trainType":"G-高铁","trainTypeCode":0,"trainTypeName":"高铁","departStationName":"北京西站","departStationCode":"1175343","destStationName":"长沙南站","destStationCode":"1176886","departureCityCode":200,"arrivalCityCode":1502,"departureCityName":"北京西","arrivalCityName":"长沙南","departDepartTime":"07:26","destArriveTime":"14:49","duration":"7时23分","durationDay":1,"departStationType":"始发","departStationTypeCode":0,"destStationType":"过路","destStationTypeCode":2,"saleStatus":"在售","saleStatusId":0,"leftNumber":345,"seat":"二等","price":649,"promotionPrice":649,"resId":345,"seatDesc":[{"leftNumber":24,"seatId":0,"seatName":"商务","price":2050,"promotionPrice":2050,"resId":355038872},{"leftNumber":102,"seatId":2,"seatName":"一等","price":1038,"promotionPrice":1038,"resId":355038877},{"leftNumber":345,"seatId":3,"seatName":"二等","price":649,"promotionPrice":649,"resId":355038883}],"memoDay":null,"memoHour":"","canGrap":true,"oneLeftNumber":1},{"trainId":1671,"trainNum":"G71","trainType":"G-高铁","trainTypeCode":0,"trainTypeName":"高铁","departStationName":"北京西站","departStationCode":"1175343","destStationName":"长沙南站","destStationCode":"1176886","departureCityCode":200,"arrivalCityCode":1502,"departureCityName":"北京西","arrivalCityName":"长沙南","departDepartTime":"07:40","destArriveTime":"14:27","duration":"6时47分","durationDay":1,"departStationType":"始发","departStationTypeCode":0,"destStationType":"过路","destStationTypeCode":2,"saleStatus":"在售","saleStatusId":0,"leftNumber":623,"seat":"二等","price":649,"promotionPrice":649,"resId":623,"seatDesc":[{"leftNumber":5,"seatId":0,"seatName":"商务","price":2050,"promotionPrice":2050,"resId":355184502},{"leftNumber":90,"seatId":2,"seatName":"一等","price":1038,"promotionPrice":1038,"resId":355184505},{"leftNumber":623,"seatId":3,"seatName":"二等","price":649,"promotionPrice":649,"resId":355184508}],"memoDay":null,"memoHour":"","canGrap":true,"oneLeftNumber":1},{"trainId":1681,"trainNum":"G81","trainType":"G-高铁","trainTypeCode":0,"trainTypeName":"高铁","departStationName":"北京西站","departStationCode":"1175343","destStationName":"长沙南站","destStationCode":"1176886","departureCityCode":200,"arrivalCityCode":1502,"departureCityName":"北京西","arrivalCityName":"长沙南","departDepartTime":"08:55","destArriveTime":"14:37","duration":"5时42分","durationDay":1,"departStationType":"始发","departStationTypeCode":0,"destStationType":"过路","destStationTypeCode":2,"saleStatus":"在售","saleStatusId":0,"leftNumber":715,"seat":"二等","price":649,"promotionPrice":649,"resId":715,"seatDesc":[{"leftNumber":24,"seatId":0,"seatName":"商务","price":2050,"promotionPrice":2050,"resId":354712607},{"leftNumber":111,"seatId":2,"seatName":"一等","price":1038,"promotionPrice":1038,"resId":354712611},{"leftNumber":715,"seatId":3,"seatName":"二等","price":649,"promotionPrice":649,"resId":354712613}],"memoDay":null,"memoHour":"","canGrap":true,"oneLeftNumber":1},{"trainId":1683,"trainNum":"G83","trainType":"G-高铁","trainTypeCode":0,"trainTypeName":"高铁","departStationName":"北京西站","departStationCode":"1175343","destStationName":"长沙南站","destStationCode":"1176886","departureCityCode":200,"arrivalCityCode":1502,"departureCityName":"北京西","arrivalCityName":"长沙南","departDepartTime":"09:00","destArriveTime":"14:43","duration":"5时43分","durationDay":1,"departStationType":"始发","departStationTypeCode":0,"destStationType":"终点","destStationTypeCode":1,"saleStatus":"在售","saleStatusId":0,"leftNumber":1000,"seat":"二等","price":649,"promotionPrice":649,"resId":1000,"seatDesc":[{"leftNumber":15,"seatId":0,"seatName":"商务","price":2050,"promotionPrice":2050,"resId":355132960},{"leftNumber":24,"seatId":2,"seatName":"一等","price":1038,"promotionPrice":1038,"resId":355132961},{"leftNumber":1000,"seatId":3,"seatName":"二等","price":649,"promotionPrice":649,"resId":355132962}],"memoDay":null,"memoHour":"","canGrap":true,"oneLeftNumber":1},{"trainId":16421,"trainNum":"G421","trainType":"G-高铁","trainTypeCode":0,"trainTypeName":"高铁","departStationName":"北京西站","departStationCode":"1175343","destStationName":"长沙南站","destStationCode":"1176886","departureCityCode":200,"arrivalCityCode":1502,"departureCityName":"北京西","arrivalCityName":"长沙南","departDepartTime":"09:07","destArriveTime":"16:09","duration":"7时2分","durationDay":1,"departStationType":"始发","departStationTypeCode":0,"destStationType":"过路","destStationTypeCode":2,"saleStatus":"在售","saleStatusId":0,"leftNumber":459,"seat":"二等","price":649,"promotionPrice":649,"resId":459,"seatDesc":[{"leftNumber":1,"seatId":0,"seatName":"商务","price":2050,"promotionPrice":2050,"resId":355037925},{"leftNumber":0,"seatId":2,"seatName":"一等","price":1038,"promotionPrice":1038,"resId":355037933},{"leftNumber":459,"seatId":3,"seatName":"二等","price":649,"promotionPrice":649,"resId":355037940}],"memoDay":null,"memoHour":"","canGrap":true,"oneLeftNumber":0},{"trainId":1679,"trainNum":"G79","trainType":"G-高铁","trainTypeCode":0,"trainTypeName":"高铁","departStationName":"北京西站","departStationCode":"1175343","destStationName":"长沙南站","destStationCode":"1176886","departureCityCode":200,"arrivalCityCode":1502,"departureCityName":"北京西","arrivalCityName":"长沙南","departDepartTime":"10:00","destArriveTime":"15:38","duration":"5时38分","durationDay":1,"departStationType":"始发","departStationTypeCode":0,"destStationType":"过路","destStationTypeCode":2,"saleStatus":"在售","saleStatusId":0,"leftNumber":84,"seat":"二等","price":649,"promotionPrice":649,"resId":84,"seatDesc":[{"leftNumber":0,"seatId":0,"seatName":"商务","price":2050,"promotionPrice":2050,"resId":355184088},{"leftNumber":36,"seatId":2,"seatName":"一等","price":1038,"promotionPrice":1038,"resId":355184090},{"leftNumber":84,"seatId":3,"seatName":"二等","price":649,"promotionPrice":649,"resId":355184092}],"memoDay":null,"memoHour":"","canGrap":true,"oneLeftNumber":0},{"trainId":1665,"trainNum":"G65","trainType":"G-高铁","trainTypeCode":0,"trainTypeName":"高铁","departStationName":"北京西站","departStationCode":"1175343","destStationName":"长沙南站","destStationCode":"1176886","departureCityCode":200,"arrivalCityCode":1502,"departureCityName":"北京西","arrivalCityName":"长沙南","departDepartTime":"10:33","destArriveTime":"17:27","duration":"6时54分","durationDay":1,"departStationType":"始发","departStationTypeCode":0,"destStationType":"过路","destStationTypeCode":2,"saleStatus":"在售","saleStatusId":0,"leftNumber":626,"seat":"二等","price":649,"promotionPrice":649,"resId":626,"seatDesc":[{"leftNumber":15,"seatId":0,"seatName":"商务","price":2050,"promotionPrice":2050,"resId":354509252},{"leftNumber":112,"seatId":2,"seatName":"一等","price":1038,"promotionPrice":1038,"resId":354509255},{"leftNumber":626,"seatId":3,"seatName":"二等","price":649,"promotionPrice":649,"resId":354509257}],"memoDay":null,"memoHour":"","canGrap":true,"oneLeftNumber":1},{"trainId":16487,"trainNum":"G487","trainType":"G-高铁","trainTypeCode":0,"trainTypeName":"高铁","departStationName":"北京西站","departStationCode":"1175343","destStationName":"长沙南站","destStationCode":"1176886","departureCityCode":200,"arrivalCityCode":1502,"departureCityName":"北京西","arrivalCityName":"长沙南","departDepartTime":"10:45","destArriveTime":"16:46","duration":"6时1分","durationDay":1,"departStationType":"始发","departStationTypeCode":0,"destStationType":"过路","destStationTypeCode":2,"saleStatus":"在售","saleStatusId":0,"leftNumber":904,"seat":"二等","price":649,"promotionPrice":649,"resId":904,"seatDesc":[{"leftNumber":15,"seatId":0,"seatName":"商务","price":2050,"promotionPrice":2050,"resId":354394062},{"leftNumber":20,"seatId":2,"seatName":"一等","price":1038,"promotionPrice":1038,"resId":354394063},{"leftNumber":904,"seatId":3,"seatName":"二等","price":649,"promotionPrice":649,"resId":354394064}],"memoDay":null,"memoHour":"","canGrap":true,"oneLeftNumber":1},{"trainId":16403,"trainNum":"G403","trainType":"G-高铁","trainTypeCode":0,"trainTypeName":"高铁","departStationName":"北京西站","departStationCode":"1175343","destStationName":"长沙南站","destStationCode":"1176886","departureCityCode":200,"arrivalCityCode":1502,"departureCityName":"北京西","arrivalCityName":"长沙南","departDepartTime":"11:43","destArriveTime":"18:40","duration":"6时57分","durationDay":1,"departStationType":"始发","departStationTypeCode":0,"destStationType":"过路","destStationTypeCode":2,"saleStatus":"在售","saleStatusId":0,"leftNumber":363,"seat":"二等","price":649,"promotionPrice":649,"resId":363,"seatDesc":[{"leftNumber":3,"seatId":0,"seatName":"商务","price":2050,"promotionPrice":2050,"resId":354713194},{"leftNumber":0,"seatId":2,"seatName":"一等","price":1038,"promotionPrice":1038,"resId":354713195},{"leftNumber":363,"seatId":3,"seatName":"二等","price":649,"promotionPrice":649,"resId":354713196}],"memoDay":null,"memoHour":"","canGrap":true,"oneLeftNumber":0},{"trainId":1667,"trainNum":"G67","trainType":"G-高铁","trainTypeCode":0,"trainTypeName":"高铁","departStationName":"北京西站","departStationCode":"1175343","destStationName":"长沙南站","destStationCode":"1176886","departureCityCode":200,"arrivalCityCode":1502,"departureCityName":"北京西","arrivalCityName":"长沙南","departDepartTime":"12:13","destArriveTime":"19:29","duration":"7时16分","durationDay":1,"departStationType":"始发","departStationTypeCode":0,"destStationType":"过路","destStationTypeCode":2,"saleStatus":"在售","saleStatusId":0,"leftNumber":753,"seat":"二等","price":649,"promotionPrice":649,"resId":753,"seatDesc":[{"leftNumber":23,"seatId":0,"seatName":"商务","price":2050,"promotionPrice":2050,"resId":354509616},{"leftNumber":122,"seatId":2,"seatName":"一等","price":1038,"promotionPrice":1038,"resId":354509620},{"leftNumber":753,"seatId":3,"seatName":"二等","price":649,"promotionPrice":649,"resId":354509627}],"memoDay":null,"memoHour":"","canGrap":true,"oneLeftNumber":1},{"trainId":16491,"trainNum":"G491","trainType":"G-高铁","trainTypeCode":0,"trainTypeName":"高铁","departStationName":"北京西站","departStationCode":"1175343","destStationName":"长沙南站","destStationCode":"1176886","departureCityCode":200,"arrivalCityCode":1502,"departureCityName":"北京西","arrivalCityName":"长沙南","departDepartTime":"12:34","destArriveTime":"20:02","duration":"7时28分","durationDay":1,"departStationType":"始发","departStationTypeCode":0,"destStationType":"过路","destStationTypeCode":2,"saleStatus":"在售","saleStatusId":0,"leftNumber":290,"seat":"二等","price":649,"promotionPrice":649,"resId":290,"seatDesc":[{"leftNumber":0,"seatId":0,"seatName":"商务","price":2050,"promotionPrice":2050,"resId":364585966},{"leftNumber":12,"seatId":1,"seatName":"特等","price":1235,"promotionPrice":1235,"resId":354394368},{"leftNumber":77,"seatId":2,"seatName":"一等","price":1038,"promotionPrice":1038,"resId":354394369},{"leftNumber":290,"seatId":3,"seatName":"二等","price":649,"promotionPrice":649,"resId":354394370}],"memoDay":null,"memoHour":"","canGrap":true,"oneLeftNumber":0},{"trainId":1669,"trainNum":"G69","trainType":"G-高铁","trainTypeCode":0,"trainTypeName":"高铁","departStationName":"北京西站","departStationCode":"1175343","destStationName":"长沙南站","destStationCode":"1176886","departureCityCode":200,"arrivalCityCode":1502,"departureCityName":"北京西","arrivalCityName":"长沙南","departDepartTime":"13:05","destArriveTime":"19:34","duration":"6时29分","durationDay":1,"departStationType":"始发","departStationTypeCode":0,"destStationType":"过路","destStationTypeCode":2,"saleStatus":"在售","saleStatusId":0,"leftNumber":673,"seat":"二等","price":649,"promotionPrice":649,"resId":673,"seatDesc":[{"leftNumber":21,"seatId":0,"seatName":"商务","price":2050,"promotionPrice":2050,"resId":354509451},{"leftNumber":95,"seatId":2,"seatName":"一等","price":1038,"promotionPrice":1038,"resId":354509456},{"leftNumber":673,"seatId":3,"seatName":"二等","price":649,"promotionPrice":649,"resId":354509461}],"memoDay":null,"memoHour":"","canGrap":true,"oneLeftNumber":1},{"trainId":16503,"trainNum":"G503","trainType":"G-高铁","trainTypeCode":0,"trainTypeName":"高铁","departStationName":"北京西站","departStationCode":"1175343","destStationName":"长沙南站","destStationCode":"1176886","departureCityCode":200,"arrivalCityCode":1502,"departureCityName":"北京西","arrivalCityName":"长沙南","departDepartTime":"14:38","destArriveTime":"21:07","duration":"6时29分","durationDay":1,"departStationType":"始发","departStationTypeCode":0,"destStationType":"终点","destStationTypeCode":1,"saleStatus":"在售","saleStatusId":0,"leftNumber":494,"seat":"二等","price":649,"promotionPrice":649,"resId":494,"seatDesc":[{"leftNumber":5,"seatId":0,"seatName":"商务","price":2050,"promotionPrice":2050,"resId":355133011},{"leftNumber":0,"seatId":2,"seatName":"一等","price":1038,"promotionPrice":1038,"resId":355133012},{"leftNumber":494,"seatId":3,"seatName":"二等","price":649,"promotionPrice":649,"resId":355133013}],"memoDay":null,"memoHour":"","canGrap":true,"oneLeftNumber":0},{"trainId":16505,"trainNum":"G505","trainType":"G-高铁","trainTypeCode":0,"trainTypeName":"高铁","departStationName":"北京西站","departStationCode":"1175343","destStationName":"长沙南站","destStationCode":"1176886","departureCityCode":200,"arrivalCityCode":1502,"departureCityName":"北京西","arrivalCityName":"长沙南","departDepartTime":"15:40","destArriveTime":"22:32","duration":"6时52分","durationDay":1,"departStationType":"始发","departStationTypeCode":0,"destStationType":"终点","destStationTypeCode":1,"saleStatus":"在售","saleStatusId":0,"leftNumber":1000,"seat":"二等","price":649,"promotionPrice":649,"resId":1000,"seatDesc":[{"leftNumber":15,"seatId":0,"seatName":"商务","price":2050,"promotionPrice":2050,"resId":355133347},{"leftNumber":24,"seatId":2,"seatName":"一等","price":1038,"promotionPrice":1038,"resId":355133348},{"leftNumber":1000,"seatId":3,"seatName":"二等","price":649,"promotionPrice":649,"resId":355133349}],"memoDay":null,"memoHour":"","canGrap":true,"oneLeftNumber":1}],"trainTypes":[{"id":null,"trainTypeId":null,"trainType":"不限"},{"id":0,"trainTypeId":"0","trainType":"G-高铁"},{"id":3,"trainTypeId":"3","trainType":"Z-直达"},{"id":4,"trainTypeId":"4","trainType":"T-特快"},{"id":5,"trainTypeId":"5","trainType":"K-普快"}],"seats":[{"seatId":null,"seatName":"不限"},{"seatId":"0","seatName":"商务"},{"seatId":"1","seatName":"特等"},{"seatId":"2","seatName":"一等"},{"seatId":"3","seatName":"二等"},{"seatId":"4","seatName":"高软"},{"seatId":"5","seatName":"软卧"},{"seatId":"6","seatName":"硬卧"},{"seatId":"8","seatName":"硬座"},{"seatId":"9","seatName":"无座"}],"departStationTypes":[{"departStationTypeId":0,"departStationTypeName":"始发"},{"departStationTypeId":2,"departStationTypeName":"过路"}],"departureTimes":[{"id":"0-6","departureTime":"0-6","isSelected":0},{"id":"6-12","departureTime":"6-12","isSelected":0},{"id":"12-18","departureTime":"12-18","isSelected":0},{"id":"18-24","departureTime":"18-24","isSelected":0}],"arrivalTimes":[{"id":"0-6","arrivalTime":"0-6","isSelected":0},{"id":"6-12","arrivalTime":"6-12","isSelected":0},{"id":"12-18","arrivalTime":"12-18","isSelected":0},{"id":"18-24","arrivalTime":"18-24","isSelected":0}],"departureStations":[{"code":"1175343","name":"北京西站"},{"code":"1175342","name":"北京站"}],"arrivalStations":[{"code":"1176886","name":"长沙南站"},{"code":"1176888","name":"长沙站"}],"departureDates":{"yesterday":"2016-11-22","today":"2016-11-23","tomorrow":"2016-11-24"}}}
def get_train_list(data):
    headers = {'User-Agent': 'TuNiuApp/8.1.6/Dalvik/1.6.0 (Linux; U; Android 4.2.2)',
               'Content-Type': 'application/json; charset=UTF-8'}

    url = 'http://m.tuniu.com/api/train/product/ticketListWithFresh?c=%7B%22v%22%3A%228.1.6%22%2C%22ct%22%3A20%2C%22dt%22%3A1%2C%22ov%22%3A1%2C%22p%22%3A15447%2C%22cc%22%3A1502%7D'
    req = requests.post(url, json=data, headers=headers)

    logger.debug('POST #1 %s\n%s \n%s' % (req.url, req.headers, data))
    try:
        resp = req.json()
        if resp['success'] and 'rows' in resp['data'] and resp['data']['rows']:
            return resp
        else:
            kyfw_req = requests.get(
                'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=%s&from_station=%s&to_station=%s' % (
                    data['departureDate'], base_data.get_station_code_12306(data['departureCityName']),
                    base_data.get_station_code_12306(data['arrivalCityName'])), verify=False)

            logger.debug('request 12306:GET %s' % kyfw_req.url)
            data['trainInfo'] = kyfw_req.text

            req = requests.post(url, json=data, headers=headers)
            logger.debug('POST #2 %s\n%s \n%s' % (req.url, req.headers, data))
            return req.json()

    except Exception, e:
        raise HttpRequestException(e, {'function': 'get_train_list', 'method': 'post', 'url': req.url,
                                       'headers': headers, 'data': data,
                                       'resp_content': req.content})

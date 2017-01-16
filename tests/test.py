# -*- coding: utf-8 -*-
# s = '你好'
# print '\u5357\u4eac'.decode('raw_unicode_escape')
import traceback
import uuid
import datetime
import random
import time
import requests


# test = u'@bjb|北京北|VAP|beijingbei|bjb|0@bjd|北京东|BOP|beijingdong|bjd|1@bji|北京|BJP|beijing|bj|2@bjn|北京南|VNP|beijingnan|bjn|3@bjx|北京西|BXP|beijingxi|bjx|4@gzn|广州南|IZQ|guangzhounan|gzn|5@cqb|重庆北|CUW|chongqingbei|cqb|6@cqi|重庆|CQW|chongqing|cq|7@cqn|重庆南|CRW|chongqingnan|cqn|8@gzd|广州东|GGQ|guangzhoudong|gzd|9@sha|上海|SHH|shanghai|sh|10@shn|上海南|SNH|shanghainan|shn|11@shq|上海虹桥|AOH|shanghaihongqiao|shhq|12@shx|上海西|SXH|shanghaixi|shx|13@tjb|天津北|TBP|tianjinbei|tjb|14@tji|天津|TJP|tianjin|tj|15@tjn|天津南|TIP|tianjinnan|tjn|16@tjx|天津西|TXP|tianjinxi|tjx|17@cch|长春|CCT|changchun|cc|18@ccn|长春南|CET|changchunnan|ccn|19@ccx|长春西|CRT|changchunxi|ccx|20@cdd|成都东|ICW|chengdudong|cdd|21@cdn|成都南|CNW|chengdunan|cdn|22@cdu|成都|CDW|chengdu|cd|23@csh|长沙|CSQ|changsha|cs|24@csn|长沙南|CWQ|changshanan|csn|25@fzh|福州|FZS|fuzhou|fz|26@fzn|福州南|FYS|fuzhounan|fzn|27@gya|贵阳|GIW|guiyang|gy|28@gzh|广州|GZQ|guangzhou|gz|29@gzx|广州西|GXQ|guangzhouxi|gzx|30@heb|哈尔滨|HBB|haerbin|heb|31@hed|哈尔滨东|VBB|haerbindong|hebd|32@hex|哈尔滨西|VAB|haerbinxi|hebx|33@hfe|合肥|HFH|hefei|hf|34@hfx|合肥西|HTH|hefeixi|hfx|35@hhd|呼和浩特东|NDC|huhehaotedong|hhhtd|36@hht|呼和浩特|HHC|huhehaote|hhht|37@hkd|海  口东|KEQ|haikoudong|hkd|38@hkd|海口东|HMQ|haikoudong|hkd|39@hko|海口|VUQ|haikou|hk|40@hzd|杭州东|HGH|hangzhoudong|hzd|41@hzh|杭州|HZH|hangzhou|hz|42@hzn|杭州南|XHH|hangzhounan|hzn|43@jna|济南|JNK|jinan|jn|44@jnd|济南东|JAK|jinandong|jnd|45@jnx|济南西|JGK|jinanxi|jnx|46@kmi|昆明|KMM|kunming|km|47@kmx|昆明西|KXM|kunmingxi|kmx|48@lsa|拉萨|LSO|lasa|ls|49@lzd|兰州东|LVJ|lanzhoudong|lzd|50@lzh|兰州|LZJ|lanzhou|lz|51@lzx|兰州西|LAJ|lanzhouxi|lzx|52@nch|南昌|NCG|nanchang|nc|53@nji|南京|NJH|nanjing|nj|54@njn|南京南|NKH|nanjingnan|njn|55@nni|南宁|NNZ|nanning|nn|56@sjb|石家庄北|VVP|shijiazhuangbei|sjzb|57@sjz|石家庄|SJP|shijiazhuang|sjz|58@sya|沈阳|SYT|shenyang|sy|59@syb|沈阳北|SBT|shenyangbei|syb|60@syd|沈阳东|SDT|shenyangdong|syd|61@tyb|太原北|TBV|taiyuanbei|tyb|62@tyd|太原东|TDV|taiyuandong|tyd|63@tyu|太原|TYV|taiyuan|ty|64@wha|武汉|WHN|wuhan|wh|65@wjx|王家营西|KNM|wangjiayingxi|wjyx|66@wln|乌鲁木齐南|WMR|wulumuqinan|wlmqn|67@xab|西安北|EAY|xianbei|xab|68@xan|西安|XAY|xian|xa|69@xan|西安南|CAY|xiannan|xan|70@xni|西宁|XNO|xining|xn|71@ych|银川|YIJ|yinchuan|yc|72'
# pattern = re.compile(ur'\|上海虹桥\|\w+?\|')
# match = pattern.findall(test)
# print match
# if match:
#     print match[0].split('|')[2]
#
#
# # print  requests.get('https://github.com', verify=True)
# #
# req = requests.get('https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8971', verify=False)
# print req.text320586199701155420




resp = requests.post('http://op.yikao666.cn/JDTrainOpen/CallBackForTNLock',data='tnOrderno=1011757210&userName=17191584036&password=a697861&sessionid=19af09733d6d195ed07bf5ee466a789d,59350296&order_id=121e876355cd427ea6987f0cd1555b8f&success=true&amount=24.5&cookie=BSFIT_OkLJUJ=LMRWJFODSWH89Y5E;_tacau=MCxkN2JkN2Y5OS0xNDI3LWUyZTEtY2IxMy0wMDdjOGUzM2E3YzYs;_tact=NzY0ZTYzYWEtOGY1OS05NjM1LWYxZmQtMzg0YjUzMjAzMWVm;_tacz2=taccsr%3D%28direct%29%7Ctacccn%3D%28none%29%7Ctaccmd%3D%28none%29%7Ctaccct%3D%28none%29%7Ctaccrt%3D%28none%29;_taca=1484549318693.1484549318693.1484549318693.1;_tacb=MDRmNjViZGMtYjhjNy03ZjkxLWZhY2ItYjFiNzU4Yjk1Yjky;_tacc=1;__utma=1.490055916.1484549319.1484549319.1484549319.1;__utmb=1.1.10.1484549319;__utmc=1;__utmz=1.1484549319.1.1.utmcsr;BSFIT_TRACEID=587c6cc7e4b0882b1ff2be2c;BSFIT_DEVICEID=22119dfeed1249bcba4d25494700abc1;BSFIT_EXPIRATION=2970959119774;isLogined=true;ssoUser=7faed0a3f1c2095ecd00e587c5b42fe6;OLBSESSID=6ifq8ri1d4akjfadstinnjldn0;tuniuuser=NTkzNTAyOTYsODA5NzU1MDE1OSw4MDk3NTUwMTU5LDAsMTQ4NDU0OTMyNCwwMTJkMTFjMTBhZWM0ZWUwNGRiM2IyOTMxNjkxZWNkZA%3D%3D;tuniusub=1;tuniuuser_vip=MA%3D%3D;tuniuuser_level=MQ%3D%3D;tuniuuser_id=59350296;tuniuuser_name=ODA5NzU1MDE1OQ%3D%3D;tuniuuser_citycode=MjQxMw%3D%3D;tuniu_partner=MTYyNDIsMCwsYjdmOTI0MTI0Mzc4MTg2NzUwM2JjYTIwYjg5NzczOTQ%3D;JSESSIONID=122A0D4BFF712D78C5064B9D1F26A4A7;NSC_gct_oqd_ck-wjq=ffffffff0920b81f45525d5f4f58455e445a4a420f3a;&m_cookie=PageSwitch=2,148454931757; _tacau=MCwzYTY0MTU4Ni1mZDI3LTQyMWUtZDI3NS1kNGI1ZDEzNDU1ODcs; _tacz2=taccsr=(direct)|tacccn=(none)|taccmd=(none)|taccct=(none)|taccrt=(none); _taca=1477397184786.1477397184786.1477397184786.1; _tacc=1; SERVERID=dnionD; app_imei=552472241138829; ov=1; tuniuuser_id=59350296;  TUNIUmuser=19af09733d6d195ed07bf5ee466a789d; sessionId=MQ==; token=Ym9yM2NvcDZvM3Q0ZnY2cA==; appVersion=9.0.0; tuniu_partner=MTU0NDcsMCwsOWIxMTFkNWY3NGQ1NmQ1NjdhNjEyZDQzYjEzYjVlYjI=; deviceType=1; SsoSession=19af09733d6d195ed07bf5ee466a789d; clientType=20; page_flag=; __utma=1.1665134217.1477397186.1477397186.1477397188.2; __utmb=1.4.10.1477397188; __utmc=1; __utmz=1.1477397188.2.2.utmcsr=morecoupon|utmccn=(not set)|utmcmd=couponcenter; _tact=NTExZDJiZTYtNGUxOS05Y2E2LWJlNjEtMTM0ZDMwYmMwNDRh;',
                     headers={'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'})
print resp.text
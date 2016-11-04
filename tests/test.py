# -*- coding: utf-8 -*-
# s = '你好'
# print '\u5357\u4eac'.decode('raw_unicode_escape')
import traceback
import uuid

try:
    raise ValueError('test',{'a':'m'})
except ValueError,e:
    print traceback.format_exc()

print 1 and None or '2'

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
# print req.text

a={'a':1,'b':'1'}
if not a.has_key('b') or not a['b']:
    print 'not'
else:
    print 'yes'


print uuid.uuid1()

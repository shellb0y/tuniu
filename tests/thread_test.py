# coding=utf-8
import threading
import requests
from time import ctime, sleep
import random

def get_order(name):
    sleep(random.randint(1,5))
    for i in range(10):
        req = requests.get('http://localhost:8000/v1/api/test')
        if req.text:
            print '%s(%d):%s' % (name, i, req.text)


threads = []
t1 = threading.Thread(target=get_order, args=('#1',))
threads.append(t1)
t2 = threading.Thread(target=get_order, args=('#2',))
threads.append(t2)
t3 = threading.Thread(target=get_order, args=('#3',))
threads.append(t3)
t4 = threading.Thread(target=get_order, args=('#4',))
threads.append(t4)
t5 = threading.Thread(target=get_order, args=('#5',))
threads.append(t5)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()

    for t in threads:
        t.join()
    print "all over %s" % ctime()

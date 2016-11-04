import requests
import app_conf
import log_ex as logger
from my_exception import *


def encode(data):
    req = requests.get(app_conf.rsa_encode % data)
    logger.debug('GET %s' % (req.url))
    try:
        resp = req.text
        return resp
    except Exception, e:
        raise HttpRequestException(e, {'function': 'rsa encode', 'url': app_conf.rsa_encode, 'method': 'get',
                                       'resp_content': req.content})

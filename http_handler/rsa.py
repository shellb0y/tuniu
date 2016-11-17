import requests
import base_data
import log_ex as logger
from my_exception import *


def encode(data):
    # s = requests.session()
    # s.keep_alive = False

    req = requests.get(base_data.rsa_encode % data, headers={'Keep-Alive': "false"})

    logger.debug('GET %s' % (req.url))
    try:
        resp = req.text
        return resp
    except Exception, e:
        raise HttpRequestException(e, {'function': 'rsa encode', 'url': base_data.rsa_encode, 'method': 'get',
                                       'resp_content': req.content})

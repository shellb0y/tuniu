import logging
import logstash
import sys
import unittest
import traceback


class LogTestSuite(unittest.TestCase):
    def setUp(self):
        self.test_logger = logging.getLogger('python-logstash-logger')
        self.test_logger.setLevel(logging.INFO)
        self.test_logger.addHandler(logstash.LogstashHandler('115.28.102.142', 55514))
        self.test_logger.addHandler(logging.StreamHandler(sys.stderr))

    def logstash_test(self):
        self.test_logger.error({'app':'tuniu#3','message':'python-logstash: test logstash error message.'})
        self.test_logger.info('python-logstash: test logstash info message.')
        self.test_logger.warning('python-logstash: test logstash warning message.')
        #
        # # add extra field to logstash message
        extra = {
            'host':'#3',
            'program':'tuniu'
        }
        self.test_logger.info('python-logstash: test extra fields %s','3', extra=extra)

    def logging_test(self):
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        logger.debug('test')


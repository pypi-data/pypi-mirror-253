import random
import unittest
import time

from src.endemic.logging.fluentd.logger import LoggerFluentd
import logging

FLUENTD_APP_HOST = '88.99.81.198'
FLUENTD_APP_PORT = 24224


class TestLoggingFluentLogger(unittest.TestCase):

    # execute before every test case function run.
    def setUp(self):
        self.__app = 'application.shai.modules.logging.fluentd.logger'
        pass

    def test_debug(self):
        print('Init {}'.format(self.__class__.__name__))

        log = LoggerFluentd('test-1',
                            self.__app,
                            'fluentd',
                            LoggerFluentd.DEBUG,
                            FLUENTD_APP_HOST,
                            FLUENTD_APP_PORT)
        self.check_instance(log)

        log.link = '1'

        log.debug('Test {}'.format(random.randint(1, 1000)),
                  self.__class__.__name__, log.func, 'test-tag', {'field1': 1, 'field2': 2})

        for i in range(1):
            try:
                a = 2 / 0
            except Exception as e:
                log.exception(repr(e))
                log.critical('Critical error')
                pass

        print(log.timer)

    def test_info(self):
        print('Init {}'.format(self.__class__.__name__))

        log2 = LoggerFluentd('test-2', self.__app)

        log2.info('Test {}'.format(random.randint(1, 1000)),
                  self.__class__.__name__, log2.func, 'test-tag', {'field1': 1, 'field2': 2})

        log2.warning('Test {}'.format(random.randint(1, 1000)),
                     self.__class__.__name__, log2.func, 'test-tag', {'field1': 1, 'field2': 2})

    def test_exception(self):
        print('Init {}'.format(self.__class__.__name__))

        log2 = LoggerFluentd('test-3', self.__app)

        try:
            a = 2 / 0
        except:
            log2.exception('error test-3')
            log2.critical('Critical error')
            pass

    def check_instance(self, logger: logging):
        pass

    def test_multiple_loggers(self):
        log2 = LoggerFluentd('test-2', self.__app, 'fluentd.2', LoggerFluentd.INFO)
        log1 = LoggerFluentd('test-1', self.__app, 'fluentd.1', LoggerFluentd.DEBUG)

        log1.debug('DEBUG')
        log1.info('INFO')

        log2.debug('DEBUG')
        log2.info('INFO')







if __name__ == '__main__':
    unittest.main()

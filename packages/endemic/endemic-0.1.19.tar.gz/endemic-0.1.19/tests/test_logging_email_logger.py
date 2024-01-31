import sys

import unittest

from src.endemic.logging.email.logger import LoggerSMTP


class TestLoggingSMTPLogger(unittest.TestCase):

    # execute before every test case function run.
    def setUp(self):
        pass

    def test_debug(self):

        logger = LoggerSMTP(
            'smtp.yandex.ru',
            465,
            'mosrem-ru@yandex.ru',
            '080723Zaq1',
            'mosrem-ru@yandex.ru',
            ['mail@endemic.ru'],
            LoggerSMTP.DEBUG,
            'Test Error',
            False
        )

        print('Init {}'.format(self.__class__.__name__))

        logger.debug('123')

        # try:
        #     x = 1 / 0
        # except Exception:
        #     logger.error(message='Error x = 1 / 0', exc_info=sys.exc_info())


if __name__ == '__main__':
    unittest.main()

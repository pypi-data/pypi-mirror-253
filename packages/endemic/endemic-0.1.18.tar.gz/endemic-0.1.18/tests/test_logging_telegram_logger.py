import random
import unittest

from src.endemic.logging.telegram.logger import LoggerTelegram


class TestLoggingTelegramLogger(unittest.TestCase):

    # execute before every test case function run.
    def setUp(self):
        pass

    def test_debug(self):

        log = LoggerTelegram(
            '1047178763:AAEZpCTDn53WGWIDBQ5K4Tg2fBW4enrlweg',
            '-435754055',
            'test.logging',
            LoggerTelegram.INFO
        )

        print('Init {}'.format(self.__class__.__name__))

        log.debug('123 ? < > * _ ')
        log.info('123 ? < > * _ ')
        log.warning('123 ? < > * _ ')
        # log.error('123 ? < > * _ ')
        # log.exception('123 ? < > * _ ')
        # log.critical('123 ? < > * _ ')


if __name__ == '__main__':
    unittest.main()

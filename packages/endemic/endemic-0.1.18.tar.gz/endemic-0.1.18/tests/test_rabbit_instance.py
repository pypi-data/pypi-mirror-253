import unittest
import pika

from src.endemic.rabbit.instance import Rabbit
from src.endemic.logging.fluentd.logger import LoggerFluentd


class TestRabbitMessage(unittest.TestCase):
    PROD_RABBITMQ_USER_LOGIN = 'user_modules'
    PROD_RABBITMQ_USER_PASSWORD = '$C573bpM9Rbl'
    PROD_RABBITMQ_HOST = '213.226.68.10'
    PROD_RABBITMQ_PORT = 5672
    PROD_RABBITMQ_EXCHANGE = 'application'
    PROD_RABBITMQ_VIRTUAL_HOST = 'modules'

    # Rabbit
    PROD_SSL_RABBITMQ_USER_LOGIN = 'sbfpgnmw'
    PROD_SSL_RABBITMQ_USER_PASSWORD = 'Oirg-mNfI8bVvdikTpPGm5h139yzWKQi'
    PROD_SSL_RABBITMQ_HOST = 's2r_mq.freshapp-iot.com'
    PROD_SSL_RABBITMQ_PORT = 5671
    PROD_SSL_RABBITMQ_EXCHANGE = 'application'
    PROD_SSL_RABBITMQ_VIRTUAL_HOST = 'prod'

    # execute before every test case function run.
    def setUp(self):
        self.__app = 'tests.python.modules.rabbit.instance'
        self.__logger = LoggerFluentd('test-1', self.__app, 'fluentd', LoggerFluentd.INFO)

    def test_single(self):
        instance = Rabbit(self.__logger,
                          pika,
                          self.PROD_RABBITMQ_HOST,
                          self.PROD_RABBITMQ_PORT,
                          self.PROD_RABBITMQ_USER_LOGIN,
                          self.PROD_RABBITMQ_USER_PASSWORD,
                          self.PROD_RABBITMQ_VIRTUAL_HOST,
                          self.PROD_RABBITMQ_EXCHANGE)

        # instance.queue = 'account.private'
        # instance.callback = callback
        #
        # instance.run()

    def test_single_ssl(self):
        instance = Rabbit(self.__logger,
                          pika,
                          self.PROD_SSL_RABBITMQ_HOST,
                          self.PROD_SSL_RABBITMQ_PORT,
                          self.PROD_SSL_RABBITMQ_USER_LOGIN,
                          self.PROD_SSL_RABBITMQ_USER_PASSWORD,
                          self.PROD_SSL_RABBITMQ_VIRTUAL_HOST,
                          self.PROD_SSL_RABBITMQ_EXCHANGE,
                          True)

        instance.queue = 'account.private'
        instance.callback = callback

        instance.run_blocking()

        for i in range(60000):
            instance.publish_message({'test': True}, 'sensor.data', 10)


    def test_create_queue(self):
        instance = Rabbit(self.__logger,
                          pika,
                          self.PROD_RABBITMQ_HOST,
                          self.PROD_RABBITMQ_PORT,
                          self.PROD_RABBITMQ_USER_LOGIN,
                          self.PROD_RABBITMQ_USER_PASSWORD,
                          self.PROD_RABBITMQ_VIRTUAL_HOST,
                          self.PROD_RABBITMQ_EXCHANGE)

        instance.queue = 'test.without.priority'
        instance.exchange = 'application'
        instance.callback = callback

        instance.run()




def callback(ch, method, properties, message):
    print()


if __name__ == '__main__':
    unittest.main()

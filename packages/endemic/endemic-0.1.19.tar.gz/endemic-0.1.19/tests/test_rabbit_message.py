import unittest
from datetime import datetime

from src.endemic.rabbit.message import Message


class TestRabbitMessage(unittest.TestCase):

    # execute before every test case function run.
    def setUp(self):
        self.__app = 'tests.python.modules.rabbit.message'
        self.__message = Message()

    def test_single(self):
        print(self.__app)

        message = self.__example_message()
        self.__message.link = message['link']

        result = self.__message.default(message['project-flow'], [123])
        self.assertEqual(self.__message.link, result['link'])
        self.assertEqual([123], result['data'])
        self.assertEqual(datetime.now().strftime('%Y-%m-%dT%H:%M:%S.000000'), result['message-created'])
        self.assertEqual(6, len(result['project-flow']))
        self.assertNotEqual(5, len(result['project-flow']))

    def __example_message(self):
        return {
            "project-flow": [
                {
                    "task": "task-1",
                    "link": "link-1",
                    'current-iteration': 121,
                    'next-task-queue': "next-q-1",
                    'next-task-priority': "next-t-1"
                },
                {
                    "task": "......",
                    "link": "......",
                    'current-iteration': 1,
                    'next-task-queue': "...",
                    'next-task-priority': "..."
                },
                {
                    "task": "......",
                    "link": "......",
                    'current-iteration': 1,
                    'next-task-queue': "...",
                    'next-task-priority': "..."
                },
                {
                    "task": "......",
                    "link": "......",
                    'current-iteration': 1,
                    'next-task-queue': "...",
                    'next-task-priority': "..."
                },
                {
                    "task": "......",
                    "link": "......",
                    'current-iteration': 1,
                    'next-task-queue': "...",
                    'next-task-priority': "..."
                },
                {
                    "task": "......",
                    "link": "......",
                    'current-iteration': 1,
                    'next-task-queue': "...",
                    'next-task-priority': "..."
                },
            ],
            "message-created": "2021-01-02 15:53:25",
            "link": "0efa7304-dc86-4fd3-95fc-9c9d2da7ae5b",
            "data": []
        }


if __name__ == '__main__':
    unittest.main()

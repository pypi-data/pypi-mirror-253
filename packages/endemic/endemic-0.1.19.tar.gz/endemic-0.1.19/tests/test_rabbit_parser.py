import unittest
from datetime import datetime

from src.endemic.rabbit.constant import *
from src.endemic.rabbit.parser import Parser


class TestRabbitMessage(unittest.TestCase):

    # execute before every test case function run.
    def setUp(self):
        self.__app = 'tests.python.modules.rabbit.message'
        self.Parser = Parser()

    def test_single(self):
        message = self.__example_message()
        self.Parser.message = message

        self.assertEqual(message[PROJECT_FLOW][0], self.Parser.current_task)
        self.assertEqual(message[PROJECT_FLOW][0][TASK], self.Parser.task_title)
        self.assertEqual(5, len(self.Parser.next_tasks))
        self.assertEqual('0efa7304-dc86-4fd3-95fc-9c9d2da7ae5b', self.Parser.link_message)
        self.assertEqual('2021-01-02 15:53:25', self.Parser.message_created)

    def test_empty_message(self):
        message = {'test': True}
        self.Parser.message = message

        self.assertEqual(None, self.Parser.task_title)
        self.assertEqual(0, len(self.Parser.next_tasks))
        self.assertEqual(None, self.Parser.link_message)
        self.assertEqual('', self.Parser.message_created)

    @staticmethod
    def __example_message():
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

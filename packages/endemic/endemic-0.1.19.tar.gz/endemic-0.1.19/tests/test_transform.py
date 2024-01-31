import unittest

from src.endemic.rabbit import Parser


class TestPublicAccount(unittest.TestCase):

    # execute before every test case function run.
    def setUp(self):
        self.__app = 'tests.python.modules.message-parser'
        self.__parser = Parser()

    def test_single(self):
        print(self.__app)

        self.__parser.message = self.__example_message()

        print(self.__parser.tasks_all)

        project_flow = self.__example_message()["project-flow"]

        self.assertEqual(6, len(self.__parser.tasks_all))
        self.assertEqual(project_flow[0]['task'], self.__parser.task_title)
        self.assertEqual(project_flow[0]['link'], self.__parser.link_task)
        self.assertEqual(project_flow[0]['current-iteration'], self.__parser.iteration)
        self.assertEqual(project_flow[0]['next-task-queue'], self.__parser.next_task_queue)
        self.assertEqual(project_flow[0]['next-task-priority'], self.__parser.next_task_priority)

        self.assertEqual('0efa7304-dc86-4fd3-95fc-9c9d2da7ae5b', self.__parser.link_message)

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

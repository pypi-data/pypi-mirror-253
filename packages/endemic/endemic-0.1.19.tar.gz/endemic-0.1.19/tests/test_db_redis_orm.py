import time
import random
import unittest
import logging
import redis

from src.endemic.db.redis.orm import RedisORM


class TestDbMysqlORM(unittest.TestCase):

    # execute before every test case function run.
    def setUp(self):
        self.__app = 'tests.python.modules.redis'
        self.Class = RedisORM(logging, redis)
        self.Class.config('95.216.153.29', 6379, 'pzqjeLJA7c6NW4EX', 0)

    def test_single(self):
        for item in self.Class.get_all_keys():
            self.Class.delete_value(item)

        self.assertEqual([], self.Class.get_all_keys())
        self.Class.set_value('111', '222')
        self.assertEqual(['111'], self.Class.get_all_keys())

        # Test ttl
        self.Class.set_value('111', '3333', 3)
        time.sleep(1)
        self.assertEqual('3333', self.Class.get_value('111'))
        time.sleep(4)
        self.assertIsNone(self.Class.get_value('111'))

    def test_second(self):
        for item in self.Class.get_all_keys():
            self.Class.delete_value(item)

        data = {
            'first-{}'.format(random.randint(100000, 200000)): str(random.randint(0, 10)),
            'second-{}'.format(random.randint(100000, 200000)): str(random.randint(0, 10)),
            'third-{}'.format(random.randint(100000, 200000)): str(random.randint(0, 10)),
        }

        self.Class.set_hash_from_dict('222', data)
        self.assertEqual(['222'], self.Class.get_all_keys())
        self.assertEqual(data, self.Class.get_hash_by_key('222'))

    def test_third(self):
        for item in self.Class.get_all_keys():
            self.Class.delete_value(item)

        index = 'first-{}'.format(random.randint(100000, 200000))

        data = {
            index: str(random.randint(0, 10)),
            'second-{}'.format(random.randint(100000, 200000)): str(random.randint(0, 10)),
            'third-{}'.format(random.randint(100000, 200000)): str(random.randint(0, 10)),
        }

        self.Class.set_hash_from_dict('222', data)
        self.assertEqual(['222'], self.Class.get_all_keys())
        self.assertEqual(data, self.Class.get_hash_by_key('222'))

        # Remove
        self.Class.remove_key_from_hash('222', index)

        del data[index]

        self.assertEqual(data, self.Class.get_hash_by_key('222'))




if __name__ == '__main__':
    unittest.main()

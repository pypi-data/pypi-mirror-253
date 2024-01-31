import unittest
import logging
import pymysql
from functools import wraps

from src.endemic.db.mysql.orm import MysqlORM


def request():
    def wrapper(f):
        @wraps(f)
        def wrapped(self, *args, **kwargs):
            result = []
            [query, values] = f(self, *args, **kwargs)
            with self.mysql_connection.cursor() as cursor:
                try:
                    cursor.execute(query, values)
                    result = cursor.fetchall()
                except pymysql.IntegrityError as err:
                    errnum, errmsg = err.args
                    if errnum == 1062:
                        print(err)
                    else:
                        raise ValueError(errnum, errmsg)
            self.mysql_connection.commit()
            return result

        return wrapped

    return wrapper


class Mysql(MysqlORM):
    def __init__(self, logger: logging):
        super().__init__(logger)
        self.__mysql_connection = None

    @request()
    def pure_sql_request(self, query=''):
        return super().pure_sql_request(query)

    def close(self):
        self.__mysql_connection.close()

    def run(self):
        self.__mysql_connection = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db_name,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)

    @property
    def mysql_connection(self):
        if not self.__mysql_connection:
            raise ValueError('Not connected')
        return self.__mysql_connection


class TestDbMysqlORM(unittest.TestCase):

    # execute before every test case function run.
    def setUp(self):
        self.__app = 'tests.python.modules.mysql-orm'

    def te1st_single(self):
        self.__orm = Mysql(logging)
        self.__orm.config('51.38.127.206', 3306, 'bitweb_user', 'gHCitcOM)9ij789ZZ', 'bitweb')
        self.__orm.run()
        result = self.__orm.pure_sql_request('Select * FROM proxy WHERE 1')
        self.assertLess(10, len(result))


if __name__ == '__main__':
    unittest.main()

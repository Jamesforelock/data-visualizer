# @author Denis Chuprynin <denischuprynin@gmail.com>


from mysql.connector import connect
from mysql.connector.connection import MySQLConnection
from app.lib.mysql.MysqlConnectionCreatorException import MysqlConnectionCreatorException
from definitions import MYSQL


class MysqlConnectionCreator:
    __connection = None

    def get_connection(self) -> MySQLConnection:
        try:
            if self.__connection is None:
                self.__connection = connect(
                    host=MYSQL['host'],
                    user=MYSQL['user'],
                    password=MYSQL['password'],
                    database=MYSQL['database']
                )

            return self.__connection
        except Exception:
            raise MysqlConnectionCreatorException('Не удалось выполнить подключение к базе данных')

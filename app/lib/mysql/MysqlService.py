# @author Denis Chuprynin <denischuprynin@gmail.com>


import os
from mysql.connector.connection import MySQLConnection
from app.lib.file.FileService import FileService
from app.lib.file.FileServiceException import FileServiceException
from app.lib.mysql.MysqlServiceException import MysqlServiceException
from definitions import DATA_DIR


class MysqlService:
    def __init__(self, connection: MySQLConnection):
        self.connection = connection

    def create_csv_from_table(self, table_name: str, with_header=False) -> None:
        file_name = f'{DATA_DIR}/temporary/{table_name}.csv'
        file = open(file_name, 'w')

        try:
            if with_header:
                try:
                    query = f'DESCRIBE {table_name};'
                    with self.connection.cursor() as cursor:
                        cursor.execute(query)
                        result = cursor.fetchall()
                        field_names = list()
                        for row in result:
                            field_names.append(row[0])
                        file.write(','.join(field_names) + '\n')
                except Exception:
                    raise MysqlServiceException('Не удалось получить названия полей')

            try:
                query = f'SELECT * FROM {table_name};'
                with self.connection.cursor() as cursor:
                    cursor.execute(query)
                    result = cursor.fetchall()
                    for row in result:
                        row = list(map(str, row))
                        file.write(','.join(row) + '\n')
            except Exception:
                raise MysqlServiceException('Не удалось получить значения полей')

            file.close()

            try:
                FileService.copy_file_to_data_dir(file_name, False)
            except FileServiceException as e:
                raise MysqlServiceException(f'Ошибка добавления файла в список: {e}')
        except MysqlServiceException as e:
            raise MysqlServiceException(e)
        finally:
            os.remove(file_name)

# @author Denis Chuprynin <denischuprynin@gmail.com>


import glob
import os
import shutil
from app.lib.file.FileServiceException import FileServiceException
from definitions import DATA_DIR


class FileService:
    @staticmethod
    def get_data(file_name: str) -> list:
        path = os.path.join(DATA_DIR, file_name)
        file = open(path, 'r')
        items = list()
        for line in file:
            item = line.replace('\n', '').split(',')
            items.append(item)

        file.close()
        return items

    @staticmethod
    def get_file_list() -> list:
        files = glob.glob(DATA_DIR + '/*.csv')
        files.sort(key=os.path.getctime)
        files = [os.path.basename(file) for file in files]
        return files

    @staticmethod
    def remove_file(file_name: str) -> None:
        path = os.path.join(DATA_DIR, file_name)
        if not os.path.isfile(path):
            raise FileServiceException(f'Файла с именем {file_name} не существует')

        os.remove(path)

    @staticmethod
    def copy_file_to_data_dir(src_path: str) -> None:
        file_name = os.path.basename(src_path)
        dst_path = os.path.join(DATA_DIR, file_name)
        if os.path.isfile(dst_path):
            raise FileServiceException(f'Файл с именем {file_name} уже добавлен')
        if not FileService.validate_file_columns_count(src_path):
            raise FileServiceException(f'Количество столбцов в таблице должно быть = 2')

        shutil.copy(src_path, DATA_DIR)

    @staticmethod
    def validate_file_columns_count(path: str) -> bool:
        file = open(path, 'r')
        for line in file:
            item = line.replace('\n', '').split(',')
            if len(item) == 2:
                continue

            file.close()
            return False

        file.close()
        return True

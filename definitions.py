# @author Denis Chuprynin <denischuprynin@gmail.com>

import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT_DIR, 'app/data')

MYSQL = {
    'host': 'localhost',
    'user': 'user',
    'password': 'user',
    'database': 'for_vis'
}

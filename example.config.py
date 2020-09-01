from os import path
from datetime import timedelta
from nonebot.default_config import *

DEBUG = False

# Nonebot设置
SUPERUSERS = {123456789}
NICKNAME = {'胖虎', '小夫', '无内鬼'}
COMMAND_START = {'/', '／', '!', '！', '\\', ''}

HOST = '127.0.0.1'
PORT = 8080

SESSION_EXPIRE_TIMEOUT = timedelta(minutes=2)
SESSION_RUN_TIMEOUT = timedelta(minutes=5)


# 日志群,一些操作会记录在群里
LOG_GROUP = 0

# 代理设置
PROXY = {'all://': 'http://localhost:1080'}

# 数据库设置
DB_HOST = '127.0.0.1'
DB_PORT = 3306
DB_USER = ''
DB_PASS = ''
DB_NAME = ''

# Steam API Key
STEAM_KEY = ''

# 资源文件路径
ROOT_PATH = path.join(path.dirname(__file__), 'panghu')
RES_PATH = path.join(ROOT_PATH, 'res')
CACHE_PATH = path.join(ROOT_PATH, 'cache')

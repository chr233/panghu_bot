
'''
# @Author       : Chr_
# @Date         : 2020-08-13 18:29:02
# @LastEditors  : Chr_
# @LastEditTime : 2020-09-01 20:44:13
# @Description  : 底层操作模块
'''

from nonebot import get_bot
from aiomysql import  Connection,connect
from pymysql.converters import conversions

config = get_bot().config

dbhost = config.DB_HOST
dbport = config.DB_PORT
dbuser = config.DB_USER
dbpass = config.DB_PASS
dbname = config.DB_NAME

# 字节转数字, PS:只能转1位
conversions[16] = lambda x: ord(x)


async def get_conn() -> Connection:
    '''
    获取数据库连接
    '''
    try:
        conn = await connect(
            host=dbhost,
            port=dbport,
            user=dbuser,
            password=dbpass,
            db=dbname,
            conv=conversions)
        return(conn)
    except Exception as e:
        print(e)
        return(False)


def close_conn(conn:Connection):
    '''
    销毁连接
    '''
    if conn:
        conn.close()

async def exec_dql_mul(conn: Connection, sql: str, value: tuple = None) -> tuple:
    '''
    查询_所有结果
    '''
    if not conn:
        print('数据库连接出错')
        return(False)
    try:
        async with conn.cursor() as cur:
            await cur.execute(sql, value)
            result = await cur.fetchall()
        return(result)
    except Exception as e:
        print(e)
        return(False)


async def exec_dql(conn: Connection, sql: str, value: tuple = None) -> tuple:
    '''
    查询_单结果
    '''
    if not conn:
        print('数据库连接出错')
        return(False)
    try:
        async with conn.cursor() as cur:
            await cur.execute(sql, value)
            result = await cur.fetchone()
        return(result)
    except Exception as e:
        print(e)
        return(False)


async def exec_dml(conn: Connection, sql: str, value: tuple = None) -> bool:
    '''
    写入
    '''
    if not conn:
        print('数据库连接出错')
        return(False)
    try:
        async with conn.cursor() as cur:
            await cur.execute(sql, value)
            await conn.commit()
        return(True)
    except Exception as e:
        print(e)
        await conn.rollback()
        return(False)

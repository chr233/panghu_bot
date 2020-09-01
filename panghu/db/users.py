
'''
# @Author       : Chr_
# @Date         : 2020-08-29 11:20:09
# @LastEditors  : Chr_
# @LastEditTime : 2020-09-01 14:15:48
# @Description  : 用户操作
'''

from re import escape
from datetime import datetime
from .sql import Connection
from .sql import exec_dml, exec_dql, exec_dql_mul, connect_db


def check_flag(flag: int) -> (int, bool, bool):
    '''
    检查用户的flag

    参数:
        flag: int
    返回:
        int: 等级 0~3
        bool: 是否注销
        bool: 是否封禁
    '''
    level = (flag & 0b1100) >> 2
    is_ban = flag & 0b01 == 1
    is_disable = flag & 0b10 == 2
    return((level, is_ban, is_disable))


def flag_to_str(flag) -> str:
    '''
    flag转字符串

    参数:
        flag: int
    返回:
        str: 文本
    '''
    level = (flag & 0b1100) >> 2
    is_ban = flag & 0b01 == 1
    is_disable = flag & 0b10 == 2
    result = f'等级:{level}'
    if is_ban:
        result += '[封禁]'
    if is_disable:
        result += '[禁用]'
    return(result)


async def __add_user(conn: Connection, qqid: int, name: str) -> bool:
    '''
    创建用户, 需要传入conn对象

    参数:
        conn: 数据库连接对象
        qqid: QQ号
        name: 昵称
    返回:
        bool: 操作是否成功
    '''
    sql = ("INSERT INTO `panghu`.`users` (`qqid`,`name`) SELECT %s,%s "
           "FROM DUAL WHERE NOT EXISTS (SELECT `qqid` FROM `panghu`.`users` WHERE `qqid`='%s')")
    result = await exec_dml(conn, sql, (qqid, name, qqid))
    return(result)


async def add_user(qqid: int, name: str) -> bool:
    '''
    创建用户

    参数:
        qqid: QQ号
        name: 昵称
    返回:
        bool: 操作是否成功
    '''
    try:
        conn = await connect_db()
        result = await __add_user(conn, qqid, name)
        conn.close()
        return result
    except Exception as e:
        print(e)
        return False


async def __get_user(conn: Connection, qqid: int = 0, name: str = '') -> tuple:
    '''
    获取用户信息, 需要传入conn对象
    '''
    sql = "SELECT `uid`,`qqid`,`name`,`flag`,`added` FROM `panghu`.`users` WHERE `qqid`=%s"
    resp = await exec_dql(conn, sql, (qqid, ))
    if resp:
        uid, qqid, flag, added, name = resp
        r = (uid, qqid, name, flag, added)
    else:
        r = (-1, 0, '', 0, datetime.datetime(1970, 1, 1, 0, 0))
    return(r)


async def get_user(qqid: int = 0, name: str = None, auto_add: bool = False) -> (int, int, str, int, datetime):
    '''
    获取用户信息

    参数:
        [qqid]: QQ号
        [name]: 昵称
    返回:
        int: uid
        int: QQ号
        str: 昵称
        int: flag
        datetime: 添加时间
    '''
    try:
        conn = await connect_db()
        resp = await __get_user(conn, qqid, name)

        if resp:
            uid, qqid, flag, added, name = resp
            r = (uid, qqid, name, flag, added)
        else:

            r = False

        conn.close()
        return(r)
    except Exception as e:
        print(e)
        return(False)


async def get_user_mul(uid: int = 0, name: str = None) -> tuple:
    '''
    获取用户信息, 批量

    参数:
    '''
    conn = await connect_db()
    sql = "SELECT `uid`,`qqid`,`name`,`flag`,`added` FROM `panghu`.`users` WHERE `qqid` LIKE %s OR `name` LIKE %s"
    resps = await exec_dql_mul(conn, sql,  (uid, name))
    conn.close()

    r = []
    for resp in resps:
        if resp:
            uid, qqid, name, flag, added = resp
            r.append((uid, qqid, name, flag, added))
    return(str(resp))

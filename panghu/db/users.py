
'''
# @Author       : Chr_
# @Date         : 2020-08-29 11:20:09
# @LastEditors  : Chr_
# @LastEditTime : 2020-09-01 21:52:02
# @Description  : users表操作
'''

from re import escape
from .sql import exec_dml, exec_dql, exec_dql_mul, get_conn, close_conn, Connection


def check_flag(flag: int) -> bool:
    '''
    检查用户的flag

    参数:
        flag: int
    返回:
        int: 等级 0~3
        bool: 是否注销
        bool: 是否封禁
    '''
    _, is_ban, is_disable = unpack_flag(flag)
    if is_ban or is_disable:
        return(False)
    else:
        return(True)


def unpack_flag(flag: int) -> (int, bool, bool):
    '''
    解包用户的flag

    参数:
        flag: int
    返回:
        int: 等级 0~3
        bool: 是否注销
        bool: 是否封禁
    '''
    level = int((flag & 0b1100) >> 2)
    is_ban = flag & 0b01 == 1
    is_disable = flag & 0b10 == 2
    return((level, is_ban, is_disable))


def flag_to_str(flag: int) -> str:
    '''
    flag转字符串

    参数:
        flag: int
    返回:
        str: 文本
    '''
    level, is_ban, is_disable = unpack_flag(flag)
    result = f'用户等级: {level}'
    if is_ban:
        result += ' [封禁]'
    if is_disable:
        result += ' [禁用]'
    return(result)


async def add_user(conn: Connection, qqid: int, name: str) -> bool:
    '''
    创建用户

    参数:
        conn: 数据库连接对象
        qqid: QQ号
        name: 昵称
    返回:
        bool: 操作是否成功
    '''
    sql = ("INSERT INTO `panghu`.`users` (`qqid`,`name`) SELECT %s,%s "
           "FROM DUAL WHERE NOT EXISTS (SELECT `qqid` FROM `panghu`.`users` "
           "WHERE `qqid`='%s')")
    result = await exec_dml(conn, sql, (qqid, name, qqid))
    return(result)


async def get_user(conn: Connection, qqid: int) -> (int, int, str, int):
    '''
    获取用户信息

    参数:
        conn: 数据库连接对象
        qqid: QQ号
    返回:
        int: uid
        int: QQ号
        str: 昵称
        int: flag
    '''
    sql = "SELECT `uid`,`qqid`,`name`,`flag` FROM `panghu`.`users` WHERE `qqid`=%s"
    result = await exec_dql(conn, sql, qqid)
    return(result)


async def get_user_mul(conn: Connection, qqid: int = 0, name: str = None) -> tuple:
    '''
    获取用户信息, 批量

    参数:
        [qqid]: QQ号
        [name]: 昵称
    返回
    '''
    sql = ("SELECT `uid`,`qqid`,`name`,`flag` FROM `panghu`.`users` "
           "WHERE `qqid` LIKE %s OR `name` LIKE %s")
    result = await exec_dql_mul(conn, sql,  (qqid, f'%{name}%'))
    return(result)


async def modify_user(conn: Connection, uid: int, qqid: int, name: str, flag: int) -> bool:
    '''
    修改用户信息

    参数:
        conn: 数据库连接对象
        uid: uid
        qqid: QQ号
        name: 昵称
        flag: flag
    返回:
        bool: 操作是否成功
    '''
    sql = "UPDATE `panghu`.`users` SET `qqid`=%s,`name`=%s,`flag`=%s WHERE `uid`=%s"
    result = await exec_dml(conn, sql,  (qqid, name, flag, uid))
    return(result)

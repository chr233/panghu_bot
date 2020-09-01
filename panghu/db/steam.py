
'''
# @Author       : Chr_
# @Date         : 2020-08-29 19:02:28
# @LastEditors  : Chr_
# @LastEditTime : 2020-09-01 22:35:27
# @Description  : steam表操作
'''

from json import dumps,loads
from .sql import exec_dml, exec_dql, exec_dql_mul, get_conn, Connection


async def add_steam_data(conn: Connection, uid: int, steamid: int) -> bool:
    '''
    获取steam状态, 需要传入conn对象

    参数:
        conn: 数据库连接对象
        uid: uid
        steamid: steam64位id
    返回:
        bool: 操作是否成功
    '''
    sql = ("SELECT `steamid`,`nickname`,`level`,`badge_name`,"
           "`game_count`,`badge_count`,`group_count`,`img_dict` "
           "FROM `panghu`.`steam` WHERE `uid`=%s")
    result = await exec_dql(conn, sql, uid)
    return(result)


async def get_steam_data(conn: Connection, uid: int) -> (int, str, int, str, int, int, int, str):
    '''
    获取steam状态, 需要传入conn对象

    参数:
        conn: 数据库连接对象
        uid: uid
    返回:
        int: steamid
        str: 昵称
        int: 等级
        str: 喜爱的徽章名
        int: 游戏数量
        int: 徽章数量
        int: 组数量
        str: 图片信息json
    '''
    sql = ("SELECT `steamid`,`nickname`,`level`,`badge_name`,"
           "`game_count`,`badge_count`,`group_count`,`img_dict` "
           "FROM `panghu`.`steam` WHERE `uid`=%s")
    result = await exec_dql(conn, sql, uid)
    return(result)


async def modify_steam_data(conn: Connection, uid: int, name: str, level: int, badge_name: str,
                            game_count: int, badge_count: int, group_count: int, img_dict: dict) -> bool:
    '''
    修改steam数据

    参数:
        uid: uid
        name: 昵称
        level: 等级
        badge_name: 喜爱的徽章名
        game_count: 游戏数量
        badge_count: 徽章数量
        group_count: 组数量
        img_dict: 图片信息json
    返回:
        bool:
            操作是否成功
    '''
    imgs = dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':'))
    sql = ("UPDATE `panghu`.`steam` SET `nickname`=%s,`level`=%s,"
           "`badge_name`=%s,`game_count`=%s,`badge_count`=%s,`group_count`=%s,"
           "`img_dict`=%s WHERE `uid`=%s")
    result = await exec_dml(conn, sql,  (name, level, badge_name, game_count,
                                         badge_count, group_count, imgs,  uid))
    return(result)

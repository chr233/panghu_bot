
'''
# @Author       : Chr_
# @Date         : 2020-08-29 19:02:28
# @LastEditors  : Chr_
# @LastEditTime : 2020-09-01 20:34:27
# @Description  : steam表操作
'''

from json import loads
from .sql import exec_dml, exec_dql, exec_dql_mul, get_conn, Connection
from .users import get_user

async def __add_steam_data(conn: Connection, uid: int) -> (int, str, int, str, int, int, int, dict):
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


async def add_steam_data(uid: int,steamid:int) -> bool:
    '''
    获取steam状态

    参数:
        uid: uid
        steamid: steam64位id
    返回:
        bool: 操作是否成功
    '''
    conn = await get_conn()
    resp = await __add_steam_data(conn, uid,steamid)
    if resp:
        steamid, name, level, b_name, g_count, b_count, g2_count, imgjson = resp
        try:
            s = loads(imgjson)
            imgs = {

            }


async def __get_steam_data(conn: Connection, uid: int) -> (int, str, int, str, int, int, int, dict):
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


async def get_steam_data(uid: int) -> (int, str, int, str, int, int, int, dict):
    '''
    获取steam状态

    参数:
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
    conn = await get_conn()
    resp = await __get_steam_data(conn, uid)
    if resp:
        steamid, name, level, b_name, g_count, b_count, g2_count, imgjson = resp
        try:
            s = loads(imgjson)
            imgs = {

            }


async def set_steamid(uid: int):

    pass

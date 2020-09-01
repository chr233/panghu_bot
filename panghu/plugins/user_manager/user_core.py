'''
# @Author       : Chr_
# @Date         : 2020-08-12 14:02:34
# @LastEditors  : Chr_
# @LastEditTime : 2020-09-01 21:37:36
# @Description  : 用户插件-核心
'''

import json
import httpx
from bs4 import BeautifulSoup
from panghu.db import users


async def add_new_user(qqid: int, name: str) -> str:
    '''
    添加新用户

    参数:
        qqid: QQ号
        name: 昵称
    返回:
        str: 消息
    '''
    conn = await users.get_conn()
    result = await users.add_user(conn, qqid, name)
    msg = '操作成功' if result else '操作失败'
    users.close_conn(conn)
    return(msg)


async def get_user_info(qqid: int, name: str) -> tuple:
    '''
    获取用户信息
    '''
    conn = await users.get_conn()
    resp = await users.get_user(conn, qqid)
    if resp:  # 找到用户
        uid, _, _, flag = resp
    else:  # 新增用户
        await users.add_user(conn, qqid, name)
        resp = await users.get_user(conn, qqid)
        if resp:
            uid, _, _, flag = resp
        else:
            return('数据库连接可能出错')
    # 更新用户信息
    await users.modify_user(conn, uid, qqid, name, flag)
    msg = users.flag_to_str(flag)
    users.close_conn(conn)
    return(msg)


# async def get_user_info_mul(qqid: int, name: str) -> tuple:
#     '''
#     获取用户信息, 批量
#     '''
#     conn = await users.get_conn()
#     resps = await users.get_user_mul(conn, qqid, True)
#     print(resps)
#     try:
#         msg = [users.flag_to_str(x[3]) for x in resps]
#         msg='\n'.join(msg)
#     except Exception as e:
#         print(e)
#         msg='数据库'
#     users.close_conn(conn)
#     return('\n'.join(msg))

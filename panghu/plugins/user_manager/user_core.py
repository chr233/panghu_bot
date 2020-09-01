'''
# @Author       : Chr_
# @Date         : 2020-08-12 14:02:34
# @LastEditors  : Chr_
# @LastEditTime : 2020-09-01 16:18:56
# @Description  : 用户插件-核心
'''

import json
import httpx
from bs4 import BeautifulSoup
from panghu.db import users


async def add_user(qqid: int, name: str) -> str:
    '''
    1
    '''

    r = await users.add_user(qqid, name)
    print(r)
    return(str(r))


async def search_user(qqid: int, name: str) -> tuple:
    '''
    获取用户信息
    '''
    resp = await users.get_user(qqid, name, True)

    print(resp)

    if resp:
        uid, _, _, flag = resp
        print(f'{qqid}{users.flag_to_str(flag)}')
        await users.modify_user(uid, qqid, name, flag)

    return(str(resp))

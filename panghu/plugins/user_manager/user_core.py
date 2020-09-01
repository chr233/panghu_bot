'''
# @Author       : Chr_
# @Date         : 2020-08-12 14:02:34
# @LastEditors  : Chr_
# @LastEditTime : 2020-09-01 12:24:27
# @Description  : 用户插件-核心
'''

import json
import httpx
from bs4 import BeautifulSoup
from panghu.db import users


async def add_user(uid: int, name: str) -> str:
    '''
    1
    '''

    r = await users.add_user(uid, name)
    print(r)
    return(r)


async def search_user(uid: int) -> tuple:
    '''
    获取用户信息
    '''
    r = await users.get_user(uid)
    print(r)
    return(r)

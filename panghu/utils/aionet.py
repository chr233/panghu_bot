
'''
# @Author       : Chr_
# @Date         : 2020-08-16 21:14:48
# @LastEditors  : Chr_
# @LastEditTime : 2020-08-31 14:20:48
# @Description  : 异步网络模块
'''

import httpx
from httpx import Response
from nonebot import get_bot

config = get_bot().config
PROXY = config.PROXY


async def async_get(url: str, params: dict = None) -> Response:
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, params=params)
    return(resp)


async def async_post(url: str, params: dict = None, data: dict = None) -> Response:
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, params=params)
    return(resp)


async def async_get_proxy(url: str, params: dict = None) -> Response:
    async with httpx.AsyncClient(proxies=PROXY) as client:
        resp = await client.get(url, params=params)
    return(resp)


async def async_post_proxy(url: str, params: dict = None, data: dict = None) -> Response:
    async with httpx.AsyncClient(proxies=PROXY) as client:
        resp = await client.get(url, params=params)
    return(resp)

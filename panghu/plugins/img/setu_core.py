'''
# @Author       : Chr_
# @Date         : 2020-08-12 14:02:34
# @LastEditors  : Chr_
# @LastEditTime : 2020-08-24 17:00:34
# @Description  : 涩图插件-数据源
'''

from os import path
from nonebot import get_bot
from random import choice
from nonebot import MessageSegment
from panghu.utils.aionet import async_get

config = get_bot().config

OUTPUTS_PATH = path.join(config.CACHE_PATH, 'img.jpg')

SETU_APIS = ['https://acg.xydwz.cn/api/api.php',
             'https://api.dongmanxingkong.com/suijitupian/acg/1080p/index.php',
             'https://acg.yanwz.cn/api.php'
             ]


async def get_setu() -> str:
    '''
    获取随机动漫图

    返回:
        str: 消息段
    '''
    url=choice(SETU_APIS)
    result=await dowmload_img(url)
    if result:
        return(MessageSegment.image(OUTPUTS_PATH))
    else:
        return('服务器出了点问题')


async def dowmload_img(url: str) -> str:
    '''
    下载图片
    '''
    try:
        r = await async_get(url)
        with open(OUTPUTS_PATH, 'wb') as f:
            f.write(r.content)
        return(True)
    except Exception as e:
        print(e.get_text())
        return(False)

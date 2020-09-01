
'''
# @Author       : Chr_
# @Date         : 2020-08-12 14:59:01
# @LastEditors  : Chr_
# @LastEditTime : 2020-08-29 16:13:37
# @Description  : 用户插件-命令
'''

from .user_core import add_user, search_user
from nonebot import on_command, CommandSession
# from nonebot import on_natural_language, NLPSession, IntentCommand
# from jieba import posseg


@on_command('register', only_to_me=True)
async def register(session: CommandSession):
    event = session.event
    uid = event.user_id
    name = event.sender.get('nickname', '')
    msg = await add_user(uid, name)
    await session.send(msg)


@on_command('getuser', only_to_me=True)
async def getuser(session: CommandSession):
    uid = session.event.user_id

    msg = await search_user(uid)
    await session.send(msg)


'''
# @Author       : Chr_
# @Date         : 2020-08-12 14:59:01
# @LastEditors  : Chr_
# @LastEditTime : 2020-09-01 21:30:52
# @Description  : 用户插件-命令
'''

from .user_core import add_new_user, get_user_info
from nonebot import on_command, CommandSession
from nonebot import permission as perm
# from nonebot import on_natural_language, NLPSession, IntentCommand
# from jieba import posseg


@on_command('myinfo', aliases=('我的信息',), only_to_me=True)
async def myinfo(session: CommandSession):
    event = session.event
    uid = event.user_id
    name = event.sender.get('nickname', '')
    msg = await get_user_info(uid, name)
    await session.send(msg)


# @on_command('adduser', alias=('添加用户',), permission=perm.SUPERUSER, only_to_me=True)
# async def adduser(session: CommandSession):
#     event = session.event
#     uid = event.user_id
#     name = event.sender.get('nickname', '')
#     msg = await get_user_info(uid, name)
#     await session.send(msg)

# @adduser.args_parser
# async def _(session: CommandSession):
#     stripped_arg = session.current_arg_text.strip()

#     if session.is_first_run:
#         if stripped_arg:
#             s= stripped_arg.split()
#         return
#     if not stripped_arg:
#         session.pause('城市名称不能为空呢，请重新输入')

#     session.state[session.current_key] = stripped_arg


# @on_command('userinfo', only_to_me=True)
# async def userinfo(session: CommandSession):
#     event = session.event
#     uid = event.user_id
#     name = event.sender.get('nickname', '')
#     msg = await get_user_info(uid, name)
#     await session.send(msg)


# @weather.args_parser
# async def _(session: CommandSession):
#     stripped_arg = session.current_arg_text.strip()

#     if session.is_first_run:
#         if stripped_arg:
#             session.state['city'] = stripped_arg
#         return
#     if not stripped_arg:
#         session.pause('城市名称不能为空呢，请重新输入')

#     session.state[session.current_key] = stripped_arg

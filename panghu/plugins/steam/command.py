
'''
# @Author       : Chr_
# @Date         : 2020-08-12 14:59:01
# @LastEditors  : Chr_
# @LastEditTime : 2020-08-13 16:08:36
# @Description  : Steam插件-命令
'''

from .steam_core import creat_user
from nonebot import on_command, CommandSession
# from nonebot import on_natural_language, NLPSession, IntentCommand
# from jieba import posseg


@on_command('steamuser', only_to_me=True)
async def steamuser(session: CommandSession):
    uid = session.ctx['user_id']
    msg = await creat_user(uid)
    await session.send(msg)


@steamuser.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    # if session.is_first_run:
    #     if stripped_arg:
    #         session.state['city'] = stripped_arg
    #     return

    # if not stripped_arg:
    #     session.pause('城市名称不能为空呢，请重新输入')

    session.state[session.current_key] = stripped_arg


# @on_natural_language(keywords={'天气'})
# async def _(session: NLPSession):
#     stripped_msg = session.msg_text.strip()
#     words = posseg.lcut(stripped_msg)

#     city = None
#     for word in words:
#         if word.flag == 'ns':
#             city = word.word
#             break

#     return IntentCommand(90.0, 'weather', current_arg=city or '')

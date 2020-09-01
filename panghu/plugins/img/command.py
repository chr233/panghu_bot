
'''
# @Author       : Chr_
# @Date         : 2020-08-12 14:59:01
# @LastEditors  : Chr_
# @LastEditTime : 2020-08-28 19:24:42
# @Description  : 图片插件-命令
'''

from .setu_core import get_setu
from nonebot import permission as perm
from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand


@on_command('setu', aliases=('来点涩图', '来点色图', '来点动漫图'))
async def setu(session: CommandSession):
    bot = session.bot
    if await perm.check_permission(bot, session.event,
                                   perm.PRIVATE | perm.SUPERUSER | perm.GROUP_ADMIN):
        msg = await get_setu()
    elif session.event.group_id == 916905424:
        msg = await get_setu()
    else:
        msg = '权限不够哦，可以找机器人私聊'
    await session.send(msg)


# @setu.args_parser
# async def _(session: CommandSession):
#     stripped_arg = session.current_arg_text.strip()

#     if session.is_first_run:
#         if stripped_arg:
#             session.state['city'] = stripped_arg
#         return
#     if not stripped_arg:
#         session.pause('城市名称不能为空呢，请重新输入')

#     session.state[session.current_key] = stripped_arg


@on_natural_language(keywords={'涩图', '色图'})
async def _(session: NLPSession):
    stripped_msg = session.msg_text.strip()
    if '来' in stripped_msg:
        return IntentCommand(70.0, 'setu')

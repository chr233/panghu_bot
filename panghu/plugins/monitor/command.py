
'''
# @Author       : Chr_
# @Date         : 2020-08-12 14:59:01
# @LastEditors  : Chr_
# @LastEditTime : 2020-08-27 15:31:45
# @Description  : 服务器监控-命令
'''

from .monitor_core import gen_usage_graph
from nonebot import permission as perm
from nonebot import on_command, CommandSession, MessageSegment
from nonebot import on_natural_language, NLPSession, IntentCommand

@on_command('dashboard', aliases={'htop','systop','系统监控','系统状态'},
            only_to_me=True, permission=perm.SUPERUSER | perm.GROUP_ADMIN)
async def dashboard(session: CommandSession):
    msg=gen_usage_graph()
    await session.send(msg)


@on_natural_language(keywords={'状态','系统'})
async def _(session: NLPSession):
    stripped_msg = session.msg_text.strip()
    return IntentCommand(60.0, 'dashboard')

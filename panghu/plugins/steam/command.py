
'''
# @Author       : Chr_
# @Date         : 2020-08-12 14:59:01
# @LastEditors  : Chr_
# @LastEditTime : 2020-09-02 15:26:49
# @Description  : Steam插件-命令
'''

from .steam_core import creat_user
from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
# from jieba import posseg


@on_command('bindsteam', only_to_me=True)
async def bindsteam(session: CommandSession):
    uid = session.ctx['user_id']

    session.get('t')

    # msg = await creat_user(uid)
    await session.send(msg)


@bindsteam.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['city'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('城市名称不能为空呢，请重新输入')

    session.state[session.current_key] = stripped_arg


@on_natural_language(keywords={'绑定'})
async def _(session: NLPSession):
    stripped_msg = session.msg_text.strip().lower()

    args=stripped_msg.split()

    if len(args)>1:
        url=args[1]

    if 'steam' in stripped_msg:
        return IntentCommand(70.0, 'bindsteam', current_arg=url or '')


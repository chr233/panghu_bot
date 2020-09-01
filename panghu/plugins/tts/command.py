
'''
# @Author       : Chr_
# @Date         : 2020-08-12 14:59:01
# @LastEditors  : Chr_
# @LastEditTime : 2020-08-13 12:54:52
# @Description  : 文字转语音-命令
'''

from .tts_core import text_to_sounds
from nonebot import on_command, CommandSession, MessageSegment
from nonebot import on_natural_language, NLPSession, IntentCommand

@on_command('read', aliases=('tts', '说', '念', '读', '生成语音'), only_to_me=True)
async def read(session: CommandSession):
    words = session.get('words', prompt='你想让胖虎说什么呢？(仅限20字以内中文)')
    filename = text_to_sounds(words)
    msg = MessageSegment.record(filename)
    print(msg)
    await session.send(msg)


@read.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()[:20]

    if session.is_first_run:
        if stripped_arg:
            session.state['words'] = stripped_arg
        return
    if not stripped_arg:
        session.pause('你想让胖虎说什么呢？')
    session.state[session.current_key] = stripped_arg


@on_natural_language(keywords={'说', '念', '读'})
async def _(session: NLPSession):
    stripped_msg = session.msg_text.strip()

    return IntentCommand(60.0, 'read', current_arg=stripped_msg or '')

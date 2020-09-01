
'''
# @Author       : Chr_
# @Date         : 2020-08-12 14:59:01
# @LastEditors  : Chr_
# @LastEditTime : 2020-08-13 23:03:16
# @Description  : 天气插件-命令
'''

from .weather_core import get_weather_report
from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from jieba import posseg


@on_command('weather', aliases=('天气', '天气预报', '查天气'))
async def weather(session: CommandSession):
    city = session.get('city', prompt='你想查询哪个城市的天气呢？')
    msg = await get_weather_report(city, 3)
    await session.send(msg)


@weather.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['city'] = stripped_arg
        return
    if not stripped_arg:
        session.pause('城市名称不能为空呢，请重新输入')

    session.state[session.current_key] = stripped_arg


@on_natural_language(keywords={'天气'})
async def _(session: NLPSession):
    stripped_msg = session.msg_text.strip()
    words = posseg.lcut(stripped_msg)

    city = None
    for word in words:
        if word.flag == 'ns':
            city = word.word
            break

    return IntentCommand(90.0, 'weather', current_arg=city or '')

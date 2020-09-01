import nonebot
from nonebot import on_command, CommandSession, MessageSegment, get_loaded_plugins


@on_command('usage', aliases=['help', '菜单', '命令', '帮助', '插件',
                              '使用帮助', '使用方法', '命令列表', '指令列表', '插件列表'])
async def usage(session: CommandSession):

    event = session.event
    bot = session.bot
    plugins = list(filter(lambda p: p.name, get_loaded_plugins()))

    msglist = ('可用插件列表：',
               *(f'{i}. {p.name}' for i, p in enumerate(plugins, 1)),
               '输入「序号」或「插件名」查看具体命令说明')

    args = session.get('args', prompt='\n'.join(msglist))

    msglist = []
    for i, plugins in enumerate(plugins, 1):
        for arg in args:
            if arg == str(i) or arg in plugins.name.lower():
                msglist.append(f'{i}. {plugins.name}\n{plugins.usage}')

    if msglist:
        msg = '\n\n'.join(msglist)
    else:
        msg = '找不到该模块,输入「帮助」查看所有插件列表'

    await session.send(msg)


@usage.args_parser
async def _(session: CommandSession):
    args = session.current_arg_text.lower().split()
    session.state[session.current_key] = args

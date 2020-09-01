from nonebot import on_command, CommandSession, MessageSegment
from nonebot.command import kill_current_session

@on_command('cancel', aliases=('kill', '取消', '放弃', '退出'), privileged=True, only_to_me=False)
async def cancel(session: CommandSession):
    await session.send('当前操作已取消')
    kill_current_session(session.ctx)
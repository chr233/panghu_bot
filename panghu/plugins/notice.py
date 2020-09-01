
'''
# @Author       : Chr_
# @Date         : 2020-07-14 19:51:31
# @LastEditors  : Chr_
# @LastEditTime : 2020-08-26 17:27:07
# @Description  : 处理通知
'''

from nonebot import get_bot
from nonebot import on_notice, NoticeSession

LOGGID = get_bot().config.LOG_GROUP


@on_notice('group_increase')
async def group_increase(session: NoticeSession):
    if session.event.user_id == session.self_id:
        event=session.event
        gid = event.group_id
        oid = event.operator_id
        await session.send(f'添加机器人成功\n输入「退出本群」让机器人退出\n输入「胖虎，帮助」查看使用说明\n输入')
        await session.bot.send_group_msg(group_id=LOGGID, message=f'被[{oid}]邀请进群[{gid}]', self_id=session.self_id)


@on_notice('group_decrease')
async def group_decrease(session: NoticeSession):
    event=session.event
    if event.user_id == session.self_id:
        reason = session.event.sub_type
        if reason in ('kick', 'kick_me'):
            reason = '移出'
        elif reason == 'leave':
            reason = '退出'
        gid = event.group_id
        oid = event.operator_id
        await session.bot.send_group_msg(group_id=LOGGID, message=f'被[{oid}]{reason}群{gid}', self_id=session.self_id)

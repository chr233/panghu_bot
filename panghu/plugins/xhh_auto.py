
'''
# @Author       : Chr_
# @Date         : 2020-08-23 19:44:55
# @LastEditors  : Chr_
# @LastEditTime : 2020-08-29 09:36:46
# @Description  : 自动加群审批
'''
from nonebot import get_bot
from nonebot import on_request, RequestSession, MessageSegment

config = get_bot().config

LOGGID = config.LOG_GROUP


@on_request('group.add')
async def handle_request(session: RequestSession):
    gid = session.event.group_id
    if gid == 916945024:
        uid = session.event.user_id
        cmt = session.event.comment
        sid = session.self_id
        if 'xhh_auto' in cmt.lower():
            uid = session.event.user_id
            msg = f'欢迎{MessageSegment.at(uid)}加入本群, 请遵守群规'
            await session.send_msg(group_id=916945024, message=msg, self_id=sid)
            await session.approve()
        else:
            await session.bot.send_msg(group_id=LOGGID,
                                             message=f'用户{uid}加入xhh_auto被拒\n{cmt}', self_id=sid)
            await session.reject(reason='答案错误, 仔细看看群简介吧')

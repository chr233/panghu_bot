
'''
# @Author       : Chr_
# @Date         : 2020-08-26 17:09:31
# @LastEditors  : Chr_
# @LastEditTime : 2020-08-26 17:27:44
# @Description  : 处理请求
'''
from nonebot import get_bot
from nonebot import on_request, RequestSession

LOGGID = get_bot().config.LOG_GROUP


@on_request('friend')
async def friend_request(session: RequestSession):
    uid = session.event.user_id
    await session.approve()
    bot = session.bot
    await bot.send_private_msg(user_id=uid, message=f'添加好友成功\n输入「帮助」查看机器人使用说明', self_id=session.self_id)
    await bot.send_group_msg(group_id=LOGGID, message=f'与[{uid}]加为好友', self_id=session.self_id)


@on_request('group.invite')
async def friend_request(session: RequestSession):
    event=session.event
    uid = event.user_id
    gid = event.group_id
    # await session.approve()
    bot = session.bot
    await bot.send_private_msg(user_id=uid, message=f'暂不开放邀请进群的功能，如有需要请联系1142033406', self_id=session.self_id)
    await bot.send_group_msg(group_id=LOGGID, message=f'[{uid}]尝试邀请进群[{gid}]', self_id=session.self_id)

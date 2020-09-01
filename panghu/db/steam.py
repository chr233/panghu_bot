
'''
# @Author       : Chr_
# @Date         : 2020-08-29 19:02:28
# @LastEditors  : Chr_
# @LastEditTime : 2020-08-31 14:49:35
# @Description  : Steam查询
'''


from .users import get_user, get_user_mul, __get_user




async def get_steamid(uid: int):
    '''
    获取用户steamid
    '''
    conn = await connect_db()
    resp = await __get_user(conn, uid, None)
    if not resp:
        return None


async def set_steamid(uid: int):

    pass



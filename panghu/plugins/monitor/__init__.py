
'''
# @Author       : Chr_
# @Date         : 2020-08-13 00:14:35
# @LastEditors  : Chr_
# @LastEditTime : 2020-08-28 23:24:06
# @Description  : 服务器监控插件
'''

__plugin_name__ = '服务器监控【管理员】'
__plugin_usage__ = '''
系统状态：获取系统资源使用情况
'''.strip()

from .command import dashboard

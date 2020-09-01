
'''
# @Author       : Chr_
# @Date         : 2020-08-12 14:02:24
# @LastEditors  : Chr_
# @LastEditTime : 2020-08-28 23:25:31
# @Description  : 天气插件
'''

__plugin_name__ = '天气预报'
__plugin_usage__ = '''
获取城市3天的天气预报

例如：温州天气、北京的天气预报
'''.strip()

from .command import weather


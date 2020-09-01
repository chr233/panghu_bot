'''
# @Author       : Chr_
# @Date         : 2020-08-12 14:02:34
# @LastEditors  : Chr_
# @LastEditTime : 2020-08-17 00:28:36
# @Description  : 天气插件-数据源
'''

import json
import httpx
from bs4 import BeautifulSoup
from panghu.utils.aionet import async_get


async def get_weather_report(city: str, days: int = 3) -> str:
    '''
    获取天气预报

    参数:
        city: 城市名
        days: 天数
    返回:
        str: 天气预报
    '''
    code = await get_city_code(city)
    if code:
        title, weather = await get_city_weather(code)
        if weather:
            weather = weather[:days]
            weather = [f'{w[0]}：{w[1]} {w[2]}℃' for w in weather]
            wstr = '\n'.join(weather)
            msg = f'{title}:\n{wstr}'
        else:
            msg = f'未查到该城市天气'
            print(title)
    else:
        msg = f'未查到该城市天气'
    return(msg)


async def get_city_weather(code: int) -> (str, list):
    '''
    获取城市天气

    参数:
        code: 城市id
    返回:
        str: 标题
        list: 7天天气详情,每个元素为(日期,天气,最高温度,最低温度)
    '''
    try:
        url = f'http://www.weather.com.cn/weather/{code}.shtml'
        r = await async_get(url)
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text, 'lxml')
        title = soup.select_one('head>title').get_text()
        w_title = title.split(',')[0]
        w_days = []
        for w in soup.select('li.skyid'):
            day = w.h1.get_text()[:-4]
            weather = w.select_one('p.wea').get_text()
            t = w.select_one('p.tem')
            t_h = t.span.get_text()[:-1] if t.span else None
            t_l = t.i.get_text()[:-1]
            temp=f'{t_h}/{t_l}' if t_h else f'{t_l}'
            w_days.append((day, weather, temp))
        result = (w_title, w_days)
    except Exception as e:
        print(e.get_text())
        result = (f'{e}', [])
    return(result)


async def get_city_code(city: str) -> int:
    '''
    获取城市id

    参数:
        city: 城市名
    返回:
        int: 城市代码
    '''
    try:
        url = 'http://toy1.weather.com.cn/search'
        p = {'cityname': city}
        r = await async_get(url, p)
        r.encoding = 'utf-8'
        txt = r.text
        txt = txt.replace('success_jsonpCallback', '', 1)
        jd = json.loads(txt[1:-1])
        code = jd[0]['ref'].split('~')[0]
    except Exception as e:
        code = -1
    return(code)
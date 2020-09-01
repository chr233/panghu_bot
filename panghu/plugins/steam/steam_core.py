'''
# @Author       : Chr_
# @Date         : 2020-08-12 14:02:34
# @LastEditors  : Chr_
# @LastEditTime : 2020-09-01 12:25:14
# @Description  : Steam插件-数据源
'''

import json
import httpx
from bs4 import BeautifulSoup
# from panghu.db import connect_db, exec_dml, exec_dql


import requests

KEY = '4E28187DDCBC796FD1972C2A43B45A76'


def _get_user_64id(cid: str) -> str:
    '''
    自定义url转64位ID, 失败返回False

    参数:
        cid: 自定义url
    返回:
        int: 64位id
    '''
    url = 'https://api.steampowered.com/ISteamUser/ResolveVanityURL/v1/'
    p = {'key': KEY, 'vanityurl': cid}
    try:
        resp = requests.get(url=url, params=p)
        jd = resp.json()
        r = jd['response']
        return(r.get('steamid', False))
    except Exception as e:
        print(e)
        return(False)


def _get_user_profile(u64: str) -> tuple:
    '''
    获取用户数据, 失败返回False

    参数:
        u64: 64位steamid
    返回:

    '''
    url = f'https://steamcommunity.com/profiles/{u64}'
    c = {'Steam_Language': 'schinese'}
    try:
        resp = requests.get(url=url, cookies=c)
        resp.encoding = 'utf-8'
        html = resp.text

        # f = open('1.html', 'wb+')
        # f.write(html.encode('utf-8'))

        # f = open('notset.html', 'rb')
        # html = f.read()
        
        soup = BeautifulSoup(html, 'lxml')
        header = soup.select_one('div.profile_header_content')
        private_tag = header.select_one('div.profile_private_info')

        if not private_tag:
            # 资料公开
            # 名称 & 等级信息
            nick_name = header.select_one(
                'div.profile_header_centered_persona>div:nth-child(1)>span:nth-child(1)'
            ).get_text()
            real_name = header.select_one(
                'div.header_real_name>bdi:nth-child(1)'
            ).get_text()
            level = int(header.select_one(
                '.persona_level>div:nth-child(1)>span:nth-child(1)'
            ).get_text())

            faveb = header.select_one('div.favorite_badge')
            if faveb:
                faveb_name = faveb.select_one(
                    'div.favorite_badge_description>div:nth-child(1)>a:nth-child(1)'
                ).get_text()
                faveb_pic = faveb.select_one(
                    'div.favorite_badge_icon>a:nth-child(1)>img:nth-child(1)'
                )['src']
            else:
                faveb_name = None
                faveb_pic = None

            rside = soup.select_one('div.profile_rightcol')
            badge_count = int(rside.select_one(
                'div.profile_badges>div:nth-child(1)>div:nth-child(1)>a:nth-child(1)>span:nth-child(2)'
            ).get_text().replace(',', ''))
            # 组信息
            group = rside.select_one('div.profile_group_links')
            if group:
                group_count = int(group.select_one(
                    'div.profile_count_link>a:nth-child(1)>span:nth-child(2)'
                ).get_text())
                group_list = group.select(
                    'div.profile_count_link_preview>div.profile_group'
                )
                group_pic = [
                    g.select_one(
                        'div:nth-child(1)>a:nth-child(1)>img:nth-child(1)')['src']
                    for g in group_list
                ]
                if group_pic:
                    group_pic[0] = group_pic[0].replace('_medium', '')
            else:
                group_count = 0
                group_list = []
                group_pic = []

            # 游戏信息
            game = soup.select_one('div.recent_games')
            if game:
                game_count = int(rside.select_one(
                    'div.profile_item_links>div:nth-child(1)>a:nth-child(1)>span:nth-child(2)'
                ).get_text().replace(',', ''))
                game_list = game.select(
                    'div.recent_game>div.recent_game_content')

                game_pic = [
                    g.select_one(
                        'div:nth-child(1)>div:nth-child(1)>a:nth-child(1)>img:nth-child(1)')['src']
                    for g in game_list
                ]

            else:
                game_count = 0
                game_list = []
                game_pic = []

            result = {
                'user': (nick_name, real_name, level),
                'badge': (faveb_name, faveb_pic, badge_count),
                'group': (group_pic, group_count),
                'game': (game_pic, game_count)
            }
            return(result)
        else:
            # 资料私密
            return(False)
    except IOError as e:
        print(e)
        return(False)


a = (_get_user_profile('1'))
print(a)
# f=open('1.jpg','wb+')
# f.write(a)
# f.close()

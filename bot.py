#!/usr/bin/python38
import jieba
import config
import nonebot
from os import path

# from nonebot import logging

if __name__ == '__main__':
    nonebot.init(config)

    jieba.set_dictionary(path.join(config.RES_PATH, 'dict.txt'))

    # if not config.DEBUG:
    #     logging.getLogger('nonebot').logger.setLevel(logging.WARN)

    nonebot.load_plugins(path.join(path.dirname(__file__),
                                   'panghu', 'plugins'), 'panghu.plugins')

    nonebot.run()

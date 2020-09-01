from os import path
from nonebot import get_bot
from base64 import b64decode
from pypinyin import lazy_pinyin
from pydub import AudioSegment

config = get_bot().config

SOUND_PATH = path.join(config.RES_PATH, 'sound')
OUTPUTS_PATH = path.join(config.CACHE_PATH, 'tts.amr')


def text_to_sounds(words: str) -> str:
    '''
    文字转语音

    参数:
        words: 要转语音的文字
    返回:
        str: Base64编码的语音
    '''
    pinyin = lazy_pinyin(words, errors='ignore')
    sounds = load_sounds(pinyin)
    merge_sounds(pinyin, sounds)
    return(OUTPUTS_PATH)


def load_sounds(pinyin: list) -> dict:
    '''
    加载语音库

    参数:
        pinyin: 拼音列表
    返回:
        dict: 键名为拼音,键值为AudioSegment
    '''
    tmp = {}
    for i in pinyin:
        if i not in tmp:
            p = path.join(SOUND_PATH, f'{i}.wav')
            d = AudioSegment.from_wav(p)
            tmp[i] = d
    return(tmp)


def merge_sounds(pinyin: list, sounds: dict) -> str:
    '''
    生成语音

    参数:
        pinyin: 拼音列表
        sounds: 音频字典
    返回:
        str: Base64编码的音频
    '''
    tmp = AudioSegment.empty()
    for i in pinyin:
        tmp += sounds[i]
    tmp.set_frame_rate(8000).export(OUTPUTS_PATH, format='amr')
    return(True)

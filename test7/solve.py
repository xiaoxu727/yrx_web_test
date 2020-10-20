#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: xuxingyuan
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@software: yrx_web_test
@file: solve.py.py
@time: 2020/10/20 11:36
@desc:
'''

import base64
from fontTools.ttLib import TTFont
import random
import requests


names = ['极镀ギ紬荕', '爷灬霸气傀儡', '梦战苍穹', '傲世哥', 'мaη肆風聲', '一刀メ隔世', '横刀メ绝杀', 'Q不死你R死你', '魔帝殤邪', '封刀不再战', '倾城孤狼', '戎马江湖', '狂得像风', '影之哀伤', '謸氕づ独尊', '傲视狂杀', '追风之梦', '枭雄在世', '傲视之巅', '黑夜刺客', '占你心为王', '爷来取你狗命', '御风踏血', '凫矢暮城', '孤影メ残刀', '野区霸王', '噬血啸月', '风逝无迹', '帅的睡不着', '血色杀戮者', '冷视天下', '帅出新高度', '風狆瑬蒗', '灵魂禁锢', 'ヤ地狱篮枫ゞ', '溅血メ破天', '剑尊メ杀戮', '塞外う飛龍', '哥‘K纯帅', '逆風祈雨', '恣意踏江山', '望断、天涯路', '地獄惡灵', '疯狂メ孽杀', '寂月灭影', '骚年霸称帝王', '狂杀メ无赦', '死灵的哀伤', '撩妹界扛把子', '霸刀☆藐视天下', '潇洒又能打', '狂卩龙灬巅丷峰', '羁旅天涯.', '南宫沐风', '风恋绝尘', '剑下孤魂', '一蓑烟雨', '领域★倾战', '威龙丶断魂神狙', '辉煌战绩', '屎来运赚', '伱、Bu够档次', '九音引魂箫', '骨子里的傲气', '霸海断长空', '没枪也很狂', '死魂★之灵'];

def solve():

    with requests.Session() as sess:
        url = "http://match.yuanrenxue.com/api/match/7?page={page}"
        result = {}
        for i in range(1, 6):
            resp = sess.get(url.format(page=i))
            cmp = get_font_map(resp.json().get('woff'))
            name_value = parse_value(resp.json().get("data"), i, cmp)
            result.update(name_value)
    maxV = max(result.values())
    # Choice is one of the keys with max value
    choice = random.choice([key for key, value in result.items() if value == maxV])
    print(choice)


def parse_value(data, i, cmp):
    name_value = {}
    for index, d in enumerate(data):
        value = ''.join([str(cmp[_]) for _ in d.get('value').split(" ") if _ != ''])
        name = names[index + 1 + (i-1)*10]
        name_value[name] = int(value)
    return name_value



def get_font_map(tff):

    b = base64.b64decode(tff)
    with open('test6.ttf', 'wb') as f:
        f.write(b)
    font = TTFont('test6.ttf') #打开本地的ttf文件
    font.saveXML('tff.xml')
    bestcmap = font.tables['post']
    cmp = {}
    for index, value in enumerate(bestcmap.extraNames):
        if index != 9:
            cmp[value.replace("uni", "&#x")] = index + 1
        else:
            cmp[value.replace("uni", "&#x")] = 0

    return cmp


if __name__ == '__main__':
    # font_face = 'AAEAAAAKAIAAAwAgT1MvMvzUaNQAAAEoAAAAYGNtYXBkRYGVAAABpAAAAYpnbHlmSsPfPQAAA0gAAAQCaGVhZBbuoWgAAACsAAAANmhoZWEGzQE2AAAA5AAAACRobXR4ArwAAAAAAYgAAAAabG9jYQSzBdoAAAMwAAAAGG1heHABGABFAAABCAAAACBuYW1lUGhGMAAAB0wAAAJzcG9zdDLlZ1YAAAnAAAAAiAABAAAAAQAA+rxFVl8PPPUACQPoAAAAANnIUd8AAAAA27QL3wAU/+wCQQLZAAAACAACAAAAAAAAAAEAAAQk/qwAfgJYAAAALwIpAAEAAAAAAAAAAAAAAAAAAAACAAEAAAALADkAAwAAAAAAAgAAAAoACgAAAP8AAAAAAAAABAIqAZAABQAIAtED0wAAAMQC0QPTAAACoABEAWkAAAIABQMAAAAAAAAAAAAAEAAAAAAAAAAAAAAAUGZFZABAoUj4RgQk/qwAfgQkAVQAAAABAAAAAAAAAAAAAAAgAAAAZAAAAlgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAMAAAAcAAEAAAAAAIQAAwABAAAAHAAEAGgAAAAWABAAAwAGoUizmLUjwjTEE8SByGPlKeiV+Eb//wAAoUizmLUjwjTEE8SByGPlKeiV+Eb//166TG9K4D3WO/E7hDelGtgXdAfAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACwBJAIIAnwDQAOYBFAEnAWgBvgIBAAEAFP/sADIAFAACAAA3MxUUHhQoAAACADP/8gImAtgAHAAoAAABIgYVFBcWMzY2NzMXFAcGIyInIxYzNjc2NTQnJgcyFxYUBiMiJjU0NgEkaYg9P2c/YhsEAS8xU34WUR3HeEhDP0J/Si0sXkVLV1kC2ItqZ0FEAT42GnhQU3q/AW9sqqZaYEUzMJVgXUtOYgAAAQAz//ICJQLKACQAABMDMzY3NjM2FhUUBiMiJyYnIxYXFjMyNzY1NCYjJgcGByM3ITVpJk4WKigzTlpiS0IrMAZRB0tCX2pITX9mMSovHgQYAVwCyv52KxUWAV5WS2AgJERiOTNBRWxzggESEiTvSQAAAgAYAAACQQLKAAoADgAAAQEVIRUzNTM1IxEHMxEhAYD+mAFnTnR0UQP+3gLK/iZOoqJDAeVr/oYAAAEAPgAAAhoC2AAdAAABIgYHMzY3NhcyFhUUBwYHBgcGFSE1ITY3Njc2NCYBNmyFAVMBKidKRk43HFRxKkcB3P6JFIhvJUaAAtiPeF8wMwFHQkU7HTxOMU9iSUhcTCdLu3IAAQBvAAABaQLKAAkAAAEGBgcVNjcRMxEBKSNmMWVDUgLKKD4OUh5E/ZoCygACADL/8gImAtkADAAZAAABJgcGEBcWIDc2ECcmBzIXFhQHBiInJjQ3NgEsgUA5OUABAEI5OUJ/YCofHyrAKh4eKgLYAXJg/rxgcXFgAURgckdnSPpKZmZK+khnAAEAQgAAAhcCygAGAAATFSEBMwE1QgGB/vZXAQcCykv9gQKHQwAAAgAz//ICJgLZABsAKAAAASIHBhUUFxYXNjY0JiMiBwYHIyc0NzYXNhczJgM2FxYUBwYHIicmNDYBNnlHQz5CgmmIfWY/MDIbBAEvMFR8GFEeyUktLC0tSEotLF0C2HBrq6NcYAEBi9KDHx44GnpOVAEBe8D+tgEwLZgzMAEzMJZfAAMAKv/yAi4C2AAfACwAOAAAASIHBhUUFxYXFQYHBhUUFjI3NjU0JyYnNTY3NjU0JyYHMhcWFAcGIicmNDc2EzIXFhQHBiImNDc2ASxwPzobHDk4JyqG90VCKic4Nx4bOj9wSywlISinJyElKk1WMCsrL65aLC4C2Do1TjknKhQCDjAzRV90OzlfRTMwDgIUKic5TjU6QychayInJyJrISf+wysngCcqUYAnKwABADP/8gImAtgAKwAAASIHBgczNjYXNhcWFAYjIxUzNhYUBwYjJicmJyMWFxYXMjY1NCcmJzY1NCYBM2Y/QgpRB1JIRiclS0g3OktTKy5NQy01A1MJTEBmb4kkIT91fQLYOjpoSE4BASQheEFAAUh/KiwBJCxUeD8zAX1hPyoqEyh4WmgAAAAAAAASAN4AAQAAAAAAAAAXAAAAAQAAAAAAAQAMABcAAQAAAAAAAgAHACMAAQAAAAAAAwAUACoAAQAAAAAABAAUACoAAQAAAAAABQALAD4AAQAAAAAABgAUACoAAQAAAAAACgArAEkAAQAAAAAACwATAHQAAwABBAkAAAAuAIcAAwABBAkAAQAYALUAAwABBAkAAgAOAM0AAwABBAkAAwAoANsAAwABBAkABAAoANsAAwABBAkABQAWAQMAAwABBAkABgAoANsAAwABBAkACgBWARkAAwABBAkACwAmAW9DcmVhdGVkIGJ5IGZvbnQtY2Fycmllci5QaW5nRmFuZyBTQ1JlZ3VsYXIuUGluZ0ZhbmctU0MtUmVndWxhclZlcnNpb24gMS4wR2VuZXJhdGVkIGJ5IHN2ZzJ0dGYgZnJvbSBGb250ZWxsbyBwcm9qZWN0Lmh0dHA6Ly9mb250ZWxsby5jb20AQwByAGUAYQB0AGUAZAAgAGIAeQAgAGYAbwBuAHQALQBjAGEAcgByAGkAZQByAC4AUABpAG4AZwBGAGEAbgBnACAAUwBDAFIAZQBnAHUAbABhAHIALgBQAGkAbgBnAEYAYQBuAGcALQBTAEMALQBSAGUAZwB1AGwAYQByAFYAZQByAHMAaQBvAG4AIAAxAC4AMABHAGUAbgBlAHIAYQB0AGUAZAAgAGIAeQAgAHMAdgBnADIAdAB0AGYAIABmAHIAbwBtACAARgBvAG4AdABlAGwAbABvACAAcAByAG8AagBlAGMAdAAuAGgAdAB0AHAAOgAvAC8AZgBvAG4AdABlAGwAbABvAC4AYwBvAG0AAAIAAAAAAAAADgAAAAAAAAAAAAAAAAAAAAAAAAAAAAsACwAAAQoBBgEFAQMBAgELAQgBBwEJAQQHdW5pYzQ4MQd1bmljNDEzB3VuaWMyMzQHdW5pYjUyMwd1bmlhMTQ4B3VuaWM4NjMHdW5pYjM5OAd1bmllODk1B3VuaWU1MjkHdW5pZjg0Ng=='
    # print(get_font_map(font_face))
    solve()

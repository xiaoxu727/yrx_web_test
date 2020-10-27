#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: xuxingyuan
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@software: yrx_web_test
@file: solve.py
@time: 2020/10/17 10:10
@desc:
'''
import requests
from collections import Counter

def solve():
    # sess = utils.yrf_login()
    with requests.Session() as sess:
        url_login = 'http://match.yuanrenxue.com/api/loginInfo'

        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
         'Accept-Encoding': 'gzip, deflate',
         'Accept-Language': 'zh-CN,zh;q=0.9',
         'Connection': 'keep-alive',
         'Referer': 'http://match.yuanrenxue.com/match/3',
         # 'Cookie':'Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1602903223,1602906447; sessionid=tv10se9un5b1k3nj0msspkrba55ixd59; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1602906512',
         'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
                   }
        values = []
        for i in range(1, 6):
            url_before = 'http://match.yuanrenxue.com/logo'
            sess.post(url=url_before, headers=headers)
            url = "http://match.yuanrenxue.com/api/match/3?page={}".format(i)
            resp = sess.get(url=url, headers=headers)
            print(resp.text)
            for value in resp.json().get('data'):
                values.append(value.get('value'))
        print(Counter(values))
        counter = Counter(values)
        print(max(counter, key=lambda x: counter[x] ))





if __name__ == '__main__':
    solve()




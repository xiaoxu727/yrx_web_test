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
import utils
import requests
# from requests.exceptions import

def solve():
    # sess = utils.yrf_login()
    with requests.Session() as sess:
        url_login = 'http://match.yuanrenxue.com/api/loginInfo'

        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
         'Accept-Encoding': 'gzip, deflate',
         'Accept-Language': 'zh-CN,zh;q=0.9',
         'Connection': 'keep-alive',
         'Host': 'match.yuanrenxue.com',
         'Referer': 'http://match.yuanrenxue.com/match/3',
         'Cookie':'Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1602903223,1602906447; sessionid=tv10se9un5b1k3nj0msspkrba55ixd59; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1602906512',
         'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
         'X-Requested-With': 'XMLHttpRequest'
                   }


        header_before ={'Accept': '*/*',
                         'Accept-Encoding': 'gzip, deflate',
                         'Accept-Language': 'zh-CN,zh;q=0.9',
                         'Content-Length': '0',
                         'Host': 'match.yuanrenxue.com',
                         'Origin': 'http://match.yuanrenxue.com',
                         # 'Proxy-Connection': 'keep-alive',
                         'Referer': 'http://match.yuanrenxue.com/match/3',
                         'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
                        }


        cookies = {'Hm_lvt_9bcbda9cbf86757998a2339a0437208e': '1602903223,1602906447',
                  'Hm_lpvt_9bcbda9cbf86757998a2339a0437208e': '1602906512',
                  'sessionid': 'tv10se9un5b1k3nj0msspkrba55ixd59'}

        url_before = 'http://match.yuanrenxue.com/logo'
        # sess.get(url_login, headers=headers, cookies=cookies)
        resp = sess.post(url=url_before, headers=header_before, proxies={'http': 'http://localhost:8888'}, cookies=cookies)
        url = "http://match.yuanrenxue.com/api/match/3?page=5"
        resp = sess.get(url=url, headers=headers, proxies={'http': 'http://localhost:8888'}, cookies=cookies)

        print(resp.text)


if __name__ == '__main__':
    solve()


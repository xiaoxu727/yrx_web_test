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
from requests.cookies import RequestsCookieJar
import urllib


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
         # 'Cookie':'Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1602903223,1602906447; sessionid=tv10se9un5b1k3nj0msspkrba55ixd59; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1602906512',
         'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
         'X-Requested-With': 'XMLHttpRequest',
            'Cookie': 'sessionid=vdc4yrac1l6xvxfk5iojphrvg4anir81; m=f817b2bbf852aff1a0352e9791b3123e|1603113170000',
          'DNT':'1'

                   }


        header_before ={'Accept': '*/*',
                         'Accept-Encoding': 'gzip, deflate',
                         'Accept-Language': 'zh-CN,zh;q=0.9',
                         'Content-Length': '0',
                         'Host': 'match.yuanrenxue.com',
                         'Origin': 'http://match.yuanrenxue.com',
                         # 'Proxy-Connection': 'keep-alive',
                         'Referer': 'http://match.yuanrenxue.com/match/3',
                         'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
                          'DNT': '1',
                            'Cookie': 'sessionid=vdc4yrac1l6xvxfk5iojphrvg4anir81; m=f817b2bbf852aff1a0352e9791b3123e|1603113170000'
                        # 'X-Requested-With': 'XMLHttpRequest',
                        }

        cookie_jar = RequestsCookieJar()
        # cookie_jar.set('Hm_lvt_9bcbda9cbf86757998a2339a0437208e','1602903223,1602906447', path='\\')
        # cookie_jar.set('Hm_lpvt_9bcbda9cbf86757998a2339a0437208e','1602906512',path='\\')
        cookie_jar.set(name='sessionid', value='vdc4yrac1l6xvxfk5iojphrvg4anir81', path='/',  domain='yuanrenxue.com')
        cookie_jar.set('m','f817b2bbf852aff1a0352e9791b3123e|1603113170000', path='/',  domain='yuanrenxue.com')
        # m=; sessionid=vdc4yrac1l6xvxfk5iojphrvg4anir81
        cookies = {'m': '78b487e3e0606312d7e8033457a5244c|1603098338000',
                  'sessionid': 'vdc4yrac1l6xvxfk5iojphrvg4anir81'}

        url_before = 'http://match.yuanrenxue.com/logo'
        # sess.get(url_login, headers=headers, cookies=cookies)
        # sess.post(url=url_before, headers=header_before, proxies={'http': 'http://localhost:8888'}, cookies=cookie_jar)
        url = "http://match.yuanrenxue.com/api/match/3?page=4"
        resp = sess.get(url=url, headers=headers, proxies={'http': 'http://localhost:8888'}, cookies=cookies)

        print(resp.text)


if __name__ == '__main__':
    solve()

    from http import cookiejar
    from urllib import request
    cookie = cookiejar.CookieJar()
    cookie.set_cookie(cookiejar.Cookie(version=0,
                 port=None,
                 port_specified=None,
                 domain='match.yuanrenxue.com',
                                       domain_specified=None, domain_initial_dot=None,
                 path='/', path_specified=None,
                 secure=None,
                 expires='1603113170000',
                 discard=None,
                 comment=None,
                 comment_url=None,
                 rest=None, value='f817b2bbf852aff1a0352e9791b3123e|1603113170000', name='m'))
    cookie.set_cookie(cookiejar.Cookie(version=0,
                 port=None,
                 port_specified=None,
                 domain='yuanrenxue.com',
                                       domain_specified=None, domain_initial_dot=None,
                 path='/', path_specified=None,
                 secure=None,
                 expires='1603113170000',
                 discard=None,
                 comment=None,
                 comment_url=None,
                 rest=None, value='vdc4yrac1l6xvxfk5iojphrvg4anir81', name='sessionid'))
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    header_before = {'Accept': '*/*',
                     'Accept-Encoding': 'gzip, deflate',
                     'Accept-Language': 'zh-CN,zh;q=0.9',
                     'Content-Length': '0',
                     'Host': 'match.yuanrenxue.com',
                     'Origin': 'http://match.yuanrenxue.com',
                     'Proxy-Connection': 'keep-alive',
                     "Cookie": "sessionid=vdc4yrac1l6xvxfk5iojphrvg4anir81; m=f817b2bbf852aff1a0352e9791b3123e|1603113170000",
                     'Referer': 'http://match.yuanrenxue.com/match/3',
                     'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
                     'DNT': '1'
                     }

    url_before = 'http://match.yuanrenxue.com/logo'
    request_before = request.Request(url=url_before, method="POST", headers=header_before)
    # resp = opener.open(request_before)
    resp = request.urlopen(request_before)

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Host': 'match.yuanrenxue.com',
        'Referer': 'http://match.yuanrenxue.com/match/3',
        "Cookie": "sessionid=vdc4yrac1l6xvxfk5iojphrvg4anir81; m=f817b2bbf852aff1a0352e9791b3123e|1603113170000",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'DNT': '1',

    }
    url = "http://match.yuanrenxue.com/api/match/3?page=4"
    request2 = request.Request(url=url, method="GET", headers=headers)
    # resp2 = opener.open(request2)
    resp2 = request.urlopen(request2)
    import chardet
    print(chardet.detect(resp2.read()))




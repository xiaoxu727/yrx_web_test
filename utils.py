#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: xuxingyuan
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@software: yrx
@file: utils.py
@time: 2020/10/16 20:57
@desc:
'''
import pprint
import math
import hashlib
import time
import requests

def hex_md5(str):
    return hashlib.md5(str.encode()).hexdigest()


def get_timestamp():
    timestamp = math.floor(time.time()) * 1000
    return timestamp


def str_2_headers(file):
    headers = {}
    with open(file) as f:
        l = f.readline()
        while l:
            k_v = l.split(":", 1)
            headers[k_v[0].strip()] = k_v[1].strip().replace('\n','')
            l = f.readline()

    pprint.pprint(headers)


def str_2_cookies(str):
    cookie = {}
    k_vs = str.split(';')
    for k_v in k_vs:
        k, v = k_v.split('=', 1)
        cookie[k.strip()] = v.strip()
    return cookie

def yrf_login():
    url = 'http://match.yuanrenxue.com/api/login'

    data = {'username':'mix2plus',
        'password': 'Yrx@2020'}

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36'}
    s = requests.session()
    r = s.post(url, data=data, headers=headers)
    print(r.json())
    url = 'http://match.yuanrenxue.com/api/loginInfo'
    r = s.get(url, data=data, headers=headers)
    # print(r.json())
    # print(s.cookies)
    return s


if __name__ == '__main__':
    # pprint.pprint(str_2_headers('resources/headers.txt'))
    pprint.pprint(str_2_cookies('Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1602903223; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1602903223; sessionid=tv10se9un5b1k3nj0msspkrba55ixd59'))
    # print(get_timestamp())
    # yrf_login()
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
            k_v = l.split(":")
            headers[k_v[0]] = k_v[1]
            l = f.readline()
    return headers

if __name__ == '__main__':
    # pprint.pprint(str_2_headers('headers.txt'))
    print(get_timestamp())

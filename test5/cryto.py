#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: xuxingyuan
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@software: yrx_web_test
@file: cryto.py
@time: 2020/10/20 10:06
@desc:
'''

from Crypto.Cipher import AES
import base64


def add_to_16(s):
    while len(s) % 16 != 0:
        s += (16 - len(s) % 16) * chr(16 - len(s) % 16)
    # return str.encode(s)  # 返回bytes
    return str.encode(s)  # 返回bytes


def get_secret_url(text, key='qnbyzzwmdgghmcnm'):
    aes = AES.new(str.encode(key), AES.MODE_ECB)  # 初始化加密器，本例采用ECB加密模式
    encrypted_text = str(base64.encodebytes(aes.encrypt(add_to_16(text))), encoding='utf8').replace('\n', '')  # 加密
    encrypted_text = encrypted_text.replace('/', "^")  # ddd.replace(/\//g, "^")
    return encrypted_text[:-2]


def get_real_url(first_url, key):
    aa = first_url.split('/')
    aaa = len(aa)
    bbb = aa[aaa - 1].split('.')
    ccc = bbb[0]
    secret_text = get_secret_url(ccc, key=key)
    return first_url.replace(ccc, secret_text)

#
# url = 'http://xxx.xxxx.xxx.xxx.cn:80/xxxx/938848.jhtml'
# key = 'qnbyzzwmdgghmcnm'  # 此处问加密key值
# url = get_real_url("a643b89274e7242c92d45937dc56ff5b,603a80b467cbebff3f5969d025e54400,b8ff7f74167b6c5425dc2f80b837c46f,fdb7555ba28de0ac1aaa949aa00c1195,f3883dbcea751f1af40c9b5785db1a16", key=key)
# print(url)
print(add_to_16('aa'))
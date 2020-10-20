#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: xuxingyuan
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@software: yrx_web_test
@file: solve.py
@time: 2020/10/18 12:53
@desc:
'''

import requests
import execjs


def solve():
    url = 'http://match.yuanrenxue.com/api/match/5?page=2&m=1603021358746&f=1603021357000'
    headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Connection': 'keep-alive',
               'Cookie': 'qpfccr=true; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1603021746; '
                         'Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1603021759; '
                         'm=abdc47ff3e6eaaec15349f37b3a707e4; '
                         'RM4hZBv0dDon443M=Loxzp2DcbeW0pTlVMImsX3eyO3WfcVA3mT1VqjPTvWf1YwqNlumlhKFD5JRWhcshM78Cg2MpnwSJtnqcsHOTJlXV/JoBxUsmO+HdfYorPbosHx2z+2shXOjw68I38iprmfIlY2FDV4EQcHEarvY1CiS4PgWqNr7zif77PsPj7ICQXnx2j+gYVsm6uqpvXftJ+TZJH76GaaVHyIiSmKg/2jrMINz2C3kw89gSV1VQ31c=',
               'Host': 'match.yuanrenxue.com',
               'Referer': 'http://match.yuanrenxue.com/match/5',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
               'X-Requested-With': 'XMLHttpRequest'}

    cookies = {'Hm_lpvt_9bcbda9cbf86757998a2339a0437208e': '1603020689',
               'Hm_lvt_9bcbda9cbf86757998a2339a0437208e': '1603020689',
               'RM4hZBv0dDon443M': 'Cinuj+USryUAtD3b/tdy67Nfggp/2Y9BCY6GbCsJhVKI7ejVnM9+zCE555oVfOJNgub2cYlKsIew2iKIYvRvgiO4G2Fi8D6gHyZ9ivr+wJn9H94RL5rW+s8n3HgJqTLRAZzFcVJ+1bLMS7AKCkz1KlCKjxmM1UDR4mxddUC3Zu5bZwWbgKoEATAeENHxiX8MH1fGbypq88Uft8TbddGhO84QWCqgIgWjwaqLQz+GMpc=',
               'm': 'e7a14fe495732a7d23f3ac84ddcd3e00',
               'qpfccr': 'true'}
    with requests.Session() as sess:
        resp = sess.get(url, headers=headers, cookies=cookies)
        print(resp.text)


def get_m():
    js_str = """"
      var _$pm = ['WRtcL8kRg8kp', 'xSkVW4mRW6ldVHLmvmofW5m=', 'W6dcPCoQtKtdK1n/WQxdQ8kBWQaRW7FdJsBdTvuSWRDX', 'W7i7r8oPW6P6e8kXk8kkaW==', 'gheEz8k0f2BcUfXtW73dGSkIWQ/dNJRdQhxcOs1kW4yOW4i=', 'WO/cQSk+bCke', 'vGZdSaa='];
                                    var _$pe = function(m, e) {
                                        m = m - 0x0;
                                        var N = _$pm[m];
                                        if (_$pe['NgZjdF'] === undefined) {
                                            var h = function(q) {
                                                var u = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/='
                                                  , Q = String(q)['replace'](/=+$/, '');
                                                var E = '';
                                                for (var P = 0x0, K, A, o = 0x0; A = Q['charAt'](o++); ~A && (K = P % 0x4 ? K * 0x40 + A : A,
                                                P++ % 0x4) ? E += String['fromCharCode'](0xff & K >> (-0x2 * P & 0x6)) : 0x0) {
                                                    A = u['indexOf'](A)
                                                }
                                                return E
                                            };
                                            var w = function(q, u) {
                                                var Q = [], E = 0x0, P, K = '', A = '';
                                                q = h(q);
                                                for (var c = 0x0, H = q['length']; c < H; c++) {
                                                    A += '%' + ('00' + q['charCodeAt'](c)['toString'](0x10))['slice'](-0x2)
                                                }
                                                q = decodeURIComponent(A);
                                                var o;
                                                for (o = 0x0; o < 0x100; o++) {
                                                    Q[o] = o
                                                }
                                                for (o = 0x0; o < 0x100; o++) {
                                                    E = (E + Q[o] + u['charCodeAt'](o % u['length'])) % 0x100,
                                                    P = Q[o],
                                                    Q[o] = Q[E],
                                                    Q[E] = P
                                                }
                                                o = 0x0,
                                                E = 0x0;
                                                for (var W = 0x0; W < q['length']; W++) {
                                                    o = (o + 0x1) % 0x100,
                                                    E = (E + Q[o]) % 0x100,
                                                    P = Q[o],
                                                    Q[o] = Q[E],
                                                    Q[E] = P,
                                                    K += String['fromCharCode'](q['charCodeAt'](W) ^ Q[(Q[o] + Q[E]) % 0x100])
                                                }
                                                return K
                                            };
                                            _$pe['fyWGxy'] = w,
                                            _$pe['WJfnpT'] = {},
                                            _$pe['NgZjdF'] = !![]
                                        }
                                        var f = _$pe['WJfnpT'][m];
                                        if (f === undefined) {
                                            if (_$pe['aGyVwa'] === undefined) {
                                                var q = function(u) {
                                                    this['SyZejG'] = u,
                                                    this['HUOqfE'] = [0x1, 0x0, 0x0],
                                                    this['ZEfZEh'] = function() {
                                                        return 'newState'
                                                    }
                                                    ,
                                                    this['ZkEluo'] = '\w+ *\(\) *{\w+ *',
                                                    this['WzlKmV'] = '['|"].+['|"];? *}'
                                                };
                                                q['prototype']['gBZWsV'] = function() {
                                                    var u = new RegExp(this['ZkEluo'] + this['WzlKmV'])
                                                      , Q = u['test'](this['ZEfZEh']['toString']()) ? --this['HUOqfE'][0x1] : --this['HUOqfE'][0x0];
                                                    return this['lKSDcD'](Q)
                                                }
                                                ,
                                                q['prototype']['lKSDcD'] = function(u) {
                                                    if (!Boolean(~u))
                                                        return u;
                                                    return this['jYVcTR'](this['SyZejG'])
                                                }
                                                ,
                                                q['prototype']['jYVcTR'] = function(u) {
                                                    for (var Q = 0x0, E = this['HUOqfE']['length']; Q < E; Q++) {
                                                        this['HUOqfE']['push'](Math['round'](Math['random']())),
                                                        E = this['HUOqfE']['length']
                                                    }
                                                    return u(this['HUOqfE'][0x0])
                                                }
                                                ,
                                                new q(_$pe)['gBZWsV'](),
                                                _$pe['aGyVwa'] = !![]
                                            }
                                            N = _$pe['fyWGxy'](N, e),
                                            _$pe['WJfnpT'][m] = N
                                        } else
                                            N = f;
                                        return N
                                    };
    
    """
    # g(e) = f(u(unescape(encodeURIComponent(e))))
    js_exc = execjs.compile(js_str)
    js_exc.call("_$pe", '0x6', 'OCbs')


if __name__ == '__main__':
    get_m()

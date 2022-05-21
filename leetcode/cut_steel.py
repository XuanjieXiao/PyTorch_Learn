#!/usr/bin/env python3
# encoding: utf-8
"""
@version: v1.0
@author: XuanjieXiao
@license: BSD Licence 
@contact: xuanjiexiao@163.com
@site: https://blog.csdn.net/weixin_40749043
@software: PyCharm
@file: cut_steel.py
@time: 2022/5/21 下午2:48
"""

p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


def cut_steel_recurision(p, n):
    if n == 0:
        return 0
    else:
        res = p[n]
        for i in range(1, n):
            res = max(res, cut_steel_recurision(p, i) + cut_steel_recurision(p, i - 1))
        return res


def cut_steel_recurision2(p, n):
    if n == 0:
        return 0
    else:
        res = 0
        for i in range(1, n + 1):
            res = max(res, p[i] + cut_steel_recurision2(p, n - i))
        return res


def cut_steel_dp(p,n):
    r = [0]
    for i in range(1,n+1):
        res = 0
        for j in range(1,i+1):
            res = max(res,p[j]+r[i-j])
        r.append(res)
    return r[n]



print(cut_steel_recurision2(p, 8))


def main():
    pass


if __name__ == "__main__":
    main()

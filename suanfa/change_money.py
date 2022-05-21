#!/usr/bin/env python3
# encoding: utf-8
"""
@version: v1.0
@author: XuanjieXiao
@license: BSD Licence 
@contact: xuanjiexiao@163.com
@site: https://blog.csdn.net/weixin_40749043
@software: PyCharm
@file: change_money.py
@time: 2022/5/20 下午7:43
"""
t = [100, 50, 20, 5, 1]


def change(t, n):
    m = [0 for i in range(len(t))]
    for i, money in enumerate(t):
        m[i] = n // money
        n = n % money
    return m, n


print(change(t, 376))


def main():
    pass


if __name__ == "__main__":
    main()

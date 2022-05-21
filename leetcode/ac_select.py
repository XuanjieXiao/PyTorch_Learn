#!/usr/bin/env python3
# encoding: utf-8
"""
@version: v1.0
@author: XuanjieXiao
@license: BSD Licence 
@contact: xuanjiexiao@163.com
@site: https://blog.csdn.net/weixin_40749043
@software: PyCharm
@file: ac_select.py
@time: 2022/5/21 下午12:37
"""
activities = [(1, 4), (3, 5), (0, 6), (5, 7), (5, 9), (3, 9), (6, 10), (8, 11), (8, 12), (12, 16), (2, 14)]
activities.sort(key=lambda x: x[1])


def activities_select(a):
    res = [a[0]]
    for i in range(1,len(a)):
        if a[i][0] >= res[-1][1]:
            res.append(a[i])
    return res

def main():
    pass


if __name__ == "__main__":
    main()

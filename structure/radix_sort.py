#!/usr/bin/env python3
# encoding: utf-8
"""
@version: v1.0
@author: XuanjieXiao
@license: BSD Licence 
@contact: xuanjiexiao@163.com
@site: https://blog.csdn.net/weixin_40749043
@software: PyCharm
@file: radix_sort.py
@time: 2022/5/19 8:36
"""


def radix_sort(li):
    max_num = max(li)
    it = 0
    while 10 ** it <= max_num:
        buckets = [[] for _ in range(10)]
        for val in li:
            digit = (val // 10 ** it) % 10
            buckets[digit].append(val)
        li.clear
        for buc in buckets:
            li.extend(buc)
        it += 1
    return li


if __name__ == "__main__":
    print()

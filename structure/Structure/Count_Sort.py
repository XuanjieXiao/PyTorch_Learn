#!/usr/bin/env python3
# encoding: utf-8
"""
@version: v1.0
@author: XuanjieXiao
@license: BSD Licence 
@contact: xuanjiexiao@163.com
@site: https://blog.csdn.net/weixin_40749043
@software: PyCharm
@file: Count_Sort.py
@time: 2022/5/19 8:02
"""


def count_sort(li, max_count=100):
    count = [0 for _ in range(max_count + 1)]
    for val in li:
        count[val] += 1
    li.clear()
    for ind, val in enumerate(count):
        for i in range(val):
            li.append(ind)


if __name__ == "__main__":
    print()

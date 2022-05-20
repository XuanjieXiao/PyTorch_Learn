#!/usr/bin/env python3
# encoding: utf-8
"""
@version: v1.0
@author: XuanjieXiao
@license: BSD Licence 
@contact: xuanjiexiao@163.com
@site: https://blog.csdn.net/weixin_40749043
@software: PyCharm
@file: Bucket_Sort.py
@time: 2022/5/19 8:16
"""


def Bucket_Sort(li, n=100, max_num=10000):
    buckets = [[] for _ in range(n)]
    for var in li:
        i = min(var // (max_num // n), n - 1)
        buckets[i].append(var)
        for j in range(len(buckets[i] - 1), 0, -1):
            if buckets[i][j] < buckets[i][j - 1]:
                buckets[i][j], buckets[i][j - 1] = buckets[i][j - 1], buckets[i][j]
            else:
                break
    sored_li = []
    for buc in buckets:
        sored_li.extend(buc)
    return sored_li


if __name__ == "__main__":
    print()

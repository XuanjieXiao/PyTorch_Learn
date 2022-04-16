#!/usr/bin/env python3
# encoding: utf-8
"""
@version: v1.0
@author: XuanjieXiao
@license: BSD Licence 
@contact: xuanjiexiao@163.com
@site: https://blog.csdn.net/weixin_40749043
@software: PyCharm
@file: fast_sort.py
@time: 2022/4/16 下午8:18
"""


def partition(li, left, right):
    temp = li[left]
    while left < right:
        while left < right and li[right] >= temp:
            right -= 1
        li[left] = li[right]

        while li[left] <= temp and left < right:
            left += 1
        li[right] = li[left]
    li[left] = temp
    return left


def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)



li = [5, 7, 4, 6, 3, 1, 2, 9, 8,4]
print(li)
quick_sort(li, 0, len(li) - 1)
print(li)

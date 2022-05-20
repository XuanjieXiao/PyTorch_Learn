#!/usr/bin/env python3
# encoding: utf-8
"""
@version: v1.0
@author: XuanjieXiao
@license: BSD Licence 
@contact: xuanjiexiao@163.com
@site: https://blog.csdn.net/weixin_40749043
@software: PyCharm
@file: demo4.py
@time: 2022/4/15 下午7:58
"""

def binary_search(li,val):
    left = 0
    right = len(li)-1
    while left <= right:
        mid = (left +right)//2
        if li[mid] == val:
            return mid
        elif li[mid]>val:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return None


li = [1,2,3,4,5,6,7,8,9]

print(binary_search(li,4))









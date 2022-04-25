#!/usr/bin/env python3
# encoding: utf-8
"""
@version: v1.0
@author: XuanjieXiao
@license: BSD Licence 
@contact: xuanjiexiao@163.com
@site: https://blog.csdn.net/weixin_40749043
@software: PyCharm
@file: demo5.py
@time: 2022/4/15 下午9:19
"""
import random


def Bubble(li):
    li_length = len(li)
    for i in range(li_length-1):
        for j in range(li_length-i-1):
            if li[j]>li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]

lis1 = [random.randint(0,100) for i in range(10)]
print(lis1)
print(Bubble(lis1),lis1)



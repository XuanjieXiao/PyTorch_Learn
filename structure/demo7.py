#!/usr/bin/env python3
# encoding: utf-8
"""
@version: v1.0
@author: XuanjieXiao
@license: BSD Licence 
@contact: xuanjiexiao@163.com
@site: https://blog.csdn.net/weixin_40749043
@software: PyCharm
@file: demo7.py
@time: 2022/4/16 下午7:21
"""

def insert_sort(li):
    for i in range(1,len(li)):
        min_loc = i
        for j in range(i):
            j = min_loc-1
            if li[j]>li[min_loc]:
                li[j],li[min_loc] = li[min_loc],li[j]
                min_loc,j = j,min_loc
        print(li)


li = [3,2,4,1,5,6,7,8,9]
insert_sort(li)

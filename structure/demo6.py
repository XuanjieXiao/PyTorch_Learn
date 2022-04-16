#!/usr/bin/env python3
# encoding: utf-8
"""
@version: v1.0
@author: XuanjieXiao
@license: BSD Licence 
@contact: xuanjiexiao@163.com
@site: https://blog.csdn.net/weixin_40749043
@software: PyCharm
@file: demo6.py
@time: 2022/4/16 下午5:18
"""

def select_sort_simple(li):
    li_new = []
    for i in range(len(li)):
        for val in li:
            min_val = min(li)
            li_new.append(min_val)
            li.remove(min_val)
    return li_new

def select_sort(li):
    for i in range(len(li)-1):
        min_loc = i
        for j in range(i+1,len(li)):
            if li[j]<li[min_loc]:
                min_loc = j
        li[i],li[min_loc] = li[min_loc],li[i]
        print(li)


li = [3,2,4,1,5,6,7,8,9]
#li_new = select_sort_simple(li)

#print(li_new)

select_sort(li)
#!/usr/bin/env python3
# encoding: utf-8
"""
@version: v1.0
@author: XuanjieXiao
@license: BSD Licence 
@contact: xuanjiexiao@163.com
@site: https://blog.csdn.net/weixin_40749043
@software: PyCharm
@file: heapq.py
@time: 2022/4/23 上午11:28
"""

import heapq
import random

li = list(range(100))
random.shuffle(li)

print(li)

heapq.heapify(li) #建立堆
print(li)
n= len(li)
for i in range(n):
    print(heapq.heappop(li), end=',')



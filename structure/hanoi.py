#!/usr/bin/env python3
# encoding: utf-8
"""
@version: v1.0
@author: XuanjieXiao
@license: BSD Licence 
@contact: xuanjiexiao@163.com
@site: https://blog.csdn.net/weixin_40749043
@software: PyCharm
@file: demo2.py
@time: 2022/4/15 下午5:39
"""

def hanoi(n,a,b,c):
    if n>0:
        hanoi(n-1,a,c,b)
        print("moving from %s to %s" % (a,c))
        hanoi(n-1,b,a,c)


hanoi(3,'A','B','C')



if __name__ == "__main__":
    print()

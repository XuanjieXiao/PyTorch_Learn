#!/usr/bin/env python3
# encoding: utf-8
"""
@version: v1.0
@author: XuanjieXiao
@license: BSD Licence 
@contact: xuanjiexiao@163.com
@site: https://blog.csdn.net/weixin_40749043
@software: PyCharm
@file: shell_sort.py
@time: 2022/4/25 上午10:24
"""

def insert_sort_gap(li,gap):
    for i in range(gap,len(li)):
        tmp = li[i]
        j = i -gap
        while j>=0 and li[j]>tmp:
            li[j+gap] = li[j]
            j-=gap
        li[j+gap] = tmp


def main():
    pass


if __name__ == "__main__":
    main()

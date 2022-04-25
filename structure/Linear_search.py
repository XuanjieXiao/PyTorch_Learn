#!/usr/bin/env python3
# encoding: utf-8
"""
@version: v1.0
@author: XuanjieXiao
@license: BSD Licence 
@contact: xuanjiexiao@163.com
@site: https://blog.csdn.net/weixin_40749043
@software: PyCharm
@file: demo3.py
@time: 2022/4/15 下午7:52
"""

def Linear_search(li,val):
    for ind,v in enumerate(li):
        if v == val:
            return ind
        else:
            return None


if __name__ == "__main__":
    print()

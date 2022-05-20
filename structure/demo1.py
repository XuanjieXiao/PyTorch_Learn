#!/usr/bin/env python3
# encoding: utf-8
"""
@version: v1.0
@author: XuanjieXiao
@license: BSD Licence 
@contact: xuanjiexiao@163.com
@site: https://blog.csdn.net/weixin_40749043
@software: PyCharm
@file: demo1.py
@time: 2022/4/15 下午3:45
"""


def fun1(x):
    if x > 0:
        fun1(x - 1)
        print(x)


def main():
    fun1(4)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# encoding: utf-8
"""
@version: v1.0
@author: XuanjieXiao
@license: BSD Licence 
@contact: xuanjiexiao@163.com
@site: https://blog.csdn.net/weixin_40749043
@software: PyCharm
@file: bintree.py
@time: 2022/5/19 16:08
"""
from collections import deque

class bintreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

def pre_order(root):
    pass


a = bintreeNode("A")
b = bintreeNode("B")
c = bintreeNode("C")
d = bintreeNode("D")
e = bintreeNode("E")
f = bintreeNode("F")
g = bintreeNode("G")

e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f






if __name__ == "__main__":
    print()

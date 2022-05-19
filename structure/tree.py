#!/usr/bin/env python3
# encoding: utf-8
"""
@version: v1.0
@author: XuanjieXiao
@license: BSD Licence 
@contact: xuanjiexiao@163.com
@site: https://blog.csdn.net/weixin_40749043
@software: PyCharm
@file: tree.py
@time: 2022/5/19 15:37
"""

class Node:
    def __init__(self,name,type='dir'):
        self.name = name
        self.type = type
        self.children = []
        self.parent = None

    def __str__(self):
        return self.name



class FileSystemTree:
    def __init__(self):
        self.root = Node("/")
        self.now = self.root

    def mkdir(self,name):
        if name[-1] != "/":
            name += "/"
        node = Node(name)
        self.now.children.append(node)
        node.parent = self.now




if __name__ == "__main__":
    print()

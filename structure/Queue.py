#!/usr/bin/env python3
# encoding: utf-8
"""
@version: v1.0
@author: XuanjieXiao
@license: BSD Licence 
@contact: xuanjiexiao@163.com
@site: https://blog.csdn.net/weixin_40749043
@software: PyCharm
@file: Queue.py
@time: 2022/5/19 11:33
"""


class Queue:
    def __init__(self, size=100):
        self.queue = [0 for _ in range(size)]
        self.size = size
        self.rear = 0
        self.front = 0

    def push(self, element):
        if not self.is_filled():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear]=element
        else:
            raise IndexError('Queue is filled')

    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1)%self.size
            return self.queue[self.front]
        else:
            raise IndexError('Queue is empty')

    def is_empty(self):
        return self.rear == self.front

    def is_filled(self):
        return (self.rear+1) % self.size == self.front


if __name__ == "__main__":
    print()

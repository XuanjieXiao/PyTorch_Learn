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
@time: 2022/5/2 下午4:23
"""
import random
price = random.randint(1000,1500)
print('jaige zai 1000 1500')
while True:
    guess = int(input())
    if guess<price:
        print('small')
    elif guess>price:
        print('big')
    else:
        print('bingo')
        break
print('the real price is',price)

def main():
    pass


if __name__ == "__main__":
    main()

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
@time: 2022/5/7 下午7:50
"""
import random

tmp = random.randint(1, 100)
flag = 0
while True:
    x_in = int(input('please input a num and we can guess'))
    if x_in == tmp:
        print('good guess')
        flag += 1
        break
    else:
        flag += 1
        if x_in < tmp:
            print('small,try bigger')
        else:
            print('big,try smaller')

print(f'the total guess is {flag}')
if flag <= 5:
    print('not bad')
else:
    print('oh shit')


def main():
    pass


if __name__ == "__main__":
    main()

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
@time: 2022/5/1 下午7:11
"""

'''第一种方式输出'''
fp = open('mbtxt.txt','w')
print('成就更好的你',file=fp)
fp.close()

'''第2种方式输出'''
with open('mbtxt1.txt','w') as file:
    file.write('chengjiugenghaode')



def main():
    pass


if __name__ == "__main__":
    main()

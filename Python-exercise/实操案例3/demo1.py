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
@time: 2022/5/2 上午10:13
"""
num = int(input('清输入一个十进制的数据'))
print(num,'的二进制数为',bin(num))
print(str(num)+'xxxx'+bin(num))
print('%s的二进制数据为%s' % (num,bin(num)))
print('{0}的二进制数据为{1}'.format(num,bin(num)))
print(f'{num}的二进制数据为{bin(num)}')
print(f'{num}的8进制数据为{oct(num)}')



def main():
    pass


if __name__ == "__main__":
    main()

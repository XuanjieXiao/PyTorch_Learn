#!/usr/bin/env python3
# encoding: utf-8
"""
@version: v1.0
@author: XuanjieXiao
@license: BSD Licence 
@contact: xuanjiexiao@163.com
@site: https://blog.csdn.net/weixin_40749043
@software: PyCharm
@file: max_num.py
@time: 2022/5/21 上午11:18
"""
li = ["32", "94", "1286", "6", "71"]
li.sort(reverse=1)
print(li)

def Max_Num(li):
    s=""
    for i,value in enumerate(li):
        s += value
        print(s)
    return int(s)



a = Max_Num(li)
print(a)


def main():
    pass


if __name__ == "__main__":
    main()

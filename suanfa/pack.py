#!/usr/bin/env python3
# encoding: utf-8
"""
@version: v1.0
@author: XuanjieXiao
@license: BSD Licence 
@contact: xuanjiexiao@163.com
@site: https://blog.csdn.net/weixin_40749043
@software: PyCharm
@file: pack.py
@time: 2022/5/20 下午7:53
"""
goods= [(60,10),(100,20),(120,30)]


def pack(goods,w):
    goods.sort(key=lambda x: x[0]/x[1] ,reverse=True)
    print(goods)
    m = [0 for i in range(len(goods))]
    total = 0
    for i ,(price,weights) in enumerate(goods):
        if w>=weights:
            m[i]=1
            w -= weights
            total +=price
        else:
            m[i]= w/weights
            w = 0
            total += m[i]*price
            break
    return m

print(pack(goods,50))


def main():
    pass


if __name__ == "__main__":
    main()

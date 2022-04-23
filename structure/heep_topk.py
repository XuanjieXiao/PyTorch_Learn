#!/usr/bin/env python3
# encoding: utf-8
"""
@version: v1.0
@author: XuanjieXiao
@license: BSD Licence 
@contact: xuanjiexiao@163.com
@site: https://blog.csdn.net/weixin_40749043
@software: PyCharm
@file: heep_topk.py
@time: 2022/4/23 下午4:59
"""


def sift(li, low, high):
    """

    :param li: 列表
    :param low: 堆的根节点位置
    :param high: 堆的最后一个元素的位置
    :return:
    """
    i = low  # i 最开始指向根节点
    j = 2 * i + 1  # j开始是左孩子
    tmp = li[low]  # 把堆顶存起来
    while j <= high:  # 只要j位置有数据
        if j + 1 <= high and li[j + 1] < li[j]:  # 如果右边孩子存在且比左边的大
            j = j + 1  # j指向右孩子
        if li[j] < tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:             #tmp 更大,把tmp放到i的位置上
            li[i] = tmp  #把tmp放到某一及领导的位置
            break
    else:
        li[i] = tmp  #把tmp放到叶子节点上


def heep_sort(li):
    n = len(li)
    for i in range((n-2)//2, -1,-1):

        # i代表建立堆的时候调整的部分的根的下标
        sift(li, i, n-1)
    #建立堆完成
    #print(li)
    for i in range(n-1,-1,-1):
        # i 指向当前堆的最后一个元素
        li[0],li[i] = li[i],li[0]
        sift(li,0,i-1) #i-1 是新的high


def topk(li,k):
    heap = li[0:k]
    for i in range((k-2)//2,-1,-1):
        sift(heap,i,k-1)
    for i in range(k,len(li)-1):


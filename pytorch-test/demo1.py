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
@time: 2022/3/31 下午2:52
"""
import torch

a = torch.rand(4,3,28,28)
print(a[0].shape)

x = torch.randn(3,4)
mask = x.ge(0.5)
y = torch.masked_select(x,mask)
print(x)
print(mask)
print(y)


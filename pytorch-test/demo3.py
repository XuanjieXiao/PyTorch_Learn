#!/usr/bin/env python3
# encoding: utf-8
"""
@version: v1.0
@author: XuanjieXiao
@license: BSD Licence 
@contact: xuanjiexiao@163.com
@site: https://blog.csdn.net/weixin_40749043
@software: PyCharm
@file: demo3.py
@time: 2022/4/1
"""
import torch
import torch.nn.functional as F
a = torch.linspace(-100, 100, 10)
print(a)
b = torch.sigmoid(a)
print(b)



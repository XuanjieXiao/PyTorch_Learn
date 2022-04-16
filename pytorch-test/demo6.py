#!/usr/bin/env python3
# encoding: utf-8
"""
@version: v1.0
@author: XuanjieXiao
@license: BSD Licence 
@contact: xuanjiexiao@163.com
@site: https://blog.csdn.net/weixin_40749043
@software: PyCharm
@file: demo6.py
@time: 2022/4/7 下午11:17
"""
import torch
import torch.nn.functional as F
w1, b1 = torch.randn(200, 784,requires_grad=True),torch.zeros(200,requires_grad=True)
w2, b2 = torch.randn(200, 200,requires_grad=True),torch.zeros(200,requires_grad=True)
w3, b3 = torch.randn(10, 200,requires_grad=True),torch.zeros(10,requires_grad=True)

def forward(x):
    x = x@w1.t() + b1
    x = F.relu(x)
    x = x@w2.t() + b2
    x = F.relu(x)
    x = x @ w3.t() + b3
    x = F.relu(x)
    return x





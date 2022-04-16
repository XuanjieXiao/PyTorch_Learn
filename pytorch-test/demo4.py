#!/usr/bin/env python3
# encoding: utf-8
"""
@version: v1.0
@author: XuanjieXiao
@license: BSD Licence 
@contact: xuanjiexiao@163.com
@site: https://blog.csdn.net/weixin_40749043
@software: PyCharm
@file: demo4.py
@time: 2022/4/5 下午7:03
"""
import torch

a = torch.rand(3)
a.requires_grad_()
print(a)
p = torch.softmax(a,dim=0)
p.backward()
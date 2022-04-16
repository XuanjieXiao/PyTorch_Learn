#!/usr/bin/env python3
# encoding: utf-8
"""
@version: v1.0
@author: XuanjieXiao
@license: BSD Licence 
@contact: xuanjiexiao@163.com
@site: https://blog.csdn.net/weixin_40749043
@software: PyCharm
@file: demo5.py
@time: 2022/4/5 下午7:25
"""
import torch

x = torch.randn(1,10)
w = torch.randn(1,10,requires_grad=True)




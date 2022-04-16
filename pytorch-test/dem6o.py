#!/usr/bin/env python3
# encoding: utf-8
"""
@version: v1.0
@author: XuanjieXiao
@license: BSD Licence 
@contact: xuanjiexiao@163.com
@site: https://blog.csdn.net/weixin_40749043
@software: PyCharm
@file: dem6o.py
@time: 2022/4/7 下午1:24
"""
import torch
import torch.nn.functional as F
x = torch.randn(1, 784)
w = torch.randn(10,784)
logits = x@w.t()
pred = torch.softmax(logits, dim=1)
pred_log = torch.log(pred)
torch.binary_cross_entropy_with_logits(logits,torch.tensor([3]))
torch.poisson_nll_loss(pred_log, torch.tensor([3]))


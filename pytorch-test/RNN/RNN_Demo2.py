#!/usr/bin/env python3
# encoding: utf-8
"""
@version: v1.0
@author: XuanjieXiao
@license: BSD Licence 
@contact: xuanjiexiao@163.com
@site: https://blog.csdn.net/weixin_40749043
@software: PyCharm
@file: RNN_Demo2.py
@time: 2022/5/10 下午3:45
"""
import torch.nn as nn
import torch

rnn = nn.RNN(input_size=100, hidden_size=20, num_layers=4)
x = torch.randn(10, 3, 100)
out, h = rnn(x)


def main():
    pass


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# encoding: utf-8
"""
@version: v1.0
@author: XuanjieXiao
@license: BSD Licence 
@contact: xuanjiexiao@163.com
@site: https://blog.csdn.net/weixin_40749043
@software: PyCharm
@file: rnn.py
@time: 2022/5/8 下午2:59
"""
import torch
import torch.nn as nn
rnn = nn.RNN(5,6,1)
input = torch.randn(1,3,5)
h0 = torch.randn(1,3,6)
output, hn = rnn(input,h0)
print(output)
print(output.shape)

def main():
    pass


if __name__ == "__main__":
    main()

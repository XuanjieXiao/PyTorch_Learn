#!/usr/bin/env python3
# encoding: utf-8
"""
@version: v1.0
@author: XuanjieXiao
@license: BSD Licence 
@contact: xuanjiexiao@163.com
@site: https://blog.csdn.net/weixin_40749043
@software: PyCharm
@file: RNN_Demo1.py
@time: 2022/5/9 下午8:57
"""
import torch.nn as nn
import torch

rnn = nn.RNN(input_size=100,hidden_size=20,num_layers=1)
print(rnn)
x=torch.randn(10,3,100)
out , h =rnn(x,torch.zeros(1,3,20))
print(out.shape,h.shape)



def main():
    pass


if __name__ == "__main__":
    main()

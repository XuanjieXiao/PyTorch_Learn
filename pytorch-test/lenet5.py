#!/usr/bin/env python3
# encoding: utf-8
"""
@version: v1.0
@author: XuanjieXiao
@license: BSD Licence 
@contact: xuanjiexiao@163.com
@site: https://blog.csdn.net/weixin_40749043
@software: PyCharm
@file: lenet5.py
@time: 2022/4/12 上午10:31
"""
import torch
from torch import nn
from torch.nn import functional as F


class Lenet5(nn.Module):
    def __init__(self):
        super(Lenet5, self).__init__()
        self.conv_unit = nn.Sequential(
            # x:[b,3,32,32]>>>[b,6,]
            nn.Conv2d(3, 6, kernel_size=5, stride=1, padding=0),
            # kernel_size juanjihedaxiao padding bucong0
            nn.AvgPool2d(kernel_size=2, stride=2, padding=0),
            #
            nn.Conv2d(6, 16, kernel_size=5, stride=1, padding=0),
            nn.AvgPool2d(kernel_size=2, stride=2, padding=0)
            #
        )
        # flatten
        # fc unit
        self.fc_unit = nn.Sequential(
            nn.Linear(16 * 5 * 5, 120),
            nn.ReLU(),
            nn.Linear(120, 84),
            nn.ReLU(),
            nn.Linear(84, 10)
        )


        # use cel
        # self.criteon = nn.MSELoss()
        self.criteon = nn.CrossEntropyLoss()

    def forward(self, x):
        """

        :param x: [b,3,32,32]
        :return:
        """
        batchsz = x.size(0)
        # [b,3,32,32]>>>>>>>>[b,16,5,5]
        x = self.conv_unit(x)
        # [b,16,5,5]>>>>>>>>>>>>>[b,16*5*5]
        x = x.view(batchsz, 16 * 5 * 5)
        # [b,16*5*5]>>>>>>>>>>[b,10]
        logits = self.fc_unit(x)
        # [b,10]
        # pred = F.softmax(logits, dim=1)
        # loss = self.criteon(logits,y)
        return logits


def main():
    net = Lenet5()
    # 【b,,3,32,32]
    temp = torch.randn(2, 3, 32, 32)
    out = net(temp)
    # [b,16,5,5]
    print('Lenet5,out', out.shape)


if __name__ == '__main__':
    main()

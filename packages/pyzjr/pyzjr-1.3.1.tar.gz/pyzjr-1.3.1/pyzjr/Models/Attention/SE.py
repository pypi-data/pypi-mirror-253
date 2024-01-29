"""
Original paper addresshttps: https://arxiv.org/pdf/1709.01507.pdf
Code originates from https://github.com/moskomule/senet.pytorch/blob/master/senet/se_module.py
Blog records: https://blog.csdn.net/m0_62919535/article/details/135761713
Time: 2024-01-23
"""
import torch
from torch import nn

class SELayer(nn.Module):
    def __init__(self, channel, reduction=16):
        super().__init__()
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.fc = nn.Sequential(
            nn.Linear(channel, channel // reduction, bias=False),
            nn.ReLU(inplace=True),
            nn.Linear(channel // reduction, channel, bias=False),
            nn.Sigmoid()
        )

    def forward(self, x):
        b, c, _, _ = x.size()
        y = self.avg_pool(x).view(b, c)
        y = self.fc(y).view(b, c, 1, 1)
        return x * y.expand_as(x)


if __name__ == '__main__':
    input = torch.randn(1, 64, 64, 64)
    se = SELayer(channel=64, reduction=8)
    output = se(input)
    print(output.shape)

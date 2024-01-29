"""
Time: 2024-01-28 0:59
"""
import torch.nn as nn


def conv3x3(in_channels, out_channels, stride=1, groups=1, dilation=1):
    """3x3 convolution with padding:捕捉局部特征和空间相关性，学习更复杂的特征和抽象表示"""
    return nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=stride,
                     padding=dilation, groups=groups, bias=False, dilation=dilation)

def conv1x1(in_channels, out_channels, stride=1):
    """1x1 convolution:实现降维或升维，调整通道数和执行通道间的线性变换"""
    return nn.Conv2d(in_channels, out_channels, kernel_size=1, stride=stride, bias=False)

class ConvBNReLU(nn.Module):
    def __init__(self, in_channels, out_channels, stride=1,  kernel_size=3, padding=1,
                 bias=False, dilation=1, groups=1):
        super(ConvBNReLU, self).__init__()
        self.conv = nn.Conv2d(in_channels=in_channels, out_channels=out_channels,
                              kernel_size=kernel_size, stride=stride, padding=padding,
                              bias=bias, dilation=dilation, groups=groups)
        self.bn = nn.BatchNorm2d(num_features=out_channels)
        self.relu = nn.ReLU(inplace=True)

    def forward(self, x):
        x = self.conv(x)
        x = self.bn(x)
        x = self.relu(x)
        return x

class ConvBN(nn.Module):
    def __init__(self, in_channels, out_channels, stride=1,  kernel_size=3, padding=1,
                 bias=False, dilation=1, groups=1):
        super(ConvBN, self).__init__()
        self.conv = nn.Conv2d(in_channels=in_channels, out_channels=out_channels,
                              kernel_size=kernel_size, stride=stride, padding=padding,
                              bias=bias, dilation=dilation, groups=groups)
        self.bn = nn.BatchNorm2d(num_features=out_channels)

    def forward(self, x):
        x = self.conv(x)
        x = self.bn(x)
        return x

class BasicBlock(nn.Module):
    """ResNet的基础块,适用于较浅的网络或较小的数据集"""
    expansion = 1
    def __init__(self, in_channels, out_channels, stride=1, downsample=False):
        super(BasicBlock, self).__init__()
        self.convbnrelu1 = ConvBNReLU(in_channels, out_channels, kernel_size=3, stride=stride)
        self.convbn1 = ConvBN(out_channels, out_channels, kernel_size=3)
        self.relu = nn.ReLU(inplace=True)
        self.downsample = downsample
        self.stride = stride
        self.conv_down = nn.Sequential(
            conv1x1(in_channels, out_channels * self.expansion, self.stride),
            nn.BatchNorm2d(out_channels * self.expansion),
        )

    def forward(self, x):
        residual = x
        out = self.convbnrelu1(x)
        out = self.convbn1(out)

        if self.downsample:
            residual = self.conv_down(x)

        out += residual
        out = self.relu(out)

        return out

class Bottleneck(nn.Module):
    """ResNet的瓶颈结构,适用于深层网络，通过较少的参数来构建更深的网络，提高性能"""
    expansion = 4
    def __init__(self, in_channels, out_channels, stride=1, downsample=False):
        super(Bottleneck, self).__init__()
        groups = 1
        base_width = 64
        dilation = 1

        width = int(out_channels * (base_width / 64.)) * groups   # wide = out_channels
        # self.convbnrelu1 = ConvBNReLU(in_channels, width, kernel_size=1, padding=0)  # 降维通道数
        # self.convbnrelu2 = ConvBNReLU(width, width, kernel_size=3, stride=stride, dilation=dilation, groups=groups)
        # self.convbn3 = ConvBN(width, out_channels * self.expansion, kernel_size=1, padding=0)   # 升维通道数
        self.conv1 = conv1x1(in_channels, width)       # 降维通道数
        self.bn1 = nn.BatchNorm2d(width)
        self.conv2 = conv3x3(width, width, stride, groups, dilation)
        self.bn2 = nn.BatchNorm2d(width)
        self.conv3 = conv1x1(width, out_channels * self.expansion)   # 升维通道数
        self.bn3 = nn.BatchNorm2d(out_channels * self.expansion)
        self.relu = nn.ReLU(inplace=True)
        self.downsample = downsample
        self.stride = stride
        self.conv_down = nn.Sequential(
            conv1x1(in_channels, out_channels * self.expansion, self.stride),
            nn.BatchNorm2d(out_channels * self.expansion),
        )

    def forward(self, x):
        residual = x

        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)

        out = self.conv2(out)
        out = self.bn2(out)
        out = self.relu(out)

        out = self.conv3(out)
        out = self.bn3(out)

        if self.downsample:
            residual = self.conv_down(x)

        out += residual
        out = self.relu(out)

        return out
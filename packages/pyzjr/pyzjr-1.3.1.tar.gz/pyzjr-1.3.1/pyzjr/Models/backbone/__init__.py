"""
Copyright (c) 2023, Auorui.
All rights reserved.

The following citation imports roughly follow the sorting by year
"""
# 1990s
from .lenet import LeNet

# 2010s
from .alexnet import AlexNet
from .vgg import vgg16_bn, vgg19_bn
from .googlenet import GoogLeNet
from .resnet import resnet18, resnet34, resnet50, resnet101, resnet152
from .se_resnet import se_resnet18, se_resnet34, se_resnet50, se_resnet101, se_resnet152
from .darknet import *

# 2020s
from .conv2former import Conv2Former_n, Conv2Former_t, Conv2Former_s, Conv2Former_l, Conv2Former_b
from .Ghostnet import *

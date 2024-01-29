"""
Copyright (c) 2024, Auorui.
All rights reserved.

Activation function pytorch handwriting implementation

Time: 2024-01-02

After a day of hard work, I successfully implemented activation functions in PyTorch, some of which were in place operations.
During this process, I spent a lot of time researching materials and formulas to ensure that my implementation was the same as
the official one. I have not made any additional modifications to the parts that have already implemented official functions,
but there may still be room for improvement in terms of details.

At the end, there is a draft record of my experiment that you can test.
"""
import math
import os
import numpy as np

import torch
import torch.nn as nn
import torch.nn.functional as F
import matplotlib.pyplot as plt

__all__ = ['Hardsigmoid', 'Hardtanh', 'Hardswish', 'Hardshrink', 'Threshold',  'Sigmoid', 'Tanh',
           'Softshrink', 'Softplus', 'Softmin', 'LogSoftmax', 'Softsign', 'Softmax',
           'ReLU', 'RReLU', 'ReLU6', 'LeakyReLU', "FReLU", 'PReLU', 'Mish',  'ELU', 'CELU', 'SELU', 'GLU', 'GELU',
           'SiLU', 'Swish', 'LogSigmoid', 'Tanhshrink', "AconC", "MetaAconC",
           "plot_activation_function"    # matplotlib 绘制以上激活函数图像, 小部分无法绘制
           ]

class PyZjrActivation(nn.Module):
    def __init__(self):
        super().__init__()

class Sigmoid(PyZjrActivation):
    def __init__(self, inplace=False):
        super().__init__()
        self.inplace = inplace

    def _sigmoid(self, x):
        return 1 / (1 + torch.exp(-x))

    def forward(self, x):
        return x.sigmoid_() if self.inplace else self._sigmoid(x)

class Tanh(PyZjrActivation):
    def __init__(self, inplace = False):
        super().__init__()
        self.inplace = inplace

    def _tanh(self, x):
        return (2 / (1 + torch.exp(-2 * x))) - 1

    def forward(self, x):
        return x.tanh_() if self.inplace else x.tanh()

class ReLU(PyZjrActivation):
    def __init__(self, inplace=False):
        super().__init__()
        self.inplace = inplace

    def _relu(self, x):
        return torch.max(torch.tensor(0.0), x)

    def forward(self, x):
        return x.relu_() if self.inplace else self._relu(x)

class ReLU6(nn.Module):
    def __init__(self, inplace=False):
        super(ReLU6, self).__init__()
        self.inplace = inplace

    def _relu6(self, x):
        return torch.clamp(x, min=0.0, max=6.0)

    def forward(self, x):
        if self.inplace:
            x.clamp_(min=0.0, max=6.0)
            return x
        else:
            return self._relu6(x)

class FReLU(PyZjrActivation):
    def __init__(self, dim, kernel=3, init_weight=False):
        super().__init__()
        self.conv = nn.Conv2d(dim, dim, kernel, 1, 1, groups=dim, bias=False)
        self.bn = nn.BatchNorm2d(dim)
        if init_weight:
            self.apply(self._init_weight)

    def _init_weight(self, m):
        init = nn.init.normal(mean=0, std=.02)
        zeros = nn.init.constant(0.)
        ones = nn.init.constant(1.)
        if isinstance(m, nn.Conv2d):
            init(m.weight)
            zeros(m.bias)
        if isinstance(m, nn.BatchNorm2d):
            ones(m.weight)
            zeros(m.bias)

    def forward(self, x):
        return torch.max(x, self.bn(self.conv(x)))

class LeakyReLU(PyZjrActivation):
    def __init__(self, negative_slope=0.01, inplace=False):
        super(LeakyReLU, self).__init__()
        self.negative_slope = negative_slope
        self.inplace = inplace

    def _leakyrelu(self, x):
        if self.inplace:
            return x.mul_(torch.where(x > 0, torch.tensor(1.0), torch.tensor(self.negative_slope)))
        else:
            return torch.where(x > 0, x, x * self.negative_slope)

    def forward(self, x):
        return self._leakyrelu(x)


class RReLU(PyZjrActivation):
    def __init__(self, lower=1.0 / 8, upper=1.0 / 3, inplace=False):
        super(RReLU, self).__init__()
        self.lower = lower
        self.upper = upper
        self.inplace = inplace

    def _rrelu(self, x):
        noise = torch.empty_like(x).uniform_(self.lower, self.upper)
        if self.inplace:
            return x.mul_(torch.where(x < 0, noise, torch.tensor(1.0)))
        else:
            return torch.where(x < 0, x * noise, x)

    def forward(self, x):
        return self._rrelu(x)

class PReLU(PyZjrActivation):
    def __init__(self, num_parameters=1, init=0.25):
        super(PReLU, self).__init__()
        self.num_parameters = num_parameters
        self.weight = nn.Parameter(torch.full((num_parameters,), init))

    def _prelu(self, x):
        return torch.where(x >= 0, x, self.weight * x)

    def forward(self, x):
        return self._prelu(x)

class Threshold(PyZjrActivation):
    def __init__(self, threshold=0.5, value=0.0, inplace=False):
        super(Threshold, self).__init__()
        self.threshold = threshold
        self.value = value
        self.inplace = inplace

    def _threshold(self, x):
        if self.inplace:
            return x.threshold_(self.threshold, self.value)
        else:
            return F.threshold(x, self.threshold, self.value, self.inplace)

    def forward(self, x):
        return self._threshold(x)

class Softsign(PyZjrActivation):
    def __init__(self, inplace=False):
        super().__init__()
        self.inplace = inplace

    def _soft_sign(self, x):
        if self.inplace:
            return x.div_(1 + torch.abs(x))
        else:
            return x / (1 + torch.abs(x))

    def forward(self, x):
        return self._soft_sign(x)

class Tanhshrink(Tanh):
    def __init__(self, inplace=False):
        super().__init__(inplace=inplace)
        self.inplace = inplace

    def _tanh_shrink(self, x):
        return x.sub_(self._tanh(x)) if self.inplace else x - self._tanh(x)

    def forward(self, x):
        return self._tanh_shrink(x)

class Softmin(PyZjrActivation):
    def __init__(self, dim=-1, inplace=False):
        super().__init__()
        self.inplace = inplace
        self.dim = dim

    def _softmin(self, x):
        exp_x = torch.exp(-x)
        softmax = exp_x / torch.sum(exp_x, dim=self.dim, keepdim=True)
        if self.inplace:
            x.copy_(softmax)
            return x
        else:
            return softmax

    def forward(self, x):
        return self._softmin(x)

class Softmax(PyZjrActivation):
    def __init__(self, dim=-1, inplace=False):
        super().__init__()
        self.inplace = inplace
        self.dim = dim

    def _softmax(self, x):
        exp_x = torch.exp(x)
        softmax = exp_x / torch.sum(exp_x, dim=self.dim, keepdim=True)
        if self.inplace:
            x.copy_(softmax)
            return x
        else:
            return softmax

    def forward(self, x):
        return self._softmax(x)

class Mish(PyZjrActivation):
    def __init__(self, inplace=False):
        super().__init__()
        self.inplace = inplace

    def _mish(self, x):
        if self.inplace:
            return x.mul_(torch.tanh(F.softplus(x)))
        else:
            return x * torch.tanh(F.softplus(x))

    def forward(self, x):
        return self._mish(x)

# Swish, also known as SiLU.
class SiLU(PyZjrActivation):
    def __init__(self, inplace=False):
        super(SiLU, self).__init__()
        self.inplace = inplace

    def _silu(self, x):
        return x.mul_(torch.sigmoid(x)) if self.inplace else x * torch.sigmoid(x)

    def forward(self, x):
        return self._silu(x)

class Swish(SiLU):
    def __init__(self, inplace=False):
        super(Swish, self).__init__(inplace=inplace)

    def forward(self, x):
        return self._silu(x)

class Hardswish(PyZjrActivation):
    def __init__(self, inplace=False):
        super(Hardswish, self).__init__()
        self.inplace = inplace

    def _hardswish(self, x):
        inner = F.relu6(x + 3.).div_(6.)
        return x.mul_(inner) if self.inplace else x.mul(inner)

    def forward(self, x):
        return self._hardswish(x)

class ELU(PyZjrActivation):
    def __init__(self, alpha=1.0, inplace=False):
        super(ELU, self).__init__()
        self.alpha = alpha
        self.inplace = inplace

    def _elu(self, x):
        if self.inplace:
            x[x < 0] = self.alpha * (torch.exp(x[x < 0]) - 1)
            return x
        else:
            return torch.where(x < 0, self.alpha * (torch.exp(x) - 1), x)

    def forward(self, x):
        return self._elu(x)

class CELU(PyZjrActivation):
    def __init__(self, alpha=1.0, inplace=False):
        super(CELU, self).__init__()
        self.alpha = alpha
        self.inplace = inplace

    def _celu(self, x, alpha):
        if self.inplace:
            x[x < 0] = alpha * (torch.exp(x[x < 0] / alpha) - 1)
            return x
        else:
            return torch.where(x < 0, alpha * (torch.exp(x / alpha) - 1), x)

    def forward(self, x):
        return self._celu(x, self.alpha)


class SELU(PyZjrActivation):
    def __init__(self):
        super(SELU, self).__init__()
        self.scale = 1.0507009873554804934193349852946
        self.alpha = 1.6732632423543772848170429916717

    def _selu(self, x):
        return self.scale * torch.where(x > 0, x, self.alpha * (torch.exp(x) - 1))

    def forward(self, x):
        return self._selu(x)

class GLU(PyZjrActivation):
    def __init__(self, dim=-1):
        super(GLU, self).__init__()
        self.dim = dim

    def _glu(self, x):
        mid = x.size(self.dim) // 2
        return x.narrow(self.dim, 0, mid) * torch.sigmoid(x.narrow(self.dim, mid, mid))

    def forward(self, x):
        return self._glu(x)

class GELU(PyZjrActivation):
    def __init__(self, inplace=False):
        super(GELU, self).__init__()
        self.inplace = inplace

    def _gelu(self, x):
        if self.inplace:
            return x.mul_(0.5 * (1.0 + torch.erf(x / math.sqrt(2.0))))
        else:
            return 0.5 * x * (1.0 + torch.erf(x / math.sqrt(2.0)))

    def forward(self, x):
        return self._gelu(x)

class Hardshrink(PyZjrActivation):
    def __init__(self, lambd=0.5):
        super(Hardshrink, self).__init__()
        self.lambd = lambd

    def _hardshrink(self, x):
        return torch.where(x < -self.lambd, x, torch.where(x > self.lambd, x, torch.tensor(0.0)))


    def forward(self, x):
        return self._hardshrink(x)


class Hardsigmoid(PyZjrActivation):
    def __init__(self, inplace=False):
        super(Hardsigmoid, self).__init__()
        self.inplace = inplace

    def _hardsigmoid(self, x):
        return F.relu6(x + 3.0, inplace=self.inplace) / 6.0

    def forward(self, x):
        return self._hardsigmoid(x)


class Hardtanh(PyZjrActivation):
    def __init__(self, inplace=False):
        super(Hardtanh, self).__init__()
        self.inplace = inplace

    def _hardtanh(self, x):
        return x.clamp_(-1.0, 1.0) if self.inplace else torch.clamp(x, min=-1.0, max=1.0)

    def forward(self, x):
        return self._hardtanh(x)

class LogSoftmax(PyZjrActivation):
    def __init__(self, dim=-1, inplace=False):
        super(LogSoftmax, self).__init__()
        self.inplace = inplace
        self.dim = dim

    def _logsoftmax(self, x):
        max_vals, _ = torch.max(x, dim=self.dim, keepdim=True)
        x_exp = torch.exp(x - max_vals)
        x_softmax = x_exp / torch.sum(x_exp, dim=self.dim, keepdim=True)
        if self.inplace:
            x.copy_(torch.log(x_softmax))
            return x
        else:
            return torch.log(x_softmax)

    def forward(self, x):
        return self._logsoftmax(x)

class LogSigmoid(PyZjrActivation):
    def __init__(self, inplace=False):
        super(LogSigmoid, self).__init__()
        self.inplace = inplace

    def _logsigmoid(self, x):
        if self.inplace:
            return x.sigmoid_().log_()
        else:
            return torch.log(torch.sigmoid(x))

    def forward(self, x):
        return self._logsigmoid(x)

class Softplus(PyZjrActivation):
    def __init__(self, beta = 1, threshold = 20, inplace=False):
        super(Softplus, self).__init__()
        self.beta = beta
        self.threshold = threshold
        self.inplace = inplace

    def _softplus(self, x):
        if self.inplace:
            return x.add_(1 / self.beta).log_()
        else:
            return torch.where(x > self.threshold, x, 1 / self.beta * torch.log(1 + torch.exp(self.beta * x)))

    def forward(self, x):
        return self._softplus(x)

class Softshrink(PyZjrActivation):
    def __init__(self, lambd=0.5):
        super(Softshrink, self).__init__()
        self.lambd = lambd

    def _softshrink(self, x):
        return torch.where(x < -self.lambd, x + self.lambd, torch.where(x > self.lambd, x - self.lambd, torch.tensor(0., device=x.device, dtype=x.dtype)))

    def forward(self, x):
        return self._softshrink(x)


# AconC与MetaAconC是从YOLOv5中复制过来的，暂时没有研究
class AconC(nn.Module):
    r""" ACON activation (activate or not)
    AconC: (p1*x-p2*x) * sigmoid(beta*(p1*x-p2*x)) + p2*x, beta is a learnable parameter
    according to "Activate or Not: Learning Customized Activation" <https://arxiv.org/pdf/2009.04759.pdf>.
    """
    def __init__(self, c1):
        super().__init__()
        self.p1 = nn.Parameter(torch.randn(1, c1, 1, 1))
        self.p2 = nn.Parameter(torch.randn(1, c1, 1, 1))
        self.beta = nn.Parameter(torch.ones(1, c1, 1, 1))

    def forward(self, x):
        dpx = (self.p1 - self.p2) * x
        return dpx * torch.sigmoid(self.beta * dpx) + self.p2 * x


class MetaAconC(nn.Module):
    r""" ACON activation (activate or not)
    MetaAconC: (p1*x-p2*x) * sigmoid(beta*(p1*x-p2*x)) + p2*x, beta is generated by a small network
    according to "Activate or Not: Learning Customized Activation" <https://arxiv.org/pdf/2009.04759.pdf>.
    """
    def __init__(self, c1, k=1, s=1, r=16):  # ch_in, kernel, stride, r
        super().__init__()
        c2 = max(r, c1 // r)
        self.p1 = nn.Parameter(torch.randn(1, c1, 1, 1))
        self.p2 = nn.Parameter(torch.randn(1, c1, 1, 1))
        self.fc1 = nn.Conv2d(c1, c2, k, s, bias=True)
        self.fc2 = nn.Conv2d(c2, c1, k, s, bias=True)
        # self.bn1 = nn.BatchNorm2d(c2)
        # self.bn2 = nn.BatchNorm2d(c1)

    def forward(self, x):
        y = x.mean(dim=2, keepdims=True).mean(dim=3, keepdims=True)
        # batch-size 1 bug/instabilities https://github.com/ultralytics/yolov5/issues/2891
        # beta = torch.sigmoid(self.bn2(self.fc2(self.bn1(self.fc1(y)))))  # bug/unstable
        beta = torch.sigmoid(self.fc2(self.fc1(y)))  # bug patch BN layers removed
        dpx = (self.p1 - self.p2) * x
        return dpx * torch.sigmoid(beta * dpx) + self.p2 * x

def plot_activation_function(activation_class, input_range=(-20, 20), num_points=10000, save_dir=None, format="png"):
    """
    经过测试，FReLU与GLU,以及AconC与MetaAconC无法绘制
    """
    x_values = np.linspace(input_range[0], input_range[1], num_points)
    activation_func = activation_class()

    with torch.no_grad():
        y_values = activation_func(torch.tensor(x_values)).numpy()

    # Handle extreme values for better visualization
    y_values[np.isinf(y_values)] = np.nan
    y_values[np.isnan(y_values)] = np.max(np.abs(y_values[~np.isnan(y_values)]))

    plt.plot(x_values, y_values, label=activation_class.__name__)
    title = f"{activation_class.__name__} Activation Function"
    plt.title(title)
    plt.xlabel('Input')
    plt.ylabel('Output')
    plt.legend()
    plt.grid(True)

    if save_dir:
        os.makedirs(save_dir, exist_ok=True)
        plt.savefig(os.path.join(save_dir, activation_class.__name__) + f".{format}")
        print(f"Plot saved at: {save_dir}")
    plt.show()

if __name__=="__main__":
    # x = torch.tensor([[ 0.6328, -0.2803,  0.2340,  0.1001,  0.1168]])
    # x = torch.cat([x, x], dim=-1)  # 将最后一个维度复制一份，使其大小变为 10
    x = torch.tensor([[[[0.6328], [-0.2803], [0.2340], [0.1001], [0.1168]],
                       [[0.4321], [-0.1234], [0.5678], [0.9876], [0.5432]]]])   # FReLU示例

    activation = FReLU(dim=2)

    x = activation(x)
    print("activation:", x)

    # Example usage:
    test = [Sigmoid, Tanh, ReLU, LeakyReLU, Swish, Mish, PReLU, Softmax, RReLU, ReLU6,  ELU, CELU, SELU,
            GELU ,Hardsigmoid, Hardtanh, Hardswish, Hardshrink, Threshold, Softshrink, Softplus, Softmin, LogSoftmax, Softsign
           ,SiLU, Swish, LogSigmoid, Tanhshrink]

    for i in test:
        plot_activation_function(i)


    """
    x = torch.tensor([[ 0.6328, -0.2803,  0.2340,  0.1001,  0.1168]])
    原始数据均用的x, 内部手写实现与torch官方实现进行了比较
    
    Sigmoid activation: tensor([[0.6531, 0.4304, 0.5582, 0.5250, 0.5292]])
    Tanh activation: tensor([[ 0.5600, -0.2732,  0.2298,  0.0998,  0.1163]])
    ReLU activation: tensor([[0.6328, 0.0000, 0.2340, 0.1001, 0.1168]])
    hardsigmoid activation: tensor([[0.6055, 0.4533, 0.5390, 0.5167, 0.5195]])
    ReLU6 activation: tensor([[0.6328, 0.0000, 0.2340, 0.1001, 0.1168]])
    hardtanh activation: tensor([[ 0.6328, -0.2803,  0.2340,  0.1001,  0.1168]])
    Swish/SiLU activation: tensor([[ 0.4133, -0.1206,  0.1306,  0.0526,  0.0618]])
    Hardswish activation: tensor([[ 0.3831, -0.1271,  0.1261,  0.0517,  0.0607]])
    ELU activation: tensor([[ 0.6328, -0.2444,  0.2340,  0.1001,  0.1168]])
    CELU activation: tensor([[ 0.6328, -0.2444,  0.2340,  0.1001,  0.1168]])
    SELU ctivation: tensor([[ 0.6649, -0.4298,  0.2459,  0.1052,  0.1227]])
    
    GLU activation: tensor([[ 0.4133, -0.1206,  0.1306,  0.0526,  0.0618]])      x = torch.cat([x, x], dim=-1) 维度要为偶数
    GELU activation: tensor([[ 0.4661, -0.1092,  0.1386,  0.0540,  0.0638]])
    Hardshrink activation: tensor([[0.6328, 0.0000, 0.0000, 0.0000, 0.0000]])
    LeakyReLU activation: tensor([[ 0.6328, -0.0028,  0.2340,  0.1001,  0.1168]])
    RReLU activation: tensor([[ 0.6328, -0.0808,  0.2340,  0.1001,  0.1168]])   不固定
    
    Mish activation: tensor([[ 0.4969, -0.1430,  0.1576,  0.0632,  0.0744]])  
    PReLu tensor([[ 0.6328, -0.0701,  0.2340,  0.1001,  0.1168]],
       grad_fn=<PreluBackward0>)
    
    nn.Threshold(0, 0.235) Threshold activation: tensor([[0.6328, 0.2350, 0.2340, 0.1001, 0.1168]])
    
    Softsign activation: tensor([[ 0.3876, -0.2189,  0.1896,  0.0910,  0.1046]])
    Tanhshrink activation: tensor([[ 0.0728, -0.0071,  0.0042,  0.0003,  0.0005]])
    Softmin activation: tensor([[0.1196, 0.2981, 0.1782, 0.2037, 0.2004]])
    
    Softmax activation: tensor([[0.3071, 0.1232, 0.2061, 0.1803, 0.1833]])
    LogSigmoid activation: tensor([[-0.4260, -0.8431, -0.5830, -0.6443, -0.6365]])
    LogSoftmax activation: tensor([[-1.1806, -2.0937, -1.5794, -1.7133, -1.6966]])
    Softplus activation: tensor([[1.0588, 0.5628, 0.8170, 0.7444, 0.7533]])
    
    Softshrink activation: tensor([[0.1328, 0.0000, 0.0000, 0.0000, 0.0000]])
    
    FReLU activation: tensor([[[[ 1.7796],
                              [-0.2803],
                              [ 0.2340],
                              [ 0.1001],
                              [ 0.1168]],
                    
                             [[ 1.0228],
                              [ 1.0072],
                              [ 0.5678],
                              [ 0.9876],
                              [ 0.5432]]]], grad_fn=<MaximumBackward0>)

    """

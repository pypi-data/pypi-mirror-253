"""
Copyright (c) 2024, Auorui.
All rights reserved.
time 2024-01-25
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
from pyzjr.nn.torchutils.loss_utils import boundary_loss

__all__ = ["L1Loss", "L2Loss", "BCELoss", "CrossEntropyLoss", "FocalLoss", "DiceLoss"]

class L1Loss(nn.Module):
    """
    L1损失，也称为平均绝对误差（MAE），测量预测输出中的每个元素与目标或地面实况中的相应元素之间的平均绝对差。
    在数学上，它表示为预测值和目标值之间差异的绝对值的平均值。与L2损耗相比，L1损耗对异常值不那么敏感。依据公式实现。
    Args:
        input (torch.Tensor): The predicted output.
        target (torch.Tensor): The target or ground truth.
        reduction (str, optional): Specifies the reduction to apply to the output.
            Options are 'none', 'mean', or 'sum'. Default is 'mean'.
    Examples::
        >>> criterion1 = nn.L1Loss()
        >>> criterion2 = L1Loss()
        >>> input_data=torch.Tensor([2, 3, 4, 5])
        >>> target_data=torch.Tensor([4, 5, 6, 7])
        >>> loss1 = criterion1(input_data, target_data)  # tensor(2.)
        >>> loss2 = criterion2(input_data, target_data)  # tensor(2.)
    Returns:
        torch.Tensor: The L1 loss between input and target.
    """
    def __init__(self):
        super(L1Loss, self).__init__()

    def forward(self, input, target):
        loss = torch.mean(torch.abs(input - target))
        return loss

class L2Loss(nn.Module):
    """
    L2损失，也称为均方误差（MSE），测量预测输出中的每个元素与目标或地面实况中的相应元素之间的平均平方差。
    在数学上，它表示为预测值和目标值之间差异的平方的平均值。相比于L1损耗，L2损耗对异常值更敏感。依据公式实现。
    在torch当中是MSELoss
    Args:
        input (torch.Tensor): The predicted output.
        target (torch.Tensor): The target or ground truth.
        reduction (str, optional): Specifies the reduction to apply to the output.
            Options are 'none', 'mean', or 'sum'. Default is 'mean'.
    Examples::
        >>> criterion1 = nn.MSELoss()
        >>> criterion2 = L2Loss()
        >>> input_data=torch.Tensor([2, 3, 4, 5])
        >>> target_data=torch.Tensor([4, 5, 6, 7])
        >>> loss1 = criterion1(input_data, target_data)  # tensor(4.)
        >>> loss2 = criterion2(input_data, target_data)  # tensor(4.)

    Returns:
        torch.Tensor: The L2 loss between input and target.
    """
    def __init__(self):
        super(L2Loss, self).__init__()

    def forward(self, input, target):
        loss = torch.mean(torch.pow(input - target, 2))
        return loss

class BCELoss(nn.Module):
    """
    二元交叉熵损失（Binary Cross Entropy Loss），也称为对数损失。
    用于测量预测输出中的每个元素与目标或地面实况中的相应元素之间的对数概率差异。依据公式实现。
    Args:
        input (torch.Tensor): The predicted output.Map to (0,1) through sigmoid function.
        target (torch.Tensor): The target or ground truth.
        reduction (str, optional): Specifies the reduction to apply to the output.
            Options are 'none', 'mean', or 'sum'. Default is 'mean'.

    Examples::
        >>> criterion1 = nn.BCELoss()
        >>> criterion2 = BCELoss()
        >>> input_data = torch.randn((5,))
        >>> target_data = torch.randint(0, 2, (5,), dtype=torch.float32)
        >>> loss1 = criterion1(torch.sigmoid(input_data), target_data)
        >>> loss2 = criterion2(input_data, target_data)
        >>> print("PyTorch BCELoss:", loss1.item())
        >>> print("Custom BCELoss:", loss2.item())

    Returns:
        torch.Tensor: The binary cross entropy loss between input and target.
    """
    def __init__(self, reduction='mean'):
        super(BCELoss, self).__init__()
        self.reduction = reduction

    def forward(self, input, target):
        input = torch.sigmoid(input)
        loss = - (target * torch.log(input) + (1 - target) * torch.log(1 - input))
        if self.reduction == 'mean':
            return loss.mean()
        elif self.reduction == 'sum':
            return loss.sum()
        elif self.reduction == 'none':
            return loss

class CrossEntropyLoss(nn.Module):
    """
    交叉熵损失（Cross Entropy Loss）用于多分类问题。
    用于测量预测输出和目标分布之间的交叉熵。依据公式实现。
    Args:
        input (torch.Tensor): The predicted output (logits).
        target (torch.Tensor): The target or ground truth (class labels).
        reduction (str, optional): Specifies the reduction to apply to the output.
            Options are 'none', 'mean', or 'sum'. Default is 'mean'.

    Examples::
        >>> criterion1 = nn.CrossEntropyLoss()
        >>> criterion2 = CrossEntropyLoss()
        >>> input_data = torch.randn((3, 5), requires_grad=True)
        >>> target_data = torch.randint(0, 5, (3,))
        >>> loss1 = criterion1(input_data, target_data)
        >>> loss2 = criterion2(input_data, target_data)
        >>> print("PyTorch CrossEntropyLoss:", loss1.item())
        >>> print("Custom CrossEntropyLoss:", loss2.item())

    Returns:
        torch.Tensor: The cross entropy loss between input and target.
    """
    def __init__(self, reduction='mean'):
        super(CrossEntropyLoss, self).__init__()
        self.reduction = reduction

    def forward(self, input, target):
        return nn.NLLLoss(reduction=self.reduction)(F.log_softmax(input, dim=1), target)


class FocalLoss(nn.Module):
    """
    Focal Loss 用于解决类别不平衡问题，通过缩小易分类的类别的损失来关注难分类的类别。依据公式实现。

    Args:
        alpha (float, optional): 控制易分类的类别的权重，大于1表示增加权重，小于1表示减小权重。默认为1.
        gamma (float, optional): 控制难分类的类别的损失的下降速度，大于0表示下降较慢，小于0表示下降较快。默认为2.
        reduction (str, optional): Specifies the reduction to apply to the output.
            Options are 'none', 'mean', or 'sum'. Default is 'mean'.

    Examples::
        >>> criterion = FocalLoss(alpha=1, gamma=2, reduction='mean')
        >>> input_data = torch.randn((5, 3), requires_grad=True)
        >>> target_data = torch.randint(0, 3, (5,))
        >>> loss = criterion(input_data, target_data)
        >>> print("Focal Loss:", loss.item())
    """
    def __init__(self, alpha=1, gamma=2, reduction='mean'):
        super(FocalLoss, self).__init__()
        self.alpha = alpha
        self.gamma = gamma
        self.reduction = reduction

    def forward(self, input, target):
        ce_loss = F.cross_entropy(input, target, reduction='none')
        class_weights = torch.exp(-ce_loss)
        focal_loss = self.alpha * (1 - class_weights) ** self.gamma * ce_loss
        if self.reduction == 'mean':
            return focal_loss.mean()
        elif self.reduction == 'sum':
            return focal_loss.sum()
        elif self.reduction == 'none':
            return focal_loss

class DiceLoss(nn.Module):
    """
    Dice Loss 测量预测的和目标的二进制分割掩码之间的不相似性。
    它被计算为1减去Dice系数，Dice系数是重叠的度量
    在预测区域和目标区域之间。

    Examples::
        >>> criterion = DiceLoss(reduction='mean')
        >>> input_data = input_data.unsqueeze(0).unsqueeze(0)
        >>> input_data = torch.randn((4, 4, 4))  # predictions
        >>> target_data = torch.randint(0, 2, (4, 4, 4))  # binary segmentation mask
        >>> loss = criterion(input_data, target_data)
        >>> print("Dice Loss:", loss.item())

    Returns:
        torch.Tensor: The Dice Loss between input and target.
    """
    def __init__(self, smooth=1.0, beta=1):
        super(DiceLoss, self).__init__()
        self.smooth = smooth
        self.beta = beta

    def forward(self, inputs, target):
        n, c, h, w = inputs.size()
        nt, ct, ht, wt = target.size()

        target = F.interpolate(target.float(), size=(h, w), mode="nearest").long()

        temp_inputs = torch.softmax(inputs.transpose(1, 2).transpose(2, 3).contiguous().view(n, -1, c), -1)
        temp_target = target.view(n, -1, ct)

        tp = torch.sum(temp_target[..., :-1] * temp_inputs, dim=[0, 1])
        fp = torch.sum(temp_inputs, dim=[0, 1]) - tp
        fn = torch.sum(temp_target[..., :-1], dim=[0, 1]) - tp

        score = ((1 + self.beta ** 2) * tp + self.smooth) / (
                (1 + self.beta ** 2) * tp + self.beta ** 2 * fn + fp + self.smooth)
        dice_loss = 1 - torch.mean(score)

        return dice_loss


class BoundaryLoss(nn.Module):
    """
    计算二进制分割的边界损失

    Args:
        None

    Examples:
        >>> criterion = BoundaryLoss()
        >>> outputs_soft = torch.rand((1, 1, 3, 3))  # model prediction
        >>> outputs_soft = torch.sigmoid(outputs_soft)
        >>> label_batch = torch.randint(2, (1, 1, 3, 3))  # binary segmentation mask
        >>> loss = criterion(outputs_soft, label_batch)
        >>> print("Boundary Loss:", loss.item())
    Returns:
        torch.Tensor: The Boundary Loss between model predictions and ground truth.
    """
    def __init__(self, reduction='mean'):
        super(BoundaryLoss, self).__init__()
        self.reduction = reduction

    def forward(self, outputs_soft, label_batch):
        loss = boundary_loss(outputs_soft, label_batch)
        if self.reduction == 'mean':
            return loss.mean()
        elif self.reduction == 'sum':
            return loss.sum()
        elif self.reduction == 'none':
            return loss
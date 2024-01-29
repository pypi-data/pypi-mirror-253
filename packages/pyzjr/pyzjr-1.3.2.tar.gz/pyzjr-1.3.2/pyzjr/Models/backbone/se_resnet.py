"""
Original paper address https://arxiv.org/pdf/1709.01507.pdf
Squeeze-and-Excitation Networks
Obtained from https://github.com/moskomule/senet.pytorch/blob/master/senet
"""
import torch.nn as nn
from pyzjr.Models.backbone.resnet import ResNet

__all__ = ["se_resnet18", "se_resnet34", "se_resnet50", "se_resnet101", "se_resnet152"]

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

def conv3x3(in_planes, out_planes, stride=1):
    return nn.Conv2d(in_planes, out_planes, kernel_size=3, stride=stride, padding=1, bias=False)

def conv1x1(in_channels, out_channels, stride=1):
    return nn.Conv2d(in_channels, out_channels, kernel_size=1, stride=stride, bias=False)

class SEBasicBlock(nn.Module):
    expansion = 1
    def __init__(self, inplanes, planes, stride=1, downsample=False, reduction=16):
        super(SEBasicBlock, self).__init__()
        self.conv1 = conv3x3(inplanes, planes, stride)
        self.bn1 = nn.BatchNorm2d(planes)
        self.relu = nn.ReLU(inplace=True)
        self.conv2 = conv3x3(planes, planes, 1)
        self.bn2 = nn.BatchNorm2d(planes)
        self.se = SELayer(planes, reduction)
        self.downsample = downsample
        self.stride = stride
        self.conv_down = nn.Sequential(
            conv1x1(inplanes, planes * self.expansion, self.stride),
            nn.BatchNorm2d(planes * self.expansion),
        )

    def forward(self, x):
        residual = x
        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)

        out = self.conv2(out)
        out = self.bn2(out)
        out = self.se(out)

        if self.downsample:
            residual = self.conv_down(x)

        out += residual
        out = self.relu(out)

        return out


class SEBottleneck(nn.Module):
    expansion = 4
    def __init__(self, inplanes, planes, stride=1, downsample=False, reduction=16):
        super(SEBottleneck, self).__init__()
        self.conv1 = nn.Conv2d(inplanes, planes, kernel_size=1, bias=False)
        self.bn1 = nn.BatchNorm2d(planes)
        self.conv2 = nn.Conv2d(planes, planes, kernel_size=3, stride=stride,
                               padding=1, bias=False)
        self.bn2 = nn.BatchNorm2d(planes)
        self.conv3 = nn.Conv2d(planes, planes * 4, kernel_size=1, bias=False)
        self.bn3 = nn.BatchNorm2d(planes * 4)
        self.relu = nn.ReLU(inplace=True)
        self.se = SELayer(planes * 4, reduction)
        self.downsample = downsample
        self.stride = stride
        self.conv_down = nn.Sequential(
            conv1x1(inplanes, planes * self.expansion, self.stride),
            nn.BatchNorm2d(planes * self.expansion),
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
        out = self.se(out)

        if self.downsample:
            residual = self.conv_down(x)

        out += residual
        out = self.relu(out)

        return out


def se_resnet18(num_classes):
    model = ResNet(SEBasicBlock, [2, 2, 2, 2], num_classes=num_classes)
    model.avgpool = nn.AdaptiveAvgPool2d(1)
    return model


def se_resnet34(num_classes):
    model = ResNet(SEBasicBlock, [3, 4, 6, 3], num_classes=num_classes)
    model.avgpool = nn.AdaptiveAvgPool2d(1)
    return model


def se_resnet50(num_classes):
    model = ResNet(SEBottleneck, [3, 4, 6, 3], num_classes=num_classes)
    model.avgpool = nn.AdaptiveAvgPool2d(1)
    return model


def se_resnet101(num_classes):
    model = ResNet(SEBottleneck, [3, 4, 23, 3], num_classes=num_classes)
    model.avgpool = nn.AdaptiveAvgPool2d(1)
    return model


def se_resnet152(num_classes):
    model = ResNet(SEBottleneck, [3, 8, 36, 3], num_classes=num_classes)
    model.avgpool = nn.AdaptiveAvgPool2d(1)
    return model

if __name__=="__main__":
    import torchsummary
    import torch
    input = torch.ones(2, 3, 224, 224).cpu()
    net = se_resnet50(num_classes=4)
    net = net.cpu()
    out = net(input)
    print(out)
    print(out.shape)
    torchsummary.summary(net, input_size=(3, 224, 224))
    # Total params: 26,031,172


""" se_resnet50:
--------------------------------------------
Layer (type)               Output Shape
============================================
Conv2d-1                  [-1, 64, 112, 112]      
BatchNorm2d-2             [-1, 64, 112, 112]
ReLU-3                    [-1, 64, 112, 112]
MaxPool2d-4               [-1, 64, 56, 56]
Conv2d-5                  [-1, 64, 56, 56]
BatchNorm2d-6             [-1, 64, 56, 56]
ReLU-7                    [-1, 64, 56, 56]
Conv2d-8                  [-1, 64, 56, 56]
BatchNorm2d-9             [-1, 64, 56, 56]
ReLU-10                   [-1, 64, 56, 56]
Conv2d-11                 [-1, 256, 56, 56]
BatchNorm2d-12            [-1, 256, 56, 56]
AdaptiveAvgPool2d-13      [-1, 256, 1, 1] 
Linear-14                 [-1, 16]    
ReLU-15                   [-1, 16]         
Linear-16                 [-1, 256]
Sigmoid-17                [-1, 256]       
SELayer-18                [-1, 256, 56, 56] 
Conv2d-19                 [-1, 256, 56, 56]
BatchNorm2d-20            [-1, 256, 56, 56]
ReLU-21                   [-1, 256, 56, 56]
SEBottleneck-22           [-1, 256, 56, 56]
Conv2d-23                 [-1, 64, 56, 56]
BatchNorm2d-24            [-1, 64, 56, 56]
ReLU-25                   [-1, 64, 56, 56]
Conv2d-26                 [-1, 64, 56, 56]
BatchNorm2d-27            [-1, 64, 56, 56]
ReLU-28                   [-1, 64, 56, 56]
Conv2d-29                 [-1, 256, 56, 56]
BatchNorm2d-30            [-1, 256, 56, 56]
AdaptiveAvgPool2d-31      [-1, 256, 1, 1]               
Linear-32                 [-1, 16]           
ReLU-33                   [-1, 16]               
Linear-34                 [-1, 256]          
Sigmoid-35                [-1, 256]          
SELayer-36                [-1, 256, 56, 56]
ReLU-37                   [-1, 256, 56, 56]
SEBottleneck-38           [-1, 256, 56, 56]
Conv2d-39                 [-1, 64, 56, 56]
BatchNorm2d-40            [-1, 64, 56, 56]
ReLU-41                   [-1, 64, 56, 56]
Conv2d-42                 [-1, 64, 56, 56]
BatchNorm2d-43            [-1, 64, 56, 56]
ReLU-44                   [-1, 64, 56, 56]
Conv2d-45                 [-1, 256, 56, 56]
BatchNorm2d-46            [-1, 256, 56, 56]
AdaptiveAvgPool2d-47      [-1, 256, 1, 1]          
Linear-48                 [-1, 16]  
ReLU-49                   [-1, 16]        
Linear-50                 [-1, 256]        
Sigmoid-51                [-1, 256]        
SELayer-52                [-1, 256, 56, 56]
ReLU-53                   [-1, 256, 56, 56]
SEBottleneck-54           [-1, 256, 56, 56]
Conv2d-55                 [-1, 128, 56, 56]
BatchNorm2d-56            [-1, 128, 56, 56]
ReLU-57                   [-1, 128, 56, 56]
Conv2d-58                 [-1, 128, 28, 28]
BatchNorm2d-59            [-1, 128, 28, 28]
ReLU-60                   [-1, 128, 28, 28]
Conv2d-61                 [-1, 512, 28, 28]
BatchNorm2d-62            [-1, 512, 28, 28]
AdaptiveAvgPool2d-63      [-1, 512, 1, 1]           
Linear-64                 [-1, 32]      
ReLU-65                   [-1, 32]     
Linear-66                 [-1, 512]    
Sigmoid-67                [-1, 512]        
SELayer-68                [-1, 512, 28, 28]               
Conv2d-69                 [-1, 512, 28, 28]     
BatchNorm2d-70            [-1, 512, 28, 28]         
ReLU-71                   [-1, 512, 28, 28]              
SEBottleneck-72           [-1, 512, 28, 28]       
Conv2d-73                 [-1, 128, 28, 28]         
BatchNorm2d-74            [-1, 128, 28, 28]        
ReLU-75                   [-1, 128, 28, 28]         
Conv2d-76                 [-1, 128, 28, 28]    
BatchNorm2d-77            [-1, 128, 28, 28]         
ReLU-78                   [-1, 128, 28, 28]           
Conv2d-79                 [-1, 512, 28, 28]          
BatchNorm2d-80            [-1, 512, 28, 28]         
AdaptiveAvgPool2d-81      [-1, 512, 1, 1]          
Linear-82                 [-1, 32]       
ReLU-83                   [-1, 32]          
Linear-84                 [-1, 512]       
Sigmoid-85                [-1, 512]           
SELayer-86                [-1, 512, 28, 28]           
ReLU-87                   [-1, 512, 28, 28]           
SEBottleneck-88           [-1, 512, 28, 28]           
Conv2d-89                 [-1, 128, 28, 28]      
BatchNorm2d-90            [-1, 128, 28, 28]      
ReLU-91                   [-1, 128, 28, 28]          
Conv2d-92                 [-1, 128, 28, 28]     
BatchNorm2d-93            [-1, 128, 28, 28]       
ReLU-94                   [-1, 128, 28, 28]       
Conv2d-95                 [-1, 512, 28, 28]      
BatchNorm2d-96            [-1, 512, 28, 28]          
AdaptiveAvgPool2d-97      [-1, 512, 1, 1]               
Linear-98                 [-1, 32]          
ReLU-99                   [-1, 32]               
Linear-100                [-1, 512]         
Sigmoid-101               [-1, 512]            
SELayer-102               [-1, 512, 28, 28]            
ReLU-103                  [-1, 512, 28, 28]            
SEBottleneck-104          [-1, 512, 28, 28]            
Conv2d-105                [-1, 128, 28, 28]         
BatchNorm2d-106           [-1, 128, 28, 28]         
ReLU-107                  [-1, 128, 28, 28]         
Conv2d-108                [-1, 128, 28, 28]     
BatchNorm2d-109           [-1, 128, 28, 28]          
ReLU-110                  [-1, 128, 28, 28]         
Conv2d-111                [-1, 512, 28, 28]        
BatchNorm2d-112           [-1, 512, 28, 28]        
AdaptiveAvgPool2d-113     [-1, 512, 1, 1]            
Linear-114                [-1, 32]          
ReLU-115                  [-1, 32]           
Linear-116                [-1, 512]        
Sigmoid-117               [-1, 512]             
SELayer-118               [-1, 512, 28, 28]              
ReLU-119                  [-1, 512, 28, 28]            
SEBottleneck-120          [-1, 512, 28, 28]          
Conv2d-121                [-1, 256, 28, 28]    
BatchNorm2d-122           [-1, 256, 28, 28]         
ReLU-123                  [-1, 256, 28, 28]          
Conv2d-124                [-1, 256, 14, 14]       
BatchNorm2d-125           [-1, 256, 14, 14]     
ReLU-126                  [-1, 256, 14, 14]         
Conv2d-127                [-1, 1024, 14, 14]        
BatchNorm2d-128           [-1, 1024, 14, 14]        
AdaptiveAvgPool2d-129     [-1, 1024, 1, 1]         
Linear-130                [-1, 64]          
ReLU-131                  [-1, 64]          
Linear-132                [-1, 1024]         
Sigmoid-133               [-1, 1024]           
SELayer-134               [-1, 1024, 14, 14]          
Conv2d-135                [-1, 1024, 14, 14]      
BatchNorm2d-136           [-1, 1024, 14, 14]       
ReLU-137                  [-1, 1024, 14, 14]      
SEBottleneck-138          [-1, 1024, 14, 14]            
Conv2d-139                [-1, 256, 14, 14]         
BatchNorm2d-140           [-1, 256, 14, 14]           
ReLU-141                  [-1, 256, 14, 14]            
Conv2d-142                [-1, 256, 14, 14]         
BatchNorm2d-143           [-1, 256, 14, 14]          
ReLU-144                  [-1, 256, 14, 14]            
Conv2d-145                [-1, 1024, 14, 14]       
BatchNorm2d-146           [-1, 1024, 14, 14]        
AdaptiveAvgPool2d-147     [-1, 1024, 1, 1]          
Linear-148                [-1, 64]          
ReLU-149                  [-1, 64]              
Linear-150                [-1, 1024]         
Sigmoid-151               [-1, 1024]            
SELayer-152               [-1, 1024, 14, 14]             
ReLU-153                  [-1, 1024, 14, 14]            
SEBottleneck-154          [-1, 1024, 14, 14]         
Conv2d-155                [-1, 256, 14, 14]        
BatchNorm2d-156           [-1, 256, 14, 14]           
ReLU-157                  [-1, 256, 14, 14]            
Conv2d-158                [-1, 256, 14, 14]        
BatchNorm2d-159           [-1, 256, 14, 14]       
ReLU-160                  [-1, 256, 14, 14]             
Conv2d-161                [-1, 1024, 14, 14]        
BatchNorm2d-162           [-1, 1024, 14, 14]          
AdaptiveAvgPool2d-163     [-1, 1024, 1, 1]         
Linear-164                [-1, 64]         
ReLU-165                  [-1, 64]               
Linear-166                [-1, 1024]          
Sigmoid-167               [-1, 1024]          
SELayer-168               [-1, 1024, 14, 14]             
ReLU-169                  [-1, 1024, 14, 14]             
SEBottleneck-170          [-1, 1024, 14, 14]              
Conv2d-171                [-1, 256, 14, 14]         
BatchNorm2d-172           [-1, 256, 14, 14]        
ReLU-173                  [-1, 256, 14, 14]           
Conv2d-174                [-1, 256, 14, 14]       
BatchNorm2d-175           [-1, 256, 14, 14]      
ReLU-176                  [-1, 256, 14, 14]            
Conv2d-177                [-1, 1024, 14, 14]         
BatchNorm2d-178           [-1, 1024, 14, 14]          
AdaptiveAvgPool2d-179     [-1, 1024, 1, 1]               
Linear-180                [-1, 64]         
ReLU-181                  [-1, 64]              
Linear-182                [-1, 1024]        
Sigmoid-183               [-1, 1024]              
SELayer-184               [-1, 1024, 14, 14]               
ReLU-185                  [-1, 1024, 14, 14]               
SEBottleneck-186          [-1, 1024, 14, 14]               
Conv2d-187                [-1, 256, 14, 14]         
BatchNorm2d-188           [-1, 256, 14, 14]             
ReLU-189                  [-1, 256, 14, 14]               
Conv2d-190                [-1, 256, 14, 14]         
BatchNorm2d-191           [-1, 256, 14, 14]        
ReLU-192                  [-1, 256, 14, 14]               
Conv2d-193                [-1, 1024, 14, 14]        
BatchNorm2d-194           [-1, 1024, 14, 14]           
AdaptiveAvgPool2d-195     [-1, 1024, 1, 1]               
Linear-196                [-1, 64]          
ReLU-197                  [-1, 64]               
Linear-198                [-1, 1024]          
Sigmoid-199               [-1, 1024]               
SELayer-200               [-1, 1024, 14, 14]               
ReLU-201                  [-1, 1024, 14, 14]               
SEBottleneck-202          [-1, 1024, 14, 14]               
Conv2d-203                [-1, 256, 14, 14]       
BatchNorm2d-204           [-1, 256, 14, 14]           
ReLU-205                  [-1, 256, 14, 14]             
Conv2d-206                [-1, 256, 14, 14]       
BatchNorm2d-207           [-1, 256, 14, 14]          
ReLU-208                  [-1, 256, 14, 14]             
Conv2d-209                [-1, 1024, 14, 14]         
BatchNorm2d-210           [-1, 1024, 14, 14]       
AdaptiveAvgPool2d-211     [-1, 1024, 1, 1]            
Linear-212                [-1, 64]        
ReLU-213                  [-1, 64]           
Linear-214                [-1, 1024]         
Sigmoid-215               [-1, 1024]          
SELayer-216               [-1, 1024, 14, 14]           
ReLU-217                  [-1, 1024, 14, 14]               
SEBottleneck-218          [-1, 1024, 14, 14]          
Conv2d-219                [-1, 512, 14, 14]        
BatchNorm2d-220           [-1, 512, 14, 14]        
ReLU-221                  [-1, 512, 14, 14]            
Conv2d-222                [-1, 512, 7, 7]       
BatchNorm2d-223           [-1, 512, 7, 7]          
ReLU-224                  [-1, 512, 7, 7]               
Conv2d-225                [-1, 2048, 7, 7]  
BatchNorm2d-226           [-1, 2048, 7, 7]         
AdaptiveAvgPool2d-227     [-1, 2048, 1, 1]           
Linear-228                [-1, 128]      
ReLU-229                  [-1, 128]           
Linear-230                [-1, 2048]      
Sigmoid-231               [-1, 2048]               
SELayer-232               [-1, 2048, 7, 7]               
Conv2d-233                [-1, 2048, 7, 7]    
BatchNorm2d-234           [-1, 2048, 7, 7]         
ReLU-235                  [-1, 2048, 7, 7]               
SEBottleneck-236          [-1, 2048, 7, 7]            
Conv2d-237                [-1, 512, 7, 7]       
BatchNorm2d-238           [-1, 512, 7, 7]         
ReLU-239                  [-1, 512, 7, 7]           
Conv2d-240                [-1, 512, 7, 7]    
BatchNorm2d-241           [-1, 512, 7, 7]         
ReLU-242                  [-1, 512, 7, 7]            
Conv2d-243                [-1, 2048, 7, 7]       
BatchNorm2d-244           [-1, 2048, 7, 7]        
AdaptiveAvgPool2d-245     [-1, 2048, 1, 1]          
Linear-246                [-1, 128]       
ReLU-247                  [-1, 128]               
Linear-248                [-1, 2048]        
Sigmoid-249               [-1, 2048]               
SELayer-250               [-1, 2048, 7, 7]               
ReLU-251                  [-1, 2048, 7, 7]               
SEBottleneck-252          [-1, 2048, 7, 7]               
Conv2d-253                [-1, 512, 7, 7]     
BatchNorm2d-254           [-1, 512, 7, 7]         
ReLU-255                  [-1, 512, 7, 7]               
Conv2d-256                [-1, 512, 7, 7]      
BatchNorm2d-257           [-1, 512, 7, 7]          
ReLU-258                  [-1, 512, 7, 7]               
Conv2d-259                [-1, 2048, 7, 7]     
BatchNorm2d-260           [-1, 2048, 7, 7]         
AdaptiveAvgPool2d-261     [-1, 2048, 1, 1]               
Linear-262                [-1, 128]         
ReLU-263                  [-1, 128]               
Linear-264                [-1, 2048]       
Sigmoid-265               [-1, 2048]               
SELayer-266               [-1, 2048, 7, 7]               
ReLU-267                  [-1, 2048, 7, 7]               
SEBottleneck-268          [-1, 2048, 7, 7]               
AdaptiveAvgPool2d-269     [-1, 2048, 1, 1]               
Linear-270                [-1, 4]         
============================================
"""
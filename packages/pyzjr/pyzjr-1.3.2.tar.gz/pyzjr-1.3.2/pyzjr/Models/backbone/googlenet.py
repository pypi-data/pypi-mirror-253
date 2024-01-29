"""
论文原址： <https://arxiv.org/pdf/1409.4842.pdf>
Going deeper with convolutions
Obtained from torchvision.models
"""
import torch
import torch.nn as nn

__all__ = ["GoogLeNet"]

class Inception(nn.Module):
    def __init__(self, in_channels, ch1x1, ch3x3red, ch3x3, ch5x5red, ch5x5, pool_proj):
        super(Inception, self).__init__()
        self.branch1 = self.BasicConv(in_channels, ch1x1, kernel_size=1)
        self.branch2 = nn.Sequential(
            self.BasicConv(in_channels, ch3x3red, kernel_size=1),
            self.BasicConv(ch3x3red, ch3x3, kernel_size=3, padding=1)
        )
        self.branch3 = nn.Sequential(
            self.BasicConv(in_channels, ch5x5red, kernel_size=1),
            self.BasicConv(ch5x5red, ch5x5, kernel_size=3, padding=1)
        )
        self.branch4 = nn.Sequential(
            nn.MaxPool2d(kernel_size=3, stride=1, padding=1, ceil_mode=True),
            self.BasicConv(in_channels, pool_proj, kernel_size=1)
        )

    def BasicConv(self, in_channels, out_channels, **kwargs):
        return nn.Sequential(nn.Conv2d(in_channels, out_channels, bias=False, **kwargs),
                             nn.BatchNorm2d(out_channels, eps=0.001),
                             nn.ReLU(inplace=True),)

    def forward(self, x):
        branch1 = self.branch1(x)
        branch2 = self.branch2(x)
        branch3 = self.branch3(x)
        branch4 = self.branch4(x)

        outputs = [branch1, branch2, branch3, branch4]
        return torch.cat(outputs, dim=1)

class GoogLeNet(nn.Module):
    def __init__(self, num_classes=1000, init_weights=False):
        super(GoogLeNet, self).__init__()
        # 可参考 https://arxiv.org/pdf/1409.4842.pdf 第七页结构图和第六页Table 1
        self.conv1 = self.BasicConv(3, 64, kernel_size=7, stride=2, padding=3)
        self.maxpool1 = nn.MaxPool2d(3, stride=2, ceil_mode=True)
        self.conv2 = self.BasicConv(64, 64, kernel_size=1, stride=1)
        self.conv3 = self.BasicConv(64, 192, kernel_size=3, padding=1)
        self.maxpool2 = nn.MaxPool2d(3, stride=2, ceil_mode=True)

        self.inception3a = Inception(192, 64, 96, 128, 16, 32, 32)
        self.inception3b = Inception(256, 128, 128, 192, 32, 96, 64)
        self.maxpool3 = nn.MaxPool2d(3, stride=2, ceil_mode=True)

        self.inception4a = Inception(480, 192, 96, 208, 16, 48, 64)
        self.inception4b = Inception(512, 160, 112, 224, 24, 64, 64)
        self.inception4c = Inception(512, 128, 128, 256, 24, 64, 64)
        self.inception4d = Inception(512, 112, 144, 288, 32, 64, 64)
        self.inception4e = Inception(528, 256, 160, 320, 32, 128, 128)
        self.maxpool4 = nn.MaxPool2d(2, stride=2, ceil_mode=True)

        self.inception5a = Inception(832, 256, 160, 320, 32, 128, 128)
        self.inception5b = Inception(832, 384, 192, 384, 48, 128, 128)

        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
        self.dropout = nn.Dropout(0.2)
        self.fc = nn.Linear(1024, num_classes)

        if init_weights:
            self._initialize_weights()

    def _initialize_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Conv2d) or isinstance(m, nn.Linear):
                import scipy.stats as stats
                X = stats.truncnorm(-2, 2, scale=0.01)
                values = torch.as_tensor(X.rvs(m.weight.numel()), dtype=m.weight.dtype)
                values = values.view(m.weight.size())
                with torch.no_grad():
                    m.weight.copy_(values)
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)

    def BasicConv(self, in_channels, out_channels, **kwargs):
        return nn.Sequential(nn.Conv2d(in_channels, out_channels, bias=False, **kwargs),
                             nn.BatchNorm2d(out_channels, eps=0.001),
                             nn.ReLU(inplace=True),)

    def forward(self, x):
        # N x 3 x 224 x 224
        x = self.conv1(x)
        # N x 64 x 112 x 112
        x = self.maxpool1(x)
        # N x 64 x 56 x 56
        x = self.conv2(x)
        # N x 64 x 56 x 56
        x = self.conv3(x)
        # N x 192 x 56 x 56
        x = self.maxpool2(x)
        # N x 192 x 28 x 28
        x = self.inception3a(x)
        # N x 256 x 28 x 28
        x = self.inception3b(x)
        # N x 480 x 28 x 28
        x = self.maxpool3(x)
        # N x 480 x 14 x 14
        x = self.inception4a(x)
        # N x 512 x 14 x 14
        x = self.inception4b(x)
        # N x 512 x 14 x 14
        x = self.inception4c(x)
        # N x 512 x 14 x 14
        x = self.inception4d(x)
        # N x 528 x 14 x 14
        x = self.inception4e(x)
        # N x 832 x 14 x 14
        x = self.maxpool4(x)
        # N x 832 x 7 x 7
        x = self.inception5a(x)
        # N x 832 x 7 x 7
        x = self.inception5b(x)
        # N x 1024 x 7 x 7
        x = self.avgpool(x)
        # N x 1024 x 1 x 1
        x = torch.flatten(x, 1)
        # N x 1024
        x = self.dropout(x)
        x = self.fc(x)
        # N x 1000 (num_classes)
        return x


if __name__=="__main__":
    import torchsummary
    input = torch.ones(2, 3, 224, 224).cpu()
    net = GoogLeNet(num_classes=4)
    net = net.cpu()
    out = net(input)
    print(out)
    print(out.shape)
    torchsummary.summary(net, input_size=(3, 224, 224))
    # Total params: 5,604,004

"""GoogLeNet  
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
Conv2d-8                  [-1, 192, 56, 56]   
BatchNorm2d-9             [-1, 192, 56, 56]   
ReLU-10                   [-1, 192, 56, 56]   
MaxPool2d-11              [-1, 192, 28, 28]   
Conv2d-12                 [-1, 64, 28, 28]    
BatchNorm2d-13            [-1, 64, 28, 28]    
ReLU-14                   [-1, 64, 28, 28]    
Conv2d-15                 [-1, 96, 28, 28]    
BatchNorm2d-16            [-1, 96, 28, 28]    
ReLU-17                   [-1, 96, 28, 28]    
Conv2d-18                 [-1, 128, 28, 28]   
BatchNorm2d-19            [-1, 128, 28, 28]   
ReLU-20                   [-1, 128, 28, 28]   
Conv2d-21                 [-1, 16, 28, 28]    
BatchNorm2d-22            [-1, 16, 28, 28]    
ReLU-23                   [-1, 16, 28, 28]    
Conv2d-24                 [-1, 32, 28, 28]    
BatchNorm2d-25            [-1, 32, 28, 28]    
ReLU-26                   [-1, 32, 28, 28]    
MaxPool2d-27              [-1, 192, 28, 28]   
Conv2d-28                 [-1, 32, 28, 28]    
BatchNorm2d-29            [-1, 32, 28, 28]    
ReLU-30                   [-1, 32, 28, 28]    
Inception-31              [-1, 256, 28, 28]   
Conv2d-32                 [-1, 128, 28, 28]   
BatchNorm2d-33            [-1, 128, 28, 28]   
ReLU-34                   [-1, 128, 28, 28]   
Conv2d-35                 [-1, 128, 28, 28]   
BatchNorm2d-36            [-1, 128, 28, 28]   
ReLU-37                   [-1, 128, 28, 28]   
Conv2d-38                 [-1, 192, 28, 28]   
BatchNorm2d-39            [-1, 192, 28, 28]   
ReLU-40                   [-1, 192, 28, 28]   
Conv2d-41                 [-1, 32, 28, 28]    
BatchNorm2d-42            [-1, 32, 28, 28]    
ReLU-43                   [-1, 32, 28, 28]    
Conv2d-44                 [-1, 96, 28, 28]    
BatchNorm2d-45            [-1, 96, 28, 28]    
ReLU-46                   [-1, 96, 28, 28]    
MaxPool2d-47              [-1, 256, 28, 28]   
Conv2d-48                 [-1, 64, 28, 28]    
BatchNorm2d-49            [-1, 64, 28, 28]    
ReLU-50                   [-1, 64, 28, 28]    
Inception-51              [-1, 480, 28, 28]   
MaxPool2d-52              [-1, 480, 14, 14]   
Conv2d-53                 [-1, 192, 14, 14]   
BatchNorm2d-54            [-1, 192, 14, 14]   
ReLU-55                   [-1, 192, 14, 14]   
Conv2d-56                 [-1, 96, 14, 14]    
BatchNorm2d-57            [-1, 96, 14, 14]
ReLU-58                   [-1, 96, 14, 14]    
Conv2d-59                 [-1, 208, 14, 14]   
BatchNorm2d-60            [-1, 208, 14, 14]   
ReLU-61                   [-1, 208, 14, 14]   
Conv2d-62                 [-1, 16, 14, 14]    
BatchNorm2d-63            [-1, 16, 14, 14]    
ReLU-64                   [-1, 16, 14, 14]    
Conv2d-65                 [-1, 48, 14, 14]    
BatchNorm2d-66            [-1, 48, 14, 14]    
ReLU-67                   [-1, 48, 14, 14]    
MaxPool2d-68              [-1, 480, 14, 14]   
Conv2d-69                 [-1, 64, 14, 14]    
BatchNorm2d-70            [-1, 64, 14, 14]    
ReLU-71                   [-1, 64, 14, 14]    
Inception-72              [-1, 512, 14, 14]   
Conv2d-73                 [-1, 160, 14, 14]   
BatchNorm2d-74            [-1, 160, 14, 14]   
ReLU-75                   [-1, 160, 14, 14]   
Conv2d-76                 [-1, 112, 14, 14]   
BatchNorm2d-77            [-1, 112, 14, 14]   
ReLU-78                   [-1, 112, 14, 14]   
Conv2d-79                 [-1, 224, 14, 14]   
BatchNorm2d-80            [-1, 224, 14, 14]   
ReLU-81                   [-1, 224, 14, 14]   
Conv2d-82                 [-1, 24, 14, 14]    
BatchNorm2d-83            [-1, 24, 14, 14]    
ReLU-84                   [-1, 24, 14, 14]    
Conv2d-85                 [-1, 64, 14, 14]    
BatchNorm2d-86            [-1, 64, 14, 14]    
ReLU-87                   [-1, 64, 14, 14]    
MaxPool2d-88              [-1, 512, 14, 14]   
Conv2d-89                 [-1, 64, 14, 14]    
BatchNorm2d-90            [-1, 64, 14, 14]    
ReLU-91                   [-1, 64, 14, 14]    
Inception-92              [-1, 512, 14, 14]   
Conv2d-93                 [-1, 128, 14, 14]   
BatchNorm2d-94            [-1, 128, 14, 14]   
ReLU-95                   [-1, 128, 14, 14]   
Conv2d-96                 [-1, 128, 14, 14]   
BatchNorm2d-97            [-1, 128, 14, 14]   
ReLU-98                   [-1, 128, 14, 14]   
Conv2d-99                 [-1, 256, 14, 14]   
BatchNorm2d-100           [-1, 256, 14, 14]   
ReLU-101                  [-1, 256, 14, 14]   
Conv2d-102                [-1, 24, 14, 14]    
BatchNorm2d-103           [-1, 24, 14, 14]    
ReLU-104                  [-1, 24, 14, 14]    
Conv2d-105                [-1, 64, 14, 14]    
BatchNorm2d-106           [-1, 64, 14, 14]    
ReLU-107                  [-1, 64, 14, 14]    
MaxPool2d-108             [-1, 512, 14, 14]   
Conv2d-109                [-1, 64, 14, 14]    
BatchNorm2d-110           [-1, 64, 14, 14]    
ReLU-111                  [-1, 64, 14, 14]    
Inception-112             [-1, 512, 14, 14]   
Conv2d-113                [-1, 112, 14, 14]   
BatchNorm2d-114           [-1, 112, 14, 14]   
ReLU-115                  [-1, 112, 14, 14]   
Conv2d-116                [-1, 144, 14, 14]   
BatchNorm2d-117           [-1, 144, 14, 14]   
ReLU-118                  [-1, 144, 14, 14]   
Conv2d-119                [-1, 288, 14, 14]   
BatchNorm2d-120           [-1, 288, 14, 14]   
ReLU-121                  [-1, 288, 14, 14]   
Conv2d-122                [-1, 32, 14, 14]    
BatchNorm2d-123           [-1, 32, 14, 14]    
ReLU-124                  [-1, 32, 14, 14]    
Conv2d-125                [-1, 64, 14, 14]    
BatchNorm2d-126           [-1, 64, 14, 14]    
ReLU-127                  [-1, 64, 14, 14]    
MaxPool2d-128             [-1, 512, 14, 14]   
Conv2d-129                [-1, 64, 14, 14]    
BatchNorm2d-130           [-1, 64, 14, 14]    
ReLU-131                  [-1, 64, 14, 14]    
Inception-132             [-1, 528, 14, 14]   
Conv2d-133                [-1, 256, 14, 14]   
BatchNorm2d-134           [-1, 256, 14, 14]   
ReLU-135                  [-1, 256, 14, 14]   
Conv2d-136                [-1, 160, 14, 14]   
BatchNorm2d-137           [-1, 160, 14, 14]   
ReLU-138                  [-1, 160, 14, 14]   
Conv2d-139                [-1, 320, 14, 14]   
BatchNorm2d-140           [-1, 320, 14, 14]   
ReLU-141                  [-1, 320, 14, 14]   
Conv2d-142                [-1, 32, 14, 14]    
BatchNorm2d-143           [-1, 32, 14, 14]    
ReLU-144                  [-1, 32, 14, 14]    
Conv2d-145                [-1, 128, 14, 14]   
BatchNorm2d-146           [-1, 128, 14, 14]   
ReLU-147                  [-1, 128, 14, 14]   
MaxPool2d-148             [-1, 528, 14, 14]   
Conv2d-149                [-1, 128, 14, 14]   
BatchNorm2d-150           [-1, 128, 14, 14]   
ReLU-151                  [-1, 128, 14, 14]   
Inception-152             [-1, 832, 14, 14]   
MaxPool2d-153             [-1, 832, 7, 7]     
Conv2d-154                [-1, 256, 7, 7]     
BatchNorm2d-155           [-1, 256, 7, 7]     
ReLU-156                  [-1, 256, 7, 7]     
Conv2d-157                [-1, 160, 7, 7]     
BatchNorm2d-158           [-1, 160, 7, 7]     
ReLU-159                  [-1, 160, 7, 7]     
Conv2d-160                [-1, 320, 7, 7]     
BatchNorm2d-161           [-1, 320, 7, 7]     
ReLU-162                  [-1, 320, 7, 7]     
Conv2d-163                [-1, 32, 7, 7]      
BatchNorm2d-164           [-1, 32, 7, 7]      
ReLU-165                  [-1, 32, 7, 7]      
Conv2d-166                [-1, 128, 7, 7]     
BatchNorm2d-167           [-1, 128, 7, 7]     
ReLU-168                  [-1, 128, 7, 7]     
MaxPool2d-169             [-1, 832, 7, 7]     
Conv2d-170                [-1, 128, 7, 7]     
BatchNorm2d-171           [-1, 128, 7, 7]     
ReLU-172                  [-1, 128, 7, 7]     
Inception-173             [-1, 832, 7, 7]     
Conv2d-174                [-1, 384, 7, 7]     
BatchNorm2d-175           [-1, 384, 7, 7]     
ReLU-176                  [-1, 384, 7, 7]     
Conv2d-177                [-1, 192, 7, 7]     
BatchNorm2d-178           [-1, 192, 7, 7]     
ReLU-179                  [-1, 192, 7, 7]     
Conv2d-180                [-1, 384, 7, 7]     
BatchNorm2d-181           [-1, 384, 7, 7]     
ReLU-182                  [-1, 384, 7, 7]    
Conv2d-183                [-1, 48, 7, 7]     
BatchNorm2d-184           [-1, 48, 7, 7]     
ReLU-185                  [-1, 48, 7, 7]     
Conv2d-186                [-1, 128, 7, 7]    
BatchNorm2d-187           [-1, 128, 7, 7]    
ReLU-188                  [-1, 128, 7, 7]    
MaxPool2d-189             [-1, 832, 7, 7]    
Conv2d-190                [-1, 128, 7, 7]    
BatchNorm2d-191           [-1, 128, 7, 7]    
ReLU-192                  [-1, 128, 7, 7]    
Inception-193             [-1, 1024, 7, 7]    
MaxPool2d-194             [-1, 1024, 1, 1]    
Dropout-195               [-1, 1024]         
Linear-196                [-1, 4]            
============================================
"""

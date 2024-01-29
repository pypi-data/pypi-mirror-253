"""
论文原址： <https://proceedings.neurips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf>
ImageNet Classification with Deep Convolutional Neural Networks
"""
import torch
import torch.nn as nn

__all__ = ['AlexNet']

class AlexNet(nn.Module):
    def __init__(self, num_classes=1000):
        super(AlexNet, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=11, stride=4, padding=2),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
            nn.Conv2d(64, 192, kernel_size=5, padding=2),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
            nn.Conv2d(192, 384, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(384, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(256, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
        )
        self.avgpool = nn.AdaptiveAvgPool2d((6, 6))
        self.classifier = nn.Sequential(
            nn.Dropout(),
            nn.Linear(256 * 6 * 6, 4096),
            nn.ReLU(inplace=True),
            nn.Dropout(),
            nn.Linear(4096, 4096),
            nn.ReLU(inplace=True),
            nn.Linear(4096, num_classes),
        )

    def forward(self, x):
        x = self.features(x)
        x = self.avgpool(x)
        x = torch.flatten(x, 1)
        x = self.classifier(x)
        return x


if __name__=='__main__':
    import torchsummary
    input = torch.ones(2, 3, 224, 224).cpu()
    net = AlexNet(num_classes=4)
    net = net.cpu()
    out = net(input)
    print(out)
    print(out.shape)
    torchsummary.summary(net, input_size=(3, 224, 224))
    # Total params: 134,285,380
""" alexnet :
--------------------------------------------
Layer (type)               Output Shape
============================================
Conv2d-1                  [-1, 64, 55, 55]         
ReLU-2                    [-1, 64, 55, 55]               
MaxPool2d-3               [-1, 64, 27, 27]               
Conv2d-4                  [-1, 192, 27, 27]         
ReLU-5                    [-1, 192, 27, 27]               
MaxPool2d-6               [-1, 192, 13, 13]               
Conv2d-7                  [-1, 384, 13, 13]         
ReLU-8                    [-1, 384, 13, 13]               
Conv2d-9                  [-1, 256, 13, 13]         
ReLU-10                   [-1, 256, 13, 13]               
Conv2d-11                 [-1, 256, 13, 13]         
ReLU-12                   [-1, 256, 13, 13]               
MaxPool2d-13              [-1, 256, 6, 6]               
AdaptiveAvgPool2d-14      [-1, 256, 6, 6]               
Dropout-15                [-1, 9216]               
Linear-16                 [-1, 4096]      
ReLU-17                   [-1, 4096]             
Dropout-18                [-1, 4096]         
Linear-19                 [-1, 4096]    
ReLU-20                   [-1, 4096]            
Linear-21                 [-1, 4]         
============================================
"""
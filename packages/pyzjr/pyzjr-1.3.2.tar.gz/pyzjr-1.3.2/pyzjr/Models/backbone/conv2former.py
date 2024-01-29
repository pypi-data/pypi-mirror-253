"""
Copyright (c) 2023, Auorui.
All rights reserved.

reference <https://arxiv.org/pdf/2211.11943.pdf> (Conv2Former: A Simple Transformer-Style ConvNet for Visual Recognition)
Time:2023.12.31, Complete before the end of 2023.
"""
import torch
import torch.nn as nn

from pyzjr.Models.bricks import DropPath

__all__=["Conv2Former_n", "Conv2Former_t", "Conv2Former_s", "Conv2Former_b", "Conv2Former_l"]


class MLP(nn.Module):
    def __init__(self, dim, mlp_ratio=4.):
        super().__init__()

        self.norm = nn.LayerNorm(dim, eps=1e-6)
        self.fc1 = nn.Conv2d(dim, dim * mlp_ratio, 1)
        self.pos = nn.Conv2d(dim * mlp_ratio, dim * mlp_ratio, 3, padding=1, groups=dim * mlp_ratio)
        self.fc2 = nn.Conv2d(dim * mlp_ratio, dim, 1)
        self.act = nn.GELU()

    def forward(self, x):
        x = self.norm(x.permute(0, 2, 3, 1)).permute(0, 3, 1, 2)
        x = self.fc1(x)
        x = self.act(x)
        x = x + self.act(self.pos(x))
        x = self.fc2(x)
        return x


class ConvMod(nn.Module):
    def __init__(self, dim):
        super().__init__()

        self.norm = nn.LayerNorm(dim, eps=1e-6)
        self.a = nn.Sequential(
            nn.Conv2d(dim, dim, 1),
            nn.GELU(),
            nn.Conv2d(dim, dim, 11, padding=5, groups=dim)
        )
        self.v = nn.Conv2d(dim, dim, 1)
        self.proj = nn.Conv2d(dim, dim, 1)

    def forward(self, x):
        x = self.norm(x.permute(0, 2, 3, 1)).permute(0, 3, 1, 2)
        a = self.a(x)
        x = a * self.v(x)
        x = self.proj(x)
        return x



class Block(nn.Module):
    def __init__(self, dim, mlp_ratio=4.0, drop_path=0.):
        super().__init__()

        self.attn = ConvMod(dim)
        self.mlp = MLP(dim, mlp_ratio)
        layer_scale_init_value = 1e-6
        self.layer_scale_1 = nn.Parameter(layer_scale_init_value * torch.ones((dim)), requires_grad=True)
        self.layer_scale_2 = nn.Parameter(layer_scale_init_value * torch.ones((dim)), requires_grad=True)
        self.drop_path = DropPath(drop_path) if drop_path > 0. else nn.Identity()

    def forward(self, x):
        x = x + self.drop_path(self.layer_scale_1.unsqueeze(-1).unsqueeze(-1) * self.attn(x))
        x = x + self.drop_path(self.layer_scale_2.unsqueeze(-1).unsqueeze(-1) * self.mlp(x))
        return x

class BaseLayer(nn.Module):
    def __init__(self, dim, depth, mlp_ratio=4., drop_path=None, downsample=True):
        super().__init__()
        self.dim = dim
        self.drop_path = drop_path

        self.blocks = nn.ModuleList([
            Block(dim=self.dim,mlp_ratio=mlp_ratio,drop_path=drop_path[i],)
            for i in range(depth)
        ])

        # patch merging layer
        if downsample:
            self.downsample = nn.Sequential(
                nn.GroupNorm(num_groups=1, num_channels=dim),
                nn.Conv2d(dim, dim * 2, kernel_size=2, stride=2,bias=False)
            )
        else:
            self.downsample = None

    def forward(self, x):
        for blk in self.blocks:
            x = blk(x)
        if self.downsample is not None:
            x = self.downsample(x)
        return x

class Conv2Former(nn.Module):
    def __init__(self, num_classes=10, depths=(2,2,8,2), dim=(64,128,256,512), mlp_ratio=2.,drop_rate=0.,
                 drop_path_rate=0.15, **kwargs):
        super().__init__()

        norm_layer = nn.LayerNorm
        self.num_classes = num_classes
        self.num_layers = len(depths)
        self.dim = dim
        self.mlp_ratio = mlp_ratio
        self.pos_drop = nn.Dropout(p=drop_rate)

        # stochastic depth decay rule
        dpr = [x.item() for x in torch.linspace(0, drop_path_rate, sum(depths))]

        # build layers
        self.layers = nn.ModuleList()
        for i_layer in range(self.num_layers):
            layer = BaseLayer(dim[i_layer],
                              depth=depths[i_layer],
                              mlp_ratio=self.mlp_ratio,
                              drop_path=dpr[sum(depths[:i_layer]):sum(depths[:i_layer + 1])],
                              downsample=(i_layer < self.num_layers - 1),
                              )
            self.layers.append(layer)
        self.fc1 = nn.Conv2d(3, dim[0], 1)
        self.norm = norm_layer(dim[-1], eps=1e-6,)
        self.avgpool = nn.AdaptiveAvgPool2d(1)
        self.head = nn.Linear(dim[-1], num_classes) \
            if num_classes > 0 else nn.Identity()

        self.apply(self._init_weights)

    def _init_weights(self, m):
        if isinstance(m, nn.Linear):
            nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            if m.bias is not None:
                nn.init.constant_(m.bias, 0.)
        elif isinstance(m, (nn.Conv1d, nn.Conv2d)):
            nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            if m.bias is not None:
                nn.init.constant_(m.bias, 0.)
        elif isinstance(m, (nn.LayerNorm, nn.GroupNorm)):
            nn.init.constant_(m.bias, 0.)
            nn.init.constant_(m.weight, 1.)

    def forward_features(self, x):
        x = self.fc1(x)
        x = self.pos_drop(x)

        for layer in self.layers:
            x = layer(x)

        x = self.norm(x.permute(0, 2, 3, 1)).permute(0, 3, 1, 2)
        x = self.avgpool(x)
        x = torch.flatten(x, 1)
        return x

    def forward(self, x):
        x = self.forward_features(x)
        x = self.head(x)
        return x


#  reference <https://arxiv.org/pdf/2211.11943.pdf> Table 1
C = {'n': [64, 128, 256, 512],
     't': [72, 144, 288, 576],
     's': [72, 144, 288, 576],
     'b': [96, 192, 384, 768],
     'l': [128, 256, 512, 1024],
     }
L = {'n': [2, 2, 8, 2],
     't': [3, 3, 12, 3],
     's': [4, 4, 32, 4],
     'b': [4, 4, 34, 4],
     'l': [4, 4, 48, 4],
     }

def Conv2Former_n(num_classes, mlp_ratio=2, drop_path_rate=0.1):
    model = Conv2Former(num_classes=num_classes, depths=L["n"], dim=C["n"], mlp_ratio=mlp_ratio, drop_path_rate=drop_path_rate)
    return model

def Conv2Former_t(num_classes, mlp_ratio=2, drop_path_rate=0.1):
    model = Conv2Former(num_classes=num_classes, depths=L["t"], dim=C["t"], mlp_ratio=mlp_ratio, drop_path_rate=drop_path_rate)
    return model

def Conv2Former_s(num_classes, mlp_ratio=2, drop_path_rate=0.1):
    model = Conv2Former(num_classes=num_classes, depths=L["s"], dim=C["s"], mlp_ratio=mlp_ratio, drop_path_rate=drop_path_rate)
    return model

def Conv2Former_b(num_classes, mlp_ratio=2, drop_path_rate=0.1):
    model = Conv2Former(num_classes=num_classes, depths=L["b"], dim=C["b"], mlp_ratio=mlp_ratio, drop_path_rate=drop_path_rate)
    return model

def Conv2Former_l(num_classes, mlp_ratio=2, drop_path_rate=0.1):
    model = Conv2Former(num_classes=num_classes, depths=L["l"], dim=C["l"], mlp_ratio=mlp_ratio, drop_path_rate=drop_path_rate)
    return model

if __name__ == '__main__':
    import torchsummary
    model = Conv2Former_n(num_classes=4)
    input_tensor = torch.ones(2, 3, 224, 224).cpu()
    model = model.cpu()
    output = model(input_tensor)
    print("Output shape:", output.shape)
    torchsummary.summary(model, input_size=(3, 224, 224))
    # n: Total params: 8,844,420
    # t: Total params: 16,241,044
    # 其他的结构容易导致CUDA error: out of memory,建议使用前面两个类型，即是 n 和 t

""" Conv2Former_n:
--------------------------------------------
Layer (type)               Output Shape
============================================
Conv2d-1                  [-1, 64, 224, 224]             
Dropout-2                 [-1, 64, 224, 224]             
LayerNorm-3               [-1, 224, 224, 64]            
Conv2d-4                  [-1, 64, 224, 224]           
GELU-5                    [-1, 64, 224, 224]            
Conv2d-6                  [-1, 64, 224, 224]           
Conv2d-7                  [-1, 64, 224, 224]           
Conv2d-8                  [-1, 64, 224, 224]           
ConvMod-9                 [-1, 64, 224, 224]               
Identity-10               [-1, 64, 224, 224]               
LayerNorm-11              [-1, 224, 224, 64]             
Conv2d-12                 [-1, 128, 224, 224]           
GELU-13                   [-1, 128, 224, 224]               
Conv2d-14                 [-1, 128, 224, 224]          
GELU-15                   [-1, 128, 224, 224]               
Conv2d-16                 [-1, 64, 224, 224]           
MLP-17                    [-1, 64, 224, 224]               
Identity-18               [-1, 64, 224, 224]               
Block-19                  [-1, 64, 224, 224]               
LayerNorm-20              [-1, 224, 224, 64]             
Conv2d-21                 [-1, 64, 224, 224]          
GELU-22                   [-1, 64, 224, 224]               
Conv2d-23                 [-1, 64, 224, 224]           
Conv2d-24                 [-1, 64, 224, 224]       
Conv2d-25                 [-1, 64, 224, 224]          
ConvMod-26                [-1, 64, 224, 224]             
DropPath-27               [-1, 64, 224, 224]            
LayerNorm-28              [-1, 224, 224, 64]            
Conv2d-29                 [-1, 128, 224, 224]          
GELU-30                   [-1, 128, 224, 224]               
Conv2d-31                 [-1, 128, 224, 224]          
GELU-32                   [-1, 128, 224, 224]               
Conv2d-33                 [-1, 64, 224, 224]           
MLP-34                    [-1, 64, 224, 224]              
DropPath-35               [-1, 64, 224, 224]            
Block-36                  [-1, 64, 224, 224]              
GroupNorm-37              [-1, 64, 224, 224]            
Conv2d-38                 [-1, 128, 112, 112]         
BaseLayer-39              [-1, 128, 112, 112]               
LayerNorm-40              [-1, 112, 112, 128]             
Conv2d-41                 [-1, 128, 112, 112]          
GELU-42                   [-1, 128, 112, 112]               
Conv2d-43                 [-1, 128, 112, 112]          
Conv2d-44                 [-1, 128, 112, 112]          
Conv2d-45                 [-1, 128, 112, 112]          
ConvMod-46                [-1, 128, 112, 112]              
DropPath-47               [-1, 128, 112, 112]              
LayerNorm-48              [-1, 112, 112, 128]             
Conv2d-49                 [-1, 256, 112, 112]          
GELU-50                   [-1, 256, 112, 112]               
Conv2d-51                 [-1, 256, 112, 112]          
GELU-52                   [-1, 256, 112, 112]               
Conv2d-53                 [-1, 128, 112, 112]         
MLP-54                    [-1, 128, 112, 112]               
DropPath-55               [-1, 128, 112, 112]             
Block-56                  [-1, 128, 112, 112]               
LayerNorm-57              [-1, 112, 112, 128]           
Conv2d-58                 [-1, 128, 112, 112]        
GELU-59                   [-1, 128, 112, 112]               
Conv2d-60                 [-1, 128, 112, 112]          
Conv2d-61                 [-1, 128, 112, 112]        
Conv2d-62                 [-1, 128, 112, 112]          
ConvMod-63                [-1, 128, 112, 112]               
DropPath-64               [-1, 128, 112, 112]               
LayerNorm-65              [-1, 112, 112, 128]            
Conv2d-66                 [-1, 256, 112, 112]          
GELU-67                   [-1, 256, 112, 112]               
Conv2d-68                 [-1, 256, 112, 112]           
GELU-69                   [-1, 256, 112, 112]               
Conv2d-70                 [-1, 128, 112, 112]          
MLP-71                    [-1, 128, 112, 112]               
DropPath-72               [-1, 128, 112, 112]               
Block-73                  [-1, 128, 112, 112]               
GroupNorm-74              [-1, 128, 112, 112]            
Conv2d-75                 [-1, 256, 56, 56]         
BaseLayer-76              [-1, 256, 56, 56]               
LayerNorm-77              [-1, 56, 56, 256]             
Conv2d-78                 [-1, 256, 56, 56]          
GELU-79                   [-1, 256, 56, 56]               
Conv2d-80                 [-1, 256, 56, 56]         
Conv2d-81                 [-1, 256, 56, 56]          
Conv2d-82                 [-1, 256, 56, 56]          
ConvMod-83                [-1, 256, 56, 56]               
DropPath-84               [-1, 256, 56, 56]               
LayerNorm-85              [-1, 56, 56, 256]            
Conv2d-86                 [-1, 512, 56, 56]      
GELU-87                   [-1, 512, 56, 56]               
Conv2d-88                 [-1, 512, 56, 56]           
GELU-89                   [-1, 512, 56, 56]               
Conv2d-90                 [-1, 256, 56, 56]        
MLP-91                    [-1, 256, 56, 56]               
DropPath-92               [-1, 256, 56, 56]               
Block-93                  [-1, 256, 56, 56]               
LayerNorm-94              [-1, 56, 56, 256]            
Conv2d-95                 [-1, 256, 56, 56]         
GELU-96                   [-1, 256, 56, 56]               
Conv2d-97                 [-1, 256, 56, 56]          
Conv2d-98                 [-1, 256, 56, 56]          
Conv2d-99                 [-1, 256, 56, 56]          
ConvMod-100               [-1, 256, 56, 56]               
DropPath-101              [-1, 256, 56, 56]               
LayerNorm-102             [-1, 56, 56, 256]             
Conv2d-103                [-1, 512, 56, 56]         
GELU-104                  [-1, 512, 56, 56]               
Conv2d-105                [-1, 512, 56, 56]           
GELU-106                  [-1, 512, 56, 56]               
Conv2d-107                [-1, 256, 56, 56]        
MLP-108                   [-1, 256, 56, 56]             
DropPath-109              [-1, 256, 56, 56]             
Block-110                 [-1, 256, 56, 56]           
LayerNorm-111             [-1, 56, 56, 256]           
Conv2d-112                [-1, 256, 56, 56]          
GELU-113                  [-1, 256, 56, 56]             
Conv2d-114                [-1, 256, 56, 56]       
Conv2d-115                [-1, 256, 56, 56]         
Conv2d-116                [-1, 256, 56, 56]          
ConvMod-117               [-1, 256, 56, 56]               
DropPath-118              [-1, 256, 56, 56]              
LayerNorm-119             [-1, 56, 56, 256]           
Conv2d-120                [-1, 512, 56, 56]        
GELU-121                  [-1, 512, 56, 56]               
Conv2d-122                [-1, 512, 56, 56]           
GELU-123                  [-1, 512, 56, 56]               
Conv2d-124                [-1, 256, 56, 56]        
MLP-125                   [-1, 256, 56, 56]               
DropPath-126              [-1, 256, 56, 56]               
Block-127                 [-1, 256, 56, 56]               
LayerNorm-128             [-1, 56, 56, 256]            
Conv2d-129                [-1, 256, 56, 56]          
GELU-130                  [-1, 256, 56, 56]               
Conv2d-131                [-1, 256, 56, 56]          
Conv2d-132                [-1, 256, 56, 56]          
Conv2d-133                [-1, 256, 56, 56]          
ConvMod-134               [-1, 256, 56, 56]               
DropPath-135              [-1, 256, 56, 56]               
LayerNorm-136             [-1, 56, 56, 256]             
Conv2d-137                [-1, 512, 56, 56]         
GELU-138                  [-1, 512, 56, 56]               
Conv2d-139                [-1, 512, 56, 56]           
GELU-140                  [-1, 512, 56, 56]               
Conv2d-141                [-1, 256, 56, 56]         
MLP-142                   [-1, 256, 56, 56]               
DropPath-143              [-1, 256, 56, 56]               
Block-144                 [-1, 256, 56, 56]               
LayerNorm-145             [-1, 56, 56, 256]             
Conv2d-146                [-1, 256, 56, 56]          
GELU-147                  [-1, 256, 56, 56]               
Conv2d-148                [-1, 256, 56, 56]          
Conv2d-149                [-1, 256, 56, 56]          
Conv2d-150                [-1, 256, 56, 56]         
ConvMod-151               [-1, 256, 56, 56]               
DropPath-152              [-1, 256, 56, 56]               
LayerNorm-153             [-1, 56, 56, 256]            
Conv2d-154                [-1, 512, 56, 56]         
GELU-155                  [-1, 512, 56, 56]              
Conv2d-156                [-1, 512, 56, 56]           
GELU-157                  [-1, 512, 56, 56]               
Conv2d-158                [-1, 256, 56, 56]         
MLP-159                   [-1, 256, 56, 56]               
DropPath-160              [-1, 256, 56, 56]              
Block-161                 [-1, 256, 56, 56]               
LayerNorm-162             [-1, 56, 56, 256]            
Conv2d-163                [-1, 256, 56, 56]          
GELU-164                  [-1, 256, 56, 56]               
Conv2d-165                [-1, 256, 56, 56]         
Conv2d-166                [-1, 256, 56, 56]          
Conv2d-167                [-1, 256, 56, 56]          
ConvMod-168               [-1, 256, 56, 56]               
DropPath-169              [-1, 256, 56, 56]               
LayerNorm-170             [-1, 56, 56, 256]            
Conv2d-171                [-1, 512, 56, 56]        
GELU-172                  [-1, 512, 56, 56]               
Conv2d-173                [-1, 512, 56, 56]          
GELU-174                  [-1, 512, 56, 56]               
Conv2d-175                [-1, 256, 56, 56]         
MLP-176                   [-1, 256, 56, 56]               
DropPath-177              [-1, 256, 56, 56]               
Block-178                 [-1, 256, 56, 56]               
LayerNorm-179             [-1, 56, 56, 256]           
Conv2d-180                [-1, 256, 56, 56]          
GELU-181                  [-1, 256, 56, 56]             
Conv2d-182                [-1, 256, 56, 56]         
Conv2d-183                [-1, 256, 56, 56]         
Conv2d-184                [-1, 256, 56, 56]         
ConvMod-185               [-1, 256, 56, 56]               
DropPath-186              [-1, 256, 56, 56]               
LayerNorm-187             [-1, 56, 56, 256]             
Conv2d-188                [-1, 512, 56, 56]         
GELU-189                  [-1, 512, 56, 56]               
Conv2d-190                [-1, 512, 56, 56]           
GELU-191                  [-1, 512, 56, 56]               
Conv2d-192                [-1, 256, 56, 56]         
MLP-193                   [-1, 256, 56, 56]               
DropPath-194              [-1, 256, 56, 56]               
Block-195                 [-1, 256, 56, 56]               
LayerNorm-196             [-1, 56, 56, 256]             
Conv2d-197                [-1, 256, 56, 56]          
GELU-198                  [-1, 256, 56, 56]               
Conv2d-199                [-1, 256, 56, 56]          
Conv2d-200                [-1, 256, 56, 56]          
Conv2d-201                [-1, 256, 56, 56]         
ConvMod-202               [-1, 256, 56, 56]               
DropPath-203              [-1, 256, 56, 56]               
LayerNorm-204             [-1, 56, 56, 256]            
Conv2d-205                [-1, 512, 56, 56]         
GELU-206                  [-1, 512, 56, 56]               
Conv2d-207                [-1, 512, 56, 56]           
GELU-208                  [-1, 512, 56, 56]               
Conv2d-209                [-1, 256, 56, 56]         
MLP-210                   [-1, 256, 56, 56]               
DropPath-211              [-1, 256, 56, 56]               
Block-212                 [-1, 256, 56, 56]               
GroupNorm-213             [-1, 256, 56, 56]            
Conv2d-214                [-1, 512, 28, 28]         
BaseLayer-215             [-1, 512, 28, 28]            
LayerNorm-216             [-1, 28, 28, 512]           
Conv2d-217                [-1, 512, 28, 28]         
GELU-218                  [-1, 512, 28, 28]               
Conv2d-219                [-1, 512, 28, 28]          
Conv2d-220                [-1, 512, 28, 28]        
Conv2d-221                [-1, 512, 28, 28]        
ConvMod-222               [-1, 512, 28, 28]               
DropPath-223              [-1, 512, 28, 28]               
LayerNorm-224             [-1, 28, 28, 512]           
Conv2d-225                [-1, 1024, 28, 28]         
GELU-226                  [-1, 1024, 28, 28]               
Conv2d-227                [-1, 1024, 28, 28]          
GELU-228                  [-1, 1024, 28, 28]               
Conv2d-229                [-1, 512, 28, 28]         
MLP-230                   [-1, 512, 28, 28]          
DropPath-231              [-1, 512, 28, 28]           
Block-232                 [-1, 512, 28, 28]            
LayerNorm-233             [-1, 28, 28, 512]       
Conv2d-234                [-1, 512, 28, 28]        
GELU-235                  [-1, 512, 28, 28]               
Conv2d-236                [-1, 512, 28, 28]          
Conv2d-237                [-1, 512, 28, 28]      
Conv2d-238                [-1, 512, 28, 28]         
ConvMod-239               [-1, 512, 28, 28]         
DropPath-240              [-1, 512, 28, 28]           
LayerNorm-241             [-1, 28, 28, 512]        
Conv2d-242                [-1, 1024, 28, 28]        
GELU-243                  [-1, 1024, 28, 28]          
Conv2d-244                [-1, 1024, 28, 28]    
GELU-245                  [-1, 1024, 28, 28]            
Conv2d-246                [-1, 512, 28, 28]        
MLP-247                   [-1, 512, 28, 28]           
DropPath-248              [-1, 512, 28, 28]            
Block-249                 [-1, 512, 28, 28]        
BaseLayer-250             [-1, 512, 28, 28]         
LayerNorm-251             [-1, 28, 28, 512]       
AdaptiveAvgPool2d-252     [-1, 512, 1, 1]      
Linear-253                [-1, 4]      
================================================================
"""
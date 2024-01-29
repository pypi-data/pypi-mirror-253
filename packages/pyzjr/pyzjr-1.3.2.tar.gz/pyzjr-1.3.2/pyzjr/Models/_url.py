# 预训练模型地址

from torch.hub import load_state_dict_from_url

model_urls = {
    'vgg16_bn': 'https://download.pytorch.org/models/vgg16_bn-6c64b313.pth',
    'vgg19_bn': 'https://download.pytorch.org/models/vgg19_bn-c79401a0.pth',
    'resnet18': 'https://download.pytorch.org/models/resnet18-5c106cde.pth',
    'resnet34': 'https://download.pytorch.org/models/resnet34-333f7ec4.pth',
    'resnet50': 'https://download.pytorch.org/models/resnet50-19c8e357.pth',
    'resnet101': 'https://download.pytorch.org/models/resnet101-5d3b4d8f.pth',
    'resnet152': 'https://download.pytorch.org/models/resnet152-b121ed2d.pth',
    'alexnet': 'https://download.pytorch.org/models/alexnet-owt-4df8aa71.pth',
    'se_resnet50': 'https://github.com/moskomule/senet.pytorch/releases/download/archive/seresnet50-60a8950a85b2b.pkl',
    'googlenet': 'https://download.pytorch.org/models/googlenet-1378be20.pth',
}

def download_from_url(name="resnet50", model_dir=None, progress=True):
    if model_dir is None:
        model_dir = './model_weight'
    load_state_dict_from_url(model_urls[name], model_dir=model_dir, progress=progress)

if __name__=="__main__":
    name = "googlenet"

    model_dir = "D:\PythonProject\Crack_classification_training_script\model_weight"
    download_from_url(name=name, model_dir=model_dir)
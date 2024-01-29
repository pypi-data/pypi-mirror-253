import math

def autopad(kernel, padding=None, dilation=1):
    """自动计算填充大小，以使输出具有与输入相同的形状
    :param k: kernel
    :param p: padding
    :param d: dilation
    :return: 自动计算得到的填充大小
    """
    k, p, d = kernel, padding, dilation
    if d > 1:
        k = d * (k - 1) + 1 if isinstance(k, int) else [d * (x - 1) + 1 for x in k]  # actual kernel-size
    if p is None:
        p = k // 2 if isinstance(k, int) else [x // 2 for x in k]  # auto-pad
    return p

def convpool_outsize(input_size, kernel_size, stride, padding, is_conv=True, ceil_mode=False):
    """
    计算卷积或池化的输出尺寸。
    Parameters:
        input_size (tuple): 输入尺寸，格式为 (height, width, channels)
        kernel_size (int or tuple): 卷积核或池化核的尺寸，如果是 int，表示高宽相同的正方形核
        stride (int): 步幅
        padding (int): 填充大小
        is_conv (bool): 是否是卷积操作，如果是 True，使用卷积输出尺寸的计算公式；否则使用池化输出尺寸的计算公式

    Returns:
        output_size (tuple): 输出尺寸，格式为 (height, width, channels)。
    """
    if isinstance(kernel_size, int):
        kernel_size = (kernel_size, kernel_size)

    h_in, w_in, c = input_size
    h_k, w_k = kernel_size

    if is_conv:
        h_out = ((h_in + 2 * padding - h_k) // stride) + 1
        w_out = ((w_in + 2 * padding - w_k) // stride) + 1
    else:
        h_out = ((h_in - h_k) // stride) + 1
        w_out = ((w_in - w_k) // stride) + 1
    if ceil_mode:
        h_out, w_out = math.ceil(h_out),math.ceil(w_out)
    return h_out, w_out, c

if __name__=="__main__":
    input_size = (112, 112, 64)
    kernel_size = 3
    stride = 2
    padding = 3
    conv_output_size = convpool_outsize(input_size, kernel_size, stride, padding, is_conv=True)
    print("卷积输出尺寸:", conv_output_size)
    pool_output_size = convpool_outsize(input_size, kernel_size, stride, padding, is_conv=False)
    print("池化输出尺寸:", pool_output_size)

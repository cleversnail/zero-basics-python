# 105-image-info.py —— 第 14 章 · 第 105 讲示例
# 对应 PPT 课后作业：打开任意一张图片，输出它的「大小信息」和「数字信息」。
#
# 只依赖 Pillow + numpy，不需要摄像头、也不需要 OpenCV。
# （正文中本章统一按「未实跑」标注：第 14 章的主体是摄像头 + OpenCV。）

# 用 try/except 包住 import：读者机器上缺依赖也不会崩溃，而是给出安装提示。
try:
    from PIL import Image
    import numpy as np
except ImportError:
    print("未实跑：本机缺少 Pillow / numpy，无法读取图片。")
    print("安装命令：pip3.9 install pillow numpy")
    raise SystemExit(0)

# 1) 打开同目录下的 cat.png（Image.open 只把文件读进内存，不会真的解码全部像素）
img = Image.open("./cat.png")

# 2) 图片的「大小信息」：（宽, 高），单位是像素
print("图片尺寸（宽, 高）：", img.size)

# 3) 颜色模式：RGB 表示每个像素由「红绿蓝」三个 0-255 的数字组成
print("颜色模式：", img.mode)

# 4) 把图片转成 NumPy 数组：形状 = 高 × 宽 × 通道数，每个数字是 0-255 的像素值
arr = np.array(img)
print("数组形状（高, 宽, 通道）：", arr.shape)

# 5) 打印左上角第一个像素点的 RGB 值，直观感受「图片就是一堆数字」
print("左上角第 1 个像素的 RGB 值：", arr[0, 0])

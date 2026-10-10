# cvtest.py —— 第 14 章 · 第 106 讲示例（OpenCV 读取、标注并保存图片）
#
# 原始课程代码用 cv2.imshow() 弹窗显示图片，必须有人盯着屏幕按任意键才结束；
# 本文件把「显示」这一步换成 cv2.imwrite() 存成图片文件，
# 这样在没有图形界面的终端环境里也能真正跑通（本机已实测）。
#
# 本机实测环境：Python 3.12.7 + opencv-python 4.11.0（本机未装 opencv-contrib-python）。

# 用 try/except 包住 import：即使读者机器上没有装 OpenCV，
# 直接 `python3 cvtest.py` 也不会因缺少 cv2 而报错崩溃，而是打印一句友好提示。
try:
    import cv2
except ImportError:
    print("未实跑：本机没有安装 opencv-python，无法运行本示例。")
    print("安装命令：pip3.9 install opencv-python")
    raise SystemExit(0)

# 1) 读取同目录下的 cat.png（返回的是一个 NumPy 数组：高 × 宽 × 3 个颜色通道）
pic = cv2.imread("./cat.png")

# 2) 用矩形框标注图片：左上角 (70, 90)，右下角 (170, 190)，红色，线宽 2
cv2.rectangle(pic, (70, 90), (170, 190), color=(0, 0, 255), thickness=2)

# 3) 保存标注后的图片（原始代码这里是 cv2.imshow('title', pic)）
cv2.imwrite("./cat_marked.png", pic)

print("已保存标注后的图片：cat_marked.png")
print("图片尺寸（高, 宽, 通道数）：", pic.shape)

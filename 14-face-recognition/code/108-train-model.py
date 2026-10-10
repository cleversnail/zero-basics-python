# 108-train-model.py —— 第 14 章 · 第 108 讲示例
# 训练人脸模型：读取 ./imgdata/ 里的训练图片，提取人脸特征，训练出 trainer/trainer.yml。
#
# 本节为说明，未实跑：需要「训练图片 + opencv-contrib-python（LBPH 算法在 contrib 包里）」，
# 本机只装了 opencv-python（没有 cv2.face 模块），故未真正执行。
# 代码与课程仓库 face_demo/face_train.py 一致。

import os
from pathlib import Path

try:
    import cv2 as cv
    from PIL import Image
    import numpy as np
except ImportError:
    print("未实跑：本机缺少 opencv-python / Pillow / numpy，无法运行本示例。")
    print("安装命令：pip3.9 install opencv-python pillow numpy")
    raise SystemExit(0)

# 人脸分类器文件（OpenCV 自带）。注意：要按你本机的实际安装路径改这一行。
HAAR_FILE = ("/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/"
             "site-packages/cv2/data/haarcascade_frontalface_default.xml")


def getImageAndLabel(path):
    """遍历目录下所有图片，提取每张图里人脸的像素块和对应标签。"""
    facesSamples = []   # 存每张人脸切出来的像素数组
    ids = []            # 存每个人脸对应的标签号

    # 加载人脸分类器（Haar 级联）
    face_detect = cv.CascadeClassifier(HAAR_FILE)

    # rglob("*") 会递归遍历 path 目录下的所有文件
    for imagePath in Path(path).rglob("*"):
        # 用灰度（L 模式）打开照片——灰度图更适合提取人脸特征
        PIL_img = Image.open(imagePath).convert('L')
        # 转成 OpenCV / NumPy 能识别的数组（0-255 的整数）
        img_numpy = np.array(PIL_img, 'uint8')
        # 检测这张图里的人脸，返回若干个 (x, y, w, h) 坐标框
        faces = face_detect.detectMultiScale(img_numpy)
        # 文件名形如 1_Boss_1.jpg，用 "_" 切分后第 0 段就是标签号
        id = int(imagePath.stem.split("_")[0])
        # 防止把「没检测到人脸」的图也当成训练数据
        for x, y, w, h in faces:
            ids.append(id)
            facesSamples.append(img_numpy[y:y + h, x:x + w])
    return facesSamples, ids


def main():
    # 1) 读取全部训练数据
    faces, ids = getImageAndLabel('imgdata')

    # 2) 创建 LBPH 人脸识别器（属于 opencv-contrib-python）
    recognizer = cv.face.LBPHFaceRecognizer_create()

    # 3) 用「人脸像素 + 标签」训练模型
    recognizer.train(faces, np.array(ids))

    # 4) 把训练好的模型存成 YAML 文件，供后面识别时加载
    recognizer.write('trainer/trainer.yml')
    print("训练完成，模型已保存到 trainer/trainer.yml")


if __name__ == "__main__":
    # 本节属于「未实跑」范围：默认只打印说明。
    # 在装好 opencv-contrib-python、且 ./imgdata/ 里已放好训练图片的电脑上，
    # 先执行 export RUN_FACE_DEMO=1 再运行本脚本即可真跑。
    if os.environ.get("RUN_FACE_DEMO") == "1":
        main()
    else:
        print("本节为说明，未实跑（需摄像头 + opencv-contrib-python 环境）。")
        print("需要先安装 opencv-contrib-python（提供 cv2.face）并准备好训练图片 imgdata/。")
        print("在满足条件的电脑上，先执行 export RUN_FACE_DEMO=1，再运行本脚本。")

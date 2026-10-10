import cv2 as cv
from PIL import Image
import numpy as np
from pathlib import Path

def getImageAndLabel(path):
    facesSamples = []
    ids = []
    
    #调用人脸分类器（注意自己文件保存的路径，英文名）
    face_detect = cv.CascadeClassifier('/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    #循环读取照片人脸数据
    for imagePath in Path(path).rglob("*"):
        #用灰度的方式打开照片
        PIL_img = Image.open(imagePath).convert('L')
        #将照片转换为计算机能识别的数组OpenCV（BGR--0-255）
        img_numpy = np.array(PIL_img,'uint8')
        #提取图像中人脸的特征值
        faces = face_detect.detectMultiScale(img_numpy)
        #将文件名按“.”进行分割
        id = int(imagePath.stem.split("_")[0])
        # 防止无人脸图像
        for x,y,w,h in faces:
            ids.append(id)
            facesSamples.append(img_numpy[y:y+h,x:x+w])
    return facesSamples,ids


faces, ids = getImageAndLabel('imgdata')

#调用LBPH算法对人脸数据进行处理
recognizer = cv.face.LBPHFaceRecognizer_create()

#训练数据
recognizer.train(faces, np.array(ids))

recognizer.write('trainer/trainer.yml')

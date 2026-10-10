import os
import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from pathlib import Path

# 加载训练数据
recogizer=cv2.face.LBPHFaceRecognizer_create()
recogizer.read('trainer/trainer.yml')

names=["Boss"] # 名字
idn = [1] # 标签

# 识别图片
def face_detect_demo(img):

    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # 调用人脸分类器
    face_detector = cv2.CascadeClassifier('/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    
    # 读取人脸特征并返回人脸坐标
    face=face_detector.detectMultiScale(gray,1.1,5,0,(100,100),(800,800))
    for x,y,w,h in face:
        # 标记人脸
        cv2.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
        # 识别人脸
        ids, confidence = recogizer.predict(gray[y:y + h, x:x + w])
        if confidence > 60:
            print("陌生人")
        else:
            print("老板来了，自动关闭游戏")
    cv2.imshow('result', img)


cap=cv2.VideoCapture(0)

while True:
    flag,frame=cap.read()
    if not flag:
        break
    face_detect_demo(frame)
    if ord(' ') == cv2.waitKey(10):
        break
cv2.destroyAllWindows()
cap.release()
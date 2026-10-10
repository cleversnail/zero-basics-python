# 109-face-recognize.py —— 第 14 章 · 第 109 讲示例
# 设计人脸识别系统：加载训练好的模型，用摄像头实时识别人脸。
#
# 本节为说明，未实跑：需要「摄像头 + opencv-contrib-python」，本机均不具备，故未真正执行。
# 代码与课程仓库 face_demo/face_detect.py 一致。

import os

try:
    import cv2
except ImportError:
    print("未实跑：本机没有安装 opencv-python，无法运行本示例。")
    print("安装命令：pip3.9 install opencv-python")
    raise SystemExit(0)

# 人脸分类器文件（OpenCV 自带）。注意：要按你本机的实际安装路径改这一行。
HAAR_FILE = ("/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/"
             "site-packages/cv2/data/haarcascade_frontalface_default.xml")

names = ["Boss"]   # 标签号 -> 名字 的映射
idn = [1]          # 标签号列表


def face_detect_demo(img, recogizer):
    """在一帧图像里检测人脸，并逐个判断是谁。"""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 加载人脸分类器
    face_detector = cv2.CascadeClassifier(HAAR_FILE)
    # 检测人脸：scaleFactor=1.1，minNeighbors=5，人脸最小/最大尺寸限定范围
    face = face_detector.detectMultiScale(gray, 1.1, 5, 0, (100, 100), (800, 800))
    for x, y, w, h in face:
        # 用红色矩形把人脸框出来
        cv2.rectangle(img, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)
        # 把这张人脸交给识别器判断：ids 是预测标签，confidence 是可信度（越小越像）
        ids, confidence = recogizer.predict(gray[y:y + h, x:x + w])
        if confidence > 60:
            print("陌生人")
        else:
            print("老板来了，自动关闭游戏")
    cv2.imshow('result', img)


def main():
    # 读取训练好的模型
    recogizer = cv2.face.LBPHFaceRecognizer_create()
    recogizer.read('trainer/trainer.yml')

    # 打开默认摄像头
    cap = cv2.VideoCapture(0)
    while True:
        flag, frame = cap.read()
        if not flag:
            break
        face_detect_demo(frame, recogizer)
        # 每 10 毫秒刷新，按空格退出
        if ord(' ') == cv2.waitKey(10):
            break
    cv2.destroyAllWindows()
    cap.release()


if __name__ == "__main__":
    # 本节属于「未实跑」范围：默认只打印说明，不真正打开摄像头。
    # 在接好摄像头、装好 opencv-contrib-python 且已生成 trainer/trainer.yml 的电脑上，
    # 先执行 export RUN_FACE_DEMO=1 再运行本脚本即可真跑。
    if os.environ.get("RUN_FACE_DEMO") == "1":
        main()
    else:
        print("本节为说明，未实跑（需摄像头 + opencv-contrib-python 环境）。")
        print("需要摄像头、opencv-contrib-python（cv2.face）以及已训练好的 trainer/trainer.yml。")
        print("在满足条件的电脑上，先执行 export RUN_FACE_DEMO=1，再运行本脚本。")

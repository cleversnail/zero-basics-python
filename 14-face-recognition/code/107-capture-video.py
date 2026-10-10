# 107-capture-video.py —— 第 14 章 · 第 107 讲示例
# 用 OpenCV 采集摄像头视频信号：按 s 截图保存到 ./imgdata/，按空格退出。
#
# 本节为说明，未实跑：需要「摄像头 + opencv-python」环境，本机没有摄像头，
# 也没有运行图形界面，故未真正执行。代码与课程仓库 face_demo/face_cap.py 一致。

try:
    import cv2 as cv
except ImportError:
    print("未实跑：本机没有安装 opencv-python，无法运行本示例。")
    print("安装命令：pip3.9 install opencv-python")
    raise SystemExit(0)

import os


def main():
    # VideoCapture() 不带参数：打开默认摄像头（编号 0 的那一个）
    cap = cv.VideoCapture()
    num = 1               # 截图序号
    face_name = "Boss"    # 这个人脸的标签名
    face_id = 1           # 这个人脸的标签号

    # 只要摄像头打开成功，就一直循环读帧
    while cap.isOpened():
        # 读一帧：ret_flag 表示读成功没有，vshow 是这一帧的图像数据
        ret_flag, vshow = cap.read()
        # 把这一帧显示到名为 capture_test 的窗口里
        cv.imshow("capture_test", vshow)
        # 每 1 毫秒刷新一次，并读取键盘按键
        k = cv.waitKey(1) & 0xff

        if k == ord('s'):
            # 按 s：把当前这一帧编码成 jpg 并写入磁盘
            cv.imencode(".jpg", vshow)[1].tofile(
                f"./imgdata/{str(face_id)}_{face_name}_{str(num)}.jpg")
            print(f"成功保存第{str(num)}张照片")
            num += 1
        elif k == ord(' '):
            # 按空格：退出循环
            break

    # 关闭摄像头、销毁所有窗口
    cap.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    # 本节属于「未实跑」范围：默认只打印说明，不真正打开摄像头。
    # 在你自己接好摄像头、装好 opencv-python 的电脑上，
    # 先执行 export RUN_FACE_DEMO=1 再运行本脚本即可真跑。
    if os.environ.get("RUN_FACE_DEMO") == "1":
        main()
    else:
        print("本节为说明，未实跑（需摄像头 + opencv-contrib-python 环境）。")
        print("在接好摄像头、装好 opencv-python 的电脑上，")
        print("先执行 export RUN_FACE_DEMO=1，再运行 python3 107-capture-video.py。")

# 第 14 章 · 计算机视觉：使用 Python 进行人脸识别

> 让程序「看见」人脸：从一张图片就是一堆数字说起，用 OpenCV 一步步做出人脸检测、模型训练与实时识别。
> **本章 6 讲（105–110）**

## 🎯 本章目标

- 说清人脸识别的**原理**与**一般步骤**（灰度 → 检测 → 训练特征库 → 比对）
- 认识人脸识别常用的 Python 库（OpenCV / TensorFlow / PyTorch），知道各自适合什么场景
- 用 OpenCV 完成图片的**读取、显示、保存、矩形标注**
- 用 OpenCV **采集摄像头视频信号**并截图、读 MP4 文件
- 理解**训练人脸模型**的三步：读取训练图片 → 加载分类器 → 提取人脸特征
- 搭出一个能实时识别的人脸识别系统，并根据 `confidence` 判断「是谁」

**本章代码**

> 📌 **代码约定**：正文代码块都保持**可直接运行**；节选会明确标注「节选」并指向 `code/` 完整文件。

> ⚠️ **本章实跑尺度（务必先读）**：人脸识别需要**摄像头 + `opencv-contrib-python`** 环境。
> 本章绝大部分示例属于**「未实跑」**——只讲原理、给出完整代码，**不提供编造的运行输出**。
> 仅有下面两处是**本机真跑**的（因为它们不需要摄像头）：
> 1. `code/cvtest.py`：在一张猫图上画矩形并**保存为图片文件**（把原版的 `imshow` 换成了 `imwrite`）；
> 2. `code/105-image-info.py`：只用 `Pillow` 读图片、打印尺寸与像素信息。
>
> 其余示例（采集视频、训练模型、实时识别）一律标注「本节为说明，未实跑（需摄像头 + opencv-contrib-python 环境）」。

| 文件 | 内容 |
| --- | --- |
| `code/105-image-info.py` | 第 105 讲：用 Pillow 打开图片，输出尺寸与像素信息（真跑，仅用 Pillow） |
| `code/cvtest.py` | 第 106 讲：用 OpenCV 读图、画矩形、保存为文件（真跑，需 opencv-python） |
| `code/107-capture-video.py` | 第 107 讲：采集摄像头视频信号并截图（未实跑，需摄像头） |
| `code/108-train-model.py` | 第 108 讲：读取训练图片、训练 LBPH 人脸模型（未实跑，需 opencv-contrib-python） |
| `code/109-face-recognize.py` | 第 109 讲：加载模型、实时识别人脸（未实跑，需摄像头 + opencv-contrib-python） |
| `code/face_demo/face_cap.py` | 课程仓库原始文件：采集摄像头截图 |
| `code/face_demo/face_train.py` | 课程仓库原始文件：训练人脸模型 |
| `code/face_demo/face_detect.py` | 课程仓库原始文件：实时人脸识别 |
| `code/face_demo/trainer/trainer.yml` | 课程仓库训练好的模型文件（LBPH 直方图数据） |
| `code/cat.png` | 示例图片（WebP 格式，1810×1081） |
| `code/required.txt` | 依赖清单（版本号） |

**依赖清单（`code/required.txt`）**

```
opencv-python==4.5.5.64
Pillow==9.1.1
opencv-contrib-python==4.5.5.64
numpy==1.22.3
```

> 💡 **为什么要用 Python 3.9？** OpenCV 对 Python 版本比较敏感：`opencv-python` / `opencv-contrib-python`
> 的这些版本在 **Python 3.9** 上最稳。课程配套用的是 3.9，所以本章统一建议用 **Python 3.9**
> （`pip3.9 install ...`），避免「装了却 `import cv2` 报错」这类版本坑。
>
> 其中 `opencv-contrib-python`（contrib = contributed，社区贡献的扩展包）**额外**提供了 `cv2.face`
> 模块，人脸识别的 LBPH 算法 `cv2.face.LBPHFaceRecognizer_create()` 就在这个扩展包里——只装
> `opencv-python` 是**找不到**它的。

---

## 第 105 讲 · 理论盘点：人脸识别的一般步骤

### 本节目标

理解「计算机为什么能识别人脸」，并记住人脸识别的**四个一般步骤**。

### 知识要点

**1. 人脸识别的原理**

计算机里的视频，本质上也**是一张张图片**；而图片是由**数字**组成的。既然是数字，就可以用**数学计算**去做图像识别。

人脸识别任务是图像识别的一个**子类**。图像识别可以拆成两个任务：

| 任务 | 干什么 | 本质 |
| --- | --- | --- |
| **图像检测** | 找出图像里有没有人脸、人脸在哪 | 一种**分类问题**（有 / 没有） |
| **图像对比** | 把检测出的人脸，和预先采集的人脸比相似程度 | 相似度计算 |

**2. 人脸识别的一般步骤**

1. 把图片**转换为灰度**（去掉颜色、只留明暗，特征更好提）
2. **识别图像中的人脸**（把脸的坐标框出来）
3. **训练特征库**：将特定的人脸标注好，存入特征库
4. **比对**目标图片（视频）：对目标里出现的人脸做判断，根据**相似程度**做后续处理

**3. 用 OpenCV 看图像的基本组成**

- 图像中的每一个**像素点**由三个元素组成，分别表示 **R、G、B** 三种颜色；
- 一张图片的宽和高，由很多个像素点组成；
- 像素点可以用数字表示，所以我们能用数学计算去处理图像。

> 💡 一句话：**「看见」这件事，在计算机里就是「算数字」。**

### 代码实操

对应 PPT 课后作业的代码。这里用 `Pillow` 打开一张图片，输出它的**大小信息**与**数字信息**：

`code/105-image-info.py`：

```python
# 105-image-info.py —— 第 14 章 · 第 105 讲示例
# 对应 PPT 课后作业：打开任意一张图片，输出它的「大小信息」和「数字信息」。
#
# 只依赖 Pillow + numpy，不需要摄像头、也不需要 OpenCV。

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
```

> ⚠️ 本章主体需要摄像头 + opencv-contrib-python 环境；但本示例**只用 `Pillow`、不涉及摄像头**，
> 属于本章可用「纯图片库」本地验证的例外，因此这里是**真跑**的（不是未实跑）。
> 在 `code/` 目录下执行 `python3 105-image-info.py`，本机实测输出：

```bash
$ python3 105-image-info.py
图片尺寸（宽, 高）： (1810, 1081)
颜色模式： RGB
数组形状（高, 宽, 通道）： (1081, 1810, 3)
左上角第 1 个像素的 RGB 值： [125  48   4]
```

读输出：图片是 **1810 × 1081** 像素；`RGB` 说明每个点由红绿蓝三个数字组成；
数组形状 `(1081, 1810, 3)` 里的 `3` 就是那三个颜色通道；左上角第一个点是 `[125 48 4]`（偏红棕）。
**这就是「图片 = 数字」最直观的证据。**

### 课后作业

请你使用本节课学习的 OpenCV 库，打开任意一张图片，输出这张图片的**大小信息**，并输出图片的**数字信息**。

> 参考答案（OpenCV 版）：
> ```python
> import cv2
> img = cv2.imread("./cat.png")   # 读入图片，返回一个 NumPy 数组
> print(img.shape)                # 形状：(高, 宽, 通道数)
> print(img[0, 0])                # 左上角第一个像素的 BGR 值
> ```
> 注意 OpenCV 读进来的颜色顺序是 **BGR**（蓝绿红），和 `Pillow` 的 RGB 正好相反——
> 这是新手最容易踩的坑之一。`code/105-image-info.py` 用的是 Pillow 的 RGB 版，效果等价。

---

## 第 106 讲 · 理论盘点：人脸识别常用的 Python 库有哪些？

### 本节目标

认识人脸识别的常用库，学会用 OpenCV 完成图片的**读取 / 显示 / 保存 / 标注**四件事。

### 知识要点

**1. 人脸识别的常用库**

| 方法路线 | 常用库 | 特点 |
| --- | --- | --- |
| **基于特征向量**（传统方法） | **OpenCV** | 上手快、依赖少，**更易验证和学习** |
| 基于 **CNN / HOG**（深度学习） | **TensorFlow、PyTorch** | 精度高，但训练成本大、门槛高 |

> 💡 本课程选 **OpenCV**：它比基于深度学习的库更容易验证、学习成本低，适合打基础。

**2. 用 OpenCV 读取和保存图片**

| 操作 | 函数 | 说明 |
| --- | --- | --- |
| 读取图片 | `cv2.imread(图片路径和名称)` | 返回一个 NumPy 数组 |
| 显示图片 | `cv2.imshow()` | 弹出一个窗口显示（需要有图形界面） |
| 保存图片 | `cv2.imwrite(路径, 图片)` | 把图片写到磁盘 |

**3. 用 OpenCV 标注图像**

标注图像常用于**调试时不断优化算法**，一般采用**矩形框**：

```python
cv2.rectangle(图片, 左上角坐标, 右下角坐标, color=颜色, thickness=线宽)
```

### 代码实操

课程示例 `cvtest.py` 打开一张猫图，在指定位置画一个红框。

> ⚠️ 原版 `cvtest.py` 用 `cv2.imshow()` + `cv2.waitKey(0)` 弹窗显示，**需要图形界面**，属未实跑。
> 我们把它改成 `cv2.imwrite()` **存成图片文件**（`imshow` 换成 `imwrite`），这样在没有界面的
> 终端里也能**真跑**。`code/cvtest.py`：

```python
# cvtest.py —— 第 14 章 · 第 106 讲示例（OpenCV 读取、标注并保存图片）
#
# 原始课程代码用 cv2.imshow() 弹窗显示图片，必须有人盯着屏幕按任意键才结束；
# 本文件把「显示」这一步换成 cv2.imwrite() 存成图片文件，
# 这样在没有图形界面的终端环境里也能真正跑通（本机已实测）。

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
```

在 `code/` 目录下执行 `python3 cvtest.py`，本机实测输出：

```bash
$ python3 cvtest.py
已保存标注后的图片：cat_marked.png
图片尺寸（高, 宽, 通道数）： (1081, 1810, 3)
```

同目录会生成 `cat_marked.png`（约 2.0 MB，1810×1081），就是那张被红框标注过的猫图。
**这一讲是本章少数「真跑」的示例之一。**

对照一下原始课程的写法（弹窗版，**未实跑**）：

```python
import cv2
pic = cv2.imread("./cat.png")
cv2.rectangle(pic,(70,90),(170,190),color=(0,0,255),thickness=2)
cv2.imshow('title',pic)     # 弹窗显示，需要有图形界面
cv2.waitKey(0)              # 等待按键，否则窗口一闪而过
cv2.destroyAllWindows()
```

> ⚠️ 本节为说明，未实跑（需摄像头 + opencv-contrib-python 环境）。
> `waitKey` 是 OpenCV 处理键盘/刷新窗口的关键：它让窗口「停住」等你看／按键。

### 课后作业

请你打开任意一张图片，并使用 `cv.rectangle()` 函数对图像进行标注，标注范围分别为
`50,50,50,50`、`100,100,100,100`，标注后保存图片，并查看标注后的图片。

> 参考答案（思路）：
> ```python
> import cv2
> pic = cv2.imread("./cat.png")
> # 第一个框：左上角 (50,50)，右下角 (100,100)
> cv2.rectangle(pic, (50, 50), (100, 100), color=(0, 0, 255), thickness=2)
> cv2.imwrite("./cat_marked2.png", pic)
> ```
> `rectangle` 的四个坐标按 `(左上角 x, 左上角 y, 右下角 x, 右下角 y)` 两两成对传入——
> 题面里的 `50,50,50,50` / `100,100,100,100` 指的是这两组坐标点的四个数。

---

## 第 107 讲 · 怎样通过 OpenCV 采集视频信号？

### 本节目标

学会用 OpenCV 采集**图片与视频信号**：转灰度、开摄像头截图、读 MP4 文件。

### 知识要点

**1. 采集图片并转为灰度**

- 转换为灰度的目的是**更好地提取特征**（颜色是干扰，明暗才是人脸结构的核心）；
- `cv.cvtColor(图片, 转换方式)` 用于颜色空间转换，比如 `cv.COLOR_BGR2GRAY`（BGR 转灰度）。

**2. 采集视频信号并保存图片**

要想识别特定的人脸，需要**训练** OpenCV 的模型；训练数据一般就是**从摄像头采集的截图**（也可以是事先准备好的图片）。

| 用途 | 函数 |
| --- | --- |
| 打开摄像头 | `cv.VideoCapture(0)` |
| 从摄像头截图并保存 | `cv.imencode(".jpg", 帧)[1].tofile(路径)` |

**3. 采集 MP4 视频**

`cv.VideoCapture()` 除了捕获摄像头，**还可以读取 MP4 格式的文件**（把参数换成文件路径即可）。
通过反复读取视频，可以不断优化 OpenCV 的模型。

### 代码实操

下面是课程仓库里的采集脚本 `face_demo/face_cap.py`（**完整代码**）：

```python
import cv2 as cv
# opencv
# pip3.9 install opencv-python
# pillow图像处理
# pip3.9 install pillow
# contrib 用于训练人脸模型的opencv扩展包
# pip3.9 install opencv-contrib-python
cap = cv.VideoCapture()
num = 1
face_name = "Boss"
face_id = 1

while (cap.isOpened()):
    #捕获摄像头图像
    ret_flag,vshow = cap.read()
    #显示捕获的照片
    cv.imshow("capture_test",vshow)
    #图像刷新的频率
    k = cv.waitKey(1)&0xff
    # 设置按键保存照片
    if k == ord('s'):
        # 保存图片
        cv.imencode(".jpg",vshow)[1].tofile(f"./imgdata/{str(face_id)}_{face_name}_{str(num)}.jpg")
        print(f"成功保存第{str(num)}张照片")
        num += 1
    elif k == ord(' '):
        break
# 关闭摄像
cap.release()
# 销毁窗口
cv.destroyAllWindows()
```

> ⚠️ 本节为说明，未实跑（需摄像头 + opencv-contrib-python 环境）。
> 它必须打开摄像头、还要弹窗显示，本机没有摄像头，也没有图形界面，因此**未真正执行**。
> 代码在 `code/face_demo/face_cap.py`，同时给出了带「未实跑开关」的可运行版
> `code/107-capture-video.py`（直接 `python3` 它会打印未实跑说明后干净退出，不会卡住）。

**读一读这段代码里的几个关键点：**

- `cv.VideoCapture()` 不带参数 = 打开**默认摄像头**；`cap.isOpened()` 为真才进入循环。
- `cap.read()` 返回两个值：`ret_flag`（这一帧读成功没有）和 `vshow`（图像数据）。
- `cv.waitKey(1) & 0xff` 返回按键编码：按 `s` 存一张截图，按**空格**退出。
- `cv.imencode(".jpg", vshow)[1].tofile(路径)` 把这一帧**编码成 jpg 并存盘**——
  文件名形如 `1_Boss_1.jpg`（标签号\_名字\_序号），这正是后面第 108 讲训练时要用的命名格式。

**扩展：把摄像头换成 MP4 文件**（读取本地视频，同样**未实跑**）：

```python
import cv2 as cv
# VideoCapture 的参数从「摄像头编号」换成「文件路径」，就能读 MP4
cap = cv.VideoCapture("./demo.mp4")
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:      # 读到视频末尾，ret 会变成 False
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)   # 逐帧转灰度
    cv.imshow("mp4", gray)
    if cv.waitKey(25) & 0xff == ord(' '):
        break
cap.release()
cv.destroyAllWindows()
```

> ⚠️ 本节为说明，未实跑（需摄像头 + opencv-contrib-python 环境）。

### 课后作业

请你使用 OpenCV 截取视频中**相同人物至少 10 张图片**，并将图片放入到一个文件夹中。

> 参考答案（思路）：把 `face_cap.py` 多按几次 `s`，或把上面的 MP4 循环里每一帧都
> `cv.imencode(".jpg", frame)[1].tofile(...)` 存下来，并按 `标签号_名字_序号.jpg` 命名、
> 统一放进 `imgdata/` 文件夹。**同一个人的多角度、多张照片**，能让后面训练的模型更准。

---

## 第 108 讲 · 如何训练人脸模型？

### 本节目标

理解训练人脸模型的三个关键动作：**读取训练图片 → 加载分类模型 → 提取人脸特征**。

### 知识要点

**1. 读取目录下全部训练文件**

训练图片一般放在一个文件夹里，需要**遍历目录**，把所有文件路径以字符串形式存进一个列表：

| 用途 | 函数 |
| --- | --- |
| 显示目录下所有文件 | `os.listdir()` |
| 连接「目录 + 文件名」 | `os.path.join()` |
| 递归遍历目录下所有文件 | `Path(path).rglob("*")` |

**2. 加载分类模型**

调用人脸分类器（Haar 级联分类器）：

```python
cv.CascadeClassifier(".../cv2/data/haarcascade_frontalface_default.xml")
```

这个人脸分类器的 XML 文件就在 OpenCV 安装目录的 `cv2/data/` 下，例如课程里的路径：

```
/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/cv2/data/haarcascade_frontalface_default.xml
```

> ⚠️ 别照抄路径！要用**你自己机器上**的实际安装路径。写代码时建议把它放进一个变量，方便替换。

**3. 提取人脸特征值**

图片被转换成数组之后，用特征提取函数把人脸特征提出来：

```python
face_detect.detectMultiScale(图片数组)
```

它会返回若干个 `(x, y, w, h)` —— 每张人脸的**左上角坐标**和**宽高**，据此可以把人脸从原图里「抠」出来。

### 代码实操

课程仓库里的训练脚本 `face_demo/face_train.py`（**完整代码**）：

```python
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
```

> ⚠️ 本节为说明，未实跑（需摄像头 + opencv-contrib-python 环境）。
> 本机只装了 `opencv-python`，**没有** `cv2.face` 模块（它属于 `opencv-contrib-python`），
> 也没有准备好的 `imgdata/` 训练图片，因此**未真正执行**。
> 代码在 `code/face_demo/face_train.py`，可运行版见 `code/108-train-model.py`。

**三个关键动作，对应代码里的三处：**

| 步骤 | 代码 | 作用 |
| --- | --- | --- |
| 读取全部训练图片 | `for imagePath in Path(path).rglob("*")` | 递归遍历 `imgdata/` 下所有图片 |
| 加载分类模型 | `cv.CascadeClassifier(...)` | 加载 Haar 人脸分类器 |
| 提取人脸特征 | `face_detect.detectMultiScale(img_numpy)` | 拿到每张脸的 `(x, y, w, h)`，切片抠出人脸块 |

训练用的是 **LBPH** 算法（Local Binary Patterns Histograms，局部二值模式直方图），
`recognizer.train(faces, np.array(ids))` 把「人脸像素块」和「标签号」一起喂给模型，
最后 `recognizer.write('trainer/trainer.yml')` 把训练好的模型**存成 YAML 文件**——
就是 `code/face_demo/trainer/trainer.yml` 这个文件（第 109 讲要用它）。

> 💡 命名是关键：`imgdata/` 里的文件名必须是 `标签号_名字_序号.jpg`（如 `1_Boss_1.jpg`），
> 代码用 `imagePath.stem.split("_")[0]` 取第一段当标签号。**文件名格式错了，标签就错了。**

### 课后作业

请你使用 `http.server` 模块，将目录 `/tmp` 通过 HTTP 协议发布到 **8080 端口**，并通过浏览器验证是否发布成功。

> 参考答案：
> ```bash
> # 在终端里执行（Python 自带 http.server，无需额外安装）
> cd /tmp
> python3 -m http.server 8080
> # 然后在浏览器打开 http://localhost:8080
> ```
> 终端会打印每一条访问记录；浏览器能列出 `/tmp` 下的文件就说明发布成功。
> 按 `Ctrl + C` 停止服务。（服务器启动后需要浏览器验证，故此处仅给命令，未在文档中演示。）

---

## 第 109 讲 · 怎样设计人脸识别系统？

### 本节目标

把「分类器 + 训练好的模型」组装起来，做出一个能实时判断「是谁」的人脸识别系统。

### 知识要点

**1. 调用分类器和训练模型对图片进行人脸识别**

| 用途 | 函数 |
| --- | --- |
| 读取训练模型 | `recogizer.read(训练模型文件)` |
| 人脸识别 | `recogizer.predict(人脸像素块)` |

`predict()` 返回两个值：

- `ids`：预测出的**标签号**（这个人是谁）；
- `confidence`：**可信度**（越小说明越像、越有把握）。

**2. 通过标注优化参数**

默认模型往往识别效果不理想。**用人眼通过矩形框标注，观察识别是否准确**，再据此调整
`detectMultiScale` 的检测参数（如 `scaleFactor`、`minNeighbors`、人脸尺寸范围）和
判断阈值，逐步把系统调准。

### 代码实操

课程仓库里的识别脚本 `face_demo/face_detect.py`（**完整代码**）：

```python
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
```

> ⚠️ 本节为说明，未实跑（需摄像头 + opencv-contrib-python 环境）。
> 需要摄像头实时画面 + `cv2.face` 模块 + 已训练好的 `trainer/trainer.yml`，本机三项不全，**未真正执行**。
> 代码在 `code/face_demo/face_detect.py`，可运行版见 `code/109-face-recognize.py`。

**这段程序的工作流：**

1. `recogizer.read('trainer/trainer.yml')` —— 把第 108 讲训练好的模型读进来；
2. 每一帧先转灰度、用分类器 `detectMultiScale` 找出所有人脸坐标；
3. 对每张脸：`cv2.rectangle` 画红框，再 `predict` 判断是谁；
4. `confidence > 60` 就认为**不像**（打印「陌生人」），否则认为就是本人（打印「老板来了，自动关闭游戏」）——
   这就是「**基于概率进行人脸归属分类**」。

### 课后作业

请你用 OpenCV 实现特定人脸识别功能：识别用户为 **A** 时，终端输出 **用户 A**；识别出是其他用户时，输出**其他用户**。

> 参考答案（改判定逻辑）：
> ```python
> ids, confidence = recogizer.predict(gray[y:y + h, x:x + w])
> if confidence <= 60 and ids == 1:      # 像，且标签是 A（标签号 1 代表 A）
>     print("用户 A")
> else:
>     print("其他用户")
> ```
> 关键点：先看 `confidence`（够不够像），再看 `ids`（像的是哪一号）。
> `names` / `idn` 列表就是把「标签号」翻译成「人名」的字典，比如 `names[0] == "Boss"`。

---

## 第 110 讲 · 再回首：“计算机视觉”单元小结

### 本节目标

把整个「计算机视觉」单元串成一条线：**为什么能识别 → 用什么库 → 怎么采集 → 怎么训练 → 怎么识别**。

### 知识要点

**单元全景**

| 讲 | 主题 | 一句话 |
| --- | --- | --- |
| 105 | 人脸识别的一般步骤 | 图片 = 数字；检测（分类）+ 对比（相似度） |
| 106 | 常用库 | 传统用 OpenCV，深度学习用 TensorFlow / PyTorch |
| 107 | 采集视频信号 | 摄像头 / MP4 → 灰度 → 截图存成训练数据 |
| 108 | 训练人脸模型 | 读图片 → 加载分类器 → 提特征 → 存 `trainer.yml` |
| 109 | 设计识别系统 | 加载模型 → `predict` 得 `confidence` → 判定是谁 |

**贯穿全章的一条主线**

```
一张图片/一帧视频
      │  ① 转灰度 cvtColor
      ▼
   灰度图 ──② 检测人脸 detectMultiScale──► 若干 (x, y, w, h)
      │
      ├─③ 训练阶段：抠出人脸块 + 标签 → train() → trainer.yml
      │
      └─④ 识别阶段：抠出人脸块 → predict() → (ids, confidence) → 判定是谁
```

### 代码实操

本讲是单元小结，没有新代码。建议你把前几讲的脚本在**自己装了摄像头和
`opencv-contrib-python` 的电脑上**依次跑一遍，走通完整链路：

```bash
# 0) 准备环境（Python 3.9）
pip3.9 install -r required.txt

# 1) 采集训练图片（按 s 截图，按空格退出）→ imgdata/*.jpg
python3 face_demo/face_cap.py

# 2) 训练模型 → trainer/trainer.yml
python3 face_demo/face_train.py

# 3) 实时识别
python3 face_demo/face_detect.py
```

> ⚠️ 本节为说明，未实跑（需摄像头 + opencv-contrib-python 环境）。
> 以上三步都依赖摄像头与 `cv2.face`，本机均不具备，所以只在文档中给出命令，未执行。

### 课后作业

（PPT 本讲无新作业。）复习建议：

1. 用一句话解释「为什么计算机能识别人脸」；
2. 默写人脸识别的**四个一般步骤**；
3. 说清 `imread` / `imshow` / `imwrite` / `rectangle` 各干什么；
4. 说清训练模型三步与识别一步分别用到哪个函数。

---

## 本章小结

**速查表**

| 主题 | 关键函数 / 要点 |
| --- | --- |
| 读图片 | `cv2.imread(路径)`（返回 NumPy 数组，颜色为 BGR） |
| 显示图片 | `cv2.imshow(窗口名, 图片)`（需图形界面） |
| 保存图片 | `cv2.imwrite(路径, 图片)` |
| 画矩形 | `cv2.rectangle(img, (x1,y1), (x2,y2), color=(0,0,255), thickness=2)` |
| 转灰度 | `cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)` |
| 打开摄像头 | `cv2.VideoCapture(0)`（参数换成路径则读 MP4） |
| 截图存盘 | `cv2.imencode(".jpg", frame)[1].tofile(路径)` |
| 加载分类器 | `cv2.CascadeClassifier(".../haarcascade_frontalface_default.xml")` |
| 检测人脸 | `face_detector.detectMultiScale(gray, 1.1, 5, 0, (100,100), (800,800))` |
| 训练模型 | `cv2.face.LBPHFaceRecognizer_create()` → `train(faces, ids)` → `write("trainer/trainer.yml")` |
| 识别人脸 | `recogizer.read("trainer/trainer.yml")` → `predict(face)` → `(ids, confidence)` |
| 判定规则 | `confidence > 60` 判为「陌生人」，否则判为本人 |

**三句话**

1. 计算机「看见」人脸的底层，是**把图片当成数字做数学计算**。
2. 人脸识别 = **检测（找出脸在哪，分类问题）+ 对比（像不像，相似度）**。
3. 整条链路是：**采集 → 灰度 → 检测 → 训练 → 预测**，OpenCV 的 `cv2.face` 模块必须靠
   `opencv-contrib-python` 才有。

**动手练习**

1. 用 `Pillow` 打开任意一张图，打印它的尺寸和左上角像素（参考 `code/105-image-info.py`）。
2. 用 `cv2.rectangle()` 在图上画两个框并 `imwrite` 保存（参考 `code/cvtest.py`）。
3. 在自己电脑上装好 `opencv-contrib-python`，跑通「采集 → 训练 → 识别」三步。

---

## 下一章预告

第 15 章进入**物联网**：用 ESP32 开发板连网，讲清 **TCP / MQTT / 物模型**，
让 Python 程序去和真实硬件「对话」。

> ⚠️ 该章需要 ESP32 硬件，同样属于「未实跑」范畴，讲原理 + 给完整代码。

---

[← 上一章：Web 开发](/guide/web) ｜ [返回总目录](/) ｜ [下一章：物联网 →](/guide/iot)

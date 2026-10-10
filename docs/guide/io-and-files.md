# 第 5 章 · 输入输出与文件操作

> 程序不只是自己算，它还要「跟人打交道」：从键盘和命令行拿输入、把结果打印到屏幕、
> 把数据存进文件再读回来。本章讲的正是这条「数据进出的管道」。
> **本章 9 讲（040–048）**，从 `input()` 一路走到文件读写与合并。

## 🎯 本章目标

- 用 `input()` 接收键盘输入，并理解它返回的永远是**字符串**
- 用 `argparse` 处理**命令行参数**，实现非交互式输入
- 掌握三种格式化输出：百分号 `%`、`str.format()`、**f-strings**
- 用 `open()` 打开文件，说清 `mode`（r / w / a / b / +）与 `encoding` 的作用
- 理解**文件编码**与乱码的成因，会用 `encoding` 参数解决
- 会用 `read` / `readline` / `readlines` / `write` 读写文件，会用 `with` 自动关闭
- 综合运用读写，把**多个文件合并**成一个

**本章代码**

> 📌 **代码约定**：正文代码块都保持**可直接运行**；节选会明确标注「节选」并指向 `code/` 完整文件。
> 所有输出都是**真实运行结果**（本机 Python 3.12.7）。
> 本章 `input()` 属于**交互式**输入，没法在文档里真的敲键盘——正文会把 `input()` 注释掉、
> 用**固定值**代替，效果完全一致。

| 文件 | 内容 |
| --- | --- |
| `code/40-input.py` | `input()` 交互输入（固定值演示）+ 循环控制 |
| `code/40-args.py` | `argparse` 命令行参数：可选参数、类型转换、默认值 |
| `code/41-format-output.py` | 百分号 `%` 与 `str.format()` 两种格式化输出 |
| `code/42-fstrings.py` | f-strings：计算、宽度、精度 |
| `code/43-open.py` | `open()` 打开文件、`mode` 概念、文件对象信息 |
| `code/44-encoding.py` | 文件编码与乱码：GBK / UTF-8 对照 |
| `code/45-read-write.py` | 文件读写：`read`/`readline`/`readlines`/`write`/`tell`/`seek` |
| `code/46-close.py` | `close()` 与 `with` 语句 |
| `code/47-merge-files.py` | 合并多个文件 |
| `code/48-summary.py` | 本章综合小练习：输入→处理→输出→写文件→读回 |

> 📎 `code/` 里还随附课程素材文件：`demo.txt`、`demo1.txt`、`demo2.txt`、`demo3.txt`、
> `demo4.txt`、`demo_GBK.txt`。文件操作示例都基于它们，或**自己新建临时文件**，不依赖外部文件。

---

## 第 40 讲 · 输入：如何接收用户通过键盘输入的数据？

### 本节目标

分清「交互式输入」与「非交互式输入」，会用 `input()` 收键盘输入、会用 `argparse` 收命令行参数。

### 知识要点

**1. 输入设备与输入方式**

- 输入，泛指计算机与人的交互方式。从分层看包括：输入硬件设备 → 硬件设备驱动 → **虚拟设备**。
- Python 编程主要关注**虚拟设备**（终端、图形界面输入），本课程聚焦终端的两种输入：

| 方式 | 手段 | 特点 |
| --- | --- | --- |
| **交互式输入** | `input()` | 程序停下来等用户敲键盘 |
| **非交互式输入** | 命令行参数、文件 | 程序启动就拿到数据，不等人 |

**2. `input()` 函数**

```python
text = input("用户输入前的提示信息")
```

- 参数是**提示信息**（会先打印到屏幕上），返回值是用户敲入的那**一行**。
- ⚠️ 关键点：`input()` 返回的**永远是字符串**。想要数字，必须自己 `int()` / `float()` 转换。
- `input()` 常放在循环里，实现「按键驱动」（按 s 保存、按 l 读取、按 q 退出）。

**3. 命令行参数**

命令后面的东西都算参数，例如 `python3 -V`、`python3 a.py b.py c.py`。Python 用标准库解析它们：

| 库 | 风格 |
| --- | --- |
| `argparse` | 用户友好（本课程采用，需 Python 3.2+） |
| `getopt` | C 风格 |

固定套路：

```python
import argparse
parser = argparse.ArgumentParser(description="这个程序的用途")
parser.add_argument(要添加的参数和参数描述)
args = parser.parse_args()   # args 用于接收参数并处理
```

### 代码实操

**示例 A：`input()` 交互输入**

> ⚠️ 交互输入无法在文档里演示。`code/40-input.py` 里真正的 `input()` 被**注释掉**，
> 用等价的固定值代替；你本地把注释去掉，就能真的敲键盘了。

`code/40-input.py`（节选，完整见文件）：

```python
# 真正交互时这样写（程序会停下来等你输入）：
# name = input("请输入你的名字：")
# age = input("请输入你的年龄：")

# 文档演示：用固定值代替上面的键盘输入
name = "小明"
age = "18"

print(f"你好，{name}！")
print(f"你的年龄是 {age} 岁")

# input() 返回的永远是字符串，想要数字必须自己做类型转换
# num = int(input("请输入一个数字："))
num = int("7")            # 演示：等价于用户敲入了 7
print(f"你输入的数字 + 1 = {num + 1}")
print(f"转换后的类型是：{type(num)}")

# input() 也常放在循环里，实现「按键驱动」：输入 q / quit 就退出
# 真实的写法是：
#   while True:
#       cmd = input("请输入控制指令（q 退出）：")
#       if cmd == "q":
#           break
#       print("你输入的是：", cmd)
# 演示：用一串固定指令代替用户依次敲入的内容
commands = ["s", "l", "q", "x"]
for cmd in commands:
    if cmd == "q":
        print("收到 q，退出程序")
        break
    print(f"收到指令 {cmd}：执行对应操作")
```

运行：

```bash
$ python3 40-input.py
```

真实输出：

```
你好，小明！
你的年龄是 18 岁
你输入的数字 + 1 = 8
转换后的类型是：<class 'int'>
收到指令 s：执行对应操作
收到指令 l：执行对应操作
收到 q，退出程序
```

**示例 B：`argparse` 命令行参数**

`code/40-args.py`：

```python
import argparse

parser = argparse.ArgumentParser(description="这个程序用来演示命令行参数处理")

# 可选参数：名字前面带 -，不写时值为 None
parser.add_argument("-number", help="输入一个数字")

# 带类型转换和默认值的可选参数
parser.add_argument("-number1", type=int, default=10, help="第一个数字")
parser.add_argument("-number2", type=int, default=20, help="第二个数字")

# 解析参数；没有传参数时用默认值
args = parser.parse_args()

print(f"你输入的 number 参数是 {args.number}")
print(f"两数之和是 {args.number1 + args.number2}")
```

不传参数运行（`-number` 没有默认值 → `None`，后两个用默认值 10 / 20）：

```bash
$ python3 40-args.py
```

真实输出：

```
你输入的 number 参数是 None
两数之和是 30
```

传入参数运行：

```bash
$ python3 40-args.py -number 100 -number1 5 -number2 7
```

真实输出：

```
你输入的 number 参数是 100
两数之和是 12
```

> 💡 把「可选参数」前面的 `-` 去掉（如 `parser.add_argument("number", ...)`），它就变成**必选参数**，
> 不传会被 argparse 直接报错拦下。用 `type=int` 能强制转换类型，用 `default=` 能设默认值。

### 课后作业

编写一个程序，当用户输入 `q` 或 `quit` 时程序退出，否则一直等待用户输入。

```python
while True:
    cmd = input("请输入（q / quit 退出）：")
    if cmd in ("q", "quit"):
        print("再见！")
        break
    print("你输入的是：", cmd)
```

> 参考答案要点：用 `while True` 死循环持续等待；用 `if cmd in ("q", "quit")` 判断退出条件，
> `break` 跳出循环。`in` 可以一次判断多个值。

---

## 第 41 讲 · 格式化输出：如何将执行结果通过屏幕输出？

### 本节目标

掌握三种常用格式化输出的前两种——百分号 `%` 与 `str.format()`，并知道 `{}` 占位符的用法。

### 知识要点

**三种常用的格式化输出方式**

```python
# 1. 百分号 %
"%s is %s than %s" % ("Beautiful", "better", "ugly")

# 2. format() 函数
"{1} is {2} than {0}".format("ugly", "Beautiful", "better")
"{B} is {b} than {u}".format(u="ugly", B="Beautiful", b="better")

# 3. f-strings（下一讲细讲）
u = "ugly"; B = "Beautiful"; b = "better"
f"{B} is {b} than {u}"
```

**百分号方式**——用 `%` 定义格式和精度：

| 占位符 | 含义 |
| --- | --- |
| `%s` | 格式化字符串 |
| `%d` | 格式化整数 |
| `%f` | 浮点数 |

宽度/精度写在 `%` 和类型之间，例如 `%05.1f`（宽度 5、保留 1 位小数、左补零）、
`%-5.3d`（宽度 5、至少 3 位数字、左对齐）。

**`format()` 方式**——字符串里用 `{}` 替换内容，`{}` 里既可以是**数字索引**，也可以是**关键字参数**。

### 代码实操

`code/41-format-output.py`：

```python
# ---------- 方式一：百分号 % ----------
# %s=字符串  %d=整数  %f=浮点数；数字可控制宽度和精度
print("%s is %s than %s" % ("Beautiful", "better", "ugly"))
print("整数：%d，浮点：%f" % (42, 3.14159))
print("宽度 5、保留 1 位小数、左边补零：[%05.1f]" % 3.14)
print("宽度 5、至少 3 位数字、左对齐：[%-5.3d]" % 123.456)

# ---------- 方式二：str.format() ----------
# {} 里可以放数字索引，也可以放关键字参数
print("{} is {} than {}".format("Beautiful", "better", "ugly"))
print("{1} is {2} than {0}".format("ugly", "Beautiful", "better"))
print("{B} is {b} than {u}".format(u="ugly", B="Beautiful", b="better"))

# ---------- 方式三：f-strings（对照） ----------
u, B, b = "ugly", "Beautiful", "better"
print(f"{B} is {b} than {u}")
```

运行：

```bash
$ python3 41-format-output.py
```

真实输出：

```
Beautiful is better than ugly
整数：42，浮点：3.141590
宽度 5、保留 1 位小数、左边补零：[003.1]
宽度 5、至少 3 位数字、左对齐：[123  ]
Beautiful is better than ugly
Beautiful is better than ugly
Beautiful is better than ugly
Beautiful is better than ugly
```

> 💡 注意 `%f` 默认保留 **6 位**小数；`[123  ]` 里后面的两个空格是宽度补出来的（左对齐）。
> 三种手段都能达到同样效果，实际开发推荐 f-strings。

### 课后作业

在程序中有字符串变量 `date="2022-05-20 13:14:00"`，请用格式化输出把它转换成：

```
智能助手为你报时，当前时间是 2022 年 5 月 20 日 13 点 14 分 0 秒
```

> 参考思路：先用字符串切片把年月日时分秒取出来（`date[:4]` 取年、`date[5:7]` 取月……），
> 再用格式化输出拼句子。要注意「5 月」「0 秒」这种**去掉前导零**的写法，用 `int()` 转一下就没了。

---

## 第 42 讲 · F-strings：如何通过定义好的格式进行输出？

### 本节目标

掌握 f-strings 的基本用法、`{}` 里的计算能力，以及**宽度和精度**的写法。

### 知识要点

- F-strings 是 **Python 3.6 新增**的字符串格式化功能，比 `%` 和 `str.format()` 更友好；
- 它沿用了早期给字符串加前缀的思路（如 `u`、`r`、`b`），只不过前缀换成了 `f`；
- 官方文档：<https://peps.python.org/pep-0498/>。

**1. `{}` 里可执行计算**：数字计算、字符串连接、调用函数等，都会被解释执行。

```python
f"{ 1 + 2 }"        # 3
f"{ 'a' + 'b' }"    # ab
f"{ 'ABC'.lower() }"  # abc
```

**2. 宽度和精度调整**，格式为：

```python
f"{对象:宽度.精度类型}"
```

- **宽度**：`f"{number:10}"` 右边补空格到 10 位；`f"{number:010}"` 左边补 0。
- 指定类型后会带默认精度，如 `{number:4f}` 默认保留小数点后 6 位。
- **精度**：`f"{number:.3f}"` 保留小数点后 3 位。

### 代码实操

`code/42-fstrings.py`：

```python
name = "小明"
score = 95.5

# ---------- 1. 基本用法：{} 里放变量 ----------
print(f"{name} 的分数是 {score}")

# ---------- 2. {} 里可以做计算、调用函数 ----------
print(f"1 + 2 = {1 + 2}")
print(f"字符串连接：{'a' + 'b'}")
print(f"调用方法：{'ABC'.lower()}")

# ---------- 3. 宽度和精度：f"{对象:宽度.精度类型}" ----------
number = 123.456
print(f"[{number:10}]")      # 宽度 10，右侧自动补空格
print(f"[{number:010}]")     # 宽度 10，左侧补 0
print(f"[{number:4f}]")      # 指定类型 f 后默认保留小数点后 6 位
print(f"[{number:.3f}]")     # 只保留小数点后 3 位
print(f"[{number:10.3f}]")   # 宽度 10 + 3 位小数

# 课后作业：输出宽度为 10、小数点后最多 3 位 —— 123.4567 → '000123.457'
value = 123.4567
print(f"'{value:010.3f}'")
```

运行：

```bash
$ python3 42-fstrings.py
```

真实输出：

```
小明 的分数是 95.5
1 + 2 = 3
字符串连接：ab
调用方法：abc
[   123.456]
[000123.456]
[123.456000]
[123.456]
[   123.456]
'000123.457'
```

> 💡 `[   123.456]` 前面有 3 个空格——因为 `123.456` 有 7 个字符，宽度 10 要补 3 个空格。
> `[123.456000]` 是 `4f` 的效果：类型符 `f` 默认 6 位小数。最后一行就是作业答案：
> 宽度 10 + 保留 3 位小数，得到 `'000123.457'`。

### 课后作业

有一组由程序处理的浮点数，为了输出时保持工整，希望输出的字面值为 **10 个数字**，
且**小数点后最多包含 3 位**。请用 F-strings 对它们进行格式调整并输出。

例：数字为 `123.4567` → 输出为 `'000123.457'`。

> 参考答案：`f"{value:010.3f}"`。`0` 表示空位补零，`10` 是总宽度，`.3f` 表示保留 3 位小数。
> 如上一讲代码实操最后两行所示，实测输出正是 `'000123.457'`。

---

## 第 43 讲 · 常见常新：文件的打开

### 本节目标

会用 `open()` 打开文件，分清 `mode` 的几种取值，理解「文件对象」。

### 知识要点

**1. 文件的概念**

类 Unix 系统的哲学是「**一切皆文件**」：设备、虚拟设备、网络套接字等都被当作文件。
文件的基本操作包括：**打开、关闭、读取、写入**。

**2. 使用 `open()` 打开文件**

```python
open(file, mode='r', buffering=-1, encoding=None, errors=None,
     newline=None, closefd=True, opener=None)
```

- 第一个参数是**文件名**（必填），第二个是 **mode**。
- 打开成功会返回一个**文件对象**（如 `name='a.file' mode='r' encoding='UTF-8'`）；
  默认是**只读**方式，避免误操作覆盖文件。

**3. 文件路径处理**

路径不对会报 `FileNotFoundError: [Errno 2] No such file or directory: 'xxx.file'`。两种解决办法：

- 打开时**写完整路径**：`open("/tmp/afile")`；
- 先**切换目录**再打开：`import os; os.chdir("/tmp"); open("afile")`。

**4. 文件打开模式**（`mode` 常用值）

| 字符 | 含义 |
| --- | --- |
| `r` | 读取（默认） |
| `w` | 写入，并**覆盖**文件 |
| `a` | 写入，文件存在则在**末尾追加** |
| `b` | 二进制模式 |
| `+` | 支持读取与写入 |

### 代码实操

`code/43-open.py`（素材 `demo1.txt` 的内容是 5 行数字）：

```python
import os

# 以只读方式打开（默认 mode='r'，最安全，避免误覆盖）
f = open("demo1.txt", mode="r", encoding="UTF-8")

print("文件对象：", f)
print("是否可读：", f.readable(), " 是否可写：", f.writable())

# readlines()：一次性读成「行的列表」
data = f.readlines()
print("读到的每一行：", data)

# 用完要关闭，释放文件描述符
f.close()

# 路径不对会报 FileNotFoundError；用 os 模块可以查看当前工作目录
print("当前工作目录：", os.getcwd())
print("该目录下的 demo 素材文件：", sorted(n for n in os.listdir(".") if n.startswith("demo")))
```

运行（在 `code/` 目录里）：

```bash
$ python3 43-open.py
```

真实输出：

```
文件对象： <_io.TextIOWrapper name='demo1.txt' mode='r' encoding='UTF-8'>
是否可读： True  是否可写： False
读到的每一行： ['111111\n', '222\n', '333\n', '444\n', '555\n']
当前工作目录： /Users/pengshicong/Desktop/zero-basics-python-cn/05-io-and-files/code
该目录下的 demo 素材文件： ['demo.txt', 'demo1.txt', 'demo2.txt', 'demo3.txt', 'demo4.txt', 'demo_GBK.txt']
```

> 💡 文件对象打印出来是 `<_io.TextIOWrapper name='demo1.txt' mode='r' encoding='UTF-8'>`，
> 里面的 `name/mode/encoding` 一目了然。`readlines()` 返回的每个元素都**带着换行符 `\n`**。
> 注意：直接用文件名（相对路径）打开，是相对于「**当前工作目录**」找文件——所以要在 `code/` 目录里运行。

### 课后作业

如果你使用 Linux 或 macOS，请用只读模式打开 `/etc/passwd`；如果是 Windows，请打开 C 盘下任意一个 `.txt` 文件。
要求文件能正常打开、不报错。

> 参考答案（Linux / macOS）：

```python
with open("/etc/passwd", mode="r", encoding="UTF-8") as f:
    print(f.readline())   # 只读第一行演示，避免刷屏
```

---

## 第 44 讲 · 文件编码：如何解决不同操作系统的文件乱码问题？

### 本节目标

理解「编码」是什么、乱码从哪来，会用 `encoding` 参数以指定编码打开文件。

### 知识要点

**1. 为什么会产生乱码**

- 计算机只能处理数字。要把文本交给计算机，就得按某种规则把文本转换成数字——这个过程叫**编码**。
- 比如 **ASCII** 把英文字母、数字和常用符号编码成特定的数字。
- 计算机普及后各国标准不一：中国制定的 **GBK** 编码一直被 Windows 沿用。
- 后来有了统一的 **Unicode**，其中最广泛使用的实现方式就是 **UTF-8**。

**2. 常见操作系统的文件编码**

| 系统 | 默认编码 |
| --- | --- |
| Windows | GBK |
| Linux / macOS | UTF-8 |

**3. 乱码举例**

同一个字符串，用错的编码去解读就会变成「鬼画符」；

```
string = "人生苦短，我用 Python"   # 正确的 UTF-8 显示
浜虹敓鑻︾煭锛屾垜鐢� Python        # 用 GBK 的规则去解读 UTF-8 字节 → 乱码
```

**4. 以不同的编码打开文件**

```python
open(filename, encoding="UTF-8")
open(filename, encoding="GBK")
```

### 代码实操

`code/44-encoding.py`（素材 `demo_GBK.txt` 是用 **GBK** 编码保存的「人生苦短， 我用Python」）：

```python
# ---------- 1. 用正确编码（GBK）读 GBK 文件 ----------
with open("demo_GBK.txt", mode="r", encoding="GBK") as f:
    print("用 GBK 读 demo_GBK.txt：", f.read())

# ---------- 2. 故意用错编码（UTF-8）读同一个文件 → 报错 ----------
try:
    with open("demo_GBK.txt", mode="r", encoding="UTF-8") as f:
        print(f.read())
except UnicodeDecodeError as e:
    print("用 UTF-8 读 GBK 文件出错：", e)

# ---------- 3. 乱码是怎么产生的：编码和解码用了不一致的规则 ----------
s = "人生苦短，我用 Python"
print("原字符串：", s)
print("先按 UTF-8 编码、再按 GBK 解码：", s.encode("utf-8").decode("gbk", errors="replace"))
```

运行：

```bash
$ python3 44-encoding.py
```

真实输出：

```
用 GBK 读 demo_GBK.txt： 人生苦短， 我用Python
用 UTF-8 读 GBK 文件出错： 'utf-8' codec can't decode byte 0xc8 in position 0: invalid continuation byte
原字符串： 人生苦短，我用 Python
先按 UTF-8 编码、再按 GBK 解码： 浜虹敓鑻︾煭锛屾垜鐢� Python
```

> 💡 三件事一次看清：① 用**对的**编码（GBK）读，中文正常；② 用**错的**编码（UTF-8）读，
> 直接 `UnicodeDecodeError`；③ 乱码的本质就是「编码用的规则」和「解码用的规则」不一致——
> 把 UTF-8 的字节按 GBK 解，就得到最后那串鬼画符。解决办法永远是：**打开文件时指定正确的 `encoding`**。

### 课后作业

使用 `open()` 打开任意一个文件并观察结果；注意根据自己的操作系统使用正确的字符集
（Windows 用 GBK，macOS 用 UTF-8）。

> 参考答案：macOS / Linux 上 `open("some.txt", encoding="UTF-8")`；
> 若打开的是 Windows 传来的文件而出现乱码，就换成 `encoding="GBK"` 再试。

---

## 第 45 讲 · 常见常新：文件的读写

### 本节目标

会读（`read` / `readline` / `readlines` / 迭代）会写（`write`），并会用 `tell` / `seek` 操作文件指针。

### 知识要点

**1. 文件读取**

| 函数 / 语句 | 作用 |
| --- | --- |
| `read([size])` | 读指定大小的内容；不给 size 则读**整个文件** |
| `readline()` | 读**一行** |
| `readlines([size])` | 读成**行的列表**；不给 size 则读全部 |
| `for line in file` | **迭代**文件的每一行 |

**2. 文件写入**

- 写入由 `write()` 实现，**写到哪里**由 `open()` 的 `mode` 决定：

| mode | 写入行为 |
| --- | --- |
| `r` | 报错 `io.UnsupportedOperation: not writable` |
| `w` / `w+` | **清空**文件再写入，返回写入的字符数 |
| `a` / `a+` | 在文件**末尾追加** |

**3. 配合指针函数实现指定位置写入**

- `tell()`：返回文件指针当前位置；
- `seek(偏移量, [起始位置])`：移动指针；
- `close()`：关闭文件。

### 代码实操

`code/45-read-write.py`：

```python
# ---------- 1. 写入：mode='w' 会清空原文件，返回写入的字符数 ----------
f = open("a.txt", mode="w", encoding="UTF-8")
n = f.write("第一行\n第二行\n第三行\n")
print("写入字符数：", n)
f.close()

# ---------- 2. read() 读全部 ----------
with open("a.txt", mode="r", encoding="UTF-8") as f:
    print("read() 整体：", repr(f.read()))

# ---------- 3. readline() 逐行读 ----------
with open("a.txt", mode="r", encoding="UTF-8") as f:
    print("readline() 第 1 行：", repr(f.readline()))
    print("readline() 第 2 行：", repr(f.readline()))

# ---------- 4. readlines() 读成列表 ----------
with open("a.txt", mode="r", encoding="UTF-8") as f:
    print("readlines()：", f.readlines())

# ---------- 5. for line in f 迭代每一行 ----------
with open("a.txt", mode="r", encoding="UTF-8") as f:
    for i, line in enumerate(f, 1):
        print(f"第 {i} 行：{line.rstrip()}")

# ---------- 6. 追加：mode='a' ----------
with open("a.txt", mode="a", encoding="UTF-8") as f:
    f.write("追加的一行\n")
with open("a.txt", mode="r", encoding="UTF-8") as f:
    print("追加后共", len(f.readlines()), "行")

# ---------- 7. 只读模式下写入会报错（用 try 捕获观察） ----------
try:
    f = open("a.txt", mode="r", encoding="UTF-8")
    f.write("写不进去")
except Exception as e:            # io.UnsupportedOperation
    print("只读模式写入报错：", type(e).__name__, "-", e)

# ---------- 8. tell() / seek()：查看和移动文件指针 ----------
with open("pos.txt", mode="w", encoding="UTF-8") as f:
    f.write("hello world")
with open("pos.txt", mode="r", encoding="UTF-8") as f:
    print("初始指针位置：", f.tell())
    print("读 5 个字符：", repr(f.read(5)), " 指针位置：", f.tell())
    f.seek(0)
    print("seek(0) 后整段读回：", repr(f.read()))
```

运行（`a.txt`、`pos.txt` 由脚本自己创建，不依赖外部文件）：

```bash
$ python3 45-read-write.py
```

真实输出：

```
写入字符数： 12
read() 整体： '第一行\n第二行\n第三行\n'
readline() 第 1 行： '第一行\n'
readline() 第 2 行： '第二行\n'
readlines()： ['第一行\n', '第二行\n', '第三行\n']
第 1 行：第一行
第 2 行：第二行
第 3 行：第三行
追加后共 4 行
只读模式写入报错： UnsupportedOperation - not writable
初始指针位置： 0
读 5 个字符： 'hello'  指针位置： 5
seek(0) 后整段读回： 'hello world'
```

> 💡 用 `repr()` 是为了让换行符 `\n` 显式显示出来（否则你看不见它）。
> 「写入字符数 12」= 9 个汉字 + 3 个换行符。`seek(0)` 把指针移回开头，所以能重新读到完整内容。

### 课后作业

1. 将下面这段字符串保存到文本文件 `a.txt` 中：

```python
string = """Python 3.11 is up to 10-60% faster than Python 3.10.
On average, we measured a 1.25x speedup on the standard
benchmark suite. See Faster CPython for details. """
```

2. 用文件读写功能把 `a.txt` 复制为 `b.txt` 并保存。

> 参考答案：

```python
string = """Python 3.11 is up to 10-60% faster than Python 3.10.
On average, we measured a 1.25x speedup on the standard
benchmark suite. See Faster CPython for details. """

with open("a.txt", mode="w", encoding="UTF-8") as f:
    f.write(string)

with open("a.txt", mode="r", encoding="UTF-8") as f_in, \
     open("b.txt", mode="w", encoding="UTF-8") as f_out:
    f_out.write(f_in.read())
```

---

## 第 46 讲 · 常见常新：文件的关闭

### 本节目标

理解「为什么要关闭文件」，掌握 `close()` 与 `with` 语句两种关闭方式。

### 知识要点

**1. 文件关闭的内部工作过程**

- `write()` 执行完成后，写入的内容**还在内存缓冲区**里；
- 内存是**易失存储**，突然断电数据就会丢；
- `close()` 会**告知内核**文件在内存中有更新（把缓冲刷到磁盘），并释放文件描述符。

**2. `close()` 函数的使用原则**

| 场景 | 是否需要 close |
| --- | --- |
| `write()` 写入后 | **必须**显式 `close()` |
| `read` 族函数读取后 | **不必**，但建议关闭（避免文件描述符耗尽） |
| `open()` 失败 | **不必**（根本没拿到文件对象） |

**3. `with` 语句**

```python
with open(文件) as 文件描述符:
    文件读写操作
# 离开 with 块，自动关闭文件
```

`with` 让「打开」和「关闭」保持一致，是最推荐的写法。

### 代码实操

`code/46-close.py`：

```python
# ---------- 1. with 语句：离开代码块自动关闭 ----------
with open("close.txt", mode="w", encoding="UTF-8") as f:
    f.write("用 with 语句写进来的内容\n")
print("with 块结束后，文件是否已关闭：", f.closed)

# ---------- 2. 手动 close() ----------
f2 = open("close.txt", mode="r", encoding="UTF-8")
print("手动读取内容：", f2.read().strip())
f2.close()
print("手动 close 后，文件是否已关闭：", f2.closed)

# ---------- 3. 打开不存在的文件会报 FileNotFoundError ----------
# 用 try 捕获，方便观察错误信息，同时不让程序中断
try:
    f3 = open("这个文件不存在.txt", mode="r", encoding="UTF-8")
    f3.close()
except FileNotFoundError as e:
    print("打开不存在的文件报错：", e)
    print("注意：open() 失败时不会创建文件对象，也不用（无法）调用 close()")
```

运行：

```bash
$ python3 46-close.py
```

真实输出：

```
with 块结束后，文件是否已关闭： True
手动读取内容： 用 with 语句写进来的内容
手动 close 后，文件是否已关闭： True
打开不存在的文件报错： [Errno 2] No such file or directory: '这个文件不存在.txt'
注意：open() 失败时不会创建文件对象，也不用（无法）调用 close()
```

> 💡 注意第 1 段：`with` 块**结束后**再访问 `f.closed`，结果是 `True`——证明它自动关了。

### 课后作业

请打开一个不存在的文件，观察报错，并尝试用 `close()` 函数关闭它，继续观察报错信息。

> 参考答案要点：打开不存在的文件会抛 `FileNotFoundError`，此时 `f` 变量**根本没被赋值**，
> 再用 `f.close()` 会抛 `NameError: name 'f' is not defined`。这正说明——**打开失败的文件无需也不能关闭**。
> （运行 `code/46-close.py` 时，脚本用 `try/except` 优雅地展示了这个 `FileNotFoundError`，
> 避免程序被中途打断。）

---

## 第 47 讲 · 小试牛刀：如何使用 Python 合并多个文件？

### 本节目标

把「读文件 + 写文件」组合起来，实现两个乃至任意多个文件的合并。

### 知识要点

**合并文件的需求分析**

```
合并文件 = 逐个读取原始文件 + 追加写入新的文件
```

**合并两个文件的关键任务**

1. 以**可读**模式打开原始文件；
2. 以**写入**模式创建并打开要合并的目标文件；
3. 正确关闭文件。

**遍历多个文件的关键任务**

1. 把多个文件的文件名写进**列表**；
2. **遍历**列表；
3. 重构文件读、写代码（这样任意多个文件都能自动合并）。

### 代码实操

`code/47-merge-files.py`（素材 `demo1.txt` / `demo2.txt` / `demo3.txt` 各含几行文本）：

```python
# ---------- 方案一：合并两个文件 ----------
with open("demo1.txt", encoding="UTF-8") as f1:
    data1 = f1.read()
with open("demo2.txt", encoding="UTF-8") as f2:
    data2 = f2.read()
with open("merge_two.txt", mode="w", encoding="UTF-8") as out:
    out.write(data1)
    out.write(data2)
print("方案一：demo1.txt + demo2.txt 已合并 -> merge_two.txt")

# ---------- 方案二：遍历列表，合并任意多个文件 ----------
files_name = ["demo1.txt", "demo2.txt", "demo3.txt"]
files_data = []

for f_name in files_name:
    with open(f_name, encoding="UTF-8") as f:
        files_data.append(f.read())

with open("merge_all.txt", mode="w", encoding="UTF-8") as out:
    for data in files_data:
        out.write(data)
print("方案二：", files_name, "已合并 -> merge_all.txt")

# ---------- 验证：读回合并结果 ----------
with open("merge_all.txt", encoding="UTF-8") as f:
    text = f.read()
print(f"合并后共 {len(text.splitlines())} 行，内容如下：")
print(text)
```

运行：

```bash
$ python3 47-merge-files.py
```

真实输出：

```
方案一：demo1.txt + demo2.txt 已合并 -> merge_two.txt
方案二： ['demo1.txt', 'demo2.txt', 'demo3.txt'] 已合并 -> merge_all.txt
合并后共 12 行，内容如下：
111111
222
333
444
555
aaa
bbb
ccc
ddd
xxx
yyy
zzz

```

> 💡 方案二先把所有文件内容读进 `files_data` 列表，再统一写进目标文件——
> 这样**任意数量的文件**都能合并，只要改动 `files_name` 列表即可。最后那行空行是 `print(text)` 的换行带来的。

### 课后作业

在 `homework` 文件夹下有三个文件夹 `dira`、`dirb`、`dirc`，各自存放了与文件夹同名的文本文件
（`dira/dira.txt`、`dirb/dirb.txt`、`dirc/dirc.txt`）。请用 Python 把这三个 txt 文件合并成
`homework.txt`，放到 `homework` 下。

> 参考答案：

```python
import os

base = "homework"
files_name = [
    os.path.join(base, "dira", "dira.txt"),
    os.path.join(base, "dirb", "dirb.txt"),
    os.path.join(base, "dirc", "dirc.txt"),
]

with open(os.path.join(base, "homework.txt"), mode="w", encoding="UTF-8") as out:
    for f_name in files_name:
        with open(f_name, encoding="UTF-8") as f:
            out.write(f.read())
```

---

## 第 48 讲 · 再回首：「输入输出与文件操作」单元小结

### 本节目标

把本章「输入 → 处理 → 格式化输出 → 写文件 → 读回」这条完整链路，用一个综合小练习串起来。

### 知识要点

本章其实就是一条**数据进出管道**：

```
input()/命令行参数  →  程序处理  →  print/f-string  →  文件写入  →  文件读取
     (输入)                          (输出)            (持久化)
```

- **输入**：交互用 `input()`，非交互用 `argparse` 命令行参数；
- **输出**：`%` / `str.format()` / **f-strings**，越靠后越推荐；
- **文件**：`open()` 打开、`read*` 读、`write` 写、`with` 关闭；编码不对会乱码。

> 📌 本讲是本章的收束，把这一章的技能点连成一条线即可，不必再引入新知识。

### 代码实操

`code/48-summary.py`——一个把周边知识全用上的小程序：

```python
# ---------- 1. 输入：用固定值模拟键盘输入（真正的代码是 input()） ----------
name = "小明"
raw_scores = "90,85,100"          # 模拟用户敲入的一串成绩

# ---------- 2. 处理 ----------
scores = [int(x) for x in raw_scores.split(",")]
average = sum(scores) / len(scores)

# ---------- 3. 格式化输出（f-string，保留 2 位小数） ----------
line = f"{name} 的成绩 {scores}，平均分 {average:.2f}"
print(line)

# ---------- 4. 写文件（with 语句自动关闭） ----------
with open("report.txt", mode="w", encoding="UTF-8") as f:
    f.write(line + "\n")

# ---------- 5. 读回文件确认落盘成功 ----------
with open("report.txt", mode="r", encoding="UTF-8") as f:
    print("读回文件内容：", f.read().strip())
```

运行：

```bash
$ python3 48-summary.py
```

真实输出：

```
小明 的成绩 [90, 85, 100]，平均分 91.67
读回文件内容： 小明 的成绩 [90, 85, 100]，平均分 91.67
```

> 💡 短短十几行，把 `input`（固定值演示）、`split`、列表推导、`sum`、f-string 精度、
> `with open` 写入与读回全串起来了——这就是本章的「最小可用闭环」。

### 课后作业

把 `code/48-summary.py` 改造一下：用 `input()`（或命令行参数）真正接收名字和成绩，
把每个人一行地追加（`mode="a"`）写进 `report.txt`，最后读回整个文件打印出来。

> 参考答案要点：把 `name`/`raw_scores` 换成 `input()`；写入时用 `mode="a"`（追加，别覆盖）；
> 读回时用 `for line in f` 逐行打印即可。

---

## 本章小结

**速查表**

| 主题 | 关键点 |
| --- | --- |
| 交互式输入 | `input("提示")`，**永远返回字符串**，要数字记得 `int()`/`float()` |
| 非交互式输入 | `argparse`：`add_argument` 加参数，`type=int` 转类型，`default=` 设默认值 |
| 百分号格式化 | `"%s/%d/%f" % (...)`，可带宽度精度如 `%05.1f` |
| `format()` | `"{} {}".format(a, b)`，`{}` 可用索引或关键字 |
| f-strings | `f"{变量:宽度.精度类型}"`，`{}` 内可计算、可调用函数 |
| 打开文件 | `open(文件名, mode, encoding)`，默认 `mode='r'` |
| 打开模式 | `r` 读 · `w` 覆盖写 · `a` 追加 · `b` 二进制 · `+` 读写 |
| 编码 | Windows 默认 GBK，macOS/Linux 默认 UTF-8；用 `encoding=` 指定 |
| 读取 | `read()` 全部 · `readline()` 一行 · `readlines()` 行列表 · `for line in f` 迭代 |
| 写入 | `write()`，写到哪里由 `mode`（w 覆盖 / a 追加）决定 |
| 指针 | `tell()` 查位置 · `seek()` 移位置 |
| 关闭 | `close()` 或 **`with open(...) as f:`** 自动关闭（推荐） |
| 合并文件 | 遍历文件名列表 → 逐个 `read` → 统一 `write` 到目标文件 |

**三句话**

1. 输入分两种：**交互**用 `input()`（返回字符串），**非交互**用命令行参数——用户不总会按你想的输入，要全面判断。
2. 输出越现代越省心：`%` → `str.format()` → **f-strings**，宽度和精度用 `f"{值:宽度.精度类型}"`。
3. 文件操作四步「**打开 → 读写 → 关闭**」；跨系统乱码靠 `encoding` 解决，关闭文件**首选 `with` 语句**。

**动手练习**

1. 用 `input()` 写一个「按 q / quit 退出」的命令行小程序（去掉注释真跑一次）。
2. 用 `argparse` 写一个接收两个数字并输出其和的计算器。
3. 把 `code/44-encoding.py` 里的 `demo_GBK.txt` 分别用 GBK 和 UTF-8 打开，对比结果。
4. 跑 `code/47-merge-files.py`，把 `demo1/2/3.txt` 合并成 `merge_all.txt`，再读回验证。
5. 完成 `code/48-summary.py` 的作业，把成绩以追加模式写进 `report.txt`。

---

## 下一章预告

下一章进入**第 6 章 · 函数**：如何把一段可复用的逻辑封装成函数，
讲清 `def` 定义、参数（位置/关键字/默认/可变参数）、`return` 返回值、作用域，以及函数式的小技巧。

---

[← 上一章：判断与循环](/guide/control-flow) ｜ [返回总目录](/) ｜ [下一章：函数 →](/guide/functions)

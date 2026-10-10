# 第 8 章 · 模块与标准库

> 别人写好的代码，拿来就能用：学会 **import** 导入模块，会用 Python 自带的**标准库**，
> 会写自己的**自定义模块**，会装**第三方模块**，最后用 sympy 给函数求导。
> **本章 6 讲（066–071）**，从「怎么借别人的代码」讲到「怎么写出一个完整功能」。

## 🎯 本章目标

- 理解**模块**是什么：一个以 `.py` 结尾、里面放着函数 / 变量 / 类的文件
- 掌握 5 种导入写法：`import 模块`、`from 模块 import 函数`、别名 `as`、包导入、多函数导入
- 认识 Python **标准库**，会用 `math` / `json` / `os.path` / `zipfile` 等常用组件
- 会编写**自定义模块**，会用 `if __name__ == "__main__"` 保护测试代码
- 知道用 `pip` 装**第三方模块**、用 `venv` 建**虚拟环境**、用镜像源**加速下载**
- 会用第三方库 `sympy` 做符号求导，配合 `matplotlib` 画函数图像

**本章代码**

> 📌 **代码约定**：正文代码块都保持**可直接运行**；节选会明确标注「节选」并指向 `code/` 完整文件。
> 所有输出都是**真实运行结果**（本机 Python 3.12.7）。

| 文件 | 内容 |
| --- | --- |
| `code/66-import.py` | 5 种模块导入写法、`模块.函数` 与 `函数` 两种调用格式 |
| `code/67-stdlib.py` | 标准库 `math` / `json` / `os.path` / `zipfile` 实操 |
| `code/mymodule.py` | 自定义模块（被导入）：变量 + 函数 + 类 + `__name__` 保护 |
| `code/68-custom-module.py` | 导入并使用自定义模块、模块内省、多次导入只执行一次 |
| `code/69-third-party.py` | 第三方模块 `requests` / `numpy` 的导入与真实计算 |
| `code/70-derivative.py` | 数值求导 + sympy 符号求导 + 求极限 + matplotlib 画图 |
| `code/71-summary.py` | 单元小结：把本章要点串一遍 |

> ⚠️ `code/mymodule.py` 是被 `68-custom-module.py` 导入的模块文件，两个文件要放在**同一个目录**里。

---

## 第 66 讲 · 模块的导入：如何使用其他人编写好的代码功能？

### 本节目标

搞懂「模块」是什么，并学会 5 种把别人的代码「借」到自己程序里来的导入写法。

### 知识要点

**1. 什么是模块**

**模块**就是**一个以 `.py` 结尾的文件**，里面存放着函数（也可以放变量、类）。
它的作用是：**把函数放进模块文件里，隐藏代码细节，让主程序的逻辑更清晰**——
你只要会「调用」，不必知道它内部怎么实现。

**2. 导入模块的 5 种写法**

| 写法 | 例子 | 调用函数时的格式 |
| --- | --- | --- |
| 导入整个模块 | `import os` | `os.getcwd()` |
| 导入指定函数 | `from os import getcwd` | `getcwd()` |
| 一次导入多个 | `from os import chdir, getcwd` | `getcwd()` |
| 起别名 | `import datetime as dt` | `dt.date(...)` |
| 导入包里的模块 | `from datetime import date` | `date.today()` |

**3. 包（package）**

把**多个模块文件放进一个文件夹**，这个文件夹就叫**包**。包的导入和模块一样：
`import 包` 或 `from 包 import 模块`；调用包里的函数时写成 **`包.模块.函数`**。

**4. 两个提醒**

- ⚠️ **不建议**用 `from os import *` 把模块所有函数都导进来——容易和现有名字撞车，也看不出函数来自哪里。
- 💡 记忆口诀：**`import` 后面接整块，`from ... import` 后面接零碎**；用了 `as` 就用别名去调。

### 代码实操

完整代码见 `code/66-import.py`：

```python
# -*- coding: utf-8 -*-
"""第 66 讲 · 模块的导入：如何使用其他人编写好的代码功能？"""
import os

# 1. 导入整个模块：调用时写「模块名.函数()」
print("== 1. import os ==")
print(os.getcwd())

# 2. 只导入模块中的某个函数：调用时直接写「函数()」
print("== 2. from os import getcwd ==")
from os import getcwd
print(getcwd())

# 3. 一次导入多个函数
print("== 3. from os import chdir, getcwd ==")
from os import chdir, getcwd as cwd
print(cwd())

# 4. 给模块起别名：import 模块 as 别名
print("== 4. import datetime as dt ==")
import datetime as dt
print(dt.date(2026, 10, 10))

# 5. 从包中导入模块：包.模块.函数
print("== 5. from datetime import date ==")
from datetime import date
print(date(2026, 10, 10).year)
```

运行命令与真实输出：

```bash
$ python3 66-import.py
== 1. import os ==
/Users/pengshicong/Desktop/zero-basics-python-cn/08-modules/code
== 2. from os import getcwd ==
/Users/pengshicong/Desktop/zero-basics-python-cn/08-modules/code
== 3. from os import chdir, getcwd ==
/Users/pengshicong/Desktop/zero-basics-python-cn/08-modules/code
== 4. import datetime as dt ==
2026-10-10
== 5. from datetime import date ==
2026
```

> 💡 `os.getcwd()` 打印的是**你当前所在的目录**，所以这行输出会因电脑不同而不同——它不是什么固定值。

### 课后作业

为了获取今天的日期，需要用到 `datetime` 包里 `date` 模块中的 `today()` 方法。
下面三种调用格式，各自要用什么**导入语法**？

- 格式一：`datetime.date.today()`
- 格式二：`date.today()`
- 格式三：`today()`

**参考答案**（已在 `code/66-import.py` 末尾真跑）：

| 格式 | 导入语法 |
| --- | --- |
| 格式一 `datetime.date.today()` | `import datetime`（用「模块.成员」逐层点出来） |
| 格式二 `date.today()` | `from datetime import date` |
| 格式三 `today()` | `from datetime import date`，再 `today = date.today`（把方法绑成名字） |

⚠️ 格式三不能写成 `from datetime import today`：`today` 是 `date` 类的方法，**不是模块级的名字**，
直接 import 会报 `ImportError: cannot import name 'today'`，所以需要额外把 `date.today` 绑定成一个变量。

真跑结果（接在上面代码后面）：

```bash
== 课后作业：三种写法 ==
格式一 datetime.date.today() -> 2026-10-10
格式二 date.today()          -> 2026-10-10
格式三 today()               -> 2026-10-10
```

---

## 第 67 讲 · 标准库：Python 默认提供的便捷功能有哪些？

### 本节目标

认识 Python 自带的**标准库**，学会「遇到新需求 → 查官方文档 → 找到合适模块」的方法。

### 知识要点

**1. 什么是标准库**

**标准库**是**随 Python 一起安装、不用额外安装就能直接 `import`** 的模块集合。
它覆盖了文本处理、数字、文件与目录、网络与进程、并发执行等大量场景，
能显著提高开发效率。常见的组件有：内置函数 / 类型 / 异常、文本处理、数字、文件目录、
通用操作系统、并发执行、网络通信、互联网协议等。

**2. 如何通过官方文档学习标准库**

不必逐个背下所有模块，**掌握查阅文档的方法即可**。以「用 Python 模拟浏览器访问百度」为例：

1. 打开官方文档总目录：`https://docs.python.org/zh-cn/3.10/library/index.html`
2. 按分类找到「互联网协议和支持」
3. 进入 HTTP 相关章节，找到 `urllib.request`
4. 参考文档里的「例子」和 `urlopen()` 的参数说明，实现目标

> ⚠️ **本节为说明，未实跑**：下面这段访问网络的代码需要**联网**才能运行，
> 而本系列约定「网络相关示例不做真实联网演示」，所以只讲代码不贴运行结果。

```python
from urllib.request import urlopen

with urlopen("http://www.baidu.com/") as f:
    print(f.read(300))          # 打印百度首页前 300 字节
```

**3. 本讲真跑的标准库**

选几个**纯本地、不依赖网络**的常用组件来实操：`math`（数学）、`json`（JSON 互转）、
`os.path`（路径处理）、`zipfile`（压缩包读写）。

### 代码实操

完整代码见 `code/67-stdlib.py`：

```python
# -*- coding: utf-8 -*-
"""第 67 讲 · 标准库：Python 默认提供的便捷功能有哪些？"""
import math
import json
import os.path
import zipfile

# 1. math：数学常量与函数
print("== math ==")
print("math.pi        =", round(math.pi, 4))
print("math.sqrt(16)  =", math.sqrt(16))
print("math.factorial =", math.factorial(5))

# 2. json：在 JSON 文本和 Python 对象之间互相转换
print("== json ==")
person = {"name": "小明", "age": 18, "city": "北京"}
text = json.dumps(person, ensure_ascii=False)
print("json.dumps ->", text)
back = json.loads(text)
print("json.loads ->", back["name"], back["age"])

# 3. os.path：拼接与拆分路径
print("== os.path ==")
print("os.path.join   ->", os.path.join("data", "sub", "a.txt"))
print("os.path.splitext ->", os.path.splitext("report.csv"))

# 4. zipfile：读 / 写 zip 压缩包（对应课后作业）
print("== zipfile ==")
with zipfile.ZipFile("a.zip", "w") as zf:
    zf.writestr("a.txt", "这是 a.txt 里的内容\n第二行")
    zf.writestr("b.txt", "这是 b.txt 里的内容")

with zipfile.ZipFile("a.zip", "r") as zf:
    print("压缩包里的文件:", zf.namelist())
    print("a.txt 的内容如下:")
    print(zf.read("a.txt").decode("utf-8"))
```

运行命令与真实输出：

```bash
$ python3 67-stdlib.py
== math ==
math.pi        = 3.1416
math.sqrt(16)  = 4.0
math.factorial = 120
== json ==
json.dumps -> {"name": "小明", "age": 18, "city": "北京"}
json.loads -> 小明 18
== os.path ==
os.path.join   -> data/sub/a.txt
os.path.splitext -> ('report', '.csv')
== zipfile ==
压缩包里的文件: ['a.txt', 'b.txt']
a.txt 的内容如下:
这是 a.txt 里的内容
第二行
```

### 课后作业

某项目采用 zip 压缩格式保存了文件 `a.txt`，目录结构如下，请参考官方文档，
**用 Python 读取 `a.txt` 的内容并打印到终端**：

```
a.zip
  ___ a.txt
  ___ b.txt
  ...
```

**参考答案**：用标准库 `zipfile`——`ZipFile(...).read("a.txt")` 拿到的是**字节（bytes）**，
要用 `.decode("utf-8")` 解码成文本。上面 `== zipfile ==` 段就是完整实现：
先建一个含 `a.txt`、`b.txt` 的 `a.zip`，再读回 `a.txt`，输出正是「这是 a.txt 里的内容 / 第二行」。

---

## 第 68 讲 · 自定义模块：如何编写一个完整功能？

### 本节目标

学会把一组变量、函数、类**写进一个 `.py` 文件**，并让别的程序 `import` 它来用。

### 知识要点

**1. 创建自定义模块**

- 用**以 `.py` 结尾的文件名**保存模块；
- 文件里定义的**变量、函数**都能被调用；
- 文件里定义的**类**可以在引用模块时进行**实例化**（`模块.类()`）。

**2. 自定义模块注意事项**

1. 导入自定义模块时，要**确保导入路径正确**（模块文件要在能被找到的目录里）；
2. 文件名**避免特殊字符**，也**避免和标准库重名**（比如别叫 `os.py`）；
3. 自定义模块**多次导入，模块里的代码也只执行一次**（Python 会缓存已导入的模块）；
4. 模块里应**只定义函数**，把「调用 / 测试代码」放进 `if __name__ == "__main__":` 代码块里，
   这样别人 `import` 你的模块时才不会误触发这些代码。

**3. `__name__` 是什么**

每个模块都有内置变量 `__name__`：

- **直接运行**这个文件时，`__name__` 等于 `"__main__"`；
- 被**别的文件 import** 时，`__name__` 等于**模块名**（这里是 `"mymodule"`）。

所以 `if __name__ == "__main__":` 里的代码**只在直接运行时执行，被导入时不执行**。

### 代码实操

本讲需要**两个文件**，都放在 `code/` 里。

**（1）被导入的模块 `code/mymodule.py`**：

```python
# -*- coding: utf-8 -*-
"""mymodule —— 一个自定义模块，被 68-custom-module.py 导入。"""

var1 = 100                    # 模块里的变量


def func1():                  # 模块里的函数
    print("func1 is called")


class Class1(object):         # 模块里的类
    def __init__(self):
        print("Class1 is instance")


if __name__ == "__main__":
    print("mymodule 被直接运行（不是被导入）")
    func1()
```

**（2）导入它的脚本 `code/68-custom-module.py`**：

```python
# -*- coding: utf-8 -*-
"""第 68 讲 · 自定义模块：如何编写一个完整功能？"""
import mymodule                 # 导入同目录的自定义模块

# 1. 使用模块里的变量
print("== 1. 模块里的变量 ==")
print("mymodule.var1 =", mymodule.var1)

# 2. 使用模块里的函数
print("== 2. 模块里的函数 ==")
mymodule.func1()

# 3. 使用模块里的类（实例化）
print("== 3. 模块里的类 ==")
obj = mymodule.Class1()

# 4. 查看模块里有哪些成员
print("== 4. dir(mymodule) 去掉下划线开头的 ==")
print([n for n in dir(mymodule) if not n.startswith("__")])

# 5. from 模块 import 成员
print("== 5. from mymodule import var1, func1 ==")
from mymodule import var1, func1
print("var1 =", var1)
func1()

# 6. 模块被多次导入，文件里的代码只执行一次
print("== 6. 多次导入只执行一次 ==")
import mymodule as again
print("两次导入得到同一个模块对象:", mymodule is again)

# 7. 模块自带的元信息（内省）
print("== 7. 模块元信息 ==")
print("__name__ =", mymodule.__name__)
print("__file__ 结尾 =", mymodule.__file__.split("/")[-1])
```

运行命令与真实输出：

```bash
$ python3 68-custom-module.py
== 1. 模块里的变量 ==
mymodule.var1 = 100
== 2. 模块里的函数 ==
func1 is called
== 3. 模块里的类 ==
Class1 is instance
== 4. dir(mymodule) 去掉下划线开头的 ==
['Class1', 'func1', 'var1']
== 5. from mymodule import var1, func1 ==
var1 = 100
func1 is called
== 6. 多次导入只执行一次 ==
两次导入得到同一个模块对象: True
== 7. 模块元信息 ==
__name__ = mymodule
__file__ 结尾 = mymodule.py
```

对照着看两点：第 6 步的 `True` 说明**两次 `import mymodule` 拿到的是同一个模块对象**（只加载一次）；
第 7 步的 `__name__` 是 `"mymodule"` 而**不是** `"__main__"`，正说明它是被**导入**、而非直接运行的。

单独直接运行模块文件本身时，`__name__` 才会变成 `"__main__"`：

```bash
$ python3 mymodule.py
mymodule 被直接运行（不是被导入）
func1 is called
```

> 💡 对比一下：直接运行时打印了「mymodule 被直接运行」，而 `68-custom-module.py` 导入它时**没有**打印这句——
> 这就是 `if __name__ == "__main__":` 起到的作用。

### 课后作业

请编写一个自定义模块，模块中定义 `date()` 和 `time()` 两个函数，分别用于**显示当前的日期**和**系统时间**。

**参考答案**：新建 `datetime_tool.py`，用标准库 `datetime` 实现：

```python
# -*- coding: utf-8 -*-
"""自定义模块：提供 date() 和 time() 两个函数。"""
from datetime import datetime


def date():
    """返回当前日期，格式 2026-10-10"""
    return datetime.now().strftime("%Y-%m-%d")


def time():
    """返回当前时间，格式 13:48:00"""
    return datetime.now().strftime("%H:%M:%S")
```

在另一个脚本里 `import datetime_tool` 后调用 `datetime_tool.date()` / `datetime_tool.time()` 即可
（输出的是当时真实日期时间，每次运行都不同）。

---

## 第 69 讲 · 第三方模块的使用：如何使用其他人编写的代码？

### 本节目标

学会用 `pip` 安装第三方模块、用虚拟环境隔离依赖、用镜像源加速下载，并真正 import 用起来。

### 知识要点

**1. 用 pip 安装第三方模块**

第三方模块 = 别人发布到 **PyPI**（`https://pypi.org`）上的包，需要先装再用。安装命令：

```bash
pip3.10 install 模块名
# 或者（更推荐，能避免 pip 版本和 python 对不上）
python3.10 -m pip install 模块名
```

**2. 虚拟环境（venv）**

虚拟环境的用途：**解决多个模块依赖冲突、一次性安装指定版本、避免污染默认环境**。常用命令：

| 目的 | 命令 |
| --- | --- |
| 创建虚拟环境（`myvenv` 是文件夹名） | `python -m venv myvenv` |
| 激活虚拟环境（macOS / Linux） | `source myvenv/bin/activate` |
| 导出当前已装包及版本 | `pip3.10 freeze > requirements.txt` |
| 按清单装包 | `pip3.10 install -r requirements.txt` |
| 离开虚拟环境 | `deactivate` |

**3. 加速第三方模块安装**

pip 默认用国外源，下载容易超时，可换国内镜像：

```bash
# 临时加速（只对本次有效）
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名
```

```ini
# 永久加速：在 ~/pip.conf 里写
[global]
index-url = http://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host = mirrors.aliyun.com
```

### 代码实操

本机**已经装好** `requests` 与 `numpy`，所以直接真跑（无需再 `pip install`）。
先看安装信息：

```bash
$ python3 -m pip --version
pip 24.2 from /opt/anaconda3/lib/python3.12/site-packages/pip (python 3.12)

$ python3 -m pip show numpy
Name: numpy
Version: 1.26.4
Summary: Fundamental package for array computing in Python
```

完整代码见 `code/69-third-party.py`：

```python
# -*- coding: utf-8 -*-
"""第 69 讲 · 第三方模块的使用：如何使用其他人编写的代码？"""
import requests
import numpy as np

print("requests 版本:", requests.__version__)
print("numpy 版本:   ", np.__version__)

# 用第三方模块 numpy 做一次真实计算
arr = np.array([1, 2, 3, 4, 5])
print("数组:   ", arr)
print("平均值: ", arr.mean())
print("每个元素的平方:", arr ** 2)
print("数组之和:", arr.sum())

# 查看某个第三方包「装在哪、版本多少」
import importlib.metadata as md
print("numpy 包名:", md.distribution("numpy").metadata["Name"])
print("numpy 版本:", md.version("numpy"))
print("requests 版本:", md.version("requests"))
```

运行命令与真实输出：

```bash
$ python3 69-third-party.py
requests 版本: 2.34.2
numpy 版本:    1.26.4
数组:    [1 2 3 4 5]
平均值:  3.0
每个元素的平方: [ 1  4  9 16 25]
数组之和: 15
numpy 包名: numpy
numpy 版本: 1.26.4
requests 版本: 2.34.2
```

> 💡 `requests` 是用来发网络请求的第三方库（比如 `requests.get("http://...")` 抓网页）。
> 因为它要**联网**才有结果，本系列约定「网络示例不做真实联网演示」，所以这里只**确认它已安装并可用**，
> 没跑真正的请求。

### 课后作业

请安装第三方模块 **Matplotlib**，安装后运行下面代码并显示执行结果：

```python
import matplotlib.pyplot as plot

x = [1, 2, 3]
y = [4, 5, 6]
plot.plot(x, y, marker="o")
plot.plot(y, x, marker="x")
plot.show()
```

**参考答案**：先 `pip install matplotlib`（本机已装 3.9.2）。`plot.show()` 会弹出一个窗口显示折线图——
在**没有图形界面**的环境（如服务器、CI）里会报错，那时改用 `plot.savefig("out.png")` 把图存成文件即可。
下一讲的 `70-derivative.py` 就用这种「存文件」的方式画了图。

---

## 第 70 讲 · 小试牛刀：如何使用 Python 为函数求导？

### 本节目标

综合运用「标准库 + 第三方库」完成一个数学任务：**给函数求导**，并画出函数图像。

### 知识要点

**1. 需求分析**

用 Python 计算函数的导数，拆成几步：

1. 找到能实现 Python 求导的第三方模块 → **sympy**；
2. 安装并测试第三方模块；
3. 用第三方模块计算函数的导数；
4. 安装绘图模块并测试 → **matplotlib**；
5. 绘制函数图像。

**2. 两种求导思路**

| 思路 | 原理 | 依赖 |
| --- | --- | --- |
| **数值求导** | 用中心差分公式 `f'(x) ≈ (f(x+h) − f(x−h)) / 2h` 近似 | 纯标准库，零依赖 |
| **符号求导** | 用 `sympy` 直接求出导函数表达式 `2*x + 3` | 第三方库 `sympy` |

**3. sympy 求导的两个关键 API**

- `Symbol('x')`：声明一个数学符号 `x`；
- `Derivative(y, x)`：构造「y 对 x 求导」；再 `.doit()` 真正执行求导；
  用 `.subs({x: 10})` 把 `x` 代入具体数值。

### 代码实操

完整代码见 `code/70-derivative.py`（本机已装 `sympy 1.14.0`、`matplotlib 3.9.2`）：

```python
# -*- coding: utf-8 -*-
"""第 70 讲 · 小试牛刀：如何使用 Python 为函数求导？"""
# 待求导的函数：f(x) = x^2 + 3x + 2
def f(x):
    return x * x + 3 * x + 2


# 方法一：纯标准库做数值求导（中心差分近似）
def numeric_derivative(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)


print("== 方法一：数值求导（纯标准库）==")
print("f'(10) ≈", numeric_derivative(f, 10))

# 方法二：用第三方库 sympy 做符号求导
from sympy import Derivative, Symbol, limit, oo

x = Symbol("x")
y = x * x + 3 * x + 2
d = Derivative(y, x)

print("== 方法二：符号求导（sympy）==")
print("原函数 f(x)  =", y)
print("导函数 f'(x) =", d.doit())
print("f'(10)       =", d.doit().subs({x: 10}))

# 课后作业：(1 + 1/n)^n 当 n 趋近无穷大时的极限
n = Symbol("n")
print("== 课后作业：极限 ==")
print("lim (1+1/n)^n =", limit((1 + 1 / n) ** n, n, oo))
print("（数学上这个极限就是自然常数 e ≈ 2.71828）")

# 画图：把 f(x) 存成 png
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

xs = [i / 10 for i in range(-60, 31)]
plt.plot(xs, [f(v) for v in xs])
plt.title("f(x) = x^2 + 3x + 2")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.savefig("derivative-plot.png")
print("== 图像 ==")
print("f(x) 的图像已保存到 derivative-plot.png")
```

运行命令与真实输出：

```bash
$ python3 70-derivative.py
== 方法一：数值求导（纯标准库）==
f'(10) ≈ 22.999999984563146
== 方法二：符号求导（sympy）==
原函数 f(x)  = x**2 + 3*x + 2
导函数 f'(x) = 2*x + 3
f'(10)       = 23
== 课后作业：极限 ==
lim (1+1/n)^n = E
（数学上这个极限就是自然常数 e ≈ 2.71828）
== 图像 ==
f(x) 的图像已保存到 derivative-plot.png
```

对照结果：数值求导得到 `22.999999984563146`，符号求导得到精确的 `23`——两者**互相验证**，
那个 `22.999...` 的尾差正是「数值近似」的典型特征。生成的图像见 `code/derivative-plot.png`。

> 💡 `sympy` 输出的 `E` 就是自然常数 **e**（≈ 2.71828），所以极限答案既「算得出」也「看得懂」。

### 课后作业

请使用 `SymPy` 模块计算：当 `n` 趋近无穷大时，`(1 + 1/n)` 的 `n` 次方的极限。

**参考答案**：就是上面代码里的

```python
from sympy import Symbol, limit, oo
n = Symbol("n")
print(limit((1 + 1 / n) ** n, n, oo))   # 输出 E
```

结果为 **`E`**，即自然常数 e，约等于 `2.718281828`。

---

## 第 71 讲 · 再回首："模块与标准库"单元小结

### 本节目标

把本章的「模块导入 / 标准库 / 自定义模块 / 第三方模块」串成一条线，形成整体印象。

### 知识要点

**1. 模块（module）**

模块就是**一个 `.py` 文件**，里面可以放变量、函数、类；用它来**隐藏细节、复用代码**。

**2. 导入方式的对应关系**

| 导入写法 | 调用格式 |
| --- | --- |
| `import 模块` | `模块.函数()` |
| `from 模块 import 函数` | `函数()` |
| `import 模块 as 别名` | `别名.函数()` |
| `import 包.模块` | `包.模块.函数()` |

**3. 三类模块**

- **标准库**：Python 自带，直接 `import`（如 `math` / `json` / `zipfile`）；
- **自定义模块**：自己写的 `.py`，注意别和标准库重名，用 `__name__` 保护测试代码；
- **第三方模块**：`pip install` 装（如 `requests` / `numpy` / `sympy`），建议放**虚拟环境**里。

**4. 完整功能靠多个模块配合**

本章最后的求导例子，就是**标准库**（数值求导）+ **第三方库**（sympy 符号求导、matplotlib 画图）
一起配合完成的——这正是模块化开发的常态。

### 代码实操

完整代码见 `code/71-summary.py`：

```python
# -*- coding: utf-8 -*-
"""第 71 讲 · 再回首：「模块与标准库」单元小结"""
import math
import importlib.metadata as md

# 1. 标准库：不用装，直接 import
print("标准库 math.pi =", round(math.pi, 5))

# 2. 第三方库：先 pip 安装，再 import
import sympy
print("第三方 sympy 版本 =", md.version("sympy"))

# 3. 模块名.成员 的调用方式小结
print("导入与调用方式：")
styles = [
    "import 模块          -> 模块.函数()",
    "from 模块 import 函数 -> 函数()",
    "import 模块 as 别名   -> 别名.函数()",
    "import 包.模块        -> 包.模块.函数()",
]
for i, s in enumerate(styles, 1):
    print(f"  {i}. {s}")
```

运行命令与真实输出：

```bash
$ python3 71-summary.py
标准库 math.pi = 3.14159
第三方 sympy 版本 = 1.14.0
导入与调用方式：
  1. import 模块          -> 模块.函数()
  2. from 模块 import 函数 -> 函数()
  3. import 模块 as 别名   -> 别名.函数()
  4. import 包.模块        -> 包.模块.函数()
```

### 课后作业

回顾本章四个示例，用自己的话回答：

1. 什么时候用 `import 模块`，什么时候用 `from 模块 import 函数`？
2. 自定义模块里为什么建议写 `if __name__ == "__main__":`？
3. 第三方模块为什么建议装在虚拟环境里？

**参考答案**：① 想保留「函数来自哪个模块」的线索、或模块里很多东西都要用时用 `import 模块`；
只用一两个函数、嫌 `模块.` 前缀啰嗦时用 `from 模块 import 函数`。
② 避免别人 import 你的模块时，把只该「直接运行才执行」的测试 / 调用代码也一起跑掉。
③ 隔离依赖，避免和系统默认环境里的包版本冲突、互相污染。

---

## 本章小结

**速查表**

| 主题 | 关键点 |
| --- | --- |
| 模块是什么 | 一个 `.py` 文件，里面放变量 / 函数 / 类 |
| 导入方式 | `import 模块`、`from 模块 import 函数`、`import 模块 as 别名` |
| 包 | 放多个模块的文件夹；`包.模块.函数()` 调用 |
| 标准库 | 随 Python 自带，直接 import：`math` / `json` / `os.path` / `zipfile` |
| 自定义模块 | 自己写的 `.py`；别和标准库重名；用 `__name__` 保护测试代码 |
| 第三方模块 | `pip install` 装：`requests` / `numpy` / `sympy` |
| 虚拟环境 | `python -m venv myvenv` 建，`source .../activate` 进，`deactivate` 出 |
| 加速下载 | `pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名` |
| 求导实战 | 数值求导用标准库；符号求导用 `sympy`；画图用 `matplotlib` |

**三句话**

1. **模块 = 一个 `.py` 文件**，`import` 进来就能复用别人（或自己）写好的函数。
2. 标准库、自定义模块、第三方模块，**import 方式完全一样**，区别只在「从哪来」。
3. 复杂功能不用自己从头造：**多个模块配合**，加上会查官方文档，就够了。

**动手练习**

1. 用 `import random` 写一个「掷骰子」小程序，打印 5 次 1–6 的随机数。
2. 把第 6 章写的购物车函数**抽出来单独存成 `cart.py`**，再写一个 `main.py` 导入它来用。
3. 用 `python -m venv venv` 建一个虚拟环境，激活后 `pip install requests`，`pip freeze` 看看清单。

---

## 下一章预告

下一章我们聊**异常**：程序出错时怎么**捕获**错误、怎么**抛出**自己的异常、
怎么写出「出错也不崩溃」的健壮程序。少一点红字报错，多一点从容应对。

---

[← 上一章：类](/guide/classes) ｜ [返回总目录](/) ｜ [下一章：异常 →](/guide/exceptions)

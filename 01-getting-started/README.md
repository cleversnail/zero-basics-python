# 第 1 章 · 入门的第一道门槛

> 非计算机专业学习编程的第一道门槛：装好环境、选好工具、学会查资料、会读报错。
> **本章 7 讲（001–007）**，不写复杂逻辑，只解决「能不能开始」的问题。

## 🎯 本章目标

- 装好 Python，并能用命令确认「装的是哪个版本」
- 认识主流 IDE（PyCharm / VSCode / Jupyter），知道什么场景用哪个
- 学会靠**官方文档**自己找答案，而不是一有问题就搜二手博客
- 跑通你的第一行代码，理解**交互式**和**非交互式**两种执行方式
- 用 Git / Gitee 管理自己的代码
- 掌握遇到报错时的排查套路：IDE 断点、`print`、`pdb`
- 知道去哪提问、怎么提问

**本章说明**

> 本章以「配置与工具」为主，没有复杂代码。每一个可以真跑的环节都附了**真实终端输出**；
> 需要你亲手在某台电脑上安装的部分（装 Python、装 IDE、注册 Gitee）标注为「动手做」。

| 文件 | 内容 |
| --- | --- |
| `code/01-hello.py` | 第一行代码：`print("Hello Python !")` |
| `code/02-syntax-error.py` | 一段「故意写错」的程序，用来观察语法错误提示 |
| `code/03-pdb-demo.py` | 用 `pdb` 单步调试，观察变量值 |

---

## 第 1 讲 · 如何配置 Python 开发环境？

### 本节目标

从官网装到正确的 Python 版本，并用命令确认它到底装成了没有、装的是哪一个。

### 知识要点

**1. 从官方网站获取安装包**

官方地址：<https://www.python.org/>（Windows / macOS / Linux 都从这里下）。

课程以最新的稳定版 **Python 3.10** 为主；在涉及项目部分的人脸识别功能（第 14 章）时，改用 **Python 3.9**。

**2. 常见操作系统的安装方法**

- 下载安装包
- 运行安装程序，**选择安装路径**
  - Windows 上安装时务必勾选 **Add Python to PATH**，否则终端里敲 `python` 会找不到

**3. 如何验证是否安装成功**

打开终端（Windows 叫「命令提示符」），敲：

```bash
python3 -V
```

本机实测输出：

```
Python 3.12.7
```

看到 `Python 3.x.x` 就说明装好了。`-V` 是「显示版本」的意思。

**4. 如何区分电脑里的多个 Python 版本**

很多系统（尤其是 macOS / Linux）自带一个 Python 2，你装的又是 Python 3。这时：

```bash
python3 -V      # 通常是新版本
python -V       # 可能是老版本
```

课程里举的例子：

```
shell ~ % python3 -V
Python 3.10.7
shell ~ % python -V
Python 2.7.12
```

> ⚠️ **避坑**：电脑里存在多个 Python 版本会显著增加开发难度——你 `pip install` 装的包，可能装进了另一个 Python 里，跑代码时却「找不到模块」。**原则：认准一个版本，全程用它。**

### 代码实操

本机实测（终端里直接敲，不需要写文件）：

```bash
$ python3 -V
Python 3.12.7
$ python -V
Python 3.12.7
```

> 你电脑上的版本号大概率不同（3.10、3.11、3.13 都行）——只要 ≥ 3.10 就能跑通全书。
> 版本号不同不影响，**这一讲要的是「能确定自己用的是哪一个」**。

### 课后作业

请在你安装 Python 之前和之后，分别执行：

```bash
python -V
python3 -V
```

观察安装前后提示的变化。

---

## 第 2 讲 · 常用 IDE：如何提高开发效率？

### 本节目标

认识三款主流 IDE，知道什么场景该用哪一个。

### 知识要点

**主流 IDE**

| IDE | 官网 | 特点 |
| --- | --- | --- |
| **PyCharm** | <https://www.jetbrains.com/pycharm/download> | 功能最全，适合大型项目；社区版免费 |
| **VSCode** | <https://code.visualstudio.com/> | 轻量、插件丰富，前端/Python 通用 |
| **Jupyter Notebook / Lab** | <https://jupyter.org/> | 交互式一行一行跑，适合数据分析与教学 |

**Jupyter 的安装与启动**（命令行）：

```bash
pip3.10 install jupyterlab
jupyter-lab
# 或者装经典版 Notebook
pip3.10 install notebook
notebook
```

**IDE 的三个优点**

1. **自动提示**：补全代码、显示函数用法
2. **自动错误提示**：写错当场标红，不用等运行
3. **支持快捷键**：效率翻倍

**应用场景怎么选**

- 适合**本地开发**：VSCode、PyCharm
- 适合**远程开发**：Jupyter（因为它跑在浏览器里，连服务器很方便）

> 💡 **IDE 不是必需品，但是对新手更友好**：它把「语法错误」提前到写代码的当下，而不是运行的时候才发现。

### 代码实操

本讲没有需要写的逻辑代码。课程留的练习是让你在装好的 IDE 里跑这一行：

```python
print("Hello Python !")
```

它的真实运行结果见下一讲的 `code/01-hello.py`。

### 课后作业

在你的电脑上安装 **VSCode** 和 **Jupyter** 两种 IDE，并运行：

```python
print("Hello Python !")
```

---

## 第 3 讲 · 如何站在官方文档的肩膀上自己「造轮子」？

### 本节目标

理解「造轮子」的含义，学会查 Python 官方文档的四个部分。

### 知识要点

**什么是「造轮子」**

> **造轮子**：别人已实现的功能，自己又重新开发了一遍。

作者的观点不是「不要造轮子」，而是——**造之前先看官方文档**，搞清楚现成的轮子是什么样、为什么这么设计。

**官方文档的四个部分**

| 部分 | 用途 | 地址 |
| --- | --- | --- |
| **版本变化** | 每个版本新增 / 优化 / 弃用了什么（PEP） | 见 `What's New` |
| **教程（Tutorial）** | 入门级系统性讲解 | <https://docs.python.org/zh-cn/3.10/tutorial/index.html> |
| **标准库参考** | 常用库的用法速查，「放在枕边」那种 | <https://docs.python.org/zh-cn/3.10/library/index.html> |
| **语言参考** | 语法与「核心语义」的权威定义 | <https://docs.python.org/zh-cn/3.10/reference/index.html> |

**几个名词**

1. **PEP**（Python Enhancement Proposals）—— Python 增强提案，所有语言特性都先有 PEP
2. 新的特性
3. 性能优化和改进
4. 弃用和移除

> 📖 语言参考手册的原话：它介绍 Python 的句法与「核心语义」；内置对象类型、内置函数、模块的语义在**标准库**里介绍；非正式入门请参阅**教程**。对 C/C++ 程序员，还额外提供「扩展和嵌入 Python 解释器」与「Python/C API 参考手册」。

### 代码实操

本讲为方法讲解，无需运行代码。建议动手：打开
<https://docs.python.org/zh-cn/3.10/library/index.html>，在搜索框里搜一个你认识的内置函数（比如 `print`），看它的官方说明长什么样。

### 课后作业

1. 根据官方文档，至少说出 **Python 3 和 Python 2** 的三点主要差异。
2. 根据官方文档，**Python 3.10 相比 3.6** 都做了哪些改变？至少三点。

---

## 第 4 讲 · 怎样运行你的第一行代码？

### 本节目标

跑通第一行代码，并分清**解释器执行程序的两个过程**、**交互与非交互**两种运行方式。

### 知识要点

**1. Python 程序的执行过程**

```
源代码 ──编译/解释──► 字节码 ──► Python 虚拟机 ──► 执行
                        │
                        └──► 二进制 ──► 执行
```

Python 是**解释型语言**：你敲下的源码先被解释器编译成**字节码**，再由 **Python 虚拟机**执行。
所以「写 → 跑」之间没有单独的编译步骤，改一行就能立刻重跑。

**2. 运行你的第一行代码**

在 VSCode / Jupyter 里新建文件，写入：

```python
print("Hello Python !")
```

**3. 交互式 vs 非交互式**

| 方式 | 命令 | 说明 |
| --- | --- | --- |
| **非交互**执行脚本 | `python3.10 hello.py` | 从开始跑到结束，不中断 |
| **交互**执行脚本 | `python3.10 -i hello.py` | 跑完**停留在解释器里**，可以继续敲命令 |

- **交互**：解释器执行完用户命令后，等用户再输入指令才继续，否则一直等待。
- **非交互**：程序从开始到结束，不会被解释器中断。

### 代码实操

**非交互式**——直接跑 `code/01-hello.py`：

```bash
$ python3 01-hello.py
Hello Python !
```

**交互式**——加 `-i`，跑完停在 `>>>` 里，可以接着做计算：

```bash
$ python3 -i 01-hello.py
Hello Python !
>>> print(1 + 1)
2
>>> exit()
```

> 注意：非交互模式下那句 `print(1 + 1)` 是**不会**执行的——因为你根本没写进文件里。
> 这正是「交互」的意义：**边跑边试**。

### 课后作业

请使用**交互模式**和**非交互模式**分别运行：

```python
print("Hello Python !")
```

---

## 第 5 讲 · 怎样使用 Gitee 管理你的代码？

### 本节目标

知道为什么用 Git，跑通「上传 / 下载代码」的基本操作。

### 知识要点

**为什么要用 Git 管理源代码**

1. **多人协作**——多人改同一份代码而不互相覆盖
2. **版本控制**——每一次改动都有记录，随时回到过去
3. **备份**——推到远程仓库，本地硬盘坏了代码还在

**操作 Git 的两种方式**

- 通过**网页**操作（Gitee / GitHub 的图形界面）
- 通过 **Git 常用命令**（终端里操作，效率更高）

**注册 Gitee 账号**

<https://gitee.com/>

**Gitee 最常用的两个操作**

1. **怎样上传**代码
2. **怎样下载**代码

常用的几组命令：

```bash
# 下载（克隆）一个仓库
git clone https://gitee.com/你的用户名/你的仓库.git

# 每天改完代码后的三连
git add .
git commit -m "说明这次改了什么"
git push
```

> 💡 远程仓库（Gitee / GitLab）的核心价值是**异地备份** + **协作**。
> 也要注意：`git clone` 后面跟的地址，决定了本地会生成一个**同名目录**。

### 代码实操

本讲以网页操作演示为主，命令见上方代码块。课程作业要求你把代码真正推到一个 Gitee 仓库上。

### 课后作业

注册一个 Gitee（或公司内部的 GitLab）账号，把你编写的代码上传到 Gitee，并通过网页查看。

---

## 第 6 讲 · 学习编程有问题？去这里找答案！

### 本节目标

建立自己的「求助顺序」：先文档、再搜索、最后社区。

### 知识要点

**1. 正确使用搜索引擎**

关键词技巧：

- `filetype: pdf python`——只搜 PDF 格式的资料
- `contents: time.geekbang.org python`——限定在某个站点的正文里搜

**2. 学会使用文档**

- 官方文档：<https://docs.python.org/zh-cn/3.10/tutorial/index.html>
- 第三方库文档（以 requests 为例）：<https://docs.python-requests.org/zh_CN/latest/>

**3. Stack Overflow**

<https://stackoverflow.com/> —— 全球程序员问答社区，绝大多数报错都能在这里搜到。

**4. Gitee / GitHub 代码参考**

在代码托管平台也可以搜代码，常用限定词：

- `in:name`——仓库名里包含关键词
- `in:readme`——README 里包含关键词
- `in:description`——描述里包含关键词

**推荐的求助顺序**：报错信息 → 官方文档 → 搜索引擎 → 社区（Stack Overflow）→ 提问。

> 📖 **提问本身就是一项能力**。提问前先读
> [《提问的智慧》](./How-To-Ask-Questions-The-Smart-Way.md)——这也是本讲的指定阅读材料。
> 一个高质量的提问应该包含：你想做什么、你试了什么、完整的报错、你的环境版本。

### 代码实操

本讲为方法讲解，无需运行代码。

### 课后作业

你和同学执行了**同一段出错的代码**，报错却不一样：

```python
e = {'a':1,
```

你的（Python 3.10）：

```
    e = {'a':1,
       ^
SyntaxError: '{' was never closed
```

同学的：

```
    e = { 'a':1,
             ^
SyntaxError: unexpected EOF while parsing
```

能否用本讲学到的知识，找出「同样代码、提示不同」的原因？
（提示：去看两个版本的官方文档里这条报错是怎么写的。）

---

## 第 7 讲 · 调试程序：代码出错了！怎么办？

### 本节目标

掌握三层调试手段：**IDE 断点** → **print 中间结果** → **pdb 命令行调试器**。

### 知识要点

**1. 使用 IDE 自带的调试器**

先分清错误的类型：

| 类型 | 表现 | 例子 |
| --- | --- | --- |
| **语法错误** | 程序**根本跑不起来** | 少括号、多缩进 |
| **程序逻辑错误** | 能跑，但**结果不对** | 该加写成减 |

调试三步：

1. 在可能出错的代码**前**设一个断点
2. 以**调试方式**运行，观察程序运行状态（变量值）
3. 解决 bug 后**再次执行**

**2. 使用 `print` 输出中间结果**

`print()` 是 Python 的标准输出函数。在想不通的地方把变量打出来，看它到底是多少：

```python
print("到这里时 x =", x)
```

**3. 使用 `pdb` 调试器**

`pdb` 是 Python 自带**命令行调试器**。两种进入方式：

```python
# 写法一（老写法，兼容所有版本）
import pdb; pdb.set_trace()

# 写法二（Python 3.7+，更推荐）
breakpoint()
```

常用命令：

| 命令 | 解释 |
| --- | --- |
| `break` | 设置断点 |
| `continue` | 继续执行 |
| `exit` | 终止并退出 |
| `next` | 执行下一行 |
| `pp` | 打印变量的值 |

也可以在命令行直接调起：

```bash
python -m pdb app.py arg1 arg2
```

### 代码实操

**示例 A：看清一段程序的语法错误**

`code/02-syntax-error.py` 是一段「故意写错」的程序，真实运行结果：

```bash
$ python3 02-syntax-error.py
  File "/path/to/code/02-syntax-error.py", line 9
    print("hello")
IndentationError: unexpected indent
```

读报错要**从下往上读**：最后一行是错误类型（`IndentationError: unexpected indent`，
多了不该有的缩进），倒数第二行给出出错位置（`line 9`）。

> 📌 这正是「第 6 讲」作业想问你的：**同样的代码，不同 Python 版本给的报错信息可能不同**。
> 因为解释器在迭代，提示会越来越精确。

**示例 B：用 pdb 单步调试**

`code/03-pdb-demo.py` 在 `pdb.set_trace()` 处会暂停。自动喂命令运行（等价于你手敲）：

```bash
$ printf 'pp x\npp y\nn\nn\nc\n' | python3 03-pdb-demo.py
> /path/to/code/03-pdb-demo.py(16)main()
-> z = add(x, y)
(Pdb) 10
(Pdb) 20
(Pdb) > /path/to/code/03-pdb-demo.py(17)main()
-> print(f"x + y = {z}")
(Pdb) x + y = 30
--Return--
> /path/to/code/03-pdb-demo.py(17)main()->None
-> print(f"x + y = {z}")
(Pdb)
```

逐行解读：

1. 停在 `add(x, y)` 这一行（第 16 行）之前 —— `(Pdb)` 是提示符
2. `pp x` → 打印出 `10`（`pp` = pretty print）
3. `pp y` → 打印出 `20`
4. 两次 `n`（next）→ 执行到下一行，打印出 `x + y = 30`
5. `c`（continue）→ 继续执行到程序结束

### 课后作业

修改下面这段程序，让它能正确运行并输出**三个 hello**：

```python
# 以下是出错的程序，请改正：
print("hello")
   print("hello")
print("hello"
```

> 参考答案：第 2 行去掉多余缩进；第 3 行补上右括号 `)`。
> 正确写法就是 `code/01-hello.py` 那种形式——三行 `print`，各自顶格、括号闭合。

---

## 本章小结

**速查表**

| 主题 | 关键命令 / 结论 |
| --- | --- |
| 查 Python 版本 | `python3 -V` |
| 跑脚本（非交互） | `python3 hello.py` |
| 跑完停在解释器（交互） | `python3 -i hello.py` |
| 装 Jupyter | `pip install jupyterlab` → `jupyter-lab` |
| 克隆仓库 | `git clone <url>` |
| 提交三连 | `git add .` → `git commit -m "..."` → `git push` |
| 打断点 | `pdb.set_trace()` 或 `breakpoint()` |
| 官方文档 | docs.python.org（教程 / 库参考 / 语言参考 / 版本变化） |

**三句话**

1. 环境是第一道门槛：**认准一个 Python 版本，全程用它**。
2. 遇到问题先查**官方文档**，再搜，再问——报错要从下往上读。
3. 调试三层：**IDE 断点 → print → pdb**，能定位到「哪一行、变量是多少」就赢了一大半。

**动手练习**

1. 装好 Python，用 `python3 -V` 确认版本。
2. 装好 VSCode 和 Jupyter，各跑一次 `print("Hello Python !")`。
3. 把 `code/02-syntax-error.py` 的 3 处错误改对，让它输出 3 个 hello。
4. 注册 Gitee，把本章代码推上去。

---

## 下一章预告

第 2 章进入**真正的 Python 语法**：输入输出、变量、字符串、数字类型、
注释、以及第一个小项目「简易计算器」。

---

[← 上一章：课程综述](/guide/intro) ｜ [返回总目录](/) ｜ [下一章：Python 编程基础知识 →](/guide/python-basics)

# 第 2 章 · Python 编程基础知识

> 从「Hello Python」到第一个小项目：把输入输出、变量、字符串、数字、注释、命名规范一次打通。
> **本章 10 讲（008–017）**，学完就能写一个能算四则运算的简易计算器。

## 🎯 本章目标

- 用 `input()` / `print()` 完成「输入 → 存储 → 输出」的基本流程
- 用**变量**给数据贴标签，理解「赋值」和「变量随时可改」
- 掌握**字符串**的定义、基本操作与常用方法
- 分清**数字类型**（整数 / 浮点数 / 复数），会做显式**类型转换**
- 说清「什么时候用数字、什么时候用字符串」
- 会用 `#` 写注释，认识「Python 之禅」
- 动手做出一个简易**四则运算计算器**
- 遵守**变量命名规范**，写出能读、不容易出错的代码

**本章代码**

> 📌 **代码约定**：正文代码块都保持**可直接运行**；节选会明确标注「节选」并指向 `code/` 完整文件。
> 所有输出都是**真实运行结果**（本机 Python 3.12.7）。
> ⚠️ 讲义里的 `input()` 会停下来等你在键盘上敲字，**交互输入无法在文档里演示**，
> 因此 `code/` 里的示例一律把键盘输入换成固定值，效果完全等价，正文会注明。

| 文件 | 内容 |
| --- | --- |
| `code/08-input-output.py` | 输入输出：`input()` / `print()` 与「反序输出」 |
| `code/09-variables.py` | 变量：赋值、改变量、连续赋值、元组解包 |
| `code/10-strings-basics.py` | 字符串（上）：定义、f-strings、成员/连接/切片运算 |
| `code/11-string-methods.py` | 字符串（下）：`count` / `isalnum` / `join` / `split` / `startswith` |
| `code/12-numbers.py` | 数字类型：常见运算、`type()`、强制类型转换 |
| `code/13-number-vs-string.py` | 数字 vs 字符串：一张运算符表，两类数据类型 |
| `code/14-comments.py` | 注释：`#`、多行说明、`import this` |
| `code/15-calculator.py` | 简易计算器：用 `eval()` 执行表达式字符串 |
| `code/16-naming.py` | 变量命名规范：合法名、关键字、好习惯 |
| `code/17-summary.py` | 本章总结：变量 / 数据类型 / 输入输出串讲 |

---

## 第 8 讲 · 修炼基本功：浅析输入输出

### 本节目标

看懂通用计算机模型里的「输入 → 计算/存储 → 输出」，并用 `input()`、`print()` 两个内置函数完成一次完整的输入输出。

### 知识要点

**1. 通用计算机模型**

现代计算机基于**冯·诺依曼结构**，无论多复杂，它做的事永远绕不开四类任务：**输入、输出、计算、存储、控制**。写程序，就是把一件事拆成这几个部件。

举个例子——「算三个小数相乘」可以拆成：

- 输入：读到三个小数
- 存储：把它们临时记下来
- 计算：做两次乘法
- 输出：把结果打印出来

**2. 输入的分类**

- **物理设备**：键盘、鼠标、传感器、雷达、摄像头……
- **逻辑概念**：终端、文件、程序的可视化窗口……

**3. `input()` 和 `print()` 的定位**

它们是 Python 的**内置函数**（built-in function）——装好 Python 就能直接用，不需要 `import`，可以反复调用（**调用**就是让函数干活的动作，写法是函数名后面跟一对括号）。

> 📖 完整内置函数清单：<https://docs.python.org/zh-cn/3.10/library/functions.html>

**4. 一个关键问题：输入的内容存到哪？**

`input()` 读进来的东西，如果不「接住」，它转身就没了。要把它存下来，就得用**变量**（下一讲的主角）。这一讲先记住这个动作：

```python
var1 = input("输入第一行内容\n")   # 把读到的内容存进 var1
```

`=` 是**赋值语句**：把右边得到的结果，交给左边的名字保存。

### 代码实操

**示例：两行内容反序输出 + 连续输出三次**

完整代码见 `code/08-input-output.py`。讲义原始版本用 `input()` 等键盘输入，**交互输入无法在文档里演示**，这里用固定值代替：

```python
# 讲义写法：var1 = input("输入第一行内容\n")
# 等价的可运行写法：用固定值代替键盘输入
var1 = "这是第一行"
var2 = "这是第二行"

print("第二行的内容是")
print(var2)
print("第一行的内容是")
print(var1)

line = "我学会了输入输出"
print(line)
print(line)
print(line)
```

运行：

```bash
$ cd code && python3 08-input-output.py
```

真实输出：

```
Hello Python!
第二行的内容是
这是第二行
第一行的内容是
这是第一行
我学会了输入输出
我学会了输入输出
我学会了输入输出
```

注意看：输入的顺序是「第一行、第二行」，输出时**先打第二行、再打第一行**——这就是用变量把数据存下来后，随意调整输出顺序的能力。

### 课后作业

编写一个程序，把用户输入的一行内容**连续输出三次**。

> 参考答案：`code/08-input-output.py` 最后 4 行。核心就是把这行内容存进一个变量 `line`，再 `print(line)` 三遍。

---

## 第 9 讲 · 变量：如何让计算机临时存储数据？

### 本节目标

搞清楚变量是什么、`=` 在干什么、变量为什么能反复改；掌握「一次赋多个变量」的写法。

### 知识要点

**1. 变量是什么**

> **变量（variable）**：程序运行过程中，用来**临时保存数据**的对象。你可以把它理解为「给内存里的数据贴的标签」——贴了什么名字，以后就用这个名字把数据取出来。

一行赋值 `text = input()` 拆开看：

| 部分 | 名称 | 含义 |
| --- | --- | --- |
| `text` | 变量名 | 给这块数据贴的标签 |
| `=` | 赋值操作符 | 把右边的结果交给左边保存 |
| `input()` | 值 | 右边算出来的东西 |

⚠️ 注意：编程里的 `=` 不是「相等」，而是**「把右边装进左边」**。判断相等用的是 `==`。

**2. 变量指向一个值**

在 Python 里，每个变量都**指向**一个值。除了用 `input()` 拿输入，也可以直接把值写给变量：

```python
x = 1
y = "hello"
```

**3. 变量理解为「贴标签」**

```
x  ──►  123          # x = 123
y  ──►  "abc"        # y = "abc"
y  ──►  "zzz"        # 再执行 y = "zzz"，标签 y 就改指向新值了
```

同一个标签可以随时改指向——这就是「变量」名字里「变」的含义。

**4. 几种不同的赋值写法**

| 写法 | 含义 |
| --- | --- |
| `a, b = 1, 2` | 一行同时给两个变量赋不同的值（叫**元组解包**） |
| `x = y = z = 3` | 连续赋值，三个变量都指向 `3` |

### 代码实操

完整代码见 `code/09-variables.py`。讲义用 `input()` 读入，**交互输入无法在文档里演示**，这里用固定值代替：

```python
text = "hello"
print(text); print(text); print(text)

x = 123
print(x)

x = 456          # 改变量：x 现在指向 456
print(x)

y = x            # 把 x 的值赋给 y
print(y)

z = y = x        # 连续赋值
print(z)

a, b = 111, 222  # 元组解包
print(a)
print(b)

pi = 3.14        # 课后作业
print(pi)
```

运行：

```bash
$ cd code && python3 09-variables.py
```

真实输出：

```
hello
hello
hello
123
456
456
456
111
222
3.14
```

### 课后作业

定义一个变量 `pi`，赋值为 `3.14`，并用 `print()` 输出 `pi` 的值。

> 参考答案：`pi = 3.14` 然后 `print(pi)`，输出 `3.14`（见上面输出最后一行）。

---

## 第 10 讲 · 字符串（上）：Python 是如何处理单词的？

### 本节目标

学会用三种引号定义字符串，会用 f-strings 把变量插进字符串，并掌握字符串的成员、连接、切片三类基本操作。

### 知识要点

**1. 什么是字符串**

> **字符串（string，类型名 `str`）**：一串文本字符，是 Python 最常用的数据类型之一。平时看到的单词、句子、文章，都是字符串。

**2. 三种定义方式**

| 写法 | 特点 |
| --- | --- |
| 单引号 `'...'` | 里面可以再放双引号 |
| 双引号 `"..."` | 里面可以再放单引号 |
| 三重引号 `'''...'''` 或 `"""..."""` | 可以**跨多行** |

**3. 字符串里插入变量：f-strings**

在字符串前加一个 `f`，用 `{变量名}` 占位，运行时会被替换成变量的值：

```python
x = 123
print(f"{x} 是变量 x 的值")
```

> ⚠️ f-strings 需要 **Python 3.6 以上**版本（本机 3.12.7，没问题）。

**4. 三类基本操作**

| 运算 | 写法 | 含义 |
| --- | --- | --- |
| 成员运算 | `x in s` / `x not in s` | 子串在不在这里面，返回 `True` / `False` |
| 连接运算 | `s + t` / `s * n` | 拼接两个字符串 / 把 s 重复 n 次 |
| 切片运算 | `s[i]` / `s[i:j]` / `s[i:j:k]` | 取第 i 项 / 取 i 到 j（不含 j）/ 取 i 到 j 步长 k |

> 📌 **下标从 0 开始**：`s[0]` 是第一个字符；负数表示从后往前，`s[-1]` 是最后一个字符。

### 代码实操

完整代码见 `code/10-strings-basics.py`：

```python
print("Hello Python")               # 双引号
print('Hello " Python " ')          # 单引号里放双引号
print('''
Hello
Python
''')                                 # 三重引号，跨多行

x = 123
print(f"{x}： {x} 是变量 x 的值 ")    # f-strings

print("xy" in "123xy456")            # 成员运算
print("x" not in "123x456")

print("abc" + "xyz")                 # 连接运算
x = "abc"; y = "xyz"
print(x + y); print(x * 3); print(x); print(y)

s = "abcdefg"                        # 切片运算
print(s[0]); print(s[-1]); print(s[1:5:2])
```

运行：

```bash
$ cd code && python3 10-strings-basics.py
```

真实输出：

```
Hello Python
Hello " Python " 

Hello
Python

123： 123 是变量 x 的值 
True
False
abcxyz
abcxyz
abcabcabc
abc
xyz
a
g
bd
```

切片 `s[1:5:2]` 得到 `bd` 的推演：`s = "abcdefg"`，下标 1、3 分别是 `b`、`d`（步长 2，也就是「隔一个取一个」，到 5 前停）。

### 课后作业

自己定义几个字符串，分别用单引号、双引号、三重引号，再用 `+` 和 `*` 各拼一个新串出来。

---

## 第 11 讲 · 字符串（下）：Python 是如何处理单词的？

### 本节目标

认识「方法」这个概念，掌握字符串最常用的六个方法：`count`、`isalnum`、`isalpha`、`join`、`split`、`startswith`。

### 知识要点

**1. 什么是「方法」**

> **方法（method）**：挂在某个对象身上的函数。写法是 `对象.方法名(参数)`，比如 `"abc".count("a")`——对字符串 `"abc"` 执行 `count`。

每种数据类型都内置了很多方法，专门用来处理这种类型的数据。

**2. 本讲重点方法**

| 方法 | 作用 | 例子 → 结果 |
| --- | --- | --- |
| `str.count(sub)` | 统计子串 `sub` 出现次数 | `"abab".count("a")` → `2` |
| `str.isalnum()` | 是否全是字母或数字（且至少一个字符） | `"a1".isalnum()` → `True` |
| `str.isalpha()` | 是否全是字母（且至少一个字符） | `"a1".isalpha()` → `False` |
| `str.join(iterable)` | 用当前字符串做「胶水」把序列拼起来 | `",".join("abc")` → `'a,b,c'` |
| `str.split(sep)` | 按分隔符拆成列表 | `"a,b".split(",")` → `['a', 'b']` |
| `str.startswith(prefix)` | 是否以某前缀开头 | `"xyz".startswith("y")` → `False` |

> 💡 `join` 和 `split` 是一对**互逆**操作：`",".join(["a","b"])` 拼成 `"a,b"`，`"a,b".split(",")` 又拆回 `['a','b']`。

> 📖 字符串全部方法：<https://docs.python.org/zh-cn/3.10/library/stdtypes.html#string-methods>

### 代码实操

完整代码见 `code/11-string-methods.py`：

```python
print("xyzxyzxyz".count("x"))
print("xyzxyzxz".count("xy"))
print("xyzxyzxz".count("a"))
print("xyzxyzxz".isalnum())
print("xyzxyzxz".isalpha())
print(",".join("abcdefg"))
print("a,b,c,d".split(","))
print("xyz".startswith("y"))

# 课后作业：统计 better 出现次数
text = (
    "Beautiful is better than ugly.\n"
    "Explicit is better than implicit.\n"
    "Simple is better than complex."
)
print(text.count("better"))
```

运行：

```bash
$ cd code && python3 11-string-methods.py
```

真实输出：

```
3
2
0
True
True
a,b,c,d,e,f,g
['a', 'b', 'c', 'd']
False
3
```

### 课后作业

统计下面这段文章里，单词 `better` 出现的次数并输出：

```
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
```

> 参考答案：用 `count` 一把梭——`text.count("better")`，结果是 `3`（见上面输出最后一行）。

---

## 第 12 讲 · 存储数字应该采用哪种数据类型？

### 本节目标

分清整数、浮点数、复数三种数字类型，掌握数字的常见运算，并学会用 `int()` / `float()` / `str()` 做**显式类型转换**。

### 知识要点

**1. 三种数字类型**

| 类型 | 名称 | 例子 |
| --- | --- | --- |
| `int` | 整数 | `123`、`-7`、`0` |
| `float` | 浮点数（带小数点的数） | `3.14`、`2.0`、`-0.5` |
| `complex` | 复数 | `3+4j` |

**2. 常见运算**

| 运算 | 含义 | 例子 → 结果 |
| --- | --- | --- |
| `x + y` | 和 | `7 + 3` → `10` |
| `x - y` | 差 | `7 - 3` → `4` |
| `x * y` | 积 | `7 * 3` → `21` |
| `x / y` | 商（**总是浮点数**） | `7 / 3` → `2.333...` |
| `x // y` | 整除（向下取整） | `7 // 3` → `2` |
| `x % y` | 余数 | `7 % 3` → `1` |
| `x ** y` 或 `pow(x, y)` | x 的 y 次幂 | `2 ** 10` → `1024` |

还有 `abs(x)`（绝对值）、`divmod(x, y)`（返回 `(商, 余数)`）、`complex(re, im)`（造复数）等。

**3. Python 是强类型语言**

> **强类型**：数据的类型不会在运算中途被悄悄改变，必须**显式转换**。用 `type()` 可以查看一个值到底是什么类型。

**4. 类型转换**

| 函数 | 作用 | 注意 |
| --- | --- | --- |
| `int(x)` | 转成整数 | 浮点 → 整数是**直接截断**小数部分；字符串 → 整数要求里面**全是数字**，否则报错 |
| `float(x)` | 转成浮点数 | |
| `str(x)` | 转成字符串 | |

### 代码实操

完整代码见 `code/12-numbers.py`：

```python
print(7 + 3); print(7 - 3); print(7 * 3)
print(7 / 3); print(7 // 3); print(7 % 3)
print(-(7)); print(+(7))
print(abs(-5)); print(int(3.9)); print(float(3))
print(complex(3, 4)); print(divmod(7, 3))
print(pow(2, 10)); print(2 ** 10)

print(type(123)); print(type(3.14))
print(int(123.456))

abc = "123"
xyz = int(abc)
print(type(xyz))

print(str(456)); print(type(str(456)))

# 课后作业：两个整数求和（讲义用 input()，这里用固定值）
num1 = int("12"); num2 = int("30")
print(num1 + num2)
```

运行：

```bash
$ cd code && python3 12-numbers.py
```

真实输出：

```
10
4
21
2.3333333333333335
2
1
-7
7
5
3
3.0
(3+4j)
(2, 1)
1024
1024
<class 'int'>
<class 'float'>
123
<class 'int'>
456
<class 'str'>
42
```

### 课后作业

编写程序，让用户通过命令行输入两个整数，程序自动计算它们的和。

> 参考答案：`input()` 读进来的是**字符串**，所以要先 `int()` 再相加——`num1 = int(input()); num2 = int(input()); print(num1 + num2)`。
> 上面示例用固定值 `"12"` 和 `"30"` 代替键盘输入，输出 `42`。

---

## 第 13 讲 · 何时使用数字，何时使用字符串？

### 本节目标

看清「同一套运算符，作用在数字和字符串上结果完全不同」，理解「什么时候用数字、什么时候用字符串」，并认识跨类型运算会报 `TypeError`。

### 知识要点

**1. 为什么要区分数据类型**

Python（还有 Java 等）都是**强类型语言**：类型不会因为运算中途改变，要改必须显式转。区分类型有三个好处：

1. 有**代码提示**（IDE 知道这个变量能干哪些事）
2. **执行效率高**
3. **安全、出错率低**

**2. 各管各的**

- **字符串**：负责统计、语义（处理文字）
- **数字**：负责计算（处理数学）

**3. 同一套运算符，两种行为**

| 表达式 | 结果 | 为什么 |
| --- | --- | --- |
| `100 + 200` | `300` | 数字做加法 |
| `"100" + "200"` | `"100200"` | 字符串做**拼接** |
| `456 > 1234` | `False` | 数字按大小比 |
| `"456" > "1234"` | `True` | 字符串按**字典序**比（逐位比字符） |
| `len("456") > len("1234")` | `False` | 先取长度：3 和 4，再比大小，3 > 4 为假 |

> 💡 `"456"` 比 `"1234"` 大，是因为它先比第一个字符 `'4'` 和 `'1'`，`'4'` 更大就立刻定了胜负——字符串比较**不看整体数值大小**。

**4. 跨类型运算会报错**

```python
>>> 123 + "456"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

数字和字符串不能直接相加，必须先转成同一类型。

### 代码实操

完整代码见 `code/13-number-vs-string.py`。演示报错那行用 `try/except` 把错误接住打印，方便在文档里看到真实报错文案：

```python
print(100 + 200)
print(456 > 1234)
print("100" + "200")
print("456" > "1234")
print(len("456") > len("1234"))

try:
    print(123 + "456")
except TypeError as err:
    print("TypeError:", err)
```

运行：

```bash
$ cd code && python3 13-number-vs-string.py
```

真实输出：

```
300
False
100200
True
False
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

### 课后作业

判断以下每行代码的执行结果：

| 代码 | 结果 | 理由 |
| --- | --- | --- |
| `"ABC" > "ABD"` | `False` | 逐位比到第 3 个字符，`'C' < 'D'` |
| `"ABC" > 123` | 报错 `TypeError` | 字符串不能和整数比较 |
| `123.0 > 123` | `False` | 浮点数和整数可直接比大小，两者相等 |
| `"123.0" > "123"` | `True` | 都是字符串，按字典序 `"123.0"` 更长、排在后 |

上面 `"ABC" > "ABD"`、`"ABC" > 123`、`123.0 > 123`、`"123.0" > "123"` 的真实运行结果依次为：

```
False
TypeError: '>' not supported between instances of 'str' and 'int'
False
True
```

---

## 第 14 讲 · 注释：如何写程序的说明书？

### 本节目标

学会用 `#` 写注释，知道注释该写在哪、写什么，并认识「Python 之禅」。

### 知识要点

**1. 怎么写注释**

- 注释的标识符是**井号 `#`**
- `#` 之后的内容会被 Python 解释器**忽略**（只给人看）

**2. 注释的位置**

```python
# 注释
# 注释    一段代码    # 注释
# 注释
```

可以单独占一行，也可以写在代码后面。

**3. 注释写什么**

注释的目的是说明代码的**用途和原理**——「做什么、怎么做」，力求简单、无歧义。对比两种写法：

```python
# 注释 1：只复述了代码（信息量低）
# 为变量 pi 赋值为 3.14
pi = 3.14

# 注释 2：说明了用途（信息量高）
# 变量 pi 用于计算圆的面积
pi = 3.14
```

**4. Python 之禅**

`import this` 会打印 Tim Peters 写的 **The Zen of Python（Python 之禅）**——一组写优雅代码的心法，比如：

- *Beautiful is better than ugly.*（优美胜于丑陋）
- *Explicit is better than implicit.*（显式胜于隐式）
- *Simple is better than complex.*（简单胜于复杂）
- *Readability counts.*（可读性很重要）

### 代码实操

完整代码见 `code/14-comments.py`：

```python
# 变量 pi 用于计算圆的面积
pi = 3.14
radius = 2
area = pi * radius * radius
print(area)

"""
这是一段多行说明。
一般放在文件开头，写清这个程序是干什么的。
"""

import this
```

运行：

```bash
$ cd code && python3 14-comments.py
```

真实输出：

```
12.56
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

### 课后作业

为上一讲「计算两数之和」的作业补上注释。

> 参考答案：给每行都写上「为什么」，而不只是「做了什么」。例如在 `num1 = int(input())` 上面写 `# 读入第一个数，input() 返回字符串，用 int 转成整数才能相加`。

---

## 第 15 讲 · 小试牛刀：如何制作简单计算器？

### 本节目标

把「输入输出 + 变量 + 字符串 + 数字类型转换」合起来，做出一个能算四则运算的简易计算器，并认识 `eval()`。

### 知识要点

**1. 问题分解（需求分析）**

做一个计算器，先想清楚：

- 需求分析 1：实现简单的计算，用户自行输入算式
- 需求分析 2：实现两个整数的四则运算，用户输入两个数后输入运算符，程序据此输出结果

> 程序设计包括：需求分析 → 代码编写 → 测试 → 维护和迭代。

**2. 使用数字和字符串**

- 用户从键盘输入的数字，被 Python 当成**字符串**处理
- 字符串**不能直接做算术运算**，得先类型转换
- 转换后再计算

**3. 解决未知问题：`eval()`**

「怎样执行字符串里的表达式？」查官方文档和搜索引擎，答案是 **`eval()` 函数**——它能把一个「表达式字符串」当代码执行，算出结果。

```python
eval("12+30")     # 得到 42
eval("8*4")       # 得到 32
```

配合 f-strings，把用户输入的两个数和运算符拼成表达式字符串：

```python
result = eval(f"{num1}{op}{num2}")
```

> ⚠️ `eval()` 会执行字符串里的内容，方便但**要小心**：只用来处理你自己拼出来的、可信的表达式，不要直接 `eval()` 用户输入的任意字符串。

### 代码实操

完整代码见 `code/15-calculator.py`。讲义用 `input()` 读键盘，**交互输入无法在文档里演示**，这里用固定值代替：

```python
# 版本一：只算加法
num1 = "12"; num2 = "30"
total = eval(f"{num1}+{num2}")
print(total)

# 版本二：支持四则运算
a = "8"; b = "4"; op = "*"
result = eval(f"{a}{op}{b}")
print(f"计算结果为{result}")

# 课后作业：支持浮点数
a = "1.5"; b = "2.5"; op = "+"
result = eval(f"{a}{op}{b}")
print(f"计算结果为{result}")
```

运行：

```bash
$ cd code && python3 15-calculator.py
```

真实输出：

```
42
计算结果为32
计算结果为4.0
```

### 课后作业

参考本讲案例，编写一个支持**浮点数**的四则运算计算器。

> 参考答案：把两数换成带小数点的字符串（如 `"1.5"`、`"2.5"`），拼进表达式交给 `eval()`，`eval` 会自动按浮点数计算，输出 `4.0`。

---

## 第 16 讲 · 变量命名规范：如何编写优雅的程序？

### 本节目标

知道什么样的变量名**合法**、哪些词是**关键字（保留字）**不能用，并养成好的命名习惯。

### 知识要点

**1. 为什么要学命名规范**

- 代码变长后，有意义的变量名能帮你**快速看懂逻辑**
- 规范的命名能帮你区分变量代表的对象（函数、类……）
- 规范的命名能帮你**避免程序错误**

**2. 合法变量名的规则**

- 只能包含**字母、数字、下划线**，且**不能以数字开头**
- **不能含空格**
- **不能使用关键字**
- Python **大小写敏感**（`name` 和 `Name` 是两个变量）

来亲眼看看以数字开头会怎样：

```python
>>> 1a = 123
  File "<stdin>", line 1
    1a = 123
    ^
SyntaxError: invalid decimal literal
```

> 📌 在 **Python 3.12**（本机）上报的是 `invalid decimal literal`；PPT 里写的是老版本的 `invalid syntax`。
> 这正好印证了第 1 章说的：**同样的错误，不同 Python 版本给的提示可能不同**。

**3. 关键字（保留字）**

关键字是语言保留的词，不能拿来当变量名。Python 3.12 的全部关键字共 35 个：

```
False  None  True   and    as     assert  async   await   break
class  continue  def  del   elif   else   except  finally  for
from   global  if    import in     is     lambda  nonlocal not
or     pass    raise  return try    while  with    yield
```

**4. 好的命名习惯**

1. 简短
2. 描述性强
3. 全小写，多个单词用 `_` 连接（如 `user_name`）
4. 尽量不用中文，避开 `l / 1 / L`、`0 / O / o` 这类易混字符

### 代码实操

完整代码见 `code/16-naming.py`。用 `str.isidentifier()` 判断名字是否合法，用 `keyword` 模块查关键字：

```python
error_number = 1
name2 = "Python"
_name = "下划线开头也合法"
print(error_number); print(name2); print(_name)

print("error_number".isidentifier())
print("1a".isidentifier())
print("my name".isidentifier())

import keyword
print(keyword.kwlist)
print(keyword.iskeyword("for"))
print(keyword.iskeyword("hello"))

user_name = "张三"; max_count = 100
print(user_name); print(max_count)
```

运行：

```bash
$ cd code && python3 16-naming.py
```

真实输出：

```
1
Python
下划线开头也合法
True
False
False
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
True
False
张三
100
```

### 课后作业

判断下列变量名哪些是**好命名**、哪些是**不好/不合法**的命名：

```
error_number        e_n        er
4dm1n               all100
create_a_database_from_file_in_HardDisk
if                  for        def
NUMBER1
fi
```

> 参考答案：
> - **好命名**：`error_number`（简短、描述性强、下划线连接）、`all100`、`NUMBER1`（合法；`NUMBER1` 全大写一般留给「常量」，这里尚可）
> - **合法但不够好**：`e_n`、`er`（太短，描述性差）、`create_a_database_from_file_in_HardDisk`（太长，且 `HardDisk` 大小写混用不合规范）、`fi`（无意义）
> - **不合法**：`4dm1n`（数字开头）、`if` / `for` / `def`（关键字）

---

## 第 17 讲 · 告别新手村：Python 编程基础知识

### 本节目标

把本章三块核心内容——**变量、数据类型、输入输出**——串成一个整体，为下一章的「内置数据类型」做准备。

### 知识要点

**1. 变量**

- 定义：程序运行时数据的**临时存储对象**
- 变量类似标签，变量引用的数据有**数据类型**
- 变量名应简洁、有意义、大小写规范

**2. 数据类型**

```
数字  ├── 整数
     ├── 浮点数
     └── 复数
序列  ├── 字符串
     ├── ...（列表等，下一章见）
     └── ...
映射  （字典，下一章见）
类、实例、异常 ……
```

每种类型都内置了常用方法，方便操作：

- 字符串支持长度、切片、大小写等处理
- 数字支持运算和数学计算功能

**3. 输入输出**

- 输入输出是和计算机**最主要的交互手段**
- Python 编程更关注**交互性**
- 输出经常充当**调试工具**
- 常用函数就是 `input()` 和 `print()`

> 💡 本章小结：**数据类型 + 输入输出 = 编程逻辑的基础**。你会发现 Python 的语法和自然语言很接近，内置功能又丰富——这正是它适合入门的原因。

### 代码实操

完整代码见 `code/17-summary.py`，把三块内容串起来：

```python
name = "小明"
print(name)
name = "小红"          # 变量的值可以改
print(name)

age = 18; height = 1.75; city = "北京"
print(type(age)); print(type(height)); print(type(city))

age_str = "18"         # input() 读入的是字符串
age_num = int(age_str) # 参与计算需先转换
print(type(age_str)); print(type(age_num))

print(city.startswith("北"))
print("a,b,c".split(","))

print(f"{name}今年{age}岁，身高{height}米，来自{city}。")
```

运行：

```bash
$ cd code && python3 17-summary.py
```

真实输出：

```
小明
小红
<class 'int'>
<class 'float'>
<class 'str'>
<class 'str'>
<class 'int'>
True
['a', 'b', 'c']
小红今年18岁，身高1.75米，来自北京。
```

### 课后作业

写一个小程序，综合用到变量、字符串、数字和输入输出：读入你的名字、年龄、身高，然后输出一句自我介绍。

> 参考答案：见 `code/17-summary.py`，最后一行用 f-string 拼出一句话。

---

## 本章小结

**速查表**

| 主题 | 关键点 |
| --- | --- |
| 输出 | `print("你好")` |
| 输入 | `var = input("提示语")`，读到的**永远是字符串** |
| 变量 | 给数据贴标签，`=` 是赋值（不是相等），可随时改指向 |
| 多变量赋值 | `a, b = 1, 2`、`x = y = z = 3` |
| 字符串定义 | 单引号 / 双引号 / 三重引号 |
| 插入变量 | `f"{变量名}"`（f-strings，需 3.6+） |
| 成员运算 | `x in s` / `x not in s` |
| 连接运算 | `s + t`、`s * n` |
| 切片 | `s[i]`、`s[i:j]`、`s[i:j:k]`，下标从 0 开始 |
| 字符串方法 | `count` / `isalnum` / `isalpha` / `join` / `split` / `startswith` |
| 数字类型 | `int` / `float` / `complex` |
| 运算 | `+ - * /`、`//` 整除、`%` 取余、`**` 幂 |
| 类型转换 | `int()` / `float()` / `str()`，必须**显式**转换 |
| 查看类型 | `type(x)` |
| 注释 | `#` 开头，解释器忽略 |
| 命名规范 | 字母数字下划线、不以数字开头、不用关键字、`snake_case` |
| 执行表达式 | `eval("12+30")` → `42` |

**三句话**

1. **程序 = 输入 + 处理 + 输出**：`input()` 读、变量存、`print()` 显示。
2. **类型要显式转换**：`input()` 拿到的都是字符串，要参与算术就得上 `int()` / `float()`。
3. **好代码从好名字开始**：合法、简短、描述性强、下划线连接——注释写「为什么」，不写「是什么」。

**动手练习**

1. 跑通本章 `code/` 全部 10 个示例，对照正文的输出了解每行在做什么。
2. 用 `input()` 改写 `08-input-output.py`，在终端里真正敲两行字，看看反序输出的效果。
3. 给 `15-calculator.py` 加上 `+ - * /` 四种运算符的切换，做减法、除法各试一次。
4. 把 `13-number-vs-string.py` 里 `123 + "456"` 改成 `123 + int("456")`，看它是否能正常输出。

---

## 下一章预告

第 3 章进入 **Python 内置数据类型**：列表、元组、字典、集合——
本章已经见过字符串（序列的一种），下一章系统讲清「序列」和「映射」，
你会学到增删改查、切片、推导式等一整套处理数据的方法。

---

[← 上一章：入门的第一道门槛](/guide/getting-started) ｜ [返回总目录](/) ｜ [下一章：内置数据类型 →](/guide/data-types)

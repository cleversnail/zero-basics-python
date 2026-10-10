# 第 10 章 · 高级数据类型与算法

> 当内置的 list、dict、tuple 不够用时：用扩展数据类型、魔术方法、缓存、设计模式，
> 把「能跑」的程序改成「跑得快、好维护」的程序。
> **本章 10 讲（077–086）**

## 🎯 本章目标

- 会用 `collections` 的扩展数据类型：`namedtuple`、`deque`、`Counter`、`UserDict`
- 理解**魔术方法**，能通过重写 `__add__`、`__getitem__`、`__call__` 等定义自己的数据类型
- 知道 Python 与 C++ 混合编程的三种方式（ctypes / pybind / Pythran）
- 会用大 O 复杂度评估算法，并用 `functools.lru_cache` 把算法「改造」得更快
- 认识三类设计模式：创建型（单例 / 单态）、结构型（适配器）、行为型（责任链）
- 掌握用 Python 操作 NoSQL（Redis）和关系型（MySQL）数据库的基本方法
- 会用 `concurrent.futures` 线程池 / 进程池做并行计算
- 会用 `multiprocessing` 的队列、管道实现多进程通信

**本章说明**

> 📌 本机实测环境为 **Python 3.12.7**。
> 本章 **纯 Python 部分全部真跑**（077、078、080、081、084、085），正文贴的是真实终端输出；
> **079（C++ 混编）、082（Redis）、083（MySQL）需要编译器或外部服务，未实跑**，
> 正文只讲原理并给出完整可复制代码，每个相关小节都明确标注了「本节为说明，未实跑」。

**本章代码**

> 📌 **代码约定**：正文代码块都保持**可直接运行**；节选会明确标注「节选」并指向 `code/` 完整文件。
> 所有输出都是**真实运行结果**（未实跑的会写明）。

| 文件 | 内容 |
| --- | --- |
| `code/77-namedtuple.py` | 扩展数据类型：namedtuple / deque / Counter / UserDict / UserList |
| `code/78-magic-method.py` | 魔术方法：`__getitem__`、`__add__`、`__call__`、`__new__`、`__del__` |
| `code/79-cpp-mix/cli_foo.py` `.cpp` `.hpp` | Pythran 把 Python 转成 C++ 的三件套（未实跑） |
| `code/80-lru-cache.py` | 用 `functools.lru_cache` 改造斐波那契算法 |
| `code/81-design-pattern.py` + `code/singleton_config.py` | 设计模式：单例 / 单态 / 适配器 |
| `code/82-redis.py` | 用 redis-py 读写 Redis（未实跑） |
| `code/83-mysql.py` | 用 PyMySQL 增删改查 MySQL（未实跑） |
| `code/84-thread-pool.py` | 线程池并发执行耗时任务 |
| `code/85-multiprocessing.py` | 多进程通信：Queue / Pipe / Pool |

---

## 第 77 讲 · 扩展数据类型：怎样使用更复杂的数据类型？

### 本节目标

学会用 `collections` 模块里的四种「扩展数据类型」，在普通列表、字典、元组不够用时补上短板。

### 知识要点

`collections` 是 Python 标准库，提供了一批比内置类型更「专用」的容器：

| 类型 | 作用 | 相对内置类型的增强 |
| --- | --- | --- |
| **`namedtuple`**（命名元组） | 每个位置都有名字的元组 | 既能像元组那样按下标取，又能像对象那样按名字取 |
| **`deque`**（双端队列） | 两端都能进出的队列 | 比 list 多了 `appendleft()` / `popleft()` |
| **`Counter`**（计数器） | 统计元素出现次数 | 一键得到 `most_common()` 排行榜 |
| **`UserDict` / `UserList`** | 字典 / 列表的「子类化」基类 | 继承它就能给字典、列表加自定义规则 |

**1. 命名元组 `namedtuple`**

`namedtuple()` 是一个**工厂函数**：你告诉它「叫什么名字、有哪些字段」，它返回一个新的类。

```python
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(11, y=22)
```

它的好处是：`p1.x` 和 `p1[0]` 都能取到同一个值，既清晰又兼容元组的用法。

**2. 双端队列 `deque`**

普通列表在**头部**插入/删除很慢（要挪动全部元素），`deque` 专门解决这个问题：

- `append()` / `pop()`：从右端进出
- `appendleft()` / `popleft()`：从左端进出

**3. 计数器 `Counter`**

把任意可迭代对象（字符串、列表都行）丢进去，它就统计出每个元素出现了几次，`most_common(n)` 直接给前 n 名。

**4. 字典 / 列表子类化**

当你需要「一个有点特殊行为的字典」，不要从 `dict` 继承，而是继承 `UserDict`。它内部用 `self.data` 持有真正的字典，重写 `__setitem__`、`__getitem__` 等方法就能定制行为。

### 代码实操

完整代码见 `code/77-namedtuple.py`。运行：

```bash
$ python3 77-namedtuple.py
==================================================
1. 命名元组 namedtuple —— 给每个位置起个名字
==================================================
p1            = Point(x=11, y=22)
p1.x          = 11
p1[0]         = 11
p1.x == p1[0] = True
p1 是元组吗   = True
p1.x = 99 失败 -> AttributeError can't set attribute

==================================================
2. 双端队列 deque —— 两端都能进出的队列
==================================================
加入两端后    = [0, 1, 2, 3, 4]
popleft 弹出  = 0
pop 弹出      = 4
剩下          = [1, 2, 3]

==================================================
3. 计数器 Counter —— 统计元素出现次数
==================================================
统计结果      = Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
出现最多的 2 个 = [('a', 5), ('b', 2)]
字母 a 出现   = 5 次

==================================================
4. 子类化 UserDict —— 给字典加规则
==================================================
赋值错误，key "a" 已存在，放弃赋值。
d['a'] 的值   = 1
7 是奇数，拒绝加入列表
MyList 内容   = [2, 4, 6]
```

> 💡 观察最后一段：`MyDict` 第二次给 key `'a'` 赋值时被拦下，所以 `d['a']` 仍是 `1`——
> 这正是「子类化」的威力：**在继承的基础上，改掉不想要的那部分行为**。

### 课后作业

编写程序，统计一篇文章中出现频率**前五**的单词，并将单词和出现次数一起输出到终端。

**参考答案**（先按非字母字符切词，转小写，再用 `Counter` 取前五）：

```python
from collections import Counter
import re

text = """
Python is great. Python is simple. Python is powerful.
Learning Python opens doors. Python is everywhere.
Code in Python, think in Python, ship with Python.
"""

words = re.findall(r"[a-z]+", text.lower())
for word, n in Counter(words).most_common(5):
    print(word, n)
```

真实输出：

```
python 8
is 4
in 2
great 1
simple 1
```

---

## 第 78 讲 · 魔术方法：怎样通过类构造自己需要的数据类型？

### 本节目标

理解什么是魔术方法，并学会通过重写它们，让自定义对象支持 `+`、`-`、`len()`、下标取值等操作。

### 知识要点

**1. 什么是魔术方法**

魔术方法是 Python **预先定义好、有特定功能**的一类方法，名字前后各有两个下划线，例如 `__init__`。
你可以把它理解为**数据类型的接口**：Python 在执行 `a + b` 时，其实是在调用 `a.__add__(b)`。

**2. 基本数据类型里也有魔术方法**

我们平时写的 `dict1['a']`，本质上就是 `dict1.__getitem__('a')`：

```python
dict1 = {'a': 1}
dict1['a']            # 结果为 1
dict1.__getitem__('a')  # 结果也是 1
```

用 `dir(对象)` 可以把一个对象身上的魔术方法全部列出来。如果你想改变「取字典值」的过程，
就重写 `__getitem__()`。

**3. 类的常用魔术方法**

| 魔术方法 | 触发时机 |
| --- | --- |
| `__new__()` | 创建对象时（比 `__init__` 更早） |
| `__init__()` | 初始化对象时 |
| `__call__()` | 把对象当函数调用 `obj()` 时 |
| `__del__()` | 对象被回收时 |
| `__add__()` / `__sub__()` | 执行 `+` / `-` 时 |
| `__getitem__()` | 执行 `obj[i]` 时 |
| `__len__()` | 执行 `len(obj)` 时 |
| `__repr__()` | `print(obj)` 时显示什么 |

> 💡 **一句话记住**：想改哪个行为，就重写哪个魔术方法。

### 代码实操

完整代码见 `code/78-magic-method.py`。运行：

```bash
$ python3 78-magic-method.py
==================================================
1. 基本数据类型里也藏着魔术方法
==================================================
dict1['a']             = 1
dict1.__getitem__('a') = 1
dict1 的魔术方法（前 8 个）=  ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__']

==================================================
2. 用 __add__ / __sub__ 让对象支持 + 和 -
==================================================
v1          = Vector(11, 22)
v1 + v2     = Vector(44, 66)
v1 - v2     = Vector(-22, -22)
len(v1)     = 2
v1[0],v1[1] = 11 22

==================================================
3. 对象的生命周期：__new__ / __init__ / __call__ / __del__
==================================================
创建 Demo 实例：
  __new__ 被调用：先创建对象
  __init__ 被调用：再初始化对象
像函数一样调用 demo(5) = 25
删除 demo：
  __del__ 被调用：对象被回收时
```

> 📌 从第 3 段的输出能清楚看到**对象的生命周期顺序**：
> `__new__`（创建）→ `__init__`（初始化）→ 使用（`demo(5)`）→ `__del__`（回收）。

### 课后作业

请编写一个自定义类，要求该类能实现字典的所有功能；当用户为字典赋值、遇到**重复的 key** 时，
向用户报错并**禁止覆盖**该 key：

```python
mydict = MyDict()
mydict['a'] = 1
mydict['a'] = 1   # 对相同的 key 赋值报错
```

**参考答案**：其实第 77 讲的 `code/77-namedtuple.py` 里已经给了一个基于 `UserDict` 的实现
（输出正是 `赋值错误，key "a" 已存在，放弃赋值。`）。如果想不借助 `UserDict`，也可以直接继承
`dict` 并重写 `__setitem__`：

```python
class MyDict(dict):
    def __setitem__(self, key, value):
        if key in self:
            print(f'赋值错误，key "{key}" 已存在，放弃赋值。')
        else:
            super().__setitem__(key, value)
```

---

## 第 79 讲 · 怎样将 Python 和 C++ 结合起来混合编程？

### 本节目标

了解为什么需要混合编程，以及 Python 调用 C++ 的三条主流路线；看懂 Pythran 把 Python 转成 C++ 的流程。

> ⚠️ **本节为说明，未实跑**。C++ 混编需要安装 `pythran`（由它带出编译器）、C++ 编译工具链等，
> 本机没有这门环境。下面给出**完整可复制的代码和命令**，命令可以直接照抄到装好环境的机器上跑。

### 知识要点

**1. 为什么需要混合编程**

| 语言 | 优点 | 缺点 |
| --- | --- | --- |
| **Python** | 开发效率高、语法简单 | 解释执行，**数学运算等密集计算性能是瓶颈** |
| **C++** | 性能卓越 | 学习门槛高、开发效率低 |

结论：**用 C++ 做密集型计算，用 Python 调用它**——各取所长。

**2. 实现混合编程的三种方式**

1. **`ctypes`**：加载 C++ 编译出来的动态链接库（`.so` / `.dll`）
   文档：<https://docs.python.org/zh-cn/3.10/library/ctypes.html>
2. **`pybind11`**：把 C++ 编译成能被 Python `import` 的扩展模块
   参考：<https://github.com/pybind/python_example>
3. **`Pythran`**：反过来，把**纯 Python 源码直接转成 C++**
   参考：<https://pypi.org/project/pythran>

**3. 用 Pythran 转换代码的三个步骤**

1. 编写需要转换的 Python 函数（用注释声明导出什么）：
   ```python
   #pythran export foo()
   #pythran export msg
   msg = "hello pythran"
   def foo():
       print(msg)
   ```
2. 用 `pythran` 命令行把 `.py` 转成 C++ 头文件 `.hpp`
3. 编写 C++ 测试代码调用它，再编译成可执行文件

**4. Pythran 命令行参数**

```bash
# 查看帮助
pythran --help

# 把 python 源码转成 C++ 头文件
pythran -e cli_foo.py -p pythran.optimizations.ConstantFolding -o cli_foo.hpp

# 编译 C++ 测试程序：pythran-config 给出编译所需的库与编译参数
`pythran-config --compiler --cflags` -std=c++11 cli_foo.cpp -o cli_foo
```

- `pythran-config --compiler --cflags`：拿到编译需要的库和参数
- `-std=c++11`：用 C++（而不是 C）来编译链接
- `-o`：指定输出文件名

### 代码实操

本讲的三个文件放在 `code/79-cpp-mix/` 下（**未实跑**）：

| 文件 | 作用 |
| --- | --- |
| `cli_foo.py` | 待转换的 Python 源码 |
| `cli_foo.hpp` | Pythran 生成的 C++ 头文件（本仓库提供的是生成结果） |
| `cli_foo.cpp` | C++ 测试程序，`main()` 里调用转换后的 `foo()` |

`cli_foo.py`（完整内容）：

```python
#pythran export foo()
#pythran export msg

msg = "hello pythran"


def foo():
    print(msg)
```

`cli_foo.cpp`（完整内容）：

```cpp
#include "cli_foo.hpp"
using namespace __pythran_cli_foo ;

int main()
{
	foo()();
	return 0 ;
}
```

在装好 Pythran + C++ 工具链的机器上，按下面两步即可运行（**本节未实跑**）：

```bash
# 第 1 步：把 Python 转成 C++ 头文件
$ pythran -e cli_foo.py -p pythran.optimizations.ConstantFolding -o cli_foo.hpp

# 第 2 步：编译 C++ 测试程序
$ `pythran-config --compiler --cflags` -std=c++11 cli_foo.cpp -o cli_foo

# 第 3 步：运行
$ ./cli_foo
hello pythran
```

> ⚠️ 上面 `hello pythran` 是**预期输出**，不是本机实跑结果——本机没有 Pythran 与 C++ 工具链。

`cli_foo.hpp` 是 Pythran 自动生成的头文件（内容较长，完整版见 `code/79-cpp-mix/cli_foo.hpp`），
它把 `foo`、`msg` 包装成了 C++ 命名空间 `__pythran_cli_foo` 里的一对结构体。

### 课后作业

基于 Pythran 编写一个计算圆周率 π 的 Python 函数，并用 C++ 调用它；
运行后比较「纯 Python 代码」和「C++ 代码」的运行时间。

> 提示：先写一个用**莱布尼茨级数**求 π 的纯 Python 函数（循环次数拉大），
> 加上 `#pythran export calc_pi(int)` 之类的声明，再按上面的三步转换、编译、运行，
> 用 `time` 分别测纯 Python 版和 C++ 版的耗时。

---

## 第 80 讲 · 怎样将已有算法改造成符合项目的特定算法？

### 本节目标

学会用**大 O 复杂度**评估算法优劣，并用 `functools.lru_cache` 把「又慢又对」的算法改造成「又快又对」。

### 知识要点

**1. 为什么要掌握算法**

- 掌握成熟软件的设计思想
- 能**正确评估**自己的代码质量（而不是凭感觉说「挺快的」）

**2. 评估算法：大 O 复杂度**

用「大 O 表示法」描述算法随数据量增长的大致耗时。常见几种，从快到慢：

| 复杂度 | 含义 | 典型例子 |
| --- | --- | --- |
| `O(1)` | 常数时间 | 数组按下标取值、字典查 key |
| `O(log n)` | 对数时间 | 二分查找 |
| `O(n)` | 线性时间 | 遍历一遍列表 |
| `O(n²)` | 平方时间 | 双层循环两两比较 |
| `O(2ⁿ)` | 指数时间 | **朴素递归斐波那契** |

**3. 改造算法：给斐波那契数列加缓存**

用朴素递归算斐波那契，复杂度是 `O(2ⁿ)`——因为同样的子问题被反复算了很多遍。
如果把「算过的结果」存起来，下次直接取，复杂度立刻降到 `O(n)`。这就是 **LRU**（Least Recently Used，
最近最少使用）思想的轻量应用，Python 已经内置好了：

- **`functools.lru_cache()`**：函数缓存装饰器（可指定缓存上限）
- **`functools.cache()`**：Python 3.9+ 的简写，等价于 `lru_cache(maxsize=None)`

### 代码实操

完整代码见 `code/80-lru-cache.py`。运行：

```bash
$ python3 80-lru-cache.py
========================================================
朴素递归 vs 加缓存：同样的结果，完全不同的速度
========================================================
fib(30)        无缓存 =       832040   耗时 0.060547 秒
fib_cached(30) 有缓存 =       832040   耗时 0.000007 秒
fib_cached(40)   有缓存 =    102334155   耗时 0.000001 秒

结论：结果一样（fib(30)=832040），但复杂度从 O(2^n) 降到 O(n)。

==================================================
cache_info()：查看缓存命中情况
==================================================
fib_cached 的缓存统计： CacheInfo(hits=39, misses=41, maxsize=None, currsize=41)
fib_cache  的缓存统计： CacheInfo(hits=0, misses=0, maxsize=None, currsize=0)

==================================================
动手试一试：同一个参数，第二次调用直接返回缓存
==================================================
再算一次 fib_cached(40) 后： CacheInfo(hits=40, misses=41, maxsize=None, currsize=41)
可以看到 hits（命中）增加了，说明第二次直接从缓存返回，没有重复计算。
```

> 💡 关键代码只有一个装饰器：
> ```python
> from functools import lru_cache
>
> @lru_cache(maxsize=None)
> def fib_cached(n):
>     if n < 2:
>         return n
>     return fib_cached(n - 1) + fib_cached(n - 2)
> ```
> 这正是「改造已有算法」的精髓：**逻辑一行没改，只加了一个装饰器，性能天差地别**。

### 课后作业

编写一个能计算 100 以内阶乘的函数；已知 60% 的人经常计算 10 和 100 的阶乘，请在此前提下优化阶乘函数。

**参考答案**（用 `lru_cache` 缓存）：

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)

print("10! =", factorial(10))
print("100! 的位数 =", len(str(factorial(100))))
```

真实输出：

```
10! = 3628800
100! 的位数 = 158
```

---

## 第 81 讲 · 设计模式：怎样合理组合多个函数和类？

### 本节目标

认识设计模式的三大分类（创建型、结构型、行为型），并动手实现单例、单态、适配器三种模式。

### 知识要点

设计模式按「解决什么问题」分为三大类：

| 类别 | 解决什么 | 典型模式 |
| --- | --- | --- |
| **创建型** | 对象的「创建」方式 | 单例模式、单态模式 |
| **结构型** | 类与对象的「组合」方式 | 适配器模式 |
| **行为型** | 对象之间的「职责分配」 | 责任链模式 |

**1. 单例模式（Singleton）**

整个程序里某个类**只有一个实例**。Python 最省事的实现方式是「靠 import」——
因为**一个模块在同一个进程里只会被导入（执行）一次**，所以模块级变量天生就是唯一的。

**2. 单态模式（Monostate）**

单例要求「只有一个对象」，单态则允许创建多个对象，但让它们**共享同一份数据**。
实现窍门：把数据存在**类属性**上，而不是实例属性上。

**3. 适配器模式（Adapter）**

用来解决**接口不兼容**的问题：把一个类的接口「转接」成调用者期望的接口。
中文名里的「转接头」——TypeC 的接口转成 TypeA 能插的样子。

**4. 责任链模式（Chain of Responsibility）**

发送者和接收者解耦：请求沿着一条链传递，直到有对象处理它。
经典场景是**异常的分层处理**——用户请求网站失败时，从 DNS → HTTP → Socket 逐层向上返回。

### 代码实操

完整代码见 `code/81-design-pattern.py`（单例用的模块 `singleton_config.py` 同目录）。运行：

```bash
$ python3 81-design-pattern.py
==================================================
1. 单例模式：靠 import 实现
==================================================
第一次取: 默认名字
改完之后: 改过之后
再次导入: 改过之后 （同一个模块对象，状态共享）

==================================================
2. 单态模式 Monostate：多个实例共享同一属性
==================================================
c1.get_variable = 3
c1.display()    = 3

==================================================
3. 适配器模式 Adapter：让不兼容的接口能一起用
==================================================
TypeA 调用 oneFace() -> 单面
适配器调用 oneFace() -> 双面
```

> 💡 第 2 段印证了单态的含义：`c1` 和 `c2` 是两个**不同对象**，
> 但修改 `c2` 的数据属性，通过类属性共享，`c1` 也能看到——这正是单态要达到的效果。

### 课后作业

为了满足「用自动饮水机泡茶、吃药、冲咖啡」等需求，给饮水机设计四个按钮，
分别设定出水温度为 40℃、60℃、90℃、100℃。请据此设计合理的设计模式。

> 提示：这里「创建不同温度的水」可以看作一串变体，**策略模式**或**简单工厂**都很合适——
> 把「出水温度」抽象成一个可替换的策略（每个按钮对应一个策略对象），主流程只负责
> 「选策略 → 执行」，将来加 80℃ 也不用改主流程。也可以结合**单例**保证饮水机全局只有一个。

---

## 第 82 讲 · Redis 数据库：怎样使用 NoSQL 数据库？

### 本节目标

了解 Redis 是什么、能干什么，并掌握用 Python（redis-py）连接、读写 Redis 的方法。

> ⚠️ **本节为说明，未实跑**，因为本机没有运行 Redis 服务（也没安装 redis-py 客户端）。
> 下面的代码是**完整可复制的**；`code/82-redis.py` 里做了「能连上就真跑、连不上就打印说明」的兜底，
> 所以本机运行它只会打印一行 `[未实跑] ...`。

### 知识要点

**1. Redis 的用途**

Redis 是一款**高性能的键值（Key-Value）数据库**，属于 **NoSQL**（非关系型）数据库。
它既快（数据主要放在内存里），编程接口又丰富，是企业开发中最常用的非关系型数据库。

**2. 用 Python 访问 Redis**

需要第三方库 `redis-py`（导入名就叫 `redis`）：

```bash
pip3 install redis
```

连接方式：

```python
import redis
conn = redis.Redis(host, port, password, db)
```

**3. Redis 的数据类型**

Redis 和 Python 一样有自己的数据类型：**字符串、双向链表、压缩列表、哈希表、跳表、整数数组**。
好处是：**Python 的数据类型可以直接存进去，不用做复杂的类型转换**。

最常用的读写：

```python
conn.set('key', 'value')   # 存字符串
conn.get('key')            # 读字符串（返回 bytes，如 b'value'）
```

### 代码实操

完整代码见 `code/82-redis.py`。在**装好 redis-py 且启动 Redis 服务**的机器上，这样运行：

```bash
# 1. 安装客户端
$ pip3 install redis

# 2. 启动 Redis 服务（用 Docker 演示）
$ docker run -d -p 6379:6379 --name myredis redis

# 3. 运行示例
$ python3 82-redis.py
```

`code/82-redis.py` 里真正的读写部分（节选，完整版见文件）：

```python
import redis

conn = redis.Redis(host='localhost', port=6379, db=0)

# 字符串
conn.set('name', 'Alice')
print("读取 name        =", conn.get('name'))          # 返回 b'Alice'

# 哈希表：一个 key 下存多个字段
conn.hset('user:1', mapping={'name': 'Bob', 'age': 30})
print("读取 user:1      =", conn.hgetall('user:1'))

# 列表：当简易消息队列用（顺序存储、顺序读取）
conn.rpush('jobs', 'job1', 'job2', 'job3')   # 从右端推入
print("队列 jobs        =", conn.lrange('jobs', 0, -1))
print("取出队首         =", conn.lpop('jobs'))          # 从左端弹出

# 计数器：原子自增
conn.incr('visits')
conn.incr('visits')
print("访问计数 visits  =", conn.get('visits'))
```

在**本机**（未安装 redis-py）真实运行 `python3 82-redis.py` 的结果是：

```
[未实跑] 本机没有安装 redis-py 客户端，无法连接 Redis。
         安装命令：pip3 install redis
```

> ⚠️ 上面这段是**本机真实输出**（脚本的兜底分支）；真正的读写结果需要启动 Redis 服务后才能看到，
> 本节**未实跑**。

### 课后作业

请将 Redis 作为 Python 的消息队列，实现消息的**顺序存储**和**顺序读取**；
要求 Python 进程结束再重新启动后，消息队列里的数据不会丢失。

> 提示：用 Redis 的**列表**类型。生产端用 `rpush`（从右入队），消费端用 `lpop`（从左出队），
> 天然保证先入先出（FIFO）；数据存在 Redis 里而不是 Python 内存里，进程重启后仍在，
> 这正是「不丢失」的关键。若要求「读走才删」，可用 `brpoplpush` 配合处理确认队列。

---

## 第 83 讲 · 关系型数据库：如何使用关系型数据库？

### 本节目标

了解关系型数据库相比普通文本的优势，掌握用 Python（PyMySQL）连接 MySQL、增删改查的方法。

> ⚠️ **本节为说明，未实跑**，因为本机没有运行 MySQL 服务（也没安装 PyMySQL 客户端）。
> `code/83-mysql.py` 同样做了兜底：能连上就真跑，连不上就打印说明。

### 知识要点

**1. 关系型数据库的用途**

| 相比普通文本文件 | 优势 |
| --- | --- |
| 操作性 | 比文本更灵活，接口更完善（有专门的 SQL） |
| 安全性 | 数据安全性比文本更强 |
| 性能 | 查询速度更快（有索引） |

**2. 连接数据库**

```bash
pip3 install PyMySQL
```

```python
import pymysql
db = pymysql.connect(host, user, password, db)
```

用上下文管理器拿游标（cursor）：

```python
with connection:                      # 用 with 管理连接
    with connection.cursor() as cursor:  # 用 with 管理游标
        cursor.execute("SELECT 1")       # 在这里执行 SQL 语句
```

**3. 数据查询与修改**

| 操作 | SQL 语句 |
| --- | --- |
| 查询 | `SELECT 列 FROM 库.表 WHERE 查询条件` |
| 插入 | `INSERT INTO 表(字段名) VALUES(字段值)` |
| 更新 | `UPDATE 表 SET 字段=值 WHERE 更新条件` |
| 删除 | `DELETE FROM 表 WHERE 删除条件` |

> ⚠️ **重要**：`connection` **不会自动提交**，数据修改后必须手动 `db.commit()` 才生效；
> 出错要 `db.rollback()` 回滚；用 `finally` 保证 `db.close()` 关闭连接。

### 代码实操

完整代码见 `code/83-mysql.py`。在**装好 PyMySQL 且启动 MySQL 服务**的机器上：

先建库建表：

```sql
CREATE DATABASE db;

CREATE TABLE `users` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `email` varchar(255) COLLATE utf8_bin NOT NULL,
    `password` varchar(255) COLLATE utf8_bin NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
AUTO_INCREMENT=1 ;
```

再运行示例：

```bash
$ pip3 install PyMySQL
$ python3 83-mysql.py
```

`code/83-mysql.py` 的核心部分（节选，完整版见文件）：

```python
import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='rootroot',
                             database='db',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:
        # 建立一条记录（用 %s 占位符，防止 SQL 注入）
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection 不能自动提交数据，必须手动提交
    connection.commit()

    with connection.cursor() as cursor:
        # 读取记录
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
```

在**本机**（未安装 PyMySQL）真实运行 `python3 83-mysql.py` 的结果是：

```
[未实跑] 本机没有安装 PyMySQL 客户端，无法连接 MySQL。
         安装命令：pip3 install PyMySQL
```

> ⚠️ 上面这段是**本机真实输出**（脚本的兜底分支）。真正连上 MySQL 后的查询结果，
> 课程原始 notebook 里得到的是 `{'password': 'very-secret', 'id': 1}`，但**本节未实跑**，
> 这里仅作参考，不作为本机实测。

### 课后作业

请尝试通过 Python 读取当前执行程序的电脑的 **IP 地址**，并将 IP 地址存储到 MySQL 数据库中。

> 提示：用标准库拿到 IP：
> ```python
> import socket
> hostname = socket.gethostname()
> ip = socket.gethostbyname(hostname)
> ```
> 然后按本讲的方法 `cursor.execute("INSERT INTO ... (ip) VALUES (%s)", (ip,))`，
> 记得 `connection.commit()`。

---

## 第 84 讲 · 计算资源充足时，如何通过并行设计提高效率？

### 本节目标

分清「并发」与「并行」，并会用 `concurrent.futures` 的线程池（`ThreadPoolExecutor`）并发执行任务。

### 知识要点

**1. 并发 vs 并行**

| | 并发（Concurrency） | 并行（Parallelism） |
| --- | --- | --- |
| 定义 | 宏观上多个任务同时在执行 | **同一时刻**真的在同时发生 |
| CPU | 一个核心交替运行多个程序 | 多个核心同时处理多个程序 |

一句话：**并发是「看起来同时」，并行是「真的同时」**。

**2. `concurrent.futures` 库**

`concurrent.futures` 里的 **`Executor`** 是「并行任务」的抽象类，它能用**线程**和**进程**两种方式实现并行：

- **`ThreadPoolExecutor`**（线程池）：用线程实现并发，适合 **I/O 密集型**任务（下载、读写文件等）
- **`ProcessPoolExecutor`**（进程池）：用多核 CPU，适合 **计算密集型**任务

提交任务用 `submit()`，它返回一个 **future**（「未来的结果」）：

```python
executor.submit(函数, 参数...)
```

用 `concurrent.futures.as_completed(...)` 可以「谁先做完就先处理谁」。

> 💡 课程原始例子是并发访问 `http://www.baidu.com`。为了不依赖网络，本仓库的示例把
> 「下载网页」换成了等价的 `time.sleep`（模拟 I/O 等待），**并发原理完全一样**。

### 代码实操

完整代码见 `code/84-thread-pool.py`。运行：

```bash
$ python3 84-thread-pool.py
========================================================
1. 串行执行：一个任务做完再做下一个
========================================================
  任务 1 完成，页面大小 600 字节
  任务 2 完成，页面大小 600 字节
  任务 3 完成，页面大小 600 字节
  任务 4 完成，页面大小 600 字节
  任务 5 完成，页面大小 600 字节
  任务 6 完成，页面大小 600 字节
串行总耗时：3.02 秒

========================================================
2. 并发执行：线程池，最多 2 个线程同时跑
========================================================
  任务 2 完成，页面大小 600 字节
  任务 1 完成，页面大小 600 字节
  任务 3 完成，页面大小 600 字节
  任务 4 完成，页面大小 600 字节
  任务 6 完成，页面大小 600 字节
  任务 5 完成，页面大小 600 字节
并发总耗时：1.51 秒

对比：串行 3.02 秒 -> 并发 1.51 秒，提速约 2.0 倍。
```

> 📌 两点提醒：
> 1. 并发部分的**任务完成顺序是不确定的**（谁先做完谁先打印），你跑出来的顺序可能和上面不同，这很正常。
> 2. 这里只开了 **2 个线程**，所以 6 个 0.5 秒的任务总耗时约 1.5 秒；串行则是 3.0 秒。
>    线程数越多、任务越多，并行优势越明显——但也不是越多越好，线程过多反而会增加切换开销。

### 课后作业

请使用并发任务模型同时访问 5 个网站，并将网页数据存储到不同的文件中。

> 提示：把本讲示例里的 `time.sleep` 换成真正的下载（课程 PPT 用的是 `urllib.request.urlopen`）：
> ```python
> import urllib.request
> def load_url(url, timeout):
>     with urllib.request.urlopen(url, timeout=timeout) as conn:
>         return conn.read()
> ```
> 然后在 `as_completed` 循环里，把 `data` 写进以 URL 序号命名的文件，例如
> `open(f"page-{i}.html", "wb").write(data)`。注意：这一步依赖真实网络，本仓库未实跑。

---

## 第 85 讲 · 多进程间如何通信？

### 本节目标

理解进程与线程的差别，并掌握 `multiprocessing` 里三种进程通信方式：**队列、管道、进程池**。

### 知识要点

**1. 进程与线程的差别**

在 CPython 里存在 **GIL（全局解释器锁）**：**同一时刻只有一个线程在执行 Python 字节码**。因此：

| 任务类型 | 推荐模型 | 原因 |
| --- | --- | --- |
| **I/O 密集型** | 多线程 | 等 I/O 时线程会释放 GIL，能重叠 |
| **计算密集型** | **多进程** | 每个进程有独立的 GIL，能真正跑满多核 |

`concurrent.futures` 并行任务的底层库就是 **`multiprocessing`**。

**2. 进程池 Pool**

```python
from multiprocessing import Pool
with Pool(10) as p:
    p.map(函数对象, 参数)
```

`Pool(10)` 表示开 10 个进程，`map` 会把第二个参数里的每一项分给进程去算。

**3. 进程通信：为什么需要它？**

多个进程**各有各的内存**，变量无法直接共享，所以要用操作系统提供的机制交换数据：

| 方式 | 用法 | 特点 |
| --- | --- | --- |
| **队列 Queue** | `q.put()` 写、`q.get()` 读 | 先进先出，最常用 |
| **管道 Pipe** | `parent, child = Pipe()`，两端都有 `send()` / `recv()` | 默认**双工**（可双向） |
| **共享内存** | `shared_memory.SharedMemory(create=True, size=10)` | 最快，但需自己管同步 |

> ⚠️ **macOS / Windows 上的坑**：多进程默认用 `spawn` 方式启动，子进程会**重新导入**你的模块。
> 因此所有「创建进程」的代码**必须写在 `if __name__ == '__main__':` 里面**，否则会无限重跑、卡死。
> 此外 `multiprocessing.Queue` 的 `qsize()` 在 macOS 上会抛 `NotImplementedError`（本讲示例没有用它，
> 而是用**哨兵值 `None`** 告诉消费者「没数据了」——这也是更可靠的做法）。

### 代码实操

完整代码见 `code/85-multiprocessing.py`。运行：

```bash
$ python3 85-multiprocessing.py
==================================================
1. Queue：一个进程产生 1~30，另一个进程挑出 7 的倍数
==================================================
  消费者：7 能被 7 整除
  消费者：14 能被 7 整除
  消费者：21 能被 7 整除
  消费者：28 能被 7 整除
  队列通信结束。

==================================================
2. Pipe：父子进程一来一回
==================================================
  父进程收到： 你好，父进程
  父进程再次收到： 子进程收到：收到，合作愉快

==================================================
3. Pool：把 square 并发地跑在多个进程上
==================================================
  pool.map(square, [1,2,3,4,5]) = [1, 4, 9, 16, 25]
```

> 💡 队列部分用的是「生产者—消费者」模型：
> 生产者 `producer` 依次放入 1~30，放完再放一个 `None` 当**结束信号**；
> 消费者 `consumer` 循环取值，遇到 `None` 就退出，其余能整除 7 的打印出来。
> 用哨兵值而不是猜「队列空没空」，是跨平台更稳的写法。

### 课后作业

请编写一个多进程任务：一个进程用于产生 1~10000 的数字，另一个进程判断该数字能否被 7 整除，
能整除就输出到终端。

**参考答案**（和本讲示例同结构，只把范围调到 10000）：

```python
from multiprocessing import Process, Queue

def producer(q, n):
    for i in range(1, n + 1):
        q.put(i)
    q.put(None)

def consumer(q):
    hits = []
    while True:
        item = q.get()
        if item is None:
            break
        if item % 7 == 0:
            hits.append(item)
    print(f"1~10000 中能被 7 整除的数共 {len(hits)} 个，前 5 个：{hits[:5]}")

if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=producer, args=(q, 10000))
    p2 = Process(target=consumer, args=(q,))
    p1.start(); p2.start(); p1.join(); p2.join()
```

真实输出：

```
1~10000 中能被 7 整除的数共 1428 个，前 5 个：[7, 14, 21, 28, 35]
```

---

## 第 86 讲 · 再回首：「高级数据类型与算法」单元小结

### 本节目标

把本单元 9 讲的内容串成一条线：**当内置工具不够用时，Python 给了你哪些「加装件」**。

### 知识要点

回到本单元的主线——**「内置的 list / dict / tuple 不够用怎么办」**，我们层层递进地学了四招：

1. **换更好的容器**：`collections` 的 `namedtuple` / `deque` / `Counter` / `UserDict`（第 77 讲）
2. **给对象加行为**：重写魔术方法，自定义数据类型（第 78 讲）
3. **改造算法**：用大 O 评估，用 `lru_cache` 加速（第 80 讲）
4. **组织代码**：用设计模式把多个函数、类合理组合（第 81 讲）

再往外，我们把这些能力接到了**真实系统**上：

- **存数据**：NoSQL 的 Redis（第 82 讲）、关系型数据库 MySQL（第 83 讲）
- **提效率**：线程池 / 进程池并行（第 84 讲）、多进程通信（第 85 讲）
- **拼性能**：把 Python 和 C++ 混编（第 79 讲）

### 代码实操

本讲是回顾，没有新代码。可以把本章所有**真跑**过的示例一次性重跑一遍，温故知新：

```bash
$ cd 10-advanced/code
$ for f in 77-namedtuple.py 78-magic-method.py 80-lru-cache.py 81-design-pattern.py 84-thread-pool.py 85-multiprocessing.py; do
    echo "===== $f ====="; python3 "$f";
  done
```

> 📌 `82-redis.py` 和 `83-mysql.py` 需要外部服务，`79-cpp-mix/` 需要 C++ 编译器，
> 本机都**未实跑**，所以没有放进上面这条循环里。

**速查表**

| 主题 | 关键点 |
| --- | --- |
| 扩展数据类型 | `namedtuple` 有名字的元组；`deque` 两端进出；`Counter` 排行榜；`UserDict` 子类化 |
| 魔术方法 | `__add__`/`__getitem__`/`__call__`… 想改哪个行为就重写哪个 |
| 复杂度 | `O(1) < O(logn) < O(n) < O(n²) < O(2ⁿ)` |
| 缓存 | `@lru_cache(maxsize=None)` 或 `@cache`，一行解决重复计算 |
| 设计模式 | 创建型（单例/单态）、结构型（适配器）、行为型（责任链） |
| Redis | 键值型 NoSQL，`pip3 install redis`，`conn.set/get` |
| MySQL | 关系型数据库，`pip3 install PyMySQL`，改完记得 `commit()` |
| 并行 | `ThreadPoolExecutor` 适合 I/O，`ProcessPoolExecutor` 适合计算 |
| 多进程通信 | Queue（队列）、Pipe（管道）、shared_memory（共享内存）；`if __name__ == '__main__'` 是标配 |

**三句话**

1. 内置类型不够用，先翻 `collections`，再考虑用魔术方法自己造一个。
2. 算法慢，先用大 O 找出瓶颈；能缓存就缓存（`lru_cache`），往往一行代码见效。
3. 需要并发，分清 I/O 密集（用线程）和计算密集（用进程）；跨进程交换数据要用队列或管道。

**动手练习**

1. 用 `namedtuple` 定义一个「学生」，包含姓名和成绩，再写函数求全班平均分。
2. 用魔术方法写一个 `MyList` 类，让 `+` 变成「拼接去重」。
3. 把第 80 讲的斐波那契换成阶乘，用 `lru_cache` 前后各跑一次，比较耗时。
4. 用 `ThreadPoolExecutor` 并发跑 4 个 `time.sleep(1)` 任务，验证总耗时约 1 秒。

### 课后作业

1. 从本单元 9 讲里挑一个你还是「有点含糊」的知识点，回到 `code/` 里把对应文件**逐行加注释**重读一遍，
   并自己改一处代码、重跑一遍看结果有什么变化。
2. 用一句话向别人解释清楚：**「并发」和「并行」到底差在哪**，并各举一个生活例子。

---

## 下一章预告

下一章进入**第 11 章 · 数据分析**：用 `requests` 抓网页、用 `re` 正则提取、用 `json` 解析，
再用 `matplotlib` 把数据画成图，把「一堆原始数据」变成「一眼能看懂的结论」。

---

[← 上一章：异常](/guide/exceptions) ｜ [返回总目录](/) ｜ [下一章：数据分析 →](/guide/data-analysis)

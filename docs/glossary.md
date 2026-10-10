# 术语表

按主题分组。每个词给「中文 · English · 一句话解释」，最后有一张**易混淆概念对照表**。

---

## 语言与环境

| 中文 | English | 说明 |
| --- | --- | --- |
| 解释型语言 | interpreted language | 源码由解释器逐句翻译并执行，不需要单独的编译步骤。Python 属于这一类 |
| 编译型语言 | compiled language | 先把源码整体编译成机器码，再执行。如 C/C++、Go |
| 字节码 | bytecode | 源码被编译成的中间形式，由 Python 虚拟机执行 |
| 解释器 | interpreter | 执行 Python 代码的程序；`python3 -V` 查的就是它的版本 |
| 交互模式 | interactive mode | 解释器跑完不退出，停在 `>>>` 等继续输入（`python3 -i x.py`） |
| 非交互模式 | non-interactive mode | 从开始跑到结束，不中断（`python3 x.py`） |
| 标准库 | standard library | Python 自带的库，装了 Python 就能用，如 `os`、`json`、`re` |
| 第三方库 | third-party library | 需要额外 `pip install` 的库，如 `requests`、`pandas` |

## 基础语法

| 中文 | English | 说明 |
| --- | --- | --- |
| 变量 | variable | 给数据起的名字，随时可改指向 |
| 赋值 | assignment | `x = 1`，把右边给左边 |
| 数据类型 | data type | `int` / `float` / `str` / `list` / `tuple` / `dict` / `set` |
| 整数 | integer (`int`) | 不带小数点的数 |
| 浮点数 | float | 带小数点的数 |
| 字符串 | string (`str`) | 用引号包起来的一串字符 |
| 列表 | list | 有序、可变、用 `[]` 表示，如 `[1, 2, 3]` |
| 元组 | tuple | 有序、**不可变**、用 `()` 表示，如 `(1, 2, 3)` |
| 集合 | set | 无序、不重复，用 `{}` 或 `set()`，如 `{1, 2, 3}` |
| 字典 | dictionary (`dict`) | 键值对映射，用 `{}`，如 `{"name": "张三"}` |
| 索引 | index | 取元素的位置，从 **0** 开始；负数表示从后往前 |
| 切片 | slice | `s[1:5:2]` 取一段 |
| 类型转换 | type conversion / casting | `int("123")`、`str(456)` |
| 注释 | comment | `#` 开头，给人看，不执行 |
| 关键字 | keyword | 语言保留字，不能当变量名，如 `if`、`for`、`class` |
| 命名规范 | naming convention | 变量用小写下划线（snake_case） |

## 流程控制与函数

| 中文 | English | 说明 |
| --- | --- | --- |
| 条件判断 | conditional | `if` / `elif` / `else` |
| 模式匹配 | pattern matching | `match` / `case`（Python 3.10+） |
| 循环 | loop | `while`（条件） / `for`（遍历） |
| 循环嵌套 | nested loop | 循环里套循环 |
| 推导式 | comprehension | `[x for x in range(10)]` |
| 函数 | function | 用 `def` 定义，可重复调用的一段代码 |
| 参数 | parameter / argument | 形参是定义时的占位，实参是调用时传入的值 |
| 默认参数 | default parameter | 不传就用默认值的参数 |
| 可变参数 | `*args` / `**kwargs` | 参数个数不固定时用 |
| 返回值 | return value | `return` 把结果交回给调用方；没有 `return` 就返回 `None` |
| 作用域 | scope | 变量在哪个范围里可见 |
| 高阶函数 | higher-order function | 参数或返回值是函数的函数 |
| 装饰器 | decorator | `@xxx` 写在函数上一行，用来增强函数功能 |

## 面向对象与模块

| 中文 | English | 说明 |
| --- | --- | --- |
| 类 | class | 用 `class` 定义，是「模板」 |
| 实例 / 对象 | instance / object | 由类创建出来的具体个体 |
| 方法 | method | 定义在类里的函数，`self` 是约定俗成的第一个参数 |
| 构造方法 | constructor (`__init__`) | 创建实例时自动调用，用来初始化属性 |
| 继承 | inheritance | 子类复用父类的属性和方法 |
| 魔术方法 | magic method / dunder | 形如 `__add__`、`__str__`，让对象支持运算符和内置函数 |
| 模块 | module | 一个 `.py` 文件就是一个模块 |
| 包 | package | 含 `__init__.py` 的目录，用来组织多个模块 |
| 导入 | import | `import math` / `from math import pi` |

## 异常与调试

| 中文 | English | 说明 |
| --- | --- | --- |
| 异常 | exception | 运行期出错，如 `ZeroDivisionError` |
| 语法错误 | syntax error | 程序**跑不起来**，如少括号、多缩进 |
| 捕获异常 | catch / handle exception | `try ... except ...` |
| 抛出异常 | raise | 主动报错 |
| 自定义异常 | custom exception | 继承 `Exception` 定义业务异常 |
| 断点 | breakpoint | 程序在此暂停，`breakpoint()` |
| 调试器 | debugger | `pdb`；常用命令 `n` / `c` / `pp` / `break` |

## 项目实战

| 中文 | English | 说明 |
| --- | --- | --- |
| 网页抓取 | web scraping | 用 `requests` 拉页面，再用 `re` / `BeautifulSoup` 提取 |
| 正则表达式 | regular expression (`re`) | 匹配文本模式的「小语言」 |
| 数据框 | DataFrame | `pandas` 的核心结构，像带行列名的表格 |
| 虚拟环境 | virtualenv / venv | 给每个项目隔离一套依赖，避免版本打架 |
| 关系型数据库 | relational database | 用表和 SQL，如 MySQL / SQLite |
| NoSQL | NoSQL | 非关系型，如 Redis（键值）、MongoDB（文档） |
| 进程 / 线程 | process / thread | 并发的两种粒度；`multiprocessing` / `threading` |
| 多进程通信 | IPC | 进程间传数据，如 `Queue`、`Pipe` |
| MVC | Model-View-Controller | Django 的架构划分：模型 / 视图模板 / 控制器 |
| 物联网 | IoT | 设备联网，如 ESP32 + MQTT |
| 消息队列协议 | MQTT | 物联网常用的轻量发布/订阅协议 |
| 物模型 | thing model | 把设备抽象成「属性 + 事件 + 方法」的数据模板 |

---

## 易混淆概念对照

| 容易混 | 区别 |
| --- | --- |
| **列表 vs 元组** | 列表可变（能改），元组不可变（不能改）；元组效率更高 |
| **列表 vs 集合** | 列表有序可重复，集合无序不重复 |
| **`=` vs `==`** | `=` 是赋值，`==` 是比较是否相等 |
| **`is` vs `==`** | `==` 比值，`is` 比是不是同一个对象（同一块内存） |
| **`/` vs `//`** | `/` 除法得浮点，`//` 整除得整数 |
| **可变对象作默认参数** | `def f(x=[])` 是陷阱：默认值只在定义时创建一次，会被反复共用 |
| **浅拷贝 vs 深拷贝** | 浅拷贝只复制第一层，里层还是同一份；深拷贝递归复制 |
| **`import a` vs `from a import b`** | 前者用 `a.b` 访问，后者直接 `b` |
| **语法错误 vs 异常** | 语法错误在**运行前**就被拦下；异常在**运行时**才发生 |
| **进程 vs 线程** | 进程有独立内存，通信要 IPC；线程共享内存，但受 GIL 限制 |
| **`while` vs `for`** | `while` 条件成立就循环，`for` 遍历可迭代对象 |
| **`append` vs `extend`** | `append([4,5])` 把整个列表当一个元素加进去；`extend([4,5])` 逐个加 |

---

[返回总目录](/)

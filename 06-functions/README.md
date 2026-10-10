# 第 6 章 · 函数

> 把一段反复要用的代码「打包」成函数：会定义、会传参、会接返回值，再学会高阶函数与装饰器。
> **本章 9 讲（049–057）**，从「怎么定义」到「怎么优雅地装饰」，最后用购物车项目串起来。

## 🎯 本章目标

- 用 `def` 定义函数、用圆括号调用函数，理解**函数对象**与**函数调用**的区别
- 分清**形参 / 实参**，会用**位置参数、关键字参数、默认值、类型提示**
- 会用 `*args` / `**kwargs` 处理不定长参数，会写 `docstring` 并用内省查看函数
- 会用 `return` 拿到执行结果，明白「不写 return 默认返回 None」，认识**递归**
- 用函数把「电商购物车」分解成若干小功能，体会**问题分解 + 封装**
- 识破「列表作参数被就地修改」的坑，学会用副本规避
- 看懂并会写**高阶函数**（`map` / `filter` / `reduce` / 偏函数）与**装饰器**

**本章代码**

> 📌 **代码约定**：正文代码块都保持**可直接运行**；节选会明确标注「节选」并指向 `code/` 完整文件。
> 所有输出都是**真实运行结果**（本机 Python 3.12.7）。

| 文件 | 内容 |
| --- | --- |
| `code/49-define.py` | 定义 / 调用函数、函数对象、`lambda` 匿名函数 |
| `code/50-args.py` | 形参与实参、位置参数、关键字参数、默认值、类型提示 |
| `code/51-varargs.py` | 不定长参数 `*args` / `**kwargs`、函数文档、函数内省 |
| `code/52-return.py` | `return` 返回值、返回 `None`、返回函数调用、递归求阶乘 |
| `code/53-shop-cart.py` | 购物车小项目：展示、加购、减购、清空、费用统计 |
| `code/54-list-arg.py` | 避坑：列表作参数被就地修改，以及用副本规避 |
| `code/55-higher-order.py` | 函数对象 vs 调用、`map` / `filter` / `reduce`、偏函数 |
| `code/56-decorator.py` | 变量作用域、闭包、`@` 装饰器、`functools.wraps` |

---

## 第 49 讲 · 函数的定义：如何优雅地反复引用同一段代码？

### 本节目标

学会用 `def` 把一段代码**打包**起来，并用圆括号随时把它「叫出来」跑一遍。

### 知识要点

**1. 函数的用途**

把需要**多次执行**的代码片段「包装」起来，用到时就调用一次，从而提高代码的**重复利用率**——同一段逻辑写一次、用很多次。

**2. 定义函数的语法**

```python
def 函数名称([函数参数]):
    函数体
    [return 返回值]
```

- `def` 是 define（定义）的缩写，后面跟函数名和一对圆括号、一个冒号；
- 函数体要**缩进**（通常是 4 个空格），缩进的部分才属于这个函数。

**3. 调用函数**

函数名后面加一对**圆括号**，就表示「调用」这个函数：`foo()`。
⚠️ 注意：`foo`（不带括号）是**函数对象**本身，`foo()`（带括号）才**执行**它。

**4. 匿名函数**

**匿名函数**就是借用 `lambda` 表达式定义的一次性小函数，适合逻辑简单、只在一处用的场合：

```python
add_1 = lambda x: x + 1     # 冒号左边是参数，右边是返回值
print(add_1(100))           # 101
```

它等价于一个正规函数 `def add_1(x): return x + 1`。

> 💡 **一句话**：`def` 负责「定义」，圆括号负责「调用」；`lambda` 是简写版的小函数。

### 代码实操

完整代码见 `code/49-define.py`：

```python
# -*- coding: utf-8 -*-
"""第 49 讲 · 函数的定义：如何优雅地反复引用同一段代码？"""


# 1. 定义函数：def + 函数名 + 圆括号 + 冒号，函数体要缩进
def foo():
    print("foo")
    print("is a function")


print("aaaaa")   # 这只是普通语句，不会执行 foo 里的内容
foo()            # 加圆括号才是「调用」，函数体这时才被完整跑一遍
foo()            # 再调用一次，同一段代码被复用

# 2. 函数对象 vs 函数调用
print(foo)       # 不加括号：得到的是「函数对象」本身
print(type(foo))

# 3. 匿名函数：用 lambda 表达式定义简单的、一次性的函数
add_1 = lambda x: x + 1
print(add_1(100))


# 上面那行 lambda，等价于下面这个正规函数
def add_1_def(x):
    return x + 1


print(add_1_def(100))
```

运行命令与真实输出：

```bash
$ python3 49-define.py
aaaaa
foo
is a function
foo
is a function
<function foo at 0x104e26340>
<class 'function'>
101
101
```

> 那个 `0x104e26340` 是函数对象在内存里的地址，**每次运行都会不同**，不影响理解——
> 它说明「`foo` 不带括号时，你拿到的是一个对象」。

### 课后作业

请找到「飞机大战」的课程代码，把**输出飞机位置**的那一段代码块改成用**函数**封装。要求：定义一个函数（例如 `show_plane_position(x, y)`，参数用**形参**），在需要的地方调用它，而不是把打印语句复制多份。

---

## 第 50 讲 · 函数的参数：怎样实现函数与外部数据通信？

### 本节目标

搞懂**形参 / 实参**的区别，学会用**位置参数、关键字参数、默认值**把数据送进函数。

### 知识要点

**1. 实参与形参**

| 名称 | 出现的位置 | 例子 |
| --- | --- | --- |
| **形参**（形参变量） | 函数**定义**处 | `def func(args):` 里的 `args` |
| **实参**（实际参数） | 函数**调用**处 | `func(variables)` 里的 `variables` |

一句话：**形参**是函数内部的「占位变量」，**实参**是你真正传进去的值。

**2. 类型提示（Type Hint）**

Python 3.5 起（PEP 484）支持类型提示：

```python
def func(变量名: 类型) -> 返回类型:
    return 变量名
```

⚠️ 类型提示**只对开发人员起提示作用**，Python **不会**据此做类型检查——传错类型照样跑，只是 IDE 会给你标红。

**3. 位置参数**

需要传多个参数时，最简单的方式是**按顺序**传递，靠「第几个」来对应参数，这叫**位置参数**：

```python
def foo(argv1, argv2, argv3):
    pass

foo(one, two, three)   # one→argv1, two→argv2, three→argv3
```

**4. 关键字参数与默认值**

以内置函数 `open()` 为例，它的完整签名参数很多：

```python
open(file, mode='r', buffering=-1, encoding=None,
     errors=None, newline=None, closefd=True, opener=None)
```

调用时可以**指名道姓**地只传你关心的：

```python
open("/path/to/file", encoding="UTF-8")
```

这种「参数名=值」的写法叫**关键字参数**，它带来两个好处：可以**换顺序**、可以**只传特定参数**。

**默认值**：定义函数时直接给参数写个初值（如 `mode='r'`）。调用时若没传，就用默认值——参数越多，这个特性越省事。

> 💡 **顺序提醒**：位置参数在前、关键字参数在后；有默认值的参数应写在没有默认值的参数**后面**。

### 代码实操

完整代码见 `code/50-args.py`：

```python
# -*- coding: utf-8 -*-
"""第 50 讲 · 函数的参数：怎样实现函数与外部数据通信？"""


# 1. 形参与实参
def foo(number):          # 定义时的 number 是「形参」
    print(number)


n1, n2, n3 = 123, 456, 789
foo(n1)                   # 调用时传进去的 n1 是「实参」
foo(n2)
foo(n3)


# 2. 类型提示（Type Hint，PEP 484）：只给人看，Python 不做强制检查
def foo2(n1: int, n2: int) -> int:
    return n1 * n2


print(foo2(3, 4))


# 3. 位置参数 + 关键字参数 + 默认值
def foo3(argv1=100, argv2=200, argv3=300):
    print(argv1)
    print(argv2)
    print(argv3)


foo3("one", "two", "three")   # 三个都按位置传
foo3()                         # 一个都不传，全部用默认值
foo3(400, argv3=500)           # argv1 按位置，argv3 按关键字，argv2 用默认值
```

运行命令与真实输出：

```bash
$ python3 50-args.py
123
456
789
12
one
two
three
100
200
300
400
200
500
```

注意最后一段 `foo3(400, argv3=500)` 的输出是 `400 / 200 / 500`——`argv1` 按位置拿到 400，`argv3` 按关键字拿到 500，而中间的 `argv2` 没传，用了默认值 200。

### 课后作业

编写一个函数，**计算圆周率 π 的近似值**，函数的参数越大，π 的值越精确。提示：可以用莱布尼茨级数 π/4 = 1 − 1/3 + 1/5 − 1/7 + …，把「项数」作为参数传进去。

---

## 第 51 讲 · 函数的参数：当函数操作对象不固定时怎么处理？

### 本节目标

当参数个数**不确定**时，用 `*args` / `**kwargs` 接住它们；并学会写函数**文档**、用**内省**查看函数。

### 知识要点

**1. 不定长参数**

- **固定长度**的参数让函数功能更明确；
- **不定长度**的参数让函数更灵活。

记号约定：

| 记号 | 接收的东西 | 表现为 |
| --- | --- | --- |
| `*telphone` | 多余的位置参数 | 一个**元组** `tuple` |
| `**custom` | 多余的关键字参数 | 一个**字典** `dict` |

讲义里的「电话本」函数：

```python
def address_book(name, *telphone, alias_name=None, **custom):
    print(f"name: {name}, tel: {telphone}, aname: {alias_name}, custom:{custom}")
```

**不定长参数的变种**：`*` 号后面**不写变量名**时，它只起到「分隔」作用——

```python
def address_book(name, *, alias_name):
    pass
```

这里的 `*` 表示它**后面的参数必须用关键字方式传**，位置参数长度被固定成 2 个（`name` 和 `alias_name`）。

**2. 函数文档（docstring）**

函数体第一行的三引号字符串就是**文档字符串**，用来写「这个函数的用途、用法、注意事项」：

```python
def foo():
    """ 这个函数的用途、用法、注意事项等 """
    pass
```

查看方式：`foo.__doc__`。

**3. 函数内省**

「内省」= 查看对象内部信息。把函数定义成**函数对象**后，它会自动带上一堆内置属性，用 `dir(foo)` 就能看到，例如 `__doc__`（文档）、`__name__`（函数名）、`__defaults__`（默认值）等。同样地，`dir(列表)`、`dir(数字)` 也能看到各种内置方法。

> 💡 **知识串联**：函数是「对象」，所以你也用过 `dir()` 查看字符串、列表的方法——底层靠的是同一套内省机制。

### 代码实操

完整代码见 `code/51-varargs.py`：

```python
# -*- coding: utf-8 -*-
"""第 51 讲 · 函数的参数：当函数操作对象不固定时怎么处理？"""


# 1. 不定长参数：* 收集位置参数，** 收集关键字参数
def address_book(name, *telphone, alias_name=None, **custom):
    print(f"name: {name}, tel: {telphone}, aname: {alias_name}, custom:{custom}")


address_book("wilson")
address_book("wilson", 1234, 4567, 5678)
address_book("wilson", 1234, 4567, 5678, home="Guangdong")
address_book("wilson", 1234, 4567, 5678, alias_name="w", aaa="bbb", home="Guangdong")


# 2. 函数文档：函数体第一行的字符串就是文档字符串（docstring）
def foo():
    """这个函数的用途、用法、注意事项都写在这里。"""
    print("test")


foo()
print(foo.__doc__)


# 3. 函数内省：用 dir() 查看函数对象自带的属性
print([d for d in dir(foo) if d in ("__call__", "__defaults__", "__doc__", "__kwdefaults__", "__name__")])
print(foo.__name__)
```

运行命令与真实输出：

```bash
$ python3 51-varargs.py
name: wilson, tel: (), aname: None, custom:{}
name: wilson, tel: (1234, 4567, 5678), aname: None, custom:{}
name: wilson, tel: (1234, 4567, 5678), aname: None, custom:{'home': 'Guangdong'}
name: wilson, tel: (1234, 4567, 5678), aname: w, custom:{'aaa': 'bbb', 'home': 'Guangdong'}
test
这个函数的用途、用法、注意事项都写在这里。
['__call__', '__defaults__', '__doc__', '__kwdefaults__', '__name__']
foo
```

可以看到：不传电话时 `tel` 是空元组 `()`；传了三个电话后 `tel` 变成 `(1234, 4567, 5678)`；而 `home=`、`aaa=` 这种关键字参数全被 `**custom` 收进字典。

### 课后作业

编写一个函数，使其能接收**长度不等**的参数。函数执行时，应当显示：

1. 一共有**几个**参数；
2. 这些参数的**全部内容**。

提示：用 `*args` 收参数，`len(args)` 数个数。

---

## 第 52 讲 · 函数的返回值：如何得到函数的执行结果？

### 本节目标

用 `return` 把函数的结果「交出来」，并认识「不写返回默认是 None」和「递归」。

### 知识要点

**1. `return` 语句**

函数可以用参数接收「输入」，也可以把结果**返回**给调用者，让结果能继续参与后续运算：

```python
var = func1()      # 把 func1 的结果接进 var
var2 = func1(var)  # 再拿 var 作为下次调用的输入
```

**2. 返回值类型**

`return` 的语法是 `return [表达式]`。如果函数里**没有** `return`，或者只写 `return`（表达式为空），那么默认返回 **`None`**（「什么都没有」）。

`return` 后面可以跟多种东西：

```python
return 变量
return 变量[, 变量, 变量]    # 返回多个值，其实是一个元组
return 字面值               # 如 return 3.14
return 函数调用
```

**3. 返回函数调用与递归**

函数可以直接返回**另一个函数的调用结果**：

```python
def foo():
    return "abc"

def foo2():
    return foo()      # 返回的是 foo() 的执行结果
```

**递归**：函数调用自己。判断、循环、递归是三大基本算法。递归必须写好**停止条件**，否则会无限自我调用，最终抛出 `RecursionError: maximum recursion depth exceeded`（递归深度超限）。

求阶乘的递归写法（用中文描述就是）：

```
def 计算阶乘(数值):
    if 数值为 1 或者 0:
        返回 1              # 停止条件
    else:
        返回 数值 * 计算阶乘(数值 - 1)   # 自己调用自己
```

> ⚠️ 递归的**停止条件**是灵魂。没有它，函数会一直调用自己直到超出 Python 的最大递归深度。

### 代码实操

完整代码见 `code/52-return.py`：

```python
# -*- coding: utf-8 -*-
"""第 52 讲 · 函数的返回值：如何得到函数的执行结果？"""


# 1. return 把结果交给调用者，结果可以继续参与运算
def add(a, b):
    return a + b


result = add(3, 4)
print(result)
print(add(result, 10))


# 2. 没有 return（或 return 为空）时，默认返回 None
def no_return():
    print("我执行了，但没有返回值")


print(no_return())


# 3. 返回函数调用：return 后面可以跟「另一个函数的调用」
def foo():
    return "abc"


def foo2():
    return foo()


print(foo2())


# 4. 递归：函数自己调用自己，必须写好「停止条件」
def factorial(n):
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


print(factorial(5))
```

运行命令与真实输出：

```bash
$ python3 52-return.py
7
17
我执行了，但没有返回值
None
abc
120
```

第 4 行输出 `None`，正是因为 `no_return()` 没有写 `return`，函数默认返回了 `None`。

### 课后作业

编写一个程序，计算圆的**周长**和**面积**：

1. 通过用户输入的整数作为圆的半径；
2. 编写两个函数：`circumference()` 计算周长，`area_of_circle()` 计算面积；
3. 将周长和面积存入一个**列表**，并把该列表输出到终端。

> 提示：π 取 `3.14` 即可；周长 = `2 * π * r`，面积 = `π * r * r`。
> 输入交互无法在文档里演示，可用固定半径（如 `r = 3`）代替输入。

---

## 第 53 讲 · 小试牛刀：如何利用函数实现电商购物车功能？

### 本节目标

把「购物车」这个大需求**分解**成几个小功能，每个功能用一个函数实现，再把它们**封装**到一起。

### 知识要点

**1. 购物车的功能分析**

购物车要方便客户：确认购买的商品名称、数量、金额、总额；调整商品数量；合并付款。简单拆分为：

- 展示商品
- 添加商品、删除商品
- 调整商品数量
- 费用总计

（本讲先**忽略**库存数量、商品类目。）

**2. 数据结构**

- 商品表用**列表**：每行是 `[商品编号, 名称, 类目, 单价]`；
- 购物车用**字典**：`{商品编号: 数量}`。

「展示商品」本质上就是**遍历字典**，逐个把商品名和数量打出来。

**3. 费用统计**

`合计费用 = 单价 × 数量 + 单价 × 数量 + …`

设计要点：**只允许修改「数量」**，每个商品的小计和总费用都在此基础上**实时算出来**——这样数量一改，总价自动跟着变，不会出现「价格和数量对不上」的不一致。

**4. 数量修改的三条规则**

- 修改数量时，应避免为 0 或超过库存（暂不考虑库存）；
- 购物车里数量减到 **0** 时，应把该商品**移除**；
- 商品数量增减时，总价同步重算；
- 用**自定义函数**比直接改字典更合适（逻辑集中、便于维护）。

> 💡 **核心思想**：先把完整功能**拆成小功能**，每个函数负责一件小事；再把相互作用的多个变量**封装**进函数统一处理。

### 代码实操

原课程用 `input()` 让用户现场一次次输入商品与数量，文档里无法演示交互输入。这里改成**固定购物序列**，让程序一次跑完，功能与讲义一致。

完整代码见 `code/53-shop-cart.py`：

```python
# -*- coding: utf-8 -*-
"""第 53 讲 · 小试牛刀：如何利用函数实现电商购物车功能？

原课程用 input() 让用户在现场一次次输入商品与数量，文档里无法演示交互输入。
这里改成「固定购物序列」，程序一次跑完，功能与讲义完全一致。
"""

# 商品表：每行是 [商品编号, 名称, 类目, 单价]
products = [
    [1000, "iphone", "phone", 12000],
    [1001, "ipad", "pad", 15000],
    [1002, "macbook", "laptop", 20000],
]

# 购物车：{商品编号: 数量}
cart = {1000: 5, 1001: 2}


def idtoname(product_id):
    """商品编号 -> 商品名称"""
    for product in products:
        if product[0] == product_id:
            return product[1]


def idtoprice(product_id):
    """商品编号 -> 单价"""
    for product in products:
        if product[0] == product_id:
            return product[3]


def show_cart():
    """展示购物车里的商品，并统计总费用"""
    total = 0
    for product_id in cart:
        print(f"购买商品 {idtoname(product_id)} 的数量为 {cart[product_id]}")
        total += idtoprice(product_id) * cart[product_id]
    print(f"总费用为: {total}")


def add_product(product_id, number):
    """加入购物车：已有就累加数量，没有就新增"""
    if product_id in cart:
        cart[product_id] += number
    else:
        cart[product_id] = number


def del_product(product_id):
    """购物车里某商品数量减 1，减到 0 就把它移除"""
    if product_id in cart:
        cart[product_id] -= 1
        if cart[product_id] == 0:
            cart.pop(product_id)


def clean_cart():
    """清空购物车"""
    cart.clear()


print("=== 初始购物车 ===")
show_cart()

print("=== 加入 15 台 macbook 后 ===")
add_product(1002, 15)
show_cart()

print("=== 从购物车减去 1 台 ipad 后 ===")
del_product(1001)
show_cart()

print("=== 清空购物车后 ===")
clean_cart()
show_cart()
```

运行命令与真实输出：

```bash
$ python3 53-shop-cart.py
=== 初始购物车 ===
购买商品 iphone 的数量为 5
购买商品 ipad 的数量为 2
总费用为: 90000
=== 加入 15 台 macbook 后 ===
购买商品 iphone 的数量为 5
购买商品 ipad 的数量为 2
购买商品 macbook 的数量为 15
总费用为: 390000
=== 从购物车减去 1 台 ipad 后 ===
购买商品 iphone 的数量为 5
购买商品 ipad 的数量为 1
购买商品 macbook 的数量为 15
总费用为: 375000
=== 清空购物车后 ===
总费用为: 0
```

核对一下第一组总费用：`12000×5 + 15000×2 = 60000 + 30000 = 90000`；加到 15 台 macbook 后：`+ 20000×15 = 390000`；再减掉 1 台 ipad：`− 15000 = 375000`。数量一改，总价立刻跟着变——这正是「只改数量、总价实时算」的设计效果。

### 课后作业

继续完善购物车程序，**新建另一个列表**用于记录**库存**，实现：

- 某商品被加入购物车时，该商品库存**减少**；
- 某商品在购物车中减少数量时，该商品库存**增加**；
- 当商品库存为 **0** 时，不再允许增加购物车中该商品的数量。

> 参考思路：用 `stock = {1000: 100, 1001: 50, 1002: 30}` 存库存；在 `add_product()` 里先判断库存是否足够，够才 `cart[...] += number` 且 `stock[...] -= number`。

---

## 第 54 讲 · 避坑指南：列表作为参数传递出错了怎么办？

### 本节目标

看懂「列表作参数被就地修改」这个经典坑，并学会用**副本**规避它。

### 知识要点

**1. 列表类型的特殊性**

- 列表是**可变数据类型**（内容可以原地改动）；
- 元组的元素可以是列表——所以「元组的某个元素」本身仍可能被改（元组只是「不让你换掉这一格」）；
- 正因为可变，**列表作为函数参数**时，函数里对它的改动会**影响到外面**。

**2. 列表作为函数参数**

讲义里的例子：

```python
list1 = [1, 2, 3]
def func(list1):
    list1.append(4)

func(list1)
print(list1)   # [1, 2, 3, 4]
func(list1)
print(list1)   # [1, 2, 3, 4, 4]
```

每调用一次，原列表就被**追加一个 4**——因为函数里 `append` 改的就是外面那个列表本身。

**3. 为什么会这样**

Python 传参时传的是「对象的引用」：函数拿到的 `list1` 和外面的 `list1` **指向同一个列表**。所以函数内部一动，外面就看到变化。（数字、字符串等**不可变类型**则不会出现这种现象。）

**4. 怎么规避**

- **原则**：容易踩坑的可变数据，尽量不要直接当参数传进去改；
- 若必须处理列表，就在函数里先 **`lst.copy()`** 复制一份，再对副本操作，或者干脆用 `list(...)` 新建列表。

> ⚠️ **一句话**：把列表交给函数，函数里的改动会「漏」到外面——不确定时就先复制。

### 代码实操

完整代码见 `code/54-list-arg.py`：

```python
# -*- coding: utf-8 -*-
"""第 54 讲 · 避坑指南：列表作为参数传递出错了怎么办？

列表是「可变数据类型」。把它交给函数后，函数内部一改动，
调用方手里的那个列表也会跟着变 —— 这是最常见的坑之一。
"""

list1 = [1, 2, 3]


def func(lst):
    lst.append(4)   # 这一步会「就地修改」传进来的列表


print("调用前:", list1)
func(list1)
print("第 1 次调用后:", list1)   # 意外地多了个 4
func(list1)
print("第 2 次调用后:", list1)   # 又多了一个 4


# 避坑：不想让原列表被改，就在函数里先复制一份再操作
list2 = [1, 2, 3]


def func_safe(lst):
    lst = lst.copy()   # 复制一份副本，动它不影响外面
    lst.append(4)
    return lst


print("原始列表:", list2)
print("函数返回值:", func_safe(list2))
print("原始列表没变:", list2)
```

运行命令与真实输出：

```bash
$ python3 54-list-arg.py
调用前: [1, 2, 3]
第 1 次调用后: [1, 2, 3, 4]
第 2 次调用后: [1, 2, 3, 4, 4]
原始列表: [1, 2, 3]
函数返回值: [1, 2, 3, 4]
原始列表没变: [1, 2, 3]
```

对比最后三行：`func_safe` 里先 `copy()` 再操作，所以返回的列表多了个 4，而**原始列表 `list2` 一点没变**——这就是正确的写法。

### 课后作业

请编写函数，将一个列表中的元素按**从大到小**的顺序排序。

> 参考答案（用列表自带的 `sort`，`reverse=True` 表示降序）：

```python
def sort_desc(lst):
    return sorted(lst, reverse=True)   # sorted 返回新列表，不动原列表

print(sort_desc([3, 1, 4, 1, 5, 9, 2, 6]))   # [9, 6, 5, 4, 3, 2, 1, 1]
```

---

## 第 55 讲 · 高阶函数：函数对象与函数调用的用法区别

### 本节目标

分清「函数对象」和「函数调用」，认识把函数当参数用的**高阶函数**以及**偏函数**。

### 知识要点

**1. 函数对象和函数调用**

```python
def foo():
    print("foo函数被执行")

foo()        # 函数调用：加圆括号，真正执行
var = foo    # 函数对象：不加圆括号，把函数本身赋给变量
var()        # var 和 foo 是同一个函数，加括号才执行
```

**函数对象**表示「函数本身」，可以赋值、可以当别的函数的参数或返回值；**函数调用**才是真的跑一遍。

**2. 高阶函数**

「高阶函数」指**接收函数作为参数**（或返回函数）的函数。Python 常说的三个高阶函数是 `map`、`filter`、`reduce`：

| 函数 | 来源 | 作用 |
| --- | --- | --- |
| `map(函数, 可迭代对象)` | 内置 | 把函数作用到每个元素上，返回处理后的结果 |
| `filter(函数, 可迭代对象)` | 内置 | **过滤**掉函数返回不为 `True` 的元素 |
| `reduce(函数, 可迭代对象)` | `functools` 导入 | 对序列**累积**成一个值 |

- `map` 的第一个参数可以是**函数对象**或 **lambda**；第二个参数是**可迭代对象**（列表、元组、`range` 等）。
- `filter` 的规则等价于：`function(item)` 为真就留下。（`function` 为 `None` 时，直接按元素本身真假来留。）
- `reduce` 需要 `from functools import reduce`。

**3. 偏函数**

**偏函数**：固定某个参数，生成一个新函数。

```python
from functools import partial
new_func = partial(旧函数对象, 被固定的参数)
new_func(参数)
```

例如 `int(数值, base=进制)` 里把 `base` 固定成 16：

```python
from functools import partial
int_16 = partial(int, base=16)
int_16("ff")        # 15，等同于 int("ff", base=16)
```

> 💡 **串起来**：`map` / `filter` / `reduce` / `partial` 的参数里都带着**函数对象**——这正是「函数是一等公民」的体现。

### 代码实操

完整代码见 `code/55-higher-order.py`：

```python
# -*- coding: utf-8 -*-
"""第 55 讲 · 高阶函数：函数对象与函数调用的用法区别"""

from functools import reduce, partial


# 1. 函数对象 vs 函数调用
def foo():
    print("foo函数被执行")


var = foo        # 不加括号：把「函数对象」赋给变量
print(f"var 的类型是: {type(var)}")
var()            # var 现在和 foo 指同一个函数，加括号才执行


# 2. map：把函数作用到可迭代对象的每个元素上
def add(number):
    return number + number


for i in map(add, range(5)):
    print(i)

print(list(map(lambda x: x + x, range(5))))


# 3. filter：只留下函数返回 True 的元素
print(list(filter(lambda x: x > 0, (-2, -1, 1, 2))))


# 4. reduce：把整个序列累积成一个值
print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))


# 5. 偏函数：固定某个参数，生成一个新函数
int_16 = partial(int, base=16)   # 把 base=16 固定下来
print(int_16("ff"))              # 等价于 int("ff", base=16)
```

运行命令与真实输出：

```bash
$ python3 55-higher-order.py
var 的类型是: <class 'function'>
foo函数被执行
0
2
4
6
8
[0, 2, 4, 6, 8]
[1, 2]
15
255
```

逐行看：`map(add, range(5))` 把 0~4 各翻倍得到 0 2 4 6 8；`filter(lambda x: x > 0, ...)` 只留下 1 和 2；`reduce` 把 1+2+3+4+5 累积成 15；`int_16("ff")` 按十六进制解析得到 255。

### 课后作业

使用**高阶函数**合并两个列表，使每个列表**对应位置**的元素相加，得到新列表：

- `[1, 3, 5, 7, 9]` 和 `[2, 4, 6, 8, 10]` 相加后得到 `[3, 7, 11, 15, 19]`。

> 参考答案（用 `map` + 两个可迭代对象）：

```python
a = [1, 3, 5, 7, 9]
b = [2, 4, 6, 8, 10]
print(list(map(lambda x, y: x + y, a, b)))   # [3, 7, 11, 15, 19]
```

---

## 第 56 讲 · 装饰器：函数嵌套的定义与调用的区别

### 本节目标

理解**变量作用域**与**闭包**，学会用 `@` 语法写**装饰器**给函数「加料」。

### 知识要点

**1. 变量作用域与 LEGB 规则**

Python 找变量按 **LEGB** 顺序：

| 字母 | 含义 | 说明 |
| --- | --- | --- |
| **L** | Local | 本地（函数内）变量 |
| **E** | Enclosed | 闭包变量（外层函数的局部变量） |
| **G** | Global | 全局变量 |
| **B** | Builtin | 内置变量（如 `len`） |

- 全局变量作用域**包含**函数，所以函数内**能读**全局变量；
- 函数内的变量是**局部变量**，在函数外访问会报「变量未定义」。

```python
def foo():
    number = 200      # 局部变量
    print(number)

foo()
print(number)         # ❌ NameError: name 'number' is not defined
```

**2. 闭包**

函数内**再次定义**的内部函数形成**闭包**；在闭包作用域之内，内部函数可以访问外部函数的变量：

```python
def func_out():
    var_out = 1

    def func_in():
        return var_out      # 用到了外层的 var_out

    return func_in          # 返回内部函数

print(func_out()())          # 1
```

**3. 装饰器语法**

「外层函数 + 内层函数同时定义」本可以手写，但**定义和调用都不优雅**：写内层的人要改外层代码，调用时还要写两个圆括号。于是引入 `@` 语法。

以「计算函数运行时间」为例。**不用装饰器**时手动计时：

```python
import time

def func():
    print("func 函数开始执行")
    time.sleep(1)
    print("func 函数执行结束")

start = time.time()
func()
stop = time.time()
print(f"func 函数一共执行了{int(stop - start)}秒")
```

**改成装饰器**后，用 `@` 挂上去即可，原函数代码一行不用改：

```python
@time_it
def work():
    print("func函数开始执行")
    time.sleep(1)
    print("func函数执行结束")

work()
```

**4. 自带装饰器**

Python 内置的装饰器来自 `functools`，常用的有：

- `@lru_cache`——缓存结果（讲义写作 `@lrucache`，标准名是 `functools.lru_cache`）；
- `@wraps`——让被装饰的函数**保持原对象不变**（名字、文档等元信息不被覆盖）。

> 💡 **一句话**：装饰器 = 「在不改动原函数的前提下，给它外面套一层新功能」；`@wraps` 是为了套完以后「名字还是原来的名字」。

### 代码实操

完整代码见 `code/56-decorator.py`：

```python
# -*- coding: utf-8 -*-
"""第 56 讲 · 装饰器：函数嵌套的定义与调用的区别"""

import time
from functools import wraps


# 1. 变量作用域：函数内部的是局部变量，函数外访问不到
def scope_demo():
    number = 200
    print(f"函数内部 number = {number}")


scope_demo()
# print(number)   # 若取消注释会报错 NameError: name 'number' is not defined
# 这里故意注释掉，让脚本能正常跑完


# 2. 闭包：内部函数可以访问外部函数的变量
def func_out():
    var_out = 1

    def func_in():
        return var_out

    return func_in


print(f"闭包取到的值: {func_out()()}")


# 3. 装饰器：给函数「加料」而不改它的代码
def time_it(func):
    @wraps(func)          # 让被装饰函数保持原来的名字等元信息
    def wrapper():
        start = time.time()
        func()
        stop = time.time()
        print(f"{func.__name__} 函数一共执行了 {int(stop - start)} 秒")

    return wrapper


@time_it
def work():
    print("work 函数开始执行")
    time.sleep(1)
    print("work 函数执行结束")


work()
print(f"work 的名字仍是: {work.__name__}")
```

运行命令与真实输出：

```bash
$ python3 56-decorator.py
函数内部 number = 200
闭包取到的值: 1
work 函数开始执行
work 函数执行结束
work 函数一共执行了 1 秒
work 的名字仍是: work
```

最后一行 `work 的名字仍是: work` 正是 `@wraps(func)` 的功劳——没有它，`work.__name__` 会变成 `wrapper`。

### 课后作业

定义一个装饰器，让被装饰的函数**运行 5 遍**，并输出**平均运行时间**。

> 参考思路：把 `wrapper` 改成跑一个 `for _ in range(5):` 循环，用总耗时除以 5：

```python
import time
from functools import wraps

def repeat5(func):
    @wraps(func)
    def wrapper():
        start = time.time()
        for _ in range(5):
            func()
        total = time.time() - start
        print(f"{func.__name__} 平均运行 {total / 5:.4f} 秒")
    return wrapper
```

---

## 第 57 讲 · 再回首：“函数”单元小结

### 本节目标

把本章 9 讲的知识点收拢成一张地图，知道「什么时候该用哪个工具」。

### 知识要点

**一张函数地图**

| 主题 | 关键点 |
| --- | --- |
| 定义 / 调用 | `def 名(参数):` 定义；`名()` 调用；`名` 是函数对象 |
| 匿名函数 | `lambda 参数: 表达式`，适合简单、一次性的小函数 |
| 参数 | 形参在定义处、实参在调用处；位置参数按顺序，关键字参数指名道姓 |
| 默认值 / 类型提示 | 有默认值的参数写在后面；`n1: int -> int` 只提示不强制 |
| 不定长参数 | `*args` 收位置参数（元组）、`**kwargs` 收关键字参数（字典） |
| 文档 / 内省 | 首行三引号是 docstring，用 `foo.__doc__` 看，`dir(foo)` 看属性 |
| 返回值 | `return` 交出结果；不写默认返回 `None`；可返回函数调用 |
| 递归 | 函数调用自己，**必须**有停止条件，否则 `RecursionError` |
| 列表作参数 | 可变类型会被就地改，先 `copy()` 再动 |
| 高阶函数 | `map` / `filter` / `reduce` / 偏函数 `partial` |
| 作用域 / 闭包 | LEGB 规则；内部函数可访问外部变量 |
| 装饰器 | `@time_it` 给函数加料；`@wraps` 保住原函数的名字 |

**三句话**

1. 函数把「反复要用的代码」打包起来，做到**写一次、用很多次**——这是结构化编程的第一步。
2. 参数负责**送数据进来**（位置 / 关键字 / 默认值 / 不定长），`return` 负责**把结果交出去**。
3. 把函数当**对象**用，就有了高阶函数与装饰器：函数可以赋值、当参数、当返回值，还能被「套一层」。

**动手练习**

1. 用 `def` 写一个 `area_of_circle(r)`，返回圆面积，并用 `print` 验证。
2. 写一个函数，接收任意数量参数，输出「参数个数 + 全部参数」。
3. 用 `reduce` 求 `[2, 4, 6, 8]` 的乘积。
4. 把 `code/54-list-arg.py` 改成「传副本」的版本，确认原列表不再被改。
5. 给一个「加法函数」套上计算耗时的装饰器，并打印函数名。

---

## 本章小结

**速查表**

| 主题 | 关键结论 |
| --- | --- |
| 定义函数 | `def foo(形参):` + 缩进函数体 |
| 调用函数 | `foo(实参)`；`foo` 是函数对象 |
| 匿名函数 | `lambda x: x + 1` |
| 位置 / 关键字参数 | 按顺序 / `名=值`，可换顺序 |
| 默认值 | 定义时给初值，调用时可不传 |
| 不定长参数 | `*args` → 元组；`**kwargs` → 字典 |
| 文档 / 内省 | `foo.__doc__`、`dir(foo)` |
| 返回值 | `return` 交出结果；缺省返回 `None` |
| 递归 | 自己调自己 + 停止条件 |
| 列表作参数 | 会被就地修改，先 `copy()` |
| 高阶函数 | `map` / `filter` / `reduce` / `partial` |
| 装饰器 | `@decorator`；`@wraps` 保名字 |

**三句话**

1. 函数是「代码的复用单位」：**写一次、调用很多次**。
2. 参数进来、`return` 出去——这一进一出打通了函数与外部世界。
3. 把函数当对象，就解锁了高阶函数与装饰器。

**动手练习**

1. 用函数重写一段你之前「复制粘贴」过的代码。
2. 给购物车 `code/53-shop-cart.py` 加上**库存**逻辑（见第 53 讲作业）。
3. 写一个装饰器，在函数执行前后各打印一行 `--- 开始 ---` / `--- 结束 ---`。

---

## 下一章预告

第 7 章进入**面向对象编程**：把「数据」和「操作数据的函数」打包成**类**，
理解 `class`、对象、属性、方法、继承与封装——这是函数之上再进一步的抽象。

---

[← 上一章：输入输出与文件操作](/guide/io-and-files) ｜ [返回总目录](/) ｜ [下一章：类 →](/guide/classes)

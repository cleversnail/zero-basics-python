# 第 4 章 · 判断与循环

> 让程序会「看情况办事」（条件分支），也会「重复干活」（循环）——这是编程里最常用的两种结构。
> **本章 8 讲（032–039）**，从 `if` / `match` 讲起，到 `while` / `for` / 嵌套，最后用「飞机大战」把它们串起来。

## 🎯 本章目标

- 掌握 `if` / `if...else` / `if...elif...else`，让程序按条件走不同分支
- 认识 Python 3.10 才有的 `match` 语句，学会用 `|` 组合多个模式
- 用 `while` 循环重复执行一段代码，并用 `break` / `continue` 控制节奏
- 用 `for` 循环遍历列表、元组、字典，会用 `enumerate()` 加编号、会写推导式
- 理解**缩进**在嵌套语句里的作用：同样的代码，缩进不同，结果不同
- 把「飞机大战」拆解成循环 + 判断 + 函数，完成第一个综合小程序
- 记住判断与循环里最容易踩的几个坑

**本章代码**

> 📌 **代码约定**：正文代码块都保持**可直接运行**；节选会明确标注「节选」并指向 `code/` 完整文件。
> 所有输出都是**真实运行结果**（本机 Python 3.12.7）。

| 文件 | 内容 |
| --- | --- |
| `code/32-if.py` | `if` / `if...else` / `if...elif...else`、比较运算，以及「能否被 3 整除」作业 |
| `code/33-match.py` | `match` 语句基本用法、`\|` 模式组合、按月份输出季节 |
| `code/34-while.py` | `while` 正向/反向计数、`break`/`continue`、操作列表、猜数字作业 |
| `code/35-for.py` | `for` 遍历元组/列表/字典、`enumerate()`、推导式、列表排序作业 |
| `code/36-nested.py` | 条件嵌套、循环里套条件、多重循环拉平矩阵、九九乘法表作业 |
| `code/37-plane-war.py` | 飞机大战（**有限回合、自动对打版**） |
| `code/38-pitfalls-loop-count.py` | 避坑一：循环内改变遍历次数无效，要用 `break` |
| `code/38-pitfalls-pop.py` | 避坑二：遍历中 `pop` 列表导致 `IndexError` |
| `code/38-pitfalls-indent.py` | 避坑三：嵌套循环缩进不同，执行结果不同 |

---

## 第 32 讲 · if 语句：数据流程出现分支时，怎样编写程序？

### 本节目标

学会用 `if` 让程序「根据条件走不同路」，并能写出一段判断奇偶、判断能否整除的小程序。

### 知识要点

**1. 什么是条件判断**

程序默认是**从上到下顺序执行**的。但很多时候我们希望它「看情况办事」——比如机械臂要判断物体是否进入抓取范围、是否抓牢。这类「是否」的问题，在 Python 里用**条件判断（条件测试）**实现，对应语句就是 `if`。

判断的结果只有两种：**真**（`True`）和 **假**（`False`）——这就是**布尔类型**。注意 `True` / `False` 的首字母必须大写。

**2. if 语句的语法**

```python
if 条件:
    条件为真时执行的语句
```

三个要点（少一个都会报错）：

- 条件后面必须有**冒号** `:`
- 语句块必须**缩进**（一般 4 个空格）——缩进是语法，不是排版
- 与 `if` **对齐**（没有缩进）的语句，不属于 `if` 的语句块，无论条件真假都会执行

**3. 三种写法**

| 写法 | 用途 |
| --- | --- |
| `if ...` | 只有一个分支：条件为真才做 |
| `if ... else ...` | 两个分支：为真做一件事，为假做另一件事 |
| `if ... elif ... else ...` | 三个及以上分支：`elif` 是「否则如果」，可以写多个 |

**4. 测试条件怎么写**

| 写法 | 含义 |
| --- | --- |
| `"date" == "2022-06-01"` | 是否**相等**（注意是双等号 `==`） |
| `"date" != "2022-06-01"` | 是否**不相等** |
| `>  <  >=  <=` | 数值比较：大于、小于、大于等于、小于等于 |

> ⚠️ **常见混淆**：`=` 是赋值（把右边给左边），`==` 才是判断相等。别写错。

### 代码实操

完整代码见 `code/32-if.py`：

```python
# 第 32 讲：if 语句 —— 数据流程出现分支时，怎样编写程序？
# 直接运行：python3 32-if.py

# 1) 最简单的 if：条件为 True 才执行缩进的那一条（或那几条）语句
if True:
    print("条件为真,执行该条语句")

if False:
    print("条件为假,不执行该条语句")
print("没有缩进,不是 if 语句块中的语句,执行")

# 2) if ... else：条件为真做一件事，为假做另一件事
if True:
    print("条件为真")
else:
    print("条件为假")

# 3) if ... elif ... else：处理三种及以上情况
number = 10
if number % 2 == 1:
    print("number是奇数")
elif number % 2 == 0:
    print("number是偶数")
else:
    print(f"number 的值是 {number}")

# 4) 测试条件：相等、不相等，以及数值比较符号
print("date" == "2022-06-01")     # 是否相等
print("date" != "2022-06-01")     # 是否不相等
print(3 > 2, 3 >= 3, 2 < 1, 2 <= 2)

# 5) 课后作业：随机生成 1~100 的整数，判断能否被 3 整除
#    为了让每次运行结果一致，这里固定随机种子；去掉 seed 就是真正随机
import random

random.seed(2026)
for _ in range(5):
    number = int(random.random() * 100 + 1)
    if number % 3 == 0:
        print(f"{number} 能被 3 整除")
    else:
        print(f"{number} 不能被 3 整除")
```

运行命令与**真实输出**：

```bash
$ python3 32-if.py
条件为真,执行该条语句
没有缩进,不是 if 语句块中的语句,执行
条件为真
number是偶数
False
True
True True False True
12 能被 3 整除
51 能被 3 整除
52 不能被 3 整除
87 能被 3 整除
11 不能被 3 整除
```

对照看第 1 段：`if True` 那条执行了；`if False` 那条**没执行**；而最后那句没缩进的 `print` 无论如何都执行——这就是「缩进决定归属」。

> `%` 是**取余**运算符：`number % 3 == 0` 表示「除以 3 余数为 0」，也就是能被 3 整除。

### 课后作业

变量 `number` 是随机生成的 1~100 的整数，请用 `if` 语句判断每次产生的随机数**能否被 3 整除**，并把结果输出到命令行。

```python
# 生成随机数的代码部分（PPT 原题）
import random
number = int(random.random() * 100 + 1)
```

> 参考答案：见上面代码的第 5 段。为让输出可复现，我在代码里加了一句 `random.seed(2026)`（固定随机种子）；**去掉它，就是真正的随机数**，每次跑结果都不一样。

---

## 第 33 讲 · match 语句：如何通过 match 关键字来处理程序的分支逻辑？

### 本节目标

认识 `match` 语句——一种比 `if...elif` 更「对口」的分支写法，尤其适合判断「等于某个具体值」。

### 知识要点

**1. match 语句的语法**

当你有一堆「等于某值就做某事」的分支时，`match` 比一长串 `if...elif` 读起来更清楚：

```python
match 变量:
    case 值1:
        语句
    case 值2:
        语句
    case _:
        兜底语句
```

以判断 HTTP 状态码为例（PPT 原例）：

```python
match http_response_status:
    case 400:
        print("Bad request")
    case 404:
        print("Not found")
    case 418:
        print("I'm a teapot")
    case _:
        print("Something's wrong with the internet")
```

- `match` 语句**需要 Python 3.10 及以上版本**（本机 3.12.7 没问题）
- 变量名 `_` 是**通配符**，意思是「其他所有情况都归我」，它保证 `match` 一定能匹配到一条分支（相当于 `if...elif` 里的 `else`）

**2. 模式组合**

如果想把多个值放进同一个 `case`，用竖线 `|` 把它们连起来：

```python
match http_response_status:
    case 400 | 403 | 404:
        print("4xx error")
    case 500 | 501 | 503:
        print("5xx error")
```

> ⚠️ **PPT 里的一处笔误**：PPT 写的是 `case 500 or 501 or 503`。但在真实的 Python 里，`case` 模式**只认竖线 `|`**，写成 `or` 会直接报 `SyntaxError`。写代码时请以 `|` 为准。

**3. match 与 if 的分工**

- `match` 更擅长**字面值比较**（等于 400、等于 404 这种）
- `if` 更擅长**数值比较**（大于、小于、区间判断）
- 用 `|` 把多个值组合成一个模式，可以有效减少嵌套，让代码更短

### 代码实操

完整代码见 `code/33-match.py`：

```python
# 第 33 讲：match 语句 —— 如何通过 match 关键字来处理程序的分支逻辑？
# match 语句需要 Python 3.10 及以上版本
# 直接运行：python3 33-match.py

# 1) 基本用法：变量名 _ 是通配符，保证 match 一定能匹配成功
http_response_status = 500

match http_response_status:
    case 400:
        print("Bad request")
    case 404:
        print("Not found")
    case 418:
        print("I'm a teapot")
    case _:
        print("Something's wrong with the internet")

# 2) 模式组合：用 "|" 在一个模式里组合多个字面值
#    注意：PPT 里写法是 "case 500 or 501 or 503"，但在真实 Python 里
#    case 模式只认 "|"，写成 "or" 会直接 SyntaxError（见避坑说明）
http_response_status = 404

match http_response_status:
    case 400 | 403 | 404:
        print("4xx error")
    case 500 | 501 | 503:
        print("5xx error")
    case _:
        print("其他状态码")

# 3) 课后作业：根据月份输出季节
month = 7

match month:
    case 3 | 4 | 5:
        print("春季")
    case 6 | 7 | 8:
        print("夏季")
    case 9 | 10 | 11:
        print("秋季")
    case 12 | 1 | 2:
        print("冬季")
    case _:
        print("月份不合法")
```

运行命令与**真实输出**：

```bash
$ python3 33-match.py
Something's wrong with the internet
4xx error
夏季
```

第一段状态码是 `500`，没匹配到 400/404/418，被 `_`（兜底）接住；第二段状态码是 `404`，命中 `400 | 403 | 404` 这条；第三段月份 `7` 落在夏季。

### 课后作业

使用 `match` 语句编写程序，根据用户输入的月份，输出该月份对应的**季节**。例如：输入 7 月输出夏季，输入 12 月输出冬季。

> 参考答案：见上面代码的第 3 段。为了能在文档里直接演示，我把「用户输入」换成了固定值 `month = 7`；你如果想真的读键盘输入，可以用 `month = int(input("请输入月份："))` 替换这一行。

---

## 第 34 讲 · while 循环：需要多次重复执行某段程序时，怎么做？

### 本节目标

学会用 `while` 循环重复执行代码，并掌握 `break` / `continue` 以及「用循环操作列表」的常见套路。

### 知识要点

**1. 循环是什么**

循环是让**一段代码多次执行**的结构。它能把「啰嗦」的重复代码变短，让程序逻辑更强。程序设计的三大常用结构就是：**顺序、判断（分支）、循环**。

**2. while 循环的语法**

```python
while 循环条件:
    循环体（要重复执行的语句）
```

只要「循环条件」为真，就一遍遍执行循环体；直到条件变假，循环才结束。

**3. 循环的几种退出情况**

| 情况 | 说明 |
| --- | --- |
| 条件不满足 | 循环自然结束 |
| 条件一开始就不成立 | 循环体一次都不执行 |
| `break` | 立刻跳出整个循环 |
| `continue` | 跳过本次剩余语句，直接进入下一次循环 |
| 死循环 | 条件永远为真，循环停不下来（要避免！） |

> ⚠️ **最容易犯的错——死循环**：如果循环体里忘了让条件「靠近终点」（比如忘记 `number += 1`），`while` 会永远跑下去。写循环时先想清楚：**这条件最后靠什么变成假？**

**4. 用 while 操作列表**

- **把循环结果放进列表**：先 `list1 = []`，再在循环里 `list1.append(...)`
- **遍历列表**：`while list1:` 表示「只要列表非空就一直循环」，配合 `list1.pop()` 不断取出元素，列表空了循环自然结束

### 代码实操

完整代码见 `code/34-while.py`：

```python
# 第 34 讲：while 循环 —— 需要多次重复执行某段程序时，怎么做？
# 直接运行：python3 34-while.py

# 1) 正向计数：1、2、3
number = 1
while number <= 3:
    print(f"number is {number}")
    number += 1
print(number)   # 循环结束时 number 已经是 4

# 2) 反向计数：3、2、1
number = 3
while number >= 1:
    print(f"number is {number}")
    number -= 1

# 3) 用 break 提前跳出循环
number = 10
while number >= 1:
    print(f"number is {number}")
    number -= 1
    if number == 5:
        break

# 4) 用 continue 跳过本次剩余语句
number = 10
while number >= 1:
    number -= 1
    if number == 5:
        continue
    print(f"number is {number}")

# 5) 用 while 把循环结果放入列表
list1 = []
number = 1
while number < 5:
    list1.append(number)
    number += 1
print(list1)

# 6) 用 while 遍历列表：不断弹出末尾元素，直到列表为空
list1 = [1, 2, 3, 4, 5]
while list1:
    print(list1.pop())

# 7) 课后作业：猜数字，最多猜三次
#    交互输入无法在文档里演示，这里用固定猜测序列代替 input()
target = 42                # 相当于随机产生的正确答案
guesses = [30, 42, 88]     # 相当于用户依次输入的三个数字
index = 0
while index < 3:
    guess = guesses[index]
    index += 1
    if guess == target:
        print(f"第 {index} 次猜中，答案是 {target}，游戏结束")
        break
    print(f"第 {index} 次猜 {guess}，没猜中")
else:
    print(f"三次都没猜中，正确答案是 {target}")
```

运行命令与**真实输出**：

```bash
$ python3 34-while.py
number is 1
number is 2
number is 3
4
number is 3
number is 2
number is 1
number is 10
number is 9
number is 8
number is 7
number is 6
number is 9
number is 8
number is 7
number is 6
number is 4
number is 3
number is 2
number is 1
number is 0
[1, 2, 3, 4]
5
4
3
2
1
第 1 次猜 30，没猜中
第 2 次猜中，答案是 42，游戏结束
```

逐段对照：

- 第 3 段（`break`）：打印到 `number is 6` 后，`number` 变成 5，命中 `break`，循环立即结束。
- 第 4 段（`continue`）：`number` 减到 5 时被 `continue` 跳过，所以输出里**没有** `number is 5`。
- 第 6 段：`pop()` 从列表**末尾**弹出，所以是 `5 4 3 2 1`。
- 第 7 段：第 2 次就猜中，`break` 跳出，`else` 分支（三次都没猜中才执行）被跳过。

> 💡 **循环的 `else`**：`while ... else ...` 里的 `else` 只在循环**正常结束**（没有 `break`）时执行。猜数字就利用它来提示「三次都没猜中」。

### 课后作业

编写一个猜数字游戏：随机产生一个 100 以内的整数，让用户最多输入三次；任意一次输入与随机数相同，游戏结束；否则程序运行三次后提示正确答案并退出。

> 提示：PPT 给的 `random.randint(1, 10)`（写在题目里的是 `random.randint(1, 10)`）可以产生指定范围的随机数。

> 参考答案：见代码第 7 段。交互输入无法在终端文档里演示，所以这里用固定列表 `guesses = [30, 42, 88]` 代替三次键盘输入，等价于用户依次按了三个数字。

---

## 第 35 讲 · for 循环：如何遍历一个对象里的所有元素？

### 本节目标

会用 `for` 遍历列表、元组、字典，会用 `enumerate()` 给遍历加序号，会写简单的推导式。

### 知识要点

**1. for 与 while 的区别**

- `while`：**条件驱动**——只要条件为真就一直重复
- `for`：**遍历驱动**——把某个对象（列表、元组、字典……）里的元素**挨个儿过一遍**

`for` 的语法：

```python
for 变量 in 对象:
    循环体
```

「把对象里的元素一个个取出来处理」这个动作，术语叫**迭代**。

> `range(1, 5)` 生成 `1、2、3、4`——**含头不含尾**，这是新手最容易记错的点。

**2. 遍历字典的三种姿势**

| 写法 | 遍历的是 |
| --- | --- |
| `for title in movie1.keys():` | 所有**键** |
| `for value in movie1.values():` | 所有**值** |
| `for title, value in movie1.items():` | 所有**键值对** |

**3. enumerate()：给遍历加上编号**

`enumerate()` 会把「元素」变成「(编号, 元素)」的形式，配合**元组解包**就能同时拿到序号和内容：

```python
for num, value in enumerate(movie1.items()):
    print(f"第 {num} 个字典元素是 {value}")
```

**4. 推导式**

推导式的作用是「从一个序列构造另一个序列」，格式为：

```
表达式 for 变量 in 序列
表达式 for 变量 in 序列 if 条件
```

它支持列表、字典、元组、集合。例如 `[i * i for i in (1, 2, 3, 4) if i > 2]` 会得到 `[9, 16]`。

### 代码实操

完整代码见 `code/35-for.py`：

```python
# 第 35 讲：for 循环 —— 如何遍历一个对象里的所有元素？
# 直接运行：python3 35-for.py

# 1) for 遍历元组：把每个元素挨个儿操作一遍
for temp_element in (1, 2, 3, 4):
    print(temp_element)

# 2) for + range：range(1, 5) 生成 1、2、3、4（含头不含尾）
for temp_element in range(1, 5):
    print(temp_element)

# 3) 遍历列表：对每个元素做处理
friends = ["wilson", "monica", "john", "wang"]
for friend in friends:
    print(friend.capitalize())   # 首字母大写

# 4) 遍历字典：键、值、键值对
movie1 = {"name": "Friends", "language": "En", "Sessions": 10, "Other name": "Six of One"}

print("-- 键 --")
for title in movie1.keys():
    print(title)

print("-- 值 --")
for value in movie1.values():
    print(value)

print("-- 键值对 --")
for title, value in movie1.items():
    print(title, value)

# 5) 用 enumerate 给遍历加上编号
for i in enumerate(movie1.items()):
    print(i)

for num, value in enumerate(movie1.items()):
    print(f"第 {num} 个字典元素是 {value}")

# 6) 推导式：从一个序列构造另一个序列
list1 = [i for i in (1, 2, 3, 4)]
print(list1)
list2 = [i * i for i in (1, 2, 3, 4)]
print(list2)
list3 = [i * i for i in (1, 2, 3, 4) if i > 2]
print(list3)

# 7) 课后作业：列表首字母升序排列、元素全部大写、输出序号和内容
names = ["rachel", "monica", "Phoebe", "joey"]
sorted_names = sorted(names)   # 按首字母升序
for index, name in enumerate(sorted_names):
    print(index, name.upper())
```

运行命令与**真实输出**：

```bash
$ python3 35-for.py
1
2
3
4
1
2
3
4
Wilson
Monica
John
Wang
-- 键 --
name
language
Sessions
Other name
-- 值 --
Friends
En
10
Six of One
-- 键值对 --
name Friends
language En
Sessions 10
Other name Six of One
(0, ('name', 'Friends'))
(1, ('language', 'En'))
(2, ('Sessions', 10))
(3, ('Other name', 'Six of One'))
第 0 个字典元素是 ('name', 'Friends')
第 1 个字典元素是 ('language', 'En')
第 2 个字典元素是 ('Sessions', 10)
第 3 个字典元素是 ('Other name', 'Six of One')
[1, 2, 3, 4]
[1, 4, 9, 16]
[9, 16]
0 PHOEBE
1 JOEY
2 MONICA
3 RACHEL
```

注意第 7 段：`sorted()` 把名字按**首字母**升序排成 `rachel, monica, Phoebe, joey` 之外的顺序——其实 Python 默认按**字符编码**比较，大写字母排在小写前面，所以结果是 `Phoebe, joey, monica, rachel`（输出中的 `PHOEBE, JOEY, MONICA, RACHEL`）。

### 课后作业

对列表 `["rachel", "monica", "Phoebe", "joey"]` 处理：

1. 按首字母升序排列；
2. 每个元素改为大写；
3. 输出排序后的**序号**和列表内容。

> 参考答案：见代码第 7 段，用 `sorted()` 排序 + `enumerate()` 取序号 + `str.upper()` 转大写。

---

## 第 36 讲 · 语句嵌套：如何处理多重循环的问题？

### 本节目标

学会把判断、循环**一层层套起来**，处理更复杂的逻辑，并能打印出九九乘法表。

### 知识要点

**1. 什么是语句嵌套**

语句嵌套就是「在一个语句里再写另一个语句」，是程序应对复杂逻辑的有效方法。条件语句、循环语句之间可以组成多层嵌套。

> ⚠️ **嵌套别超过 3 层**：超过 3 层的嵌套既影响执行效率，也让读代码的人头疼。遇到多层嵌套，应该回到需求层面**把任务拆分**。

**2. 在条件语句里套条件语句**

以「找出 100 以内能被 7 整除的数」为例，两个条件（小于 100、能被 7 整除）有两种写法：

| 写法 | 思路 |
| --- | --- |
| 写法一 | 先判断「小于 100」，再用临时变量存中间结果，接着判断「能否被 7 整除」 |
| 写法二 | 用 `and` 把两个条件合并进同一个 `if` |

**3. 在循环里套条件语句**

最常见的场景是「遍历序列并做条件判断」。这种「循环 + 条件」还能改写成**推导式**：

```python
>>> [x * x for x in range(10) if x % 7 == 0]
[0, 49]
```

**4. 多重循环**

多重循环常用来处理**二维数据**，比如一个 3×5 的矩阵：

```
[[1, 2, 1, 2, 0],
 [2, 2, 2, 1, 0],
 [1, 1, 2, 2, 0]]
```

外层循环一行行取，内层循环取行里的每个元素，就能把二维结构「拉平」成一维。

### 代码实操

完整代码见 `code/36-nested.py`：

```python
# 第 36 讲：语句嵌套 —— 如何处理多重循环的问题？
# 直接运行：python3 36-nested.py

# 1) 在条件语句里再写条件语句：找出 100 以内能被 7 整除的数
#    写法一：分步判断，用临时变量存储中间结果
number = 49
if number < 100:
    temp = number % 7
    if temp == 0:
        print(f"写法一：{number} 能被 7 整除")

#    写法二：把两个条件合并到一个 if 里
for number in (7, 49, 100):
    if number < 100 and number % 7 == 0:
        print(f"写法二：{number} 能被 7 整除")

# 2) 循环里嵌套条件语句，也能写成推导式
print([x * x for x in range(10) if x % 7 == 0])

# 3) 多重循环：把 3x5 的矩阵拉平成一维列表
data = [[1, 2, 1, 2, 0],
        [2, 2, 2, 1, 0],
        [1, 1, 2, 2, 0]]
list2 = []
for i in data:          # 外层循环：一行一行取
    for j in i:         # 内层循环：取行里的每个元素
        list2.append(j)
print(list2)

# 4) 课后作业：用嵌套循环在命令行打印九九乘法表
for i in range(1, 10):
    row = []
    for j in range(1, i + 1):
        row.append(f"{j}*{i}={i * j}")
    print(" ".join(row))
```

运行命令与**真实输出**：

```bash
$ python3 36-nested.py
写法一：49 能被 7 整除
写法二：7 能被 7 整除
写法二：49 能被 7 整除
[0, 49]
[1, 2, 1, 2, 0, 2, 2, 2, 1, 0, 1, 1, 2, 2, 0]
1*1=1
1*2=2 2*2=4
1*3=3 2*3=6 3*3=9
1*4=4 2*4=8 3*4=12 4*4=16
1*5=5 2*5=10 3*5=15 4*5=20 5*5=25
1*6=6 2*6=12 3*6=18 4*6=24 5*6=30 6*6=36
1*7=7 2*7=14 3*7=21 4*7=28 5*7=35 6*7=42 7*7=49
1*8=8 2*8=16 3*8=24 4*8=32 5*8=40 6*8=48 7*8=56 8*8=64
1*9=9 2*9=18 3*9=27 4*9=36 5*9=45 6*9=54 7*9=63 8*9=72 9*9=81
```

注意「写法二」里 `100` 没有输出——因为 `100 < 100` 不成立；「写法一」只判断了 `49`。「拉平矩阵」得到的是 15 个元素（3 行 × 5 列）。

### 课后作业

请你使用**嵌套语句**在命令行打印**九九乘法表**（形如 `1*1=1` / `1*2=2 2*2=4` …）。

> 参考答案：见代码第 4 段。外层 `for i` 控制第几行，内层 `for j` 控制行内每一项，`range(1, i + 1)` 保证每行只乘到 `i`，形成阶梯状。

---

## 第 37 讲 · 小试牛刀：如何设计一个飞机大战的程序？

### 本节目标

把前面的「循环 + 判断 + 函数」组合起来，读懂一个完整的小程序——飞机大战，并理解「把任务逐层分解」的思路。

### 知识要点

**1. 核心玩法分析**

把游戏拆成「对象 / 属性 / 行为」三块来看：

| 方面 | 内容 |
| --- | --- |
| 对象 | 我方飞机、敌机 |
| 属性 | 坐标、生命值 |
| 行为 | 移动、命中（敌我双方互相攻击） |

**2. 飞机怎么移动**

用二维列表表示地图，`0` 是空位，`"x"` 是我方飞机：

```python
background = [[0, 0, 0],
              [0, "x", 0],
              [0, 0, 0]]
```

所谓「移动」，其实就是把 `[1][1]` 的 `"x"` 搬到相邻坐标、原位置改回 `0`。例如向上移动一格：

```
[0, 0, 0]        [0, "x", 0]
[0, "x", 0]  →   [0, 0, 0]
[0, 0, 0]        [0, 0, 0]
```

**3. 生命值怎么算**

生命值初始为 100；一旦「命中」就减血；减到 0 就游戏结束。逻辑骨架就是这样（下面是伪代码，用中文示意，不是可运行的 Python）：

```
如果 命中:
    生命值 减少
    如果 生命值减到0:
        游戏结束
    否则:
        继续战斗
```

> 📌 这里用中文伪代码只是为了看清逻辑；真正的 Python 写法（可运行）见下面的 `code/37-plane-war.py`。

**4. 本讲的特别说明（重要）**

> 📌 课程原始的飞机大战用 `pynput` 库**监听键盘**来玩——需要额外装库，而且得一直按键程序才有反应，**没法在文档里直接演示，还会卡住**。
>
> 因此本章的 `code/37-plane-war.py` 改成了**「有限回合、自动对打」**版本：我方随机移动、自动开火，敌机自动反击，最多打 6 个回合，**跑完自动退出，不会卡住**。这既保留了「循环 + 判断 + 函数」的全部核心逻辑，又能直接 `python3` 跑出结果。

### 代码实操

完整代码见 `code/37-plane-war.py`：

```python
# 第 37 讲：小试牛刀 —— 飞机大战（有限回合、自动对打版）
# 原始代码用 pynput 监听键盘（需要装库、还要一直按键才能玩），
# 这里改成「有限回合、自动对打」的演示版：跑完自动退出，不会卡住。
# 直接运行：python3 37-plane-war.py

import random

random.seed(7)   # 固定随机种子，让每次运行结果一致

# 生成地图：3x3 网格，0 表示空位，"x" 表示我方飞机
background = [[0, 0, 0],
              [0, "x", 0],
              [0, 0, 0]]


def show_map():
    """打印当前地图。"""
    for row in background:
        print(row)
    print("-" * 12)


def find_player():
    """找到我方飞机当前坐标 (行, 列)，找不到返回 None。"""
    for i in range(3):
        for j in range(3):
            if background[i][j] == "x":
                return i, j
    return None


def move_player(direction):
    """按方向移动我方飞机，越过边界就不动。"""
    pos = find_player()
    if pos is None:
        return
    i, j = pos
    di, dj = direction
    ni, nj = i + di, j + dj
    if 0 <= ni < 3 and 0 <= nj < 3:
        background[i][j] = 0
        background[ni][nj] = "x"


# 敌机：每个敌机有名字和生命值
enemies = [
    {"name": "敌机A", "hp": 60},
    {"name": "敌机B", "hp": 40},
    {"name": "敌机C", "hp": 80},
]

player_hp = 100
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]   # 右、左、下、上

print("=== 飞机大战（自动对打版）===")
show_map()

round_no = 0
max_rounds = 6
while player_hp > 0 and enemies and round_no < max_rounds:
    round_no += 1
    print(f"\n第 {round_no} 回合")

    # 我方随机移动并显示地图
    move_player(random.choice(moves))
    show_map()

    # 我方开火，攻击当前目标敌机
    enemy = enemies[0]
    damage = random.randint(10, 30)
    enemy["hp"] -= damage
    print(f"我方开火，{enemy['name']} 受到 {damage} 点伤害，剩余生命值 {max(enemy['hp'], 0)}")
    if enemy["hp"] <= 0:
        print(f"{enemy['name']} 被击落！")
        enemies.pop(0)

    # 敌机反击
    if enemies:
        counter = random.randint(5, 20)
        player_hp -= counter
        print(f"敌机反击，我方受到 {counter} 点伤害，剩余生命值 {max(player_hp, 0)}")

print("\n=== 战斗结束 ===")
if player_hp <= 0:
    print("我方飞机被击落，游戏结束")
elif not enemies:
    print("敌机全部被击落，我方胜利！")
else:
    print(f"到达回合上限({max_rounds})，战斗中止。我方剩余生命值 {max(player_hp, 0)}")


# 课后作业演示：用 +、- 符号恢复 / 扣除血量，血量为 0 时游戏结束
# 交互按键无法在文档里演示，这里用固定按键序列代替键盘输入
print("\n=== 课后作业：血量增减演示 ===")
hp = 100
keys = ["+", "-", "+", "-", "-", "-"]   # 相当于用户依次按下的键
for key in keys:
    if key == "+":
        delta = random.randint(1, 100)
        hp = min(100, hp + delta)   # 最大血量 100
        print(f"按下 +，恢复 {delta} 点，当前血量 {hp}")
    else:
        delta = random.randint(1, 100)
        hp -= delta
        print(f"按下 -，扣除 {delta} 点，当前血量 {max(hp, 0)}")
    if hp <= 0:
        print("血量为 0，游戏结束")
        break
```

运行命令与**真实输出**（跑完自动退出）：

```bash
$ python3 37-plane-war.py
=== 飞机大战（自动对打版）===
[0, 0, 0]
[0, 'x', 0]
[0, 0, 0]
------------

第 1 回合
[0, 0, 0]
[0, 0, 0]
[0, 'x', 0]
------------
我方开火，敌机A 受到 14 点伤害，剩余生命值 46
敌机反击，我方受到 17 点伤害，剩余生命值 83

第 2 回合
[0, 0, 0]
[0, 0, 0]
[0, 0, 'x']
------------
我方开火，敌机A 受到 12 点伤害，剩余生命值 34
敌机反击，我方受到 8 点伤害，剩余生命值 75

第 3 回合
[0, 0, 0]
[0, 0, 0]
[0, 0, 'x']
------------
我方开火，敌机A 受到 28 点伤害，剩余生命值 6
敌机反击，我方受到 6 点伤害，剩余生命值 69

第 4 回合
[0, 0, 0]
[0, 0, 0]
[0, 'x', 0]
------------
我方开火，敌机A 受到 11 点伤害，剩余生命值 0
敌机A 被击落！
敌机反击，我方受到 7 点伤害，剩余生命值 62

第 5 回合
[0, 0, 0]
[0, 'x', 0]
[0, 0, 0]
------------
我方开火，敌机B 受到 23 点伤害，剩余生命值 17
敌机反击，我方受到 7 点伤害，剩余生命值 55

第 6 回合
[0, 0, 0]
['x', 0, 0]
[0, 0, 0]
------------
我方开火，敌机B 受到 12 点伤害，剩余生命值 5
敌机反击，我方受到 18 点伤害，剩余生命值 37

=== 战斗结束 ===
到达回合上限(6)，战斗中止。我方剩余生命值 37

=== 课后作业：血量增减演示 ===
按下 +，恢复 8 点，当前血量 100
按下 -，扣除 73 点，当前血量 27
按下 +，恢复 16 点，当前血量 43
按下 -，扣除 29 点，当前血量 14
按下 -，扣除 81 点，当前血量 0
血量为 0，游戏结束
```

读这段代码时抓三条主线就行：

1. **主循环**：`while player_hp > 0 and enemies and round_no < max_rounds` —— 三个条件「与」在一起，任一不满足就结束（这就是 `while` + 条件嵌套）。
2. **移动**：`move_player()` 用「找到坐标 → 算新坐标 → 判断是否越界 → 搬移」四步完成，内部是一段 `if` 嵌套。
3. **战斗**：我方开火扣敌机血，敌机反击扣我方血，血归零 / 敌机清空 / 到回合上限三种结局对应最后那段 `if...elif...else`。

> 💡 正如 PPT 总结的：**学会把任务逐层分解，转化为循环和条件语句**；循环和判断一多就容易出 bug，要靠调试去修；涉及底层操作时，能用函数库就别自己从头造。

### 课后作业

参考本节案例代码，通过 `+`、`-` 符号实现飞机大战的**血量恢复**和**血量扣除**：每次按键随机增加或减少 100 以内的整数，当血量为 0 时游戏结束。

例如：初始血量 100，按一次 `+`（最大血量 100，无变化）；再按一次 `-`，随机减少 100 以内整数并显示剩余血量；反复按键直到血量为 0，提示游戏结束。

> 参考答案：见代码末尾的「课后作业：血量增减演示」。交互按键无法在终端文档里演示，这里用固定序列 `keys = ["+", "-", "+", "-", "-", "-"]` 代替按键；`+` 用 `min(100, hp + delta)` 保证不超过上限 100，`-` 每次都随机扣血，归零即 `break` 结束。

---

## 第 38 讲 · 避坑指南：判断和循环中的常见错误

### 本节目标

认识判断与循环里最容易踩的三个坑，看到「错误长什么样」，以后遇到能一眼认出。

> ⚠️ 本讲三个示例中，`38-pitfalls-pop.py` 是**故意触发错误**的，它会以 `IndexError` 退出——这是正常的演示，不是代码坏了。

### 知识要点

**避坑一：循环过程中改变遍历次数，改不动**

```python
for i in (1, 2, 3, 4, 5):
    i = 5
    print(i)
# 执行结果：5 5 5 5 5
```

在循环里给 `i` 赋值 `5`，并不会让循环提前结束——循环**依旧执行 5 次**。原因是：每次迭代开始时，`for` 都会用序列里的下一个值**重新给 `i` 赋值**，你上一次的赋值被覆盖了。想提前结束循环，应该用 **`break`**，而不是给循环变量赋值。

**避坑二：遍历过程中修改列表，会导致误操作**

```python
list1 = ["a", "b", "c", "d"]
for i in range(len(list1)):
    list1.pop(i)
```

`range(len(list1))` 在循环开始前就按**原始长度 4** 把索引定死成了 `0, 1, 2, 3`。可列表 `pop()` 之后长度会**变短**，索引越走越靠后，最终**越界**报 `IndexError`。

> 结论：列表、字典等**可变对象**，一旦长度被修改，就要**重新遍历**，别用固定长度的 `for` 去边遍历边改。

**避坑三：嵌套循环的缩进不同，执行结果不同**

缩进决定了「这句话属于哪一层循环」：

| 缩进位置 | 执行时机 |
| --- | --- |
| 与内层循环体对齐 | 内层、外层循环**都会**执行 |
| 与内层 `while` 对齐 | 每次**外层**循环执行一次 |
| 与外层 `while` 对齐 | 只在循环**全部结束后**执行一次 |

> 因为 Python 靠缩进划分语句块，一旦套了多层循环，缩进错一点结果就全不同。所以**不建议构建 3 层以上的循环**，该拆分就拆分。

### 代码实操

**示例 A：循环过程中改变遍历次数（`code/38-pitfalls-loop-count.py`）**

```python
# 第 38 讲 · 避坑 1：循环过程中改变遍历次数，不会改变循环次数
# 直接运行：python3 38-pitfalls-loop-count.py

# 想在循环里把 i 改成 5，让循环提前结束？做不到。
# 每次迭代开始时，for 都会用序列里的下一个值重新给 i 赋值，
# 所以「循环内的赋值」覆盖不了「循环的次数」，依旧是 5 次。
for i in (1, 2, 3, 4, 5):
    i = 5
    print(i)

# 想让循环提前结束，应该用 break，而不是给循环变量赋值。
print("--- 用 break 才能真正跳出 ---")
for i in (1, 2, 3, 4, 5):
    if i == 3:
        break
    print(i)
```

真实输出：

```bash
$ python3 38-pitfalls-loop-count.py
5
5
5
5
5
--- 用 break 才能真正跳出 ---
1
2
```

前半段打印了 5 个 `5`，证明「循环内赋值」改变不了循环次数；后半段用 `break`，到 `i == 3` 时真的跳出了。

**示例 B：遍历中修改列表导致越界（`code/38-pitfalls-pop.py`，故意报错）**

```python
# 第 38 讲 · 避坑 2：遍历过程中修改列表，导致误操作
# 直接运行：python3 38-pitfalls-pop.py
# 本文件【故意触发错误】，会以 IndexError 退出，属于正常演示。

# 列表在执行 pop() 之后长度会减少，
# 而 range(len(list1)) 在一开始就按「原长度 4」定好了，
# 于是索引越走越界，最终报 IndexError。
list1 = ["a", "b", "c", "d"]
for i in range(len(list1)):
    list1.pop(i)

print(list1)
```

真实输出（这里的报错是**故意设计**的演示）：

```bash
$ python3 38-pitfalls-pop.py
Traceback (most recent call last):
  File "/Users/pengshicong/Desktop/zero-basics-python-cn/04-control-flow/code/38-pitfalls-pop.py", line 10, in <module>
    list1.pop(i)
IndexError: pop index out of range
```

报错要**从下往上读**：最后一行 `IndexError: pop index out of range` 是错误类型——「弹出的索引超出了范围」；倒数第二行 `list1.pop(i)` 是出错的那句话；`line 10` 是出错的行号。

**示例 C：嵌套循环缩进不同，结果不同（`code/38-pitfalls-indent.py`）**

```python
# 第 38 讲 · 避坑 3：循环嵌套中的缩进，会让执行结果出现差别
# 直接运行：python3 38-pitfalls-indent.py

# 缩进决定了「这句话属于哪一层循环」：
#   与内层循环体对齐  → 内层、外层循环都会执行
#   与内层 while 对齐 → 每次外层循环执行一次
#   与外层 while 对齐 → 只在循环全部结束后执行一次

outer = 1
while outer <= 2:
    inner = 1
    while inner <= 2:
        print(f"内外层都执行：outer={outer}, inner={inner}")
        inner += 1
    print(f"只有外层每次执行一次：outer={outer}")
    outer += 1          # 别忘了让外层循环前进，否则会死循环

print("循环全部结束后才执行一次")
```

真实输出：

```bash
$ python3 38-pitfalls-indent.py
内外层都执行：outer=1, inner=1
内外层都执行：outer=1, inner=2
只有外层每次执行一次：outer=1
内外层都执行：outer=2, inner=1
内外层都执行：outer=2, inner=2
只有外层每次执行一次：outer=2
循环全部结束后才执行一次
```

对照输出就能看出三种缩进的差别：

- 「内外层都执行」这行属于**最内层**循环，所以出现了 4 次；
- 「只有外层每次执行一次」与内层 `while` 对齐，所以每个 `outer` 只出现 1 次，共 2 次；
- 「循环全部结束后才执行一次」与外层 `while` 对齐，整段只出现 1 次。

> ⚠️ 示例 C 里 `outer += 1` 那行千万不能漏——否则外层条件永远为真，就成死循环了。

### 课后作业

1. 把 `code/38-pitfalls-pop.py` 改对，使它不报错、并能正确地「每次弹出列表最后一个元素直到列表为空」。（提示：用 `while list1:` 而不是 `for i in range(len(list1))`。）
2. 自己动手改一改 `38-pitfalls-indent.py`，把三句 `print` 分别换到另外两层缩进上，观察输出有什么变化。

---

## 第 39 讲 · 再回首：“判断循环”单元小结

### 本节目标

回顾本章学到的判断与循环工具，把「什么时候用哪个」心里理清。

### 知识要点

本章把「让程序做选择」和「让程序重复干活」两件事讲完了，核心就三组工具：

**判断（做选择）**

- `if` / `if...else` / `if...elif...else`：按条件走不同分支
- 条件结果是布尔值 `True` / `False`；`==` 判相等、`!=` 判不等、`> < >= <=` 比大小
- `match ... case ...`（Python 3.10+）：一堆「等于某具体值」的分支，用 `|` 组合多个模式

**循环（重复干活）**

- `while 条件:`：条件为真就一直重复，适合「次数不确定」的场景
- `for 变量 in 对象:`：把列表/元组/字典里的元素挨个过一遍，适合「遍历」
- `break` 跳出整个循环；`continue` 跳过本次；`while...else` 在「没被 break」时执行

**组合与避坑**

- 语句嵌套能把简单结构拼成复杂逻辑，但**别超过 3 层**
- 循环里改循环变量，改变不了循环次数（要用 `break`）
- 边遍历边修改列表/字典，会导致越界或遗漏（要重新遍历）
- 缩进决定语句属于哪一层，嵌套里尤其要盯紧

### 代码实操

本讲为单元小结，无需新代码；把 `code/32-if.py` ~ `code/38-pitfalls-indent.py` 再跑一遍，对照本章小结的速查表即可。

### 课后作业

用本章所学，随便选一个完成：

1. 用 `for` + `if` 打印 1~100 中所有能被 7 整除的数；
2. 用 `while` 写一个「倒计时」：从 10 数到 0，然后打印「发射！」。

> 参考答案：
> 1. `for x in range(1, 101):` 里加 `if x % 7 == 0: print(x)`。
> 2. `n = 10` + `while n >= 0:` 循环 `print(n); n -= 1`，循环结束后再 `print("发射！")`。

---

## 本章小结

**速查表**

| 主题 | 关键点 |
| --- | --- |
| 单分支 | `if 条件:` + 缩进语句块 |
| 双分支 | `if 条件: ... else: ...` |
| 多分支 | `if ... elif ... else ...`（`elif` 可多个） |
| 布尔值 | `True` / `False`（首字母大写） |
| 比较运算 | `==` `!=` `>` `<` `>=` `<=` |
| match 语句 | Python 3.10+；`case 值:`，`_` 兜底，`\|` 组合多个值 |
| while 循环 | `while 条件:`；注意别写成死循环 |
| 提前退出 | `break` 跳出整个循环；`continue` 跳过本次 |
| for 循环 | `for 变量 in 对象:`，用于遍历 |
| range | `range(1, 5)` → `1,2,3,4`（含头不含尾） |
| 遍历字典 | `.keys()` / `.values()` / `.items()` |
| 加编号 | `enumerate(对象)` + 元组解包 |
| 推导式 | `[表达式 for 变量 in 序列 if 条件]` |
| 嵌套 | 判断、循环可互相嵌套；别超过 3 层 |
| 常见错误 | 循环内改变量无用、遍历中改列表越界、缩进不同结果不同 |

**三句话**

1. **判断让程序会选，循环让程序会重复**——几乎所有程序的骨架都是「顺序 + 判断 + 循环」。
2. **`while` 看条件、`for` 看对象**：次数不确定用 `while`，要遍历集合用 `for`；`break` 跳出、`continue` 跳过。
3. **缩进就是语法**：分支和嵌套里错一个缩进，结果可能完全不同；多层嵌套要克制。

**动手练习**

1. 跑通 `code/32-if.py` ~ `code/36-nested.py`，逐行对照输出，确认分支和循环各走了哪条路。
2. 把 `code/34-while.py` 的猜数字改成**真的随机数**（去掉固定序列，改用 `random.randint`）。
3. 把 `code/37-plane-war.py` 的 `max_rounds` 改成 10 或 20，看三种结局分别怎么触发。
4. 修复 `code/38-pitfalls-pop.py`，让它正确地把列表清空。

---

## 下一章预告

下一章（第 5 章）进入**输入输出与文件操作**：学会用 `input()` 读键盘输入、用 `open()` 读写文件、
处理路径与编码，让程序第一次和「外面的世界」交换数据。本章的循环，也会被大量用来一行行读取文件。

---

[← 上一章：内置数据类型](/guide/data-types) ｜ [返回总目录](/) ｜ [下一章：输入输出与文件操作 →](/guide/io-and-files)

# 第 3 章 · 内置数据类型

> 数据不是散落一地的字符，而是要装进合适的「容器」。本章把 Python 最常用的几种内置容器——
> 列表、元组、集合、字典——一次讲清，并带你用它们搭出一个手机通讯录。
> **本章 14 讲（018–031）**，从「有哪几种类型」到「何时用哪一种」，最后再教你查官方文档自己找答案。

## 🎯 本章目标

- 说清楚 Python 内置数据类型有哪几大类，能用 `type()` 看清一个值的真实类型
- 用**列表**存放有序的同类数据，并掌握增、删、改、查、排序的常见操作
- 用**元组**存放「一次成型、不再修改」的数据，理解它与列表的区别
- 用**集合**自动去重、做并交差运算
- 用**字典**存放键值对，掌握访问、遍历、合并等常见操作
- 把「非结构化数据」（一段文本、一个 csv）转换成结构化数据（列表、字典）
- 综合运用前面所学，做一个**手机通讯录**小项目
- 认识内置数据类型的常见报错，学会看报错、查官方文档与 `help()`

**本章代码**

> 📌 **代码约定**：正文代码块都保持**可直接运行**；节选会明确标注「节选」并指向 `code/` 完整文件。
> 所有输出都是**真实运行结果**（本机 Python 3.12.7）。

| 文件 | 内容 |
| --- | --- |
| `code/18-data-types.py` | 用 `type()` 看清各种内置数据类型 |
| `code/19-list.py` | 列表的创建、索引、嵌套、删除 |
| `code/20-list-ops.py` | 列表常见操作：增删改查、长度、排序 |
| `code/21-tuple.py` | 元组的创建、序列通用操作、不可变性与去重 |
| `code/22-set.py` | 集合的创建、成员检测、集合运算 |
| `code/23-dict.py` | 字典的三种创建方式、键的要求、删除 |
| `code/24-dict-ops-a.py` | 字典常见操作（上）：访问、遍历、增改、pop |
| `code/25-dict-ops-b.py` | 字典常见操作（下）：setdefault、合并、转换、混合 |
| `code/26-phonebook-a.py` | 通讯录（上）：文章分析 + csv 转字典 |
| `code/26-demo.txt` / `code/26-demo.csv` | 第 26 讲用到的样例文本与通讯录 csv |
| `code/27-phonebook-b.py` | 通讯录（下）：存 json、查询、增删 |
| `code/db.json` | 第 27 讲生成的通讯录文件 |
| `code/28-when-to-use.py` | 各类数据类型的适用场景 |
| `code/29-index-error.py` 等 5 个 | 避坑指南：故意触发的 5 种真实报错 |
| `code/30-help-doc.py` | 用 `help()` 查用法、判断迭代器 |
| `code/31-summary.py` | 单元小结：一表回顾六种类型 |

---

## 第 18 讲 · 内置数据类型包括哪几种？

### 本节目标

认识 Python 数据类型的「族谱」，并学会用 `type()` 查看任意一个值的真实类型。

### 知识要点

Python 把数据按「怎么组织、能不能修改」分成几大类。**内置类型**就是语言自带、无需安装就能用的类型。

| 大类 | 代表类型 | 举例 |
| --- | --- | --- |
| 数字类型 | `int` / `float` / `complex` | `10`、`3.14`、`1+2j` |
| 文本类型 | `str` | `"hello"` |
| 序列类型 | `list` / `tuple` / `range` | `[1,2,3]`、`(1,"a")`、`range(1,5)` |
| 集合类型 | `set`（可变）/ `frozenset`（不可变） | `{1,2,3}` |
| 映射类型 | `dict` | `{"one":1, "two":2}` |
| 布尔 / 空值 | `bool` / `NoneType` | `True` / `None` |

**为什么要有这么多类型？** 用作者的话说，好处有三点：

- **内置常用函数**：每种类型都自带一批现成方法，拿来就用；
- **运算符复用**：同一套 `+`、`in`、`[i]` 在不同类型上有各自合理的含义；
- **语义明确，不容易出错**：看到 `{}` 就知道是集合或字典，看到 `[]` 就知道是有序列表。

处理数据的常见路径是：**非结构化 → 半结构化 → 结构化**。
一段文章是非结构化的，切成列表就变得有结构；用字典把「姓名→电话」关联起来，就是半结构化的键值对。

### 代码实操

完整代码 `code/18-data-types.py`：

```python
# 第 18 讲 · 内置数据类型包括哪几种？
# 用 type() 看看各种内置数据类型的「真面目」

# 数字类型
num_int = 10
num_float = 3.14
num_complex = 1 + 2j
print(type(num_int), num_int)
print(type(num_float), num_float)
print(type(num_complex), num_complex)

# 文本类型
text = "hello"
print(type(text), text)

# 序列类型：列表、元组、range
my_list = [1, 2, 3]
my_tuple = (1, "a", 3.0)
my_range = range(1, 5)
print(type(my_list), my_list)
print(type(my_tuple), my_tuple)
print(type(my_range), list(my_range))

# 集合类型
my_set = {1, 2, 3}
print(type(my_set), my_set)

# 映射类型：字典
my_dict = {"one": 1, "two": 2}
print(type(my_dict), my_dict)

# 布尔与空值
print(type(True), True)
print(type(None), None)
```

运行命令与真实输出：

```bash
$ python3 18-data-types.py
<class 'int'> 10
<class 'float'> 3.14
<class 'complex'> (1+2j)
<class 'str'> hello
<class 'list'> [1, 2, 3]
<class 'tuple'> (1, 'a', 3.0)
<class 'range'> [1, 2, 3, 4]
<class 'set'> {1, 2, 3}
<class 'dict'> {'one': 1, 'two': 2}
<class 'bool'> True
<class 'NoneType'> None
```

可以看到 `type(x)` 告诉我们 `x` 到底是哪一类；`True` 的类型是 `bool`，而 `None` 有自己专门的类型 `NoneType`。

### 课后作业

请根据以下需求，选择一个合适的数据类型：

1. 开发通讯录工具，需要存储姓名和手机号码；
2. 开发电商程序，需要存储商品的种类；
3. 开发游戏，需要存储一段与 NPC 的对话。

> 参考答案：① 姓名和手机号是「一对一」的关联，用**字典** `{姓名: 手机号}`；
> ② 商品种类不能重复，用**集合** `set`（若要保持上架顺序也可以先用列表）；
> ③ 一段对话是一串有先后的文本，用**字符串**或**列表**（每句话作为一个元素）。

---

## 第 19 讲 · 列表：如何处理同类数据？

### 本节目标

认识列表的写法、创建方式、用索引取元素、以及删除元素和整个列表。

### 知识要点

**列表（list）** 是存放**一系列有序数据**的容器：

- 用**方括号** `[]` 表示，元素之间用逗号 `,` 分隔；
- 里面的元素可以是数字、字符串，甚至另一个列表；
- 列表**有序**，每个元素都有编号（**索引**），**下标从 0 开始**；
- 列表**可以修改**，定义之后还能增删改元素。

合法的列表写法举例：`[1, 2, 3, 4, 5]`、`['aa', 'cc', 'dd']`、`[123, 'abc']`、`[[1,'a'], [2,'b']]`。

**创建列表**有三种常见方式：

1. 直接用 `[]` 写出来，如 `colours = ["red", "blue", "green"]`；
2. 用内置函数 `list()` 转换，如 `list("red")` 会把字符串拆成 `['r','e','d']`；
3. 用**列表推导式**，如 `[x for x in range(1, 10)]`（循环章会细讲）。

**索引访问**：`list1[0]` 取第一个，`list1[1]` 取第二个，`list1[-1]` 取**最后一个**（负号表示从右往左数）。
嵌套列表要两级索引，比如 `list2[2][0]` 表示「第 3 个元素（它本身是个列表）的第 1 项」。

**删除**：`del list1[0]` 删掉某个元素；`del list1` 把整个列表删掉（之后再用它会报 `NameError`）。

### 代码实操

完整代码 `code/19-list.py`：

```python
# 第 19 讲 · 列表：如何处理同类数据？

# 创建列表：方括号 []，元素之间用逗号分隔
colours = ["red", "blue", "green"]
print(colours)
print(type(colours))

# 内置函数 list() 可以把字符串拆成「字符的列表」
print(list("red"))

# 列表推导式（第 35 讲细讲，这里先看一眼）
print([x for x in range(1, 10)])

# 索引访问：列表是有序的，下标从 0 开始，-1 表示最后一个
list1 = ["a", "b", "c", "d"]
print(list1[0])
print(list1[1])
print(list1[-1])

# 嵌套列表：元素本身也可以是列表
list2 = ["a", "b", ["c", "d"]]
print(list2[2][0])   # 第 3 个元素（一个列表）的第 1 项
print(list2[2][1])   # 想拿到字符串 'd'，就要这样两级索引

# 删除列表中的元素 / 删除整个列表
del list1[0]
print(list1)
del list1
print("list1 已被删除（再访问它会报 NameError）")
```

运行命令与真实输出：

```bash
$ python3 19-list.py
['red', 'blue', 'green']
<class 'list'>
['r', 'e', 'd']
[1, 2, 3, 4, 5, 6, 7, 8, 9]
a
b
d
c
d
['b', 'c', 'd']
list1 已被删除（再访问它会报 NameError）
```

注意 `del list1[0]` 之后，`['a','b','c','d']` 变成了 `['b','c','d']`——删掉的是元素，不是列表本身。

### 课后作业

如果我想创建如下「嵌套列表」，需要如何成功创建？

```
[ [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9] ]
```

> 参考答案：`grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`，
> 取第 2 行第 3 列就是 `grid[1][2]`（值为 `6`）。

---

## 第 20 讲 · 常见常新：列表的常见操作

### 本节目标

掌握列表的**增、删、查、排序**等常用方法，并记住哪些是「原地修改」、哪些会返回新列表。

### 知识要点

**添加元素**

| 方法 | 作用 |
| --- | --- |
| `list.insert(索引, 元素)` | 在指定索引位置插入元素 |
| `list.append(元素)` | 在列表**结尾**追加一个元素 |
| `list.extend(可迭代对象)` | 把可迭代对象**逐个拆开**追加 |

> ⚠️ `append` 和 `extend` 传列表时结果不同：`append([1,2])` 会把整个列表当成**一个**元素塞进去；`extend([1,2])` 会把 `1`、`2` 分别追加。

**修改 / 删除元素**

| 方法 | 作用 |
| --- | --- |
| `list.remove(元素)` | 移除**第一个**匹配的元素 |
| `list.reverse()` | 反转顺序（原地） |
| `list.pop(索引)` | 移除并**返回**该元素；不写索引则移除最后一个 |
| `list.copy()` | 复制列表（浅拷贝） |
| `list.clear()` | 清空列表 |

**计算长度**：`len(list)` 得到长度，`len(list[0])` 得到第 1 个元素的长度，`list.count(元素)` 统计某元素出现次数。

**排序**：`list.sort()` **原地**排序；`sorted(list)` 排序后返回**新列表**，原列表不变。二者都可加 `reverse=True` 表示降序。

### 代码实操

完整代码 `code/20-list-ops.py`：

```python
# 第 20 讲 · 常见常新：列表的常见操作

list_demo = ['a', 'b', 'c', 'd', 'e', ['f', 'g']]
print(list_demo)

# 添加元素：insert（指定位置插入）
list_demo.insert(0, "first")
print(list_demo)

list_demo.insert(-1, "last")   # -1 表示插在最后一个元素之前
print(list_demo)

# 添加元素：append（在结尾追加一个元素）
list_demo.append("last_one")
print(list_demo)

# 扩展元素：extend（把可迭代对象逐个拆开追加）
list_demo.extend("last_one")   # 注意：字符串被拆成了一串单个字符
print(list_demo)

# 移除元素：remove（移除第一个匹配项）
list_demo.remove("last_one")
print(list_demo)

# 弹出元素：pop（移除并返回指定索引的元素）
result = list_demo.pop(0)
print(f"list is {list_demo}")
print(f"result is {result}")

# 反转：reverse（原地）
nums = [3, 1, 2]
nums.reverse()
print(nums)

# 复制：copy（浅拷贝，改副本不影响原列表）
nums_copy = nums.copy()
nums_copy.append(99)
print("原列表:", nums)
print("副本:", nums_copy)

# 清空：clear（原地）
nums.clear()
print("clear 之后:", nums)

# 计算长度：len
print(len("abc"))          # 字符串的长度
print(len([1, 2, 3]))      # 列表的长度

# 统计出现次数：count
print([1, 2, 2, 3, 2].count(2))

# 排序：sorted() 返回新列表，原列表不变
data = [3, 1, 2]
sorted_data = sorted(data)
print("sorted 返回新列表:", sorted_data, "原列表不变:", data)

# 排序：list.sort() 原地排序
data.sort()
print("sort 原地排序:", data)

data.sort(reverse=True)
print("reverse=True 降序:", data)
```

运行命令与真实输出：

```bash
$ python3 20-list-ops.py
['a', 'b', 'c', 'd', 'e', ['f', 'g']]
['first', 'a', 'b', 'c', 'd', 'e', ['f', 'g']]
['first', 'a', 'b', 'c', 'd', 'e', 'last', ['f', 'g']]
['first', 'a', 'b', 'c', 'd', 'e', 'last', ['f', 'g'], 'last_one']
['first', 'a', 'b', 'c', 'd', 'e', 'last', ['f', 'g'], 'last_one', 'l', 'a', 's', 't', '_', 'o', 'n', 'e']
['first', 'a', 'b', 'c', 'd', 'e', 'last', ['f', 'g'], 'l', 'a', 's', 't', '_', 'o', 'n', 'e']
list is ['a', 'b', 'c', 'd', 'e', 'last', ['f', 'g'], 'l', 'a', 's', 't', '_', 'o', 'n', 'e']
result is first
[2, 1, 3]
原列表: [2, 1, 3]
副本: [2, 1, 3, 99]
clear 之后: []
3
3
3
sorted 返回新列表: [1, 2, 3] 原列表不变: [3, 1, 2]
sort 原地排序: [1, 2, 3]
reverse=True 降序: [3, 2, 1]
```

两个关键观察：`extend("last_one")` 把字符串拆成了 `'l','a','s','t','_','o','n','e'` 一串单字符；`sorted(data)` 之后原列表 `data` 仍是 `[3, 1, 2]`，**只有 `sort()` 才是原地改**。

### 课后作业

```
[ 'a', 1, 'b', 2, 'c', 'c', 3 ]
```

请把上面列表里重复的元素 `'c'` 移除，并输出结果。

> 参考答案：`remove('c')` 只会删掉第一个 `'c'`，要删干净可以循环，或借助集合去重后再转回列表。
> 例如：`data = ['a', 1, 'b', 2, 'c', 'c', 3]` → `print(list(dict.fromkeys(data)))` 得到去掉重复 `'c'` 后的结果。

---

## 第 21 讲 · 元组：如何处理一次性数据？

### 本节目标

认识元组，理解它与列表的区别，掌握序列的通用操作与元组的不可变性。

### 知识要点

**元组（tuple）** 和列表很像，也是有序序列，但**创建之后不可修改**——所以适合存放「一次成型、以后不再变」的数据。

**序列家族**：基本序列包括**列表、元组、range**；字符串与二进制数据是特别定制的序列。

**可变 vs 不可变**：

- 列表属于**可变序列**；
- 元组、字符串属于**不可变序列**——`append()`、`pop()`、`insert()` 这些修改元素的函数，在它们身上**用不了**。

**元组与列表的区别**：

1. 创建后：元组**不可修改**，列表**可修改**；
2. 元组执行效率**更高**，列表相对低。

**创建元组**：用**圆括号** `()` 定义；用 `tuple()` 函数创建；或把 `range()`、列表、字符串**转换**成元组。

**序列的通用操作**（列表、元组、range 都支持）：

| 运算 | 结果 |
| --- | --- |
| `x in s` | 若 s 中有某项等于 x，则为 `True`，否则 `False` |
| `x not in s` | 与上一行相反 |
| `s + t` | s 与 t 拼接 |
| `s * n` / `n * s` | s 与自身拼接 n 次 |
| `s[i]` | 第 i 项，起始为 0 |
| `s[i:j]` | 从 i 到 j 的**切片** |
| `s[i:j:k]` | 步长为 k 的切片 |
| `len(s)` | 长度 |
| `min(s)` / `max(s)` | 最小 / 最大项 |
| `s.index(x)` | x 首次出现的索引 |
| `s.count(x)` | x 出现的总次数 |

**删除元组**：用 `del` 可以删除整个元组。

### 代码实操

完整代码 `code/21-tuple.py`：

```python
# 第 21 讲 · 元组：如何处理一次性数据？

# 创建元组：圆括号 () —— 三种方式
color = ("r", "g", "b", "g", "b", "b")
print(type(color), color)

print(tuple("red"))        # 字符串 → 元组
print(tuple(range(1, 4)))  # range → 元组
print(tuple(["a", "b"]))   # 列表 → 元组

# 序列的通用操作（列表、元组、range 都支持）
s = (1, 2, 3, 4, 5)
print(1 in s)              # x in s
print(9 not in s)          # x not in s
print((1, 2) + (3, 4))     # s + t 拼接
print((0,) * 3)            # s * n 重复
print(s[0])                # s[i]
print(s[1:4])              # s[i:j] 切片
print(s[1:4:2])            # s[i:j:k] 带步长的切片
print(len(s))              # len(s)
print(min(s), max(s))      # min / max
print(s.index(3))          # 首次出现的索引
print(s.count(2))          # 出现次数

# 元组不可变：想「修改」只能拼一个新的
color2 = color + ("m",)
print(color2)

# 借助集合给元组去重
new_color = set(color)
print(new_color)
print(tuple(new_color))
```

运行命令与真实输出：

```bash
$ python3 21-tuple.py
<class 'tuple'> ('r', 'g', 'b', 'g', 'b', 'b')
('r', 'e', 'd')
(1, 2, 3)
('a', 'b')
True
True
(1, 2, 3, 4)
(0, 0, 0)
1
(2, 3, 4)
(2, 4)
5
1 5
2
1
('r', 'g', 'b', 'g', 'b', 'b', 'm')
{'g', 'r', 'b'}
('g', 'r', 'b')
```

想给元组「加元素」时，不能改原元组，只能像 `color + ("m",)` 这样拼出一个**新元组**。

### 课后作业

请你创建元组，元组中包含三个元素，分别为 `'x'`、`'y'`、`'z'`。
然后分别执行：增加元素、删除元素、访问第四个元素索引操作。
执行后观察它们的出错信息，并区分不同错误产生的不同提示。

> 参考答案：元组不可变，`t.append('w')` 会报 `AttributeError`（没有 append 方法）；
> `del t[0]` 会报 `TypeError`（不支持删除项）；`t[3]` 会报 `IndexError`（下标越界）。
> 同样是「做错」，报错的**类型**各不相同，这正是判断病因的线索。

---

## 第 22 讲 · 常见常新：集合的常见操作

### 本节目标

认识集合 `set`，掌握它的创建、成员检测、集合运算，以及原地增删。

### 知识要点

**集合（set）** 的最大特点：**元素唯一、不重复**，而且**无序**。

- 集合类型有两种：`set`（**可变**）和 `frozenset`（**不可变**）；日常编程中用 `set` 更多。
- 集合的**唯一性**是它最常被使用的理由——去重、判断「有没有」。

**创建集合**有三种方式：

1. 花括号内用逗号分隔元素，如 `{'wilson', 'yin'}`；
2. 集合推导式，如 `{x for x in range(5)}`；
3. 类型构造器 `set()`，如 `set("hello")`。

**常用操作**：

| 操作 | 含义 |
| --- | --- |
| `len(s)` | 元素数量 |
| `x in s` | 检测 x 是否为成员 |
| `set <= other` | 检测 set 的每个元素是否都在 other 中（子集，允许相等） |
| `set < other` | 检测 set 是否为 other 的**真子集** |

其他内置函数 `add()`、`remove()`、`pop()`、`clear()` 都能对集合做**原地修改**。

**集合运算**：并集 `|`、交集 `&`、差集 `-`、对称差 `^`。

**删除集合**：用 `del` 删除整个集合对象。

### 代码实操

完整代码 `code/22-set.py`：

```python
# 第 22 讲 · 常见常新：集合的常见操作

# 创建集合：花括号 {}
s1 = {'wilson', 'yin'}
print(type(s1), s1)

print(set("hello"))            # 用 set() 构造，自动去掉重复字符
print({x for x in range(5)})   # 集合推导式

# 常用操作
print(len({'a', 'b', 'c'}))        # 元素数量
print('a' in {'a', 'b'})           # 成员检测
print({'a'} <= {'a', 'b'})         # 子集（允许相等）
print({'a', 'b'} <= {'a', 'b'})    # 相等也算子集
print({'a'} < {'a', 'b'})          # 真子集
print({'a', 'b'} < {'a', 'b'})     # 相等 → 不是真子集

# 原地修改：add / remove / pop / clear
s2 = {1, 2, 3}
s2.add(4)
print(s2)

s2.remove(1)
print(s2)

s2.pop()   # 弹出任意一个元素（集合无序，弹哪个不确定）
print(s2)

s2.clear()
print(s2)

# 集合运算
a = {1, 2, 3}
b = {3, 4, 5}
print("并集:", a | b)
print("交集:", a & b)
print("差集:", a - b)
print("对称差:", a ^ b)

# 删除集合
del s1
print("s1 已被删除")
```

运行命令与真实输出：

```bash
$ python3 22-set.py
<class 'set'> {'wilson', 'yin'}
{'e', 'l', 'o', 'h'}
{0, 1, 2, 3, 4}
3
True
True
True
True
False
{1, 2, 3, 4}
{2, 3, 4}
{3, 4}
set()
并集: {1, 2, 3, 4, 5}
交集: {3}
差集: {1, 2}
对称差: {1, 2, 4, 5}
s1 已被删除
```

`set("hello")` 只剩 `{'e', 'l', 'o', 'h'}`——重复的 `l` 被自动去掉了，而且打印顺序与输入不同，这就是「无序」。

### 课后作业

给定列表 `list1 = ['r', 'g', 'b', 'g', 'b', 'r', 'g']`，
请用集合删掉重复元素，并转成**元组**输出。

> 参考答案：`print(tuple(set(list1)))`，得到类似 `('g', 'r', 'b')` 的结果（顺序不定，但无重复）。

---

## 第 23 讲 · 字典：如何处理映射类型的数据？

### 本节目标

认识映射与字典，掌握字典的三种创建方式、键的规则，以及删除操作。

### 知识要点

**映射（mapping）** 描述的是「**一对一的对应关系**」，最典型的例子是「学号 → 姓名」「姓名 → 电话」。

- 映射是**可变类型**；
- Python 里映射**只有一种**数据类型，就是**字典（dict）**；
- 字典里每个元素由**键（key）** 和**值（value）** 两部分组成，写作 `{键: 值}`；
- **键不能重复**，因此「不可哈希」的类型（如列表、字典本身）不能当键；
- 整数 `1` 和浮点数 `1.0` 会被当作**同一个键**。

**创建字典**三种方式：

1. 花括号：`{'one': 1, 'two': 2}`；
2. 类型构造器：`dict(one=1, two=2)`；
3. 字典推导式：`{x: x**2 for x in range(10)}`。

**删除**：`del 字典` 删掉整个字典；`del 字典[键]` 删掉字典里指定的那一个键值对。

### 代码实操

完整代码 `code/23-dict.py`：

```python
# 第 23 讲 · 字典：如何处理映射类型的数据？

# 创建字典：三种方式
d1 = {'one': 1, 'two': 2}
print(type(d1), d1)

d2 = dict(one=1, two=2)          # 类型构造器
print(d2)

d3 = {x: x ** 2 for x in range(5)}   # 字典推导式
print(d3)

# 由两个列表拼出字典（本讲课后作业的答案之一）
list_name = ['name1', 'name2', 'name3']
list_sn = ['1111', '2222', '3333']
name_sn = {
    list_name[0]: list_sn[0],
    list_name[1]: list_sn[1],
    list_name[2]: list_sn[2],
}
print(name_sn)

# 键的要求：必须「可哈希」；整数 1 和浮点 1.0 是同一个键
print({1: '这是 int 键', 1.0: '这行会覆盖上面那行'})

# 删除字典中的元素
del name_sn['name3']
print(name_sn)

# 删除整个字典
temp = {'x': 1}
del temp
print("temp 已被删除")
```

运行命令与真实输出：

```bash
$ python3 23-dict.py
<class 'dict'> {'one': 1, 'two': 2}
{'one': 1, 'two': 2}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
{'name1': '1111', 'name2': '2222', 'name3': '3333'}
{1: '这行会覆盖上面那行'}
{'name1': '1111', 'name2': '2222'}
temp 已被删除
```

注意 `{1: '...', 1.0: '...'}` 打印出来只剩一项——因为 `1` 和 `1.0` 是**同一个键**，后写的把先写的覆盖了。

### 课后作业

已知有两个列表：

```
['name1', 'name2', 'name3']
['1111', '2222', '3333']
```

请把它们组成字典 `{'name1':'1111', 'name2':'2222', 'name3':'3333'}`。

> 参考答案：既可以用上面代码里的下标法逐个赋值，也可以用 `dict(zip(list_name, list_sn))` 一行搞定（`zip` 的用法见第 25 讲）。

---

## 第 24 讲 · 常见常新：字典的常见操作（上）

### 本节目标

掌握字典的**访问、遍历、增改、判断、弹出**等操作。

### 知识要点

**访问字典的内容**：

- `字典.items()` 返回所有「键值对」；
- `字典.keys()` 返回所有键，`字典.values()` 返回所有值。

**访问指定键**：

- `mail_list['tom']`：直接用 `[]`，键**不存在会报 `KeyError`**；
- `mail_list.get('tom')`：用 `get`，键不存在**返回 `None`**，不报错；
- `mail_list.get('tom', '默认值')`：给个默认值，键不存在时返回它。

**遍历字典**：`for key, value in mail_list.items():` 可以同时拿到键和值。

**修改字典**：`mail_list['wilson'] = '...'`——键不存在就**新增**，已存在就**更新**。

**其他**：`len(字典)` 返回项数；`'tom' in 字典` 判断键是否存在；
`pop(键)` 移除该键并返回它的值；`popitem()` 移除**最后加入**的一对键值并返回。

### 代码实操

完整代码 `code/24-dict-ops-a.py`：

```python
# 第 24 讲 · 常见常新：字典的常见操作（上）

mail_list = {'tom': 'tom@gmail.com', 'jerry': 'jerry@foxmail.com', 'john': 'john@163.com'}
print(mail_list)

# 访问「所有元素」：items() / keys() / values()
print(mail_list.items())
print(list(mail_list.keys()))
print(list(mail_list.values()))

# 访问「指定键」
print(mail_list.get('tom'))            # 用 get，键不存在返回 None
print(mail_list['tom'])                # 用 []，键不存在会报 KeyError
print(mail_list.get('nobody'))         # 不存在的键 → None
print(mail_list.get('nobody', '未找到'))  # 给个默认值，键不存在也不报错

# 遍历字典
for key, value in mail_list.items():
    print(key, value)

# 修改字典：新增 / 更新一个键值对
mail_list['wilson'] = 'wilson@163.com'
print(mail_list)

mail_list['wilson'] = 'wilson@new.com'   # 键已存在 → 覆盖旧值
print(mail_list)

# 返回项数 / 判断键是否存在
print(len(mail_list))
print('tom' in mail_list)

# pop：移除指定键并返回它的值
print(mail_list.pop('tom'))
print(mail_list)

# popitem：移除「最后加入」的一对键值并返回
print(mail_list.popitem())
print(mail_list)
```

运行命令与真实输出：

```bash
$ python3 24-dict-ops-a.py
{'tom': 'tom@gmail.com', 'jerry': 'jerry@foxmail.com', 'john': 'john@163.com'}
dict_items([('tom', 'tom@gmail.com'), ('jerry', 'jerry@foxmail.com'), ('john', 'john@163.com')])
['tom', 'jerry', 'john']
['tom@gmail.com', 'jerry@foxmail.com', 'john@163.com']
tom@gmail.com
tom@gmail.com
None
未找到
tom tom@gmail.com
jerry jerry@foxmail.com
john john@163.com
{'tom': 'tom@gmail.com', 'jerry': 'jerry@foxmail.com', 'john': 'john@163.com', 'wilson': 'wilson@163.com'}
{'tom': 'tom@gmail.com', 'jerry': 'jerry@foxmail.com', 'john': 'john@163.com', 'wilson': 'wilson@new.com'}
4
True
tom@gmail.com
{'jerry': 'jerry@foxmail.com', 'john': 'john@163.com', 'wilson': 'wilson@new.com'}
('wilson', 'wilson@new.com')
{'jerry': 'jerry@foxmail.com', 'john': 'john@163.com'}
```

用 `get('nobody')` 得到 `None`、用 `get('nobody', '未找到')` 得到 `未找到`——这就是「不确定键在不在」时优先用 `get` 的原因。

### 课后作业

请你设计一个字典用于存储通讯录，要求包含：必须填写的**姓名**、可以为空的**备注名**、**1 个邮箱**、**至少 2 个手机号码**，并尝试增加和删除联系人。

> 参考答案：

```python
contacts = {
    "张三": {
        "remark": "",
        "email": "zhangsan@163.com",
        "tels": ["13511112222", "13511112223"],
    }
}
contacts["李四"] = {"remark": "老同学", "email": "lisi@qq.com", "tels": ["13900001111", "13900002222"]}
del contacts["张三"]           # 删除联系人
print(contacts)
```

---

## 第 25 讲 · 常见常新：字典的常见操作（下）

### 本节目标

掌握 `setdefault`、字典合并、`zip` 拼字典，以及字典与其它类型的转换和混合使用。

### 知识要点

- `字典.setdefault(key[, default])`：如果键存在就返回它的值；不存在就**插入**默认值并返回。
- **合并字典**：`新字典 = 字典1 | 字典2` 生成一个**新字典**，右边的优先；`字典1 |= 字典2` 是**原地**合并（需 Python 3.9 及以上）。
- **`zip()` 拼字典**：`dict(zip(列表1, 列表2))` 把两个列表按下标「配对」成字典。
- **类型转换**：`list(字典)` 得到键的列表，`str(字典)` 得到字符串形式。
- **混合使用**：字典里可以放列表（`{'red': [255,0,0]}`），列表里也可以放字典（`[{'color':'red', 'value':[255,0,0]}, ...]`），这样就组成了更复杂的数据结构。

### 代码实操

完整代码 `code/25-dict-ops-b.py`：

```python
# 第 25 讲 · 常见常新：字典的常见操作（下）

mail_list = {'tom': 'tom@gmail.com', 'jerry': 'jerry@foxmail.com'}

# setdefault：键存在就返回它的值；不存在就插入默认值并返回
print(mail_list.setdefault('tom', 'xxx@x.com'))    # 已存在 → 返回原值，不覆盖
print(mail_list.setdefault('john', 'john@163.com'))  # 不存在 → 插入
print(mail_list)

# 合并字典：用 | 生成一个新字典（右边优先）
new_mail = {'tom': 'tom@newmail.com', 'kate': 'kate@163.com'}
merged = mail_list | new_mail
print("合并结果:", merged)
print("原字典不变:", mail_list)

# |= 原地合并（Python 3.9 及以上）
mail_list |= new_mail
print("|= 之后:", mail_list)

# zip 把两个列表「配对」成字典
names = ['name1', 'name2', 'name3']
sn = ['1111', '2222', '3333']
print(dict(zip(names, sn)))

# 数据类型之间的转换
print(list({'a': 1, 'b': 2}))   # 字典 → 键列表
print(str({'a': 1}))

# 与其他类型混合使用：字典里放列表
colors = {'red': [255, 0, 0], 'green': [0, 255, 0], 'blue': [0, 0, 255]}
print(colors['red'])

# 与其他类型混合使用：列表里放字典
color_list = [
    {'color': 'red', 'value': [255, 0, 0]},
    {'color': 'green', 'value': [0, 255, 0]},
]
print(color_list[1]['value'])
```

运行命令与真实输出：

```bash
$ python3 25-dict-ops-b.py
tom@gmail.com
john@163.com
{'tom': 'tom@gmail.com', 'jerry': 'jerry@foxmail.com', 'john': 'john@163.com'}
合并结果: {'tom': 'tom@newmail.com', 'jerry': 'jerry@foxmail.com', 'john': 'john@163.com', 'kate': 'kate@163.com'}
原字典不变: {'tom': 'tom@gmail.com', 'jerry': 'jerry@foxmail.com', 'john': 'john@163.com'}
|= 之后: {'tom': 'tom@newmail.com', 'jerry': 'jerry@foxmail.com', 'john': 'john@163.com', 'kate': 'kate@163.com'}
{'name1': '1111', 'name2': '2222', 'name3': '3333'}
['a', 'b']
{'a': 1}
[255, 0, 0]
[0, 255, 0]
```

`|` 生成的是新字典、原字典不动；`|=` 则直接改原字典。`dict(zip(names, sn))` 一行就把两个列表拼成了作业里要的那种字典。

### 课后作业

（同上一讲的通讯录设计题）请用字典存储通讯录，并尝试增加、删除联系人。

> 参考答案：

```python
contacts = {"王武": {"tels": ["18912344321", "18912344322"], "email": "wangwu@163.com"}}
contacts["赵六"] = {"tels": ["13712345678"], "email": "zhaoliu@qq.com"}
print(contacts.pop("王武"))     # 删除并拿到被删的内容
```

---

## 第 26 讲 · 小试牛刀：如何利用类型转换实现手机通讯录？（上）

### 本节目标

理解「数据需要汇总、清洗、从非结构化转成结构化」这一思路，并动手把一段文章和一个 csv 通讯录转成结构化数据。

### 知识要点

**数据处理的思路**：

- 数据要**汇总**才能体现价值；
- 大部分数据**无法直接处理**，需要先清洗掉噪声；
- 数据要从**非结构化**（一段纯文本）转成**半结构化**（键值对）或**结构化**（列表、字典）形式。

**本讲要解决的两件事**：

1. **文章分析**：把一个文本文件读进来，统计总行数、非空行数、某个单词出现的次数；
2. **通讯录转换**：把以 `,` 分隔的 csv 每一行，读成一个**字典** `{'name': ..., 'source': ..., 'tel': ...}`。

**关键技巧**：

- 读文件用 `f.readlines()`，它返回一个**列表**，每一行（含换行符 `\n`）是一个元素；
- 空行就是「只含 `\n` 的行」，用 `list.count("\n")` 就能数出来；
- 统计单词：先用 `" ".join(...)` 把所有行拼成一大段，再用 `.split()` 按空白切分成**单词列表**，最后用 `list.count(单词)` 统计；
- 处理 csv 时，先 `line.strip()` 去掉结尾换行，再 `.split(",")` 按逗号切成字段。

> 📌 本讲代码要读取同目录下的样例文件 `26-demo.txt` 与 `26-demo.csv`；运行前请确保它们在同样的 `code/` 目录里。

### 代码实操

完整代码 `code/26-phonebook-a.py`：

```python
# 第 26 讲 · 小试牛刀：如何利用类型转换实现手机通讯录？（上）
# 本讲分两部分：先把「文章」分析成结构化数据，再把 csv 通讯录读成字典。
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------- 第一部分：把文章当成数据来分析（非结构化 → 结构化）----------
with open(os.path.join(HERE, "26-demo.txt"), encoding="utf-8") as f:
    file_data = f.readlines()   # 每一行（含换行符）作为一个元素，得到一个列表

print("文件一共", len(file_data), "行")

# 空行就是「只含换行符」的行
blank_lines = file_data.count("\n")
print("其中空行", blank_lines, "行")
print("非空行", len(file_data) - blank_lines, "行")

# 统计单词：先把所有行拼成一大段文本，再按空白切分
all_text = " ".join(file_data)
words = all_text.split()
print("单词 I 出现", words.count("I"), "次")
print("单词 you 出现", words.count("you"), "次")
print("单词 You 出现", words.count("You"), "次")
print("you 与 You 一共出现", words.count("you") + words.count("You"), "次")

# ---------- 第二部分：把 csv 通讯录读成「字典」（非结构化 → 结构化）----------
with open(os.path.join(HERE, "26-demo.csv"), encoding="utf-8") as f:
    csv_lines = f.readlines()
print("\n原始 csv 文本:", csv_lines)

contacts = []
for line in csv_lines:
    name, source, tel = line.strip().split(",")   # 按逗号切成 3 个字段
    contacts.append({"name": name, "source": source, "tel": tel})

print("转换后的通讯录（列表套字典）:")
for contact in contacts:
    print(contact)
```

样例文件 `code/26-demo.csv`（3 位联系人）：

```
张三,同事,13511112222
李四,朋友,13900001111
王武,同事,18912344321
```

运行命令与真实输出：

```bash
$ python3 26-phonebook-a.py
文件一共 27 行
其中空行 13 行
非空行 14 行
单词 I 出现 23 次
单词 you 出现 5 次
单词 You 出现 3 次
you 与 You 一共出现 8 次

原始 csv 文本: ['张三,同事,13511112222\n', '李四,朋友,13900001111\n', '王武,同事,18912344321']
转换后的通讯录（列表套字典）:
{'name': '张三', 'source': '同事', 'tel': '13511112222'}
{'name': '李四', 'source': '朋友', 'tel': '13900001111'}
{'name': '王武', 'source': '同事', 'tel': '18912344321'}
```

注意 `readlines()` 读出来的每一行**都带着换行符 `\n`**，所以后面的处理里要先 `strip()` 再去切分，这就是「清洗噪声」。

### 课后作业

请基于本讲的代码，统计样例文件中**每个单词**出现的次数，并把「单词 → 次数」存进字典，形式如下：

```
{ "I": 5, "You": 3, ... }
```

> 参考答案：

```python
words = all_text.split()
counter = {}
for w in words:
    counter[w] = counter.get(w, 0) + 1   # 没有就当作 0 再 +1
print(counter)
```

（其中 `counter.get(w, 0)` 用到了第 24 讲的 `get` 默认值技巧。）

---

## 第 27 讲 · 小试牛刀：如何利用类型转换实现手机通讯录？（下）

### 本节目标

把通讯录存成 `json` 文件、读回来，并实现**查询、增加、删除**联系人。

### 知识要点

- **`json`** 是一种通用的数据交换格式，Python 用内置的 `json` 模块处理它；
- `json.dump(数据, 文件对象, ensure_ascii=False, indent=2)` 把数据**写成** json 文件；`ensure_ascii=False` 让中文原样保存，`indent=2` 让格式更易读；
- `json.load(文件对象)` 把 json 文件**读回**成 Python 对象（这里是「列表套字典」）；
- 查询用**循环 + 条件判断**遍历列表；删除用**列表推导式**过滤；
- 编程除了结果正确，**可读性**也要好——适当多定义变量，把复杂程序拆成几小步。

### 代码实操

完整代码 `code/27-phonebook-b.py`：

```python
# 第 27 讲 · 小试牛刀：如何利用类型转换实现手机通讯录？（下）
# 本讲把 csv 通讯录转成字典、存进 json 文件，再实现查询与增删。
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(HERE, "26-demo.csv")
DB_FILE = os.path.join(HERE, "db.json")

# 1. 读取 csv，每行转成一个字典（非结构化 → 结构化）
contacts = []
with open(CSV_FILE, encoding="utf-8") as f:
    for line in f:
        name, source, tel = line.strip().split(",")
        contacts.append({"name": name, "source": source, "tel": tel})

# 2. 把字典列表保存成 json 格式的「通讯录文件」
with open(DB_FILE, "w", encoding="utf-8") as f:
    json.dump(contacts, f, ensure_ascii=False, indent=2)
print("已保存通讯录文件:", os.path.basename(DB_FILE))

# 3. 从 json 文件读回来
with open(DB_FILE, encoding="utf-8") as f:
    db = json.load(f)
print("通讯录共有", len(db), "位好友")

# 4. 查询：按姓名找到联系人
print("查询「李四」:")
for c in db:
    if c["name"] == "李四":
        print(f"  {c['name']}（{c['source']}）的电话是 {c['tel']}")

# 5. 增加一位联系人
db.append({"name": "赵六", "source": "客户", "tel": "13712345678"})
print("增加赵六后共有", len(db), "位好友")

# 6. 删除一位联系人（这里把「张三」都删掉）
db = [c for c in db if c["name"] != "张三"]
print("删除张三后共有", len(db), "位好友")

# 7. 写回文件，并打印最终通讯录
with open(DB_FILE, "w", encoding="utf-8") as f:
    json.dump(db, f, ensure_ascii=False, indent=2)
print("最终通讯录:")
for c in db:
    print(" ", c)
```

运行命令与真实输出：

```bash
$ python3 27-phonebook-b.py
已保存通讯录文件: db.json
通讯录共有 3 位好友
查询「李四」:
  李四（朋友）的电话是 13900001111
增加赵六后共有 4 位好友
删除张三后共有 3 位好友
最终通讯录:
  {'name': '李四', 'source': '朋友', 'tel': '13900001111'}
  {'name': '王武', 'source': '同事', 'tel': '18912344321'}
  {'name': '赵六', 'source': '客户', 'tel': '13712345678'}
```

程序会把最终结果写回 `code/db.json`，内容长这样：

```json
[
  {
    "name": "李四",
    "source": "朋友",
    "tel": "13900001111"
  },
  {
    "name": "王武",
    "source": "同事",
    "tel": "18912344321"
  },
  {
    "name": "赵六",
    "source": "客户",
    "tel": "13712345678"
  }
]
```

这样，通讯录就从一个 csv 文本，变成了一个能被程序反复读写、查询、增删的**结构化数据文件**。

### 课后作业

在你的通讯录程序里增加一个「按手机号查询联系人」的功能。

> 参考答案：

```python
def find_by_tel(db, tel):
    for c in db:
        if c["tel"] == tel:
            return c
    return None

print(find_by_tel(db, "18912344321"))
```

---

## 第 28 讲 · 常见的内置数据类型都何时使用？

### 本节目标

记住每种类型「擅长什么」，从而在写代码时**选对类型、少写代码**。

### 知识要点

**常见数据类型一览**：常量 `None`；逻辑值 `True` / `False`；空集 `''`、`()`、`[]`、`{}`、`set()`、`range(0)`；
数字 `int` / `float`；序列 `list` / `tuple` / `range`；文本序列 `str`；集合 `set`；映射 `dict`。

**哪些值代表「假」**（`bool()` 会返回 `False`）：

1. 常量 `None`
2. 布尔值 `False`
3. 数值 `0`、`0.0`
4. **空的**序列、映射（如 `""`、`[]`、`{}`、`set()`）

**比较规则因类型而异**：

| 比较对象 | 规则 |
| --- | --- |
| 数字 | 按数值大小 |
| 字符串 | 按首字母的 ASCII 编码大小 |
| 列表 / 元组 | 从第一个元素开始逐项比较 |

**选型口诀**：

- 要**去重** → 用**集合**（自动去重最省事）；
- 想**避免被误修改** → 用**不可变的元组**；
- 要**键值对应** → 用**字典**；
- 要**有序、可增删** → 用**列表**；
- 类型之间可以**组合**成更复杂的结构（列表套字典、字典套列表）。

### 代码实操

完整代码 `code/28-when-to-use.py`：

```python
# 第 28 讲 · 常见的内置数据类型都何时使用？

# 1. 哪些值代表「假」——用 bool() 一眼看穿
falsy = [None, False, 0, 0.0, "", (), [], {}, set(), range(0)]
for value in falsy:
    print(repr(value), "->", bool(value))

# 2. 不同类型的比较规则不一样
print(1 < 2)                 # 数字：按数值大小
print("apple" < "banana")    # 字符串：按首字母的 ASCII 编码
print([1, 2] < [1, 3])       # 列表：从第一个元素开始逐项比较
print((1, 2) < (1, 3))       # 元组：同理

# 3. 需要「不重复」的数据 —— 集合最省事
names = ["tom", "tom", "jerry", "tom"]
print(list(set(names)))

# 4. 想避免被误修改 —— 用不可变的元组
point = (3, 5)
print(point)

# 5. 组合出复杂结构：列表里放字典
users = [
    {"name": "tom", "age": 18},
    {"name": "jerry", "age": 20},
]
print(users[0]["name"], users[1]["age"])
```

运行命令与真实输出：

```bash
$ python3 28-when-to-use.py
None -> False
False -> False
0 -> False
0.0 -> False
'' -> False
() -> False
[] -> False
{} -> False
set() -> False
range(0, 0) -> False
True
True
True
True
['tom', 'jerry']
(3, 5)
tom 20
```

可以看到，`None`、`False`、`0`、各种**空**容器，`bool()` 出来都是 `False`——这就是写 `if 列表:` 时「空就当作假」的道理。

### 课后作业

请根据本讲学习的数据类型回答：

1. 当你需要存储**不重复**的数据时，采用哪种类型？
2. 当你既需要存储**数字**、又要存储**字符**时，采用哪种类型？
3. 当你需要存储**汉字**时，采用哪种类型？

> 参考答案：① **集合 `set`**；② **列表 `list`**（可以混放不同类型的元素）；③ **字符串 `str`**（Python 的字符串天然支持 Unicode 汉字）。

---

## 第 29 讲 · 避坑指南：内置数据类型的常见错误

### 本节目标

认识内置数据类型最常出现的几类错误，学会**读懂报错**并知道怎么避免。

### 知识要点

本章的错误大致分四类：

**1. 访问错误**——访问了不存在的元素：

- 列表：`IndexError: list index out of range`（下标越界）
- 字典：`KeyError: 'xxx'`（键不存在）
- 解决办法：先判断元素是否存在（`元素 in 对象`）再操作，或用字典的 `get()`。

**2. 不同类型之间操作报错**——如 `1 + 'a'`，报 `TypeError: unsupported operand type(s)`。解决办法：**转换成相同的类型**。

**3. 对只读类型写入报错**——如对元组调用 `append()`，报 `AttributeError: 'tuple' object has no attribute 'append'`。写之前先确认类型（`type(t)`）。

**4. 引用错误**——用不可哈希对象（如列表）当字典的键，报 `TypeError: unhashable type: 'list'`。解决办法：用**元组、字符串、数字**当键。

> ⚠️ 下面 5 个文件都是**故意触发错误**的，运行时会报错——这正是它们的用途。

### 代码实操

**错误 1：下标越界 `IndexError`** —— `code/29-index-error.py`

```python
# 第 29 讲 · 避坑指南（1）：访问越界
# ⚠️ 本文件故意触发错误，用来演示真实报错：IndexError
numbers = [1, 2, 3]
print("合法访问:", numbers[0])
print("合法访问:", numbers[2])
print(numbers[3])   # 下标越界！
```

```bash
$ python3 29-index-error.py
合法访问: 1
合法访问: 3
Traceback (most recent call last):
  File "/Users/pengshicong/Desktop/zero-basics-python-cn/03-data-types/code/29-index-error.py", line 6, in <module>
    print(numbers[3])   # 下标越界！
          ~~~~~~~^^^
IndexError: list index out of range
```

列表只有下标 `0、1、2`，`numbers[3]` 越界，报 `IndexError`。

**错误 2：键不存在 `KeyError`** —— `code/29-key-error.py`

```python
# 第 29 讲 · 避坑指南（2）：访问不存在的键
# ⚠️ 本文件故意触发错误，用来演示真实报错：KeyError
mail_list = {"tom": "tom@gmail.com"}
print("存在的键:", mail_list["tom"])
print(mail_list["jerry"])   # 字典里没有 jerry 这个键！
```

```bash
$ python3 29-key-error.py
存在的键: tom@gmail.com
Traceback (most recent call last):
  File "/Users/pengshicong/Desktop/zero-basics-python-cn/03-data-types/code/29-key-error.py", line 5, in <module>
    print(mail_list["jerry"])   # 字典里没有 jerry 这个键！
          ~~~~~~~~~^^^^^^^^^
KeyError: 'jerry'
```

改成 `mail_list.get("jerry")` 就不会报错，只会得到 `None`。

**错误 3：不同类型相加 `TypeError`** —— `code/29-type-error.py`

```python
# 第 29 讲 · 避坑指南（3）：不同类型之间做运算
# ⚠️ 本文件故意触发错误，用来演示真实报错：TypeError
print(1 + "a")   # int 和 str 相加，无法自动转换！
```

```bash
$ python3 29-type-error.py
Traceback (most recent call last):
  File "/Users/pengshicong/Desktop/zero-basics-python-cn/03-data-types/code/29-type-error.py", line 3, in <module>
    print(1 + "a")   # int 和 str 相加，无法自动转换！
          ~~^~~~~
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

`int` 和 `str` 不能用 `+` 混加，要先统一类型，比如 `1 + int("2")` 或 `str(1) + "a"`。

**错误 4：对只读类型写入 `AttributeError`** —— `code/29-attr-error.py`

```python
# 第 29 讲 · 避坑指南（4）：对只读类型做写入
# ⚠️ 本文件故意触发错误，用来演示真实报错：AttributeError
t = (1, 2, 3)
print("先确认它是元组:", type(t))
t.append("new_element")   # 元组没有 append 方法！
```

```bash
$ python3 29-attr-error.py
先确认它是元组: <class 'tuple'>
Traceback (most recent call last):
  File "/Users/pengshicong/Desktop/zero-basics-python-cn/03-data-types/code/29-attr-error.py", line 5, in <module>
    t.append("new_element")   # 元组没有 append 方法！
    ^^^^^^^^
AttributeError: 'tuple' object has no attribute 'append'
```

元组不可变，根本没有 `append` 方法，所以报 `AttributeError`。

**错误 5：不可哈希的键 `TypeError: unhashable type`** —— `code/29-unhashable.py`

```python
# 第 29 讲 · 避坑指南（5）：用不可哈希对象做字典的键
# ⚠️ 本文件故意触发错误，用来演示真实报错：TypeError: unhashable type
d = {}
d[[1, 2]] = "列表不能当键"   # 列表不可哈希！
```

```bash
$ python3 29-unhashable.py
Traceback (most recent call last):
  File "/Users/pengshicong/Desktop/zero-basics-python-cn/03-data-types/code/29-unhashable.py", line 4, in <module>
    d[[1, 2]] = "列表不能当键"   # 列表不可哈希！
    ~^^^^^^^^
TypeError: unhashable type: 'list'
```

列表是可变、不可哈希的，不能当键；换成元组 `(1, 2)` 就可以了。

### 课后作业

定义一个列表 `list1` 和元组 `tuple1`，当 `tuple1` 作为字典 `dict1` 的键时，能否成功定义字典？请说明原因并执行观察。

```python
list1 = [1, 2, 3]
tuple1 = ('abc', list1)
print(type(tuple1))
dict1 = {tuple1, 1}   # 此语句是否能够正确执行？
```

> 参考答案：**不能**。`tuple1` 里含有一个**列表** `list1`，列表不可哈希，
> 所以 `tuple1` 整体也不可哈希，用它当键会报 `TypeError: unhashable type: 'list'`。
> （另外，`{tuple1, 1}` 用的是花括号，那其实是在创建**集合**而不是字典——字典要用 `键: 值` 的写法。）

---

## 第 30 讲 · 内置数据类型参考：如何使用官方文档与帮助？

### 本节目标

学会两件事：**读官方文档**，以及用 `help()` 在终端里「随手查」。

### 知识要点

**官方文档**（权威、体系化）：

- 标准库总入口：<https://docs.python.org/zh-cn/3.10/library/index.html>
- 内置类型（str、list、dict 等）专门页面：<https://docs.python.org/zh-cn/3.10/library/stdtypes.html>

读文档时，要学会拆解一条签名，例如 `str.count(sub[, start[, end]])`：

- `str` 是**对象/类型**；
- `count()` 是它的**方法**；
- `sub` 是**必须**给的参数；
- `[start[, end]]` 用方括号包起来，表示**可选**参数。

**使用帮助**：

- IDE 自带的智能提示 / 补全，也是「帮助」的一种；
- `help(对象)` 是**提醒式**帮助，会直接把对象的用法打印出来。

**一句话对照**：官方文档是**体系化**的帮助，`help()` 是**提醒式**的帮助。

### 代码实操

完整代码 `code/30-help-doc.py`：

```python
# 第 30 讲 · 内置数据类型参考：如何使用官方文档与帮助？

# help() 是「提醒式」帮助：把对象的用法直接打出来
help(str.count)

# 判断一个对象是不是「迭代器」
it = iter([1, 2, 3, 4])
print("it 的类型:", type(it))
print("it 有 __next__ 方法吗:", hasattr(it, "__next__"))
print("逐个取出元素:")
print(next(it))
print(next(it))
```

运行命令与真实输出：

```bash
$ python3 30-help-doc.py
Help on method_descriptor:

count(...) unbound builtins.str method
    S.count(sub[, start[, end]]) -> int

    Return the number of non-overlapping occurrences of substring sub in
    string S[start:end].  Optional arguments start and end are
    interpreted as in slice notation.

it 的类型: <class 'list_iterator'>
it 有 __next__ 方法吗: True
逐个取出元素:
1
2
```

`help(str.count)` 打出的正是 count 的用法与参数说明；`iter([1,2,3,4])` 得到的是 `list_iterator`，它有 `__next__` 方法，所以**是**迭代器——这正好回答了本讲的作业。

### 课后作业

在学习中遇到一条没见过的语句 `it = iter([1, 2, 3, 4])`，请结合官方文档判断 `it` 是否**迭代器类型**。

> 参考答案：**是**。迭代器必须实现 `__next__`（和 `__iter__`）方法。
> 上面代码里 `hasattr(it, "__next__")` 打印出 `True`，`type(it)` 是 `<class 'list_iterator'>`，
> 所以 `it` 是迭代器，可以用 `next()` 逐个取值。

---

## 第 31 讲 · 再回首：“内置数据类型”单元小结

### 本节目标

用一个整体视角把本章六种核心数据类型串起来，形成一张「随手可查」的速查表。

### 知识要点

**六种核心类型一览**

| 类型 | 关键字 | 可变？ | 有序？ | 记法 | 典型用途 |
| --- | --- | --- | --- | --- | --- |
| 数字 | `int` / `float` / `complex` | 不可变 | — | `10`、`3.14` | 算术运算 |
| 字符串 | `str` | 不可变 | 有序 | `"abc"` | 处理文本 |
| 列表 | `list` | **可变** | 有序 | `[]` | 存放同类、可增删的数据 |
| 元组 | `tuple` | **不可变** | 有序 | `()` | 一次性、不想被改的数据 |
| 集合 | `set` | 可变 | **无序** | `{}` | 去重、集合运算 |
| 字典 | `dict` | 可变 | 有序（3.7+） | `{键: 值}` | 键值对应的映射数据 |

**常用转换**：`list(set(...))` 去重、`tuple(...)` 转元组、`dict(zip(a, b))` 两列表拼字典、`set(tuple)` 去重。

### 代码实操

完整代码 `code/31-summary.py`：

```python
# 第 31 讲 · 再回首：内置数据类型单元小结

# 一表回顾：本章 6 种核心数据类型
summary = {
    "数字": "int / float / complex —— 参与算术运算",
    "字符串": "str —— 不可变、有序，处理文本",
    "列表": "list —— 可变、有序，[]，存放同类数据",
    "元组": "tuple —— 不可变、有序，()，存放一次性数据",
    "集合": "set —— 可变、无序、元素唯一，{}",
    "字典": "dict —— 键值对映射，{键: 值}",
}
for key, value in summary.items():
    print(f"{key}：{value}")

# 各类型的典型操作串一遍
scores = [90, 85, 90]
print("列表:", scores, "→ 去重并排序:", sorted(set(scores)))

info = (("tom", 18), ("jerry", 20))
print("元组:", info)

mail = dict(info)
print("元组转字典:", mail)
```

运行命令与真实输出：

```bash
$ python3 31-summary.py
数字：int / float / complex —— 参与算术运算
字符串：str —— 不可变、有序，处理文本
列表：list —— 可变、有序，[]，存放同类数据
元组：tuple —— 不可变、有序，()，存放一次性数据
集合：set —— 可变、无序、元素唯一，{}
字典：dict —— 键值对映射，{键: 值}
列表: [90, 85, 90] → 去重并排序: [85, 90]
元组: (('tom', 18), ('jerry', 20))
元组转字典: {'tom': 18, 'jerry': 20}
```

`sorted(set([90, 85, 90]))` 一行同时用了列表、集合、排序；`dict(元组)` 又把「键值对元组」变成了字典——类型之间的转换与组合，正是本章的精髓。

### 课后作业

请不看书，凭记忆说出：列表、元组、集合、字典四者各**一个**最不能替代的用途。

> 参考答案：列表——**有序、可随时增删**的序列；元组——**不可变**、防止误改；
> 集合——**自动去重**、做交并差运算；字典——**键值对应**的快速查找。

---

## 本章小结

**速查表**

| 主题 | 关键点 |
| --- | --- |
| 看类型 | `type(x)` |
| 列表创建 | `[]`、`list()`、列表推导式 `[x for x in ...]` |
| 列表增删 | `append` / `insert` / `extend` / `remove` / `pop` / `clear` |
| 列表排序 | `sort()`（原地）、`sorted()`（返回新列表），均可 `reverse=True` |
| 元组 | `()` 圆括号，**不可变**，序列通用操作都支持 |
| 集合 | `{}`，**元素唯一、无序**；`|` `&` `-` `^`；`set` 去重 |
| 字典创建 | `{k: v}`、`dict()`、字典推导式、`dict(zip(a, b))` |
| 字典访问 | `d[k]`（KeyError）、`d.get(k, 默认值)`（安全） |
| 字典遍历 | `for k, v in d.items():` |
| 字典合并 | `d1 | d2`（新字典）、`d1 |= d2`（原地，3.9+） |
| 真 / 假判断 | `None`、`False`、`0`、空容器 都为假 → `bool(x)` 可验证 |
| 常见报错 | `IndexError` / `KeyError` / `TypeError` / `AttributeError` / `unhashable type` |
| 查帮助 | `help(对象)`；官方文档 docs.python.org/zh-cn/3.10/library/stdtypes.html |
| 存文件 | `json.dump(...)` / `json.load(...)`，中文加 `ensure_ascii=False` |

**三句话**

1. 数据类型是「装数据的容器」：**列表有序可改、元组有序不可改、集合唯一无序、字典键值对应**——选对容器，代码自然变短。
2. 处理数据的通用套路是 **非结构化（文本）→ 半结构化（键值对）→ 结构化（列表/字典）**，清洗、切分、转换三步走。
3. 报错是最好的老师：**先读最后一行看类型、再往上找出错行**，不确定就 `help()` 或翻官方文档。

**动手练习**

1. 造一个列表 `[3, 1, 2, 3, 1]`，先 `sorted()` 排序，再用集合去掉重复，输出 `[1, 2, 3]`。
2. 用两个列表 `['a','b','c']` 和 `[1,2,3]` 拼成一个字典 `{'a':1,'b':2,'c':3}`。
3. 把 `code/26-demo.csv` 读成「列表套字典」，并打印「朋友」这一类的所有联系人。
4. 故意写下 `letters = ['a','b']; print(letters[5])`，观察报错，再用 `if len(letters) > 5:` 的方式避免它。

---

## 下一章预告

第 4 章进入 **判断与循环**：`if / elif / else` 让程序会「做选择」，
`for` 与 `while` 让程序会「重复做」；还会讲到 `break`、`continue` 和列表推导式的完整用法。
本章的列表、字典，下一章会开始被大量「循环遍历」——准备好了吗？

---

[← 上一章：Python 编程基础知识](/guide/python-basics) ｜ [返回总目录](/) ｜ [下一章：判断与循环 →](/guide/control-flow)

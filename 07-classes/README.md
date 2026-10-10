# 第 7 章 · 类

> 从「面向过程」走到「面向对象」：学会用类把数据和动作封装在一起，再用继承、装饰器、魔术方法写出可复用的代码。
> **本章 8 讲（058–065）**

## 🎯 本章目标

- 说清「面向过程」和「面向对象」两种编程思想到底差在哪
- 会用 `class` 定义类、实例化对象，分清**类属性**与**实例属性**
- 用**继承**和 `super()` 复用父类代码，理解多继承、`__mro__` 与 Mixin
- 掌握三个类装饰器：`classmethod`、`staticmethod`、`property`
- 综合运用，写一个「自动咖啡机」小项目
- 会用 `__init__` 为对象传递参数，认识魔术方法
- 知道类的常见错误，并能用 SOLID 原则指导类的设计

**本章代码**

> 📌 **代码约定**：正文代码块都保持**可直接运行**；节选会明确标注「节选」并指向 `code/` 完整文件。
> 所有输出都是**真实运行结果**（本机 Python 3.12.7）。

| 文件 | 内容 |
| --- | --- |
| `code/58-thinking.py` | 面向过程 vs 面向对象，以及对象的 `is` / `==` |
| `code/59-class-instance.py` | 定义类、实例化、类属性 / 实例属性 / 方法 |
| `code/60-inherit.py` | 继承、`super()`、多继承、`__mro__` 与 Mixin |
| `code/61-decorators.py` | `classmethod` / `staticmethod` / `property` |
| `code/62-coffee-machine.py` | 自动咖啡机（用 Mixin 拼装三种原料） |
| `code/63-no-self.py`、`code/63-self-cls.py` | 避坑指南：故意触发的两种真实报错 |
| `code/64-init.py` | `__init__` 传参、魔术方法与 `dir()` |
| `code/65-review.py` | 单元小结：把本章要点串一遍 |

---

## 第 58 讲 · 编程思想不同会导致怎样的代码差异？

### 本节目标

看懂「面向过程」和「面向对象」两种编程思想，并理解 Python 里「一切都是对象」这句话的含义。

### 知识要点

**1. 面向过程**

- 以**过程（步骤）**为核心，强调「解决问题的流程」。
- 写代码时的思路是：**先 xxx，再 xxx，然后 xxx**。
- 特点：**符合时间顺序，易于理解程序逻辑**。
- 适合流程清晰、规模不大的需求。

**2. Python 中的对象**

Python 即使写「面向过程」的代码，用到的数据也都是**对象**：

- 变量指向的基础数据类型（数字、字符串、列表……）全都是对象；
- `id()` 函数返回对象的**整数标识**（可以理解为对象在内存里的编号）；
- `is` 判断两个名字是否指向**同一个对象**；`==` 判断两个对象的**值**是否相等。

| 比较 | 含义 | 例子 |
| --- | --- | --- |
| `list1 == list2` | 值相等 | `[1,2,3] == [1,2,3]` → `True` |
| `list1 is list2` | 是同一个对象 | `[1,2,3] is [1,2,3]` → `False` |

**3. 面向对象编程**

- 更关注**一个对象的定义**：它有什么数据、能做什么动作。
- 优点是**更容易抽象和复用**：以列表为例，列表是一类对象，它们都有「添加、删除、切片」等共同能力；你为「列表」这一类增加一个能力，所有列表就都具备了。

**4. 两者的区别**

- 面向对象比面向过程**更适合复杂度高的编码需求**；
- 面向对象适合**封装需求更严格**的程序；
- 面向对象可设计的**编程模式更丰富**；
- 面向对象涉及的**技术概念更多**（后面几讲的类、继承、装饰器就是明证）。

> 💡 一句话：面向过程盯着「怎么做」，面向对象盯着「谁来负责做」。

### 代码实操

完整代码见 `code/58-thinking.py`。同一个「做一杯美式咖啡」的需求，用两种思想各写一遍：

```python
# 第 58 讲 · 编程思想不同会导致怎样的代码差异？
#
# 同一个需求「做一杯美式咖啡」，用两种编程思想各写一遍，体会差异。

print("========== 面向过程：以「步骤」为核心 ==========")


def make_coffee():
    # 先 xxx，再 xxx，然后 xxx —— 完全按照时间顺序排列
    water = 200
    print(f"  1. 加水 {water} ML")
    coffee = 1
    print(f"  2. 加咖啡液 {coffee} 份")
    print("  3. 美式咖啡完成")


make_coffee()

print()
print("========== 面向对象：以「对象」为核心 ==========")


class Coffee:
    """一杯咖啡：数据（水和咖啡液的量）和动作（制作）被封装在一起。"""

    def __init__(self, water, coffee):
        self.water = water
        self.coffee = coffee

    def make(self):
        if self.water:
            print(f"  加水 {self.water} ML")
        if self.coffee:
            print(f"  加咖啡液 {self.coffee} 份")
        print("  美式咖啡完成")


americano = Coffee(water=200, coffee=1)
americano.make()

print("  再换一个对象，就是另一杯：")
another = Coffee(water=150, coffee=1)
another.make()

print()
print("========== Python 里一切都是对象：is 与 == ==========")

num = 100
num2 = num
print("  num is num2 （是同一个对象吗）  :", num is num2)
print("  num == num2 （值相等吗）        :", num == num2)

num = 456  # num 指向了一个新对象
print("  改 num 之后 num is num2         :", num is num2)
print("  num =", num, " num2 =", num2)

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print("  list1 == list2 （值相等吗）      :", list1 == list2)
print("  list1 is list2 （是同一个对象吗）:", list1 is list2)

list1.append(4)
print("  给 list1 追加 4 之后：")
print("    list1 =", list1)
print("    list2 =", list2)
```

运行命令：

```bash
$ python3 58-thinking.py
```

本机实测输出：

```
========== 面向过程：以「步骤」为核心 ==========
  1. 加水 200 ML
  2. 加咖啡液 1 份
  3. 美式咖啡完成

========== 面向对象：以「对象」为核心 ==========
  加水 200 ML
  加咖啡液 1 份
  美式咖啡完成
  再换一个对象，就是另一杯：
  加水 150 ML
  加咖啡液 1 份
  美式咖啡完成

========== Python 里一切都是对象：is 与 == ==========
  num is num2 （是同一个对象吗）  : True
  num == num2 （值相等吗）        : True
  改 num 之后 num is num2         : False
  num = 456  num2 = 100
  list1 == list2 （值相等吗）      : True
  list1 is list2 （是同一个对象吗）: False
  给 list1 追加 4 之后：
    list1 = [1, 2, 3, 4]
    list2 = [1, 2, 3]
```

读一遍就能看出面向对象的优势：数据（水、咖啡液）和动作（制作）被**打包在一起**，换一杯咖啡只要 `Coffee(150, 1)`，而面向过程的写法里，这些量要靠一个又一个参数在函数间传递。

### 课后作业

有一首经典童谣：「故事讲的是从前有座山，山上有座庙，庙里有个老和尚，老和尚在给小和尚讲故事，故事讲的是从前有座山……」

请分别用**面向过程**和**面向对象**的伪代码，描述怎么编写这个「无限循环讲故事」的程序。

> 参考思路：
>
> **面向过程**——写一个函数 `讲故事()`，里面打印「从前有座山」，最后再调用 `讲故事()` 自己（递归）。
> **面向对象**——定义 `山`、`庙`、`老和尚`、`小和尚` 几个类，`老和尚.讲故事(小和尚)` 这个方法内部再让「新的老和尚」继续讲，把「故事」这个行为封装进对象里。

---

## 第 59 讲 · 类与实例：如何使用面向对象的思想编写程序？

### 本节目标

学会用 `class` 定义一个类、用「实例化」造出对象，分清类属性、实例属性和方法的区别。

### 知识要点

**1. 定义一个类**

```python
class Coffee(object):
    pass  # 类体（放在这里定义属性和方法）
```

- `class` 是定义类的关键字；
- `Coffee` 是类名，**一般首字母大写**；
- `object` 是父类，**可以不写**，默认就继承自 `object`；
- 还可以用 `type()` 函数动态创建类（一般用于特殊场景）。

**2. 类的实例化**

```python
mocha = Coffee()
```

`mocha` 就是「用 `Coffee` 这个类实例化出来的一个对象」。可以把**类**想成图纸，**实例**是按图纸造出来的具体一件东西。

**3. 类的属性**

```python
class Coffee():
    water = 0
    milk = 0
```

写在类里、方法外的变量叫**类属性**，被这个类的所有实例**共享**。

**4. 类的方法**

```python
class Coffee(object):
    def add_water(self):
        self.water = 1
```

- 定义在类里的函数叫**方法**；
- 实例方法的**第一个参数固定是 `self`**，代表「当前这个对象」；
- 用 `self.xxx = ...` 赋的值是**实例属性**，只属于调用的那个对象。

> ⚠️ 要能根据上下文，区分「类的实例化」(`Coffee()`) 和「函数调用」——前者造对象，后者执行逻辑。

### 代码实操

完整代码见 `code/59-class-instance.py`：

```python
# 第 59 讲 · 类与实例：如何使用面向对象的思想编写程序？


# class 是定义类的关键字；Coffee 是类名（约定首字母大写）
class Coffee:
    # 类属性：写在类里、方法外，被所有实例「共享」
    water = 0
    milk = 0

    # 实例方法：第一个参数固定是 self，代表「当前这个对象」
    def add_water(self):
        # self.xxx 这样写，产生的是「实例属性」，只属于调用的那个对象
        self.hot_water = 1


print("========== 1. 类的实例化 ==========")
# Coffee() 就是「实例化」：类像一张图纸，实例是按图纸造出来的具体一个
mocha = Coffee()
print("  mocha 的类型        :", type(mocha))
print("  mocha 是 Coffee 实例吗:", isinstance(mocha, Coffee))
print("  注意：类本身也是对象 :", type(Coffee))

print()
print("========== 2. 对象拥有类的属性 ==========")
print("  mocha.water =", mocha.water)
print("  mocha.milk  =", mocha.milk)

print()
print("========== 3. 调用实例方法，产生实例属性 ==========")
mocha.add_water()
print("  mocha.hot_water =", mocha.hot_water)

print()
print("========== 4. 两个实例互不干扰 ==========")
latte = Coffee()
print("  改之前：mocha.water =", mocha.water, " latte.water =", latte.water)
mocha.water = 300  # 只给 mocha 自己挂一个实例属性
print("  改之后：mocha.water =", mocha.water, " latte.water =", latte.water)
print("  类属性的原值没变：Coffee.water =", Coffee.water)
```

运行命令：

```bash
$ python3 59-class-instance.py
```

本机实测输出：

```
========== 1. 类的实例化 ==========
  mocha 的类型        : <class '__main__.Coffee'>
  mocha 是 Coffee 实例吗: True
  注意：类本身也是对象 : <class 'type'>

========== 2. 对象拥有类的属性 ==========
  mocha.water = 0
  mocha.milk  = 0

========== 3. 调用实例方法，产生实例属性 ==========
  mocha.hot_water = 1

========== 4. 两个实例互不干扰 ==========
  改之前：mocha.water = 0  latte.water = 0
  改之后：mocha.water = 300  latte.water = 0
  类属性的原值没变：Coffee.water = 0
```

第 4 段尤其要读懂：`mocha.water = 300` 只是给 `mocha` 挂了一个**自己的**实例属性，`latte.water` 读到的仍是类属性 `0`，`Coffee.water` 也没变。

### 课后作业

定义一个类表示**汉堡**，要求：

1. 有增加 / 减少「一片蔬菜」、增加 / 减少「一片肉饼」的方法；
2. 有显示当前蔬菜、肉饼数量的方法；
3. 实例化一个汉堡后，用这些方法改数量并显示层数。

> 参考思路（节选）：把蔬菜、肉饼数量写成 `self.蔬菜`、`self.肉饼`，用 `+1` / `-1` 的方法修改，再用一个 `显示()` 方法把它们打印出来。

---

## 第 60 讲 · 类的继承：如何解决代码重用的问题？

### 本节目标

理解继承的用途，会用 `super()` 复用父类方法，并分清多继承与 Mixin。

### 知识要点

**1. 为什么需要继承**

继承能让新手**快速上手大牛设计的代码**。比如你想让自定义的字典「在字典功能之上加点料」，直接继承 `UserDict` 即可：

```python
from collections import UserDict

class my_dict(UserDict):
    pass  # 在继承来的字典功能之上，再添加你自己的功能
```

**2. 父类与子类**

- 在继承里，被继承的类叫**父类**，继承的类叫**子类**；
- 子类**继承父类的属性和方法**；
- 想「加一点、但不丢掉父类逻辑」时，用 `super()` 调用父类的同名方法。

```python
class Father(object):
    def run(self):
        pass

class Son(Father):
    def run(self):
        super().run()      # 先执行父类的 run
        print("run")       # 再补充自己的行为
```

> 💡 思考一下：如果**不用** `super()`，父类 `run` 里的代码就**完全不执行**了——这正是「复用」的关键。

**3. 类的多继承**

一个类可以同时继承多个父类：

```python
class D(B, C):
    pass
```

当继承图出现「菱形」（A 被 B、C 继承，D 又同时继承 B、C）时，Python 用 **C3 算法**按顺序遍历继承图。用 `类名.__mro__` 可以查看真实顺序。注意：**多重继承会增加复杂度，应当少用**。

**4. 混入（Mixin）**

- Mixin 是**借用多继承语法给现有类加方法**的技巧；
- Mixin **只包含方法、不定义新属性**；
- Mixin **便于重用，但绝不能被单独实例化**；
- 命名习惯在类名后加 `Mixin`。

比如披萨可以按层数（单层 / 双层）和形状（圆形 / 方形）分别做成 Mixin，再拼出一个披萨类：

```python
class 披萨(主要材料, 单层Mixin, 圆形Mixin):
    pass
```

### 代码实操

完整代码见 `code/60-inherit.py`：

```python
# 第 60 讲 · 类的继承：如何解决代码重用的问题？


print("========== 1. 父类与子类，super() 复用父类方法 ==========")


# 被继承的类叫父类，继承的类叫子类
class Father(object):
    def run(self):
        print("  run in father")


class Son(Father):
    def run(self):
        super().run()  # 先执行父类同名方法的内容
        print("  run in son")  # 再补充子类自己的行为


f = Father()
f.run()
print("  ---")
s = Son()
s.run()

print()
print("========== 2. 查看继承顺序：__mro__ ==========")
print("  Son.__mro__ =", Son.__mro__)

print()
print("========== 3. 多继承与 Mixin ==========")
# Mixin（混入）：借用多继承语法，只提供方法、不定义属性，也绝不单独实例化，
# 类名习惯以 Mixin 结尾。用它给现有类「拼装」能力，而不是构造复杂继承树。


class CookMixin:
    def cook(self):
        print("  会做饭")


class DriveMixin:
    def drive(self):
        print("  会开车")


class Person(CookMixin, DriveMixin):
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f"  我是 {self.name}")


p = Person("小明")
p.hello()
p.cook()
p.drive()
print("  Person.__mro__ =", Person.__mro__)
```

运行命令：

```bash
$ python3 60-inherit.py
```

本机实测输出：

```
========== 1. 父类与子类，super() 复用父类方法 ==========
  run in father
  ---
  run in father
  run in son

========== 2. 查看继承顺序：__mro__ ==========
  Son.__mro__ = (<class '__main__.Son'>, <class '__main__.Father'>, <class 'object'>)

========== 3. 多继承与 Mixin ==========
  我是 小明
  会做饭
  会开车
  Person.__mro__ = (<class '__main__.Person'>, <class '__main__.CookMixin'>, <class '__main__.DriveMixin'>, <class 'object'>)
```

`__mro__`（Method Resolution Order，方法解析顺序）从左到右就是「找方法时的搜索次序」：`Son` 自己没有的方法，就去 `Father` 找，再找不到就去 `object`。

### 课后作业

请结合类的继承，为童谣定义类和它的方法：「小老鼠，上灯台，偷油吃，下不来，喵喵喵，猫来了，叽里咕噜滚下来。」

> 参考思路（节选）：定义父类 `老鼠`，带一个 `上灯台()` 方法；再定义子类 `小老鼠(老鼠)`，重写 `偷油()`，并在里面用 `super().上灯台()` 复用父类行为，最后加一个 `被猫吓到()` 方法完成「滚下来」。

---

## 第 61 讲 · 类的装饰器：如何改变类方法的功能？

### 本节目标

认识三个类装饰器 `classmethod`、`staticmethod`、`property`，知道它们各自改变方法的调用方式和行为。

### 知识要点

「类的装饰器」是「类方法的装饰器」的简称：**通过装饰器改变方法的调用方式和行为**。

**1. `classmethod`**

把实例方法变成**类方法**，用**类直接调用**：

```python
class Klass:
    @classmethod
    def func(cls):
        pass
```

`cls` 表示**当前操作的类**（不是实例），可以用 `Klass.func()` 调用。

**2. `staticmethod`**

有些函数「不需要类的任何信息，但又和类相关」，为了维护方便、代码工整，可以放进类里用 `@staticmethod` 修饰：

```python
class Klass():
    @staticmethod
    def func():
        pass
```

`staticmethod` 修饰的方法**既不需要 `self`，也不需要 `cls`**。

**3. `property`**

把方法「伪装成属性」：读取时走 getter，赋值时走 setter。

```python
class Klass:
    @property
    def func(self):
        return self.__varName

    @func.setter
    def func(self, varValue):
        self.__varName = varValue
```

> ⚠️ 装饰器让类更灵活，但也**增加了新手的学习难度**——「非必要，不要用」。

### 代码实操

完整代码见 `code/61-decorators.py`：

```python
# 第 61 讲 · 类的装饰器：如何改变类方法的功能？


print("========== 1. classmethod：方法绑定到「类」 ==========")


class Klass:
    @classmethod
    def func(cls):  # cls 代表「当前这个类」（不是实例）
        print("  调用 classmethod，cls =", cls.__name__)


Klass.func()  # 直接用类调用
Klass().func()  # 也可以用实例调用

print()
print("========== 2. staticmethod：和类相关，但不需要 self / cls ==========")


class Tool:
    @staticmethod
    def add(a, b):  # 没有 self，也没有 cls
        return a + b


print("  Tool.add(3, 4)    =", Tool.add(3, 4))  # 不需要先实例化
print("  Tool().add(3, 4)  =", Tool().add(3, 4))  # 也可以实例调用

print()
print("========== 3. property：把方法伪装成属性 ==========")


class Klass3:
    @property
    def func(self):  # getter：读取 obj.func 时执行
        return self.__var_name

    @func.setter
    def func(self, value):  # setter：给 obj.func 赋值时执行
        self.__var_name = value


obj = Klass3()
obj.func = "123"  # 触发 setter
print("  obj.func =", obj.func)  # 触发 getter
```

运行命令：

```bash
$ python3 61-decorators.py
```

本机实测输出：

```
========== 1. classmethod：方法绑定到「类」 ==========
  调用 classmethod，cls = Klass
  调用 classmethod，cls = Klass

========== 2. staticmethod：和类相关，但不需要 self / cls ==========
  Tool.add(3, 4)    = 7
  Tool().add(3, 4)  = 7

========== 3. property：把方法伪装成属性 ==========
  obj.func = 123
```

注意第 3 段：`obj.func = "123"` 看起来像给普通属性赋值，其实触发的是 `setter`；`print(obj.func)` 看起来像读属性，其实触发的是 `getter`。

### 课后作业

定义一个类，类中的属性 `userData` 具有以下行为：

1. 对属性赋值时，该值自动保存到文件 `userData.txt` 中；
2. 读取属性值时，如果属性为空，就从文件 `userData.txt` 中读取并显示。

> 参考思路（节选）：用 `@property` 写 getter，在里面判断 `self.__data is None` 时读文件；再用 `@userData.setter` 写 setter，赋值时把内容写进 `userData.txt`。

---

## 第 62 讲 · 小试牛刀：如何开发自动咖啡机？

### 本节目标

把前面几讲的类、继承、Mixin 综合起来，做一个「自动咖啡机」小项目。

### 知识要点

**1. 案例解析**

- 调配各种咖啡需要**咖啡原液、水、牛奶**三种原料；
- 三种原料按不同比例、属性叠加，形成新的咖啡品类（美式、拿铁……）；
- 为了支持前端展示，开发时要交付「后端接口」（也就是实例的方法）。

**2. 定义类**

- 每一杯咖啡成品是一个**对象**，所以要有「咖啡类」；
- 水、咖啡液、牛奶三种原料各定义一个 **Mixin**。

**3. 定义属性和方法**

- 咖啡成品有冷、热之分，所以水、牛奶都要带**冷热属性**；
- 三种原料都要能「添加」，所以各有**添加方法**；
- 单位不同：咖啡液以**份**为单位，水和牛奶以**毫升**为单位。

**4. 测试**

实例化后跑一遍，再优化输出——也就是课程说的「程序迭代」。

### 代码实操

完整代码见 `code/62-coffee-machine.py`。程序用**固定订单自动跑完**，不需要手工输入：

```python
# 第 62 讲 · 小试牛刀：如何开发自动咖啡机？
#
# 一杯咖啡由三种原料调配：水、咖啡液、牛奶。
# 每种原料做成一个 Mixin（只放方法），咖啡类把它们拼装起来。
# 本程序用「固定订单」自动跑完，不需要手工输入。


class WaterMixin:
    def add_water(self, volume, temperature):
        # 水以毫升为单位，并且区分冷热
        return f"水     ：{temperature} 水 {volume} ML"


class CoffeeMixin:
    def add_coffee(self, parts):
        # 咖啡液以「份」为单位
        return f"咖啡液 ：{parts} 份"


class MilkMixin:
    def add_milk(self, volume, temperature):
        # 牛奶以毫升为单位，也区分冷热
        return f"牛奶   ：{temperature} 奶 {volume} ML"


class Coffee(WaterMixin, CoffeeMixin, MilkMixin):
    """一杯咖啡成品；某种原料传 -1 表示不放。"""

    def __init__(self, name, water=-1, water_temp="hot",
                 coffee=1, milk=-1, milk_temp="hot"):
        self.name = name
        self.recipe = []  # 配方：逐条记录加了哪种原料

        if water > 0:
            self.recipe.append(self.add_water(water, water_temp))
        if coffee > 0:
            self.recipe.append(self.add_coffee(coffee))
        if milk > 0:
            self.recipe.append(self.add_milk(milk, milk_temp))

    def show(self):
        print(f"【{self.name}】")
        for line in self.recipe:
            print("  " + line)
        print(f"  —— 共 {len(self.recipe)} 种原料")


# 固定的三张订单，程序自动处理完
orders = [
    Coffee("美式", water=200, water_temp="hot", coffee=1),
    Coffee("拿铁", water=50, water_temp="hot", coffee=1, milk=150, milk_temp="hot"),
    Coffee("冰美式", water=200, water_temp="cold", coffee=1),
]

for cup in orders:
    cup.show()
    print()

print("Coffee.__mro__ =", Coffee.__mro__)
```

运行命令：

```bash
$ python3 62-coffee-machine.py
```

本机实测输出：

```
【美式】
  水     ：hot 水 200 ML
  咖啡液 ：1 份
  —— 共 2 种原料

【拿铁】
  水     ：hot 水 50 ML
  咖啡液 ：1 份
  牛奶   ：hot 奶 150 ML
  —— 共 3 种原料

【冰美式】
  水     ：cold 水 200 ML
  咖啡液 ：1 份
  —— 共 2 种原料

Coffee.__mro__ = (<class '__main__.Coffee'>, <class '__main__.WaterMixin'>, <class '__main__.CoffeeMixin'>, <class '__main__.MilkMixin'>, <class 'object'>)
```

三张订单共用同一个 `Coffee` 类：换原料、换冷热，改的是**参数**，不用改一行逻辑——这就是面向对象的价值。

### 课后作业

在 `code/62-coffee-machine.py` 基础上，再加一种「卡布奇诺」（水 + 咖啡液 + 牛奶，牛奶量比拿铁多），并把订单列表跑一遍看结果。

> 参考答案（节选）：往 `orders` 里加一行
> `Coffee("卡布奇诺", water=50, water_temp="hot", coffee=1, milk=200, milk_temp="hot")` 即可，其它代码不用动。

---

## 第 63 讲 · 避坑指南：类的常见错误

### 本节目标

认识类的两类典型错误：**语法错误**（导致程序异常）和**设计错误**（导致代码耦合严重、无法拆分）。

### 知识要点

**1. 语法错误：导致使用异常**

- **忘记写 `self`**：实例方法的第一个参数必须是 `self`，忘了它，调用时就会多传一个参数而报 `TypeError`。
- **误用 `self` 和 `cls`**：`classmethod` 的第一个参数是 `cls`，`staticmethod` 里则**既没有 `self` 也没有 `cls`**；在 `staticmethod` 里写 `self` 会报 `NameError`。

> `self`（当前实例）和 `cls`（当前类）是初学面向对象时**最容易忽略**的语法。

**2. 设计错误：导致耦合严重，无法拆分**

要回答三个问题：哪些对象该抽象成类？哪些功能该做成属性、哪些做成方法？类之间的依赖怎么解决？——用 **SOLID** 原则来指导。

| 字母 | 原则 | 一句话理解 |
| --- | --- | --- |
| **S** | 单一职责原则 | 一个类只负责做一件事，越小越好 |
| **O** | 开闭原则 | 对扩展开放，对修改关闭 |
| **L** | 里氏替换原则 | 子类能无差别替换父类，行为一致 |
| **I** | 接口隔离原则 | 接口越小越好；Python 用「鸭子类型」实现接口 |
| **D** | 依赖倒置原则 | 高层与低层模块都依赖抽象，而不是互相依赖 |

> ⚠️ 下面两个文件都是**故意触发错误**的，运行时会报错——这正是它们的用途。

### 代码实操

**错误 1：忘记写 `self`（`TypeError`）** —— `code/63-no-self.py`

```python
# 第 63 讲 · 避坑指南（1）：忘记写 self
# ⚠️ 本文件故意触发错误，用来演示真实报错：TypeError
class Coffee:
    def add_water(volume):  # 错误：第一个参数忘了写 self
        print("加水", volume)


mocha = Coffee()
mocha.add_water(200)  # 报错：实例调用时会自动多传一个 self
```

运行命令与真实报错：

```bash
$ python3 63-no-self.py
```

```
Traceback (most recent call last):
  File "/path/to/code/63-no-self.py", line 9, in <module>
    mocha.add_water(200)  # 报错：实例调用时会自动多传一个 self
    ^^^^^^^^^^^^^^^^^^^^
TypeError: Coffee.add_water() takes 1 positional argument but 2 were given
```

报错说「只需要 1 个位置参数，却给了 2 个」：因为实例调用时，Python 会**自动把 `mocha` 当作第一个参数**传进去，而方法却没留 `self` 的位置。改法：把 `def add_water(volume):` 改成 `def add_water(self, volume):`。

**错误 2：`staticmethod` 里误用 `self`（`NameError`）** —— `code/63-self-cls.py`

```python
# 第 63 讲 · 避坑指南（2）：staticmethod 里误用了 self
# ⚠️ 本文件故意触发错误，用来演示真实报错：NameError
class Coffee:
    @staticmethod
    def make():
        # 错误：staticmethod 里既没有 self 也没有 cls，self 是不存在的名字
        print("制作", self.name)


Coffee.make()
```

运行命令与真实报错：

```bash
$ python3 63-self-cls.py
```

```
Traceback (most recent call last):
  File "/path/to/code/63-self-cls.py", line 10, in <module>
    Coffee.make()
  File "/path/to/code/63-self-cls.py", line 7, in make
    print("制作", self.name)
                  ^^^^
NameError: name 'self' is not defined
```

`staticmethod` 不会自动接收实例，`self` 这个变量根本不存在。需要在方法里用实例数据时，就别用 `staticmethod`，改成普通实例方法（带上 `self`）。

### 课后作业

请你设计一款「网络音乐播放器」，并基于本讲学习的 SOLID 原则，试着把它的各功能**拆分成函数**（只需设计函数之间的依赖关系，不用实现具体功能）。

> 参考思路（节选）：
> **单一职责**——`搜索()`、`播放()`、`下载()`、`歌词()` 各管一件事；
> **依赖倒置**——`播放器` 依赖抽象的「音频源」，而不是直接依赖「某个网站」；
> **开闭**——新增一种音源时，只加一个新类，不改动 `播放器` 本身。

---

## 第 64 讲 · init 方法：如何为对象传递参数？

### 本节目标

认识**魔术方法**，掌握用 `__init__` 在实例化时接收参数，并学会用 `dir()` 探索更多魔术方法。

### 知识要点

**1. 魔术方法**

有一类方法**以双下划线 `__` 开头、以双下划线 `__` 结尾**，它们实现了常规方法之外的「特殊功能」，被称为**魔术方法**（magic method）。例如 `__init__`、`__call__`、`__getitem__`……

**2. `__init__` 方法**

- `__init__()` 称作**初始化方法**，用于属性和方法的初始化；
- 它在**类实例化时自动执行**，你不需要手动调用；
- 有了它，**实例化时就能接收参数**。

```python
class Klass:
    def __init__(self, 接收参数):
        self.var = 参数

实例 = Klass(参数)
```

**3. 其他魔术方法**

Python 的魔术方法非常多，可以按「数据模型」分类查阅官方文档：
<https://docs.python.org/zh-cn/3.10/reference/datamodel.html#special-method-names>；
也可以用 `dir(数据类型)` 拿到某个类型的全部魔术方法，按类型来学。

### 代码实操

完整代码见 `code/64-init.py`：

```python
# 第 64 讲 · init 方法：如何为对象传递参数？


print("========== 1. __init__：实例化时自动执行 ==========")


class Klass:
    def __init__(self, name, age):  # 实例化时自动调用，用来接收参数
        self.name = name
        self.age = age

    def information(self):
        print("  姓名：", self.name)
        print("  年龄：", self.age)


myself = Klass("Tom", 18)  # 参数传给 __init__
myself.information()

print()
print("========== 2. 魔术方法：以 __ 开头和结尾 ==========")


# __call__ 让「实例」也能像函数一样被调用
class Class1:
    def __call__(self):
        print("  类也可以被调用")


c1 = Class1()
c1()  # 实例后面加括号，触发 __call__

print()
print("========== 3. 用 dir() 查看一个类型有哪些魔术方法 ==========")
magic = [name for name in dir(dict) if name.startswith("__")]
print("  dict 的魔术方法个数：", len(magic))
print("  前 8 个：", magic[:8])
print("  其中就有：__init__、__call__、__getitem__ 等")
```

运行命令：

```bash
$ python3 64-init.py
```

本机实测输出：

```
========== 1. __init__：实例化时自动执行 ==========
  姓名： Tom
  年龄： 18

========== 2. 魔术方法：以 __ 开头和结尾 ==========
  类也可以被调用

========== 3. 用 dir() 查看一个类型有哪些魔术方法 ==========
  dict 的魔术方法个数： 35
  前 8 个： ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__']
  其中就有：__init__、__call__、__getitem__ 等
```

第 1 段里 `Klass("Tom", 18)` 的两个参数，正是被 `__init__` 的 `name`、`age` 接住并存成了实例属性。

### 课后作业

参考字典数据类型，实现自己的字典类 `MyDict`，要求：当**重复的 key 被修改**时，提示用户该 key 重复，不允许修改。

```python
dict1 = MyDict()
dict1['a'] = 100
dict1['a'] = 200   # 报错：已有名为 'a' 的 key
```

> 参考思路（节选）：继承 `dict`，用 `__setitem__` 魔术方法拦截赋值——先判断 `key in self`，若已存在就 `raise` 一个异常或打印提示，否则再 `self[key] = value`。这正好演示了「扩展数据类型默认功能时，应首先考虑魔术方法」。

---

## 第 65 讲 · 再回首：「类」单元小结

### 本节目标

用一个小例子把本章要点串一遍：定义类、`__init__` 传参、方法、`staticmethod`、继承 + `super()`、多继承 / Mixin。

### 知识要点

回顾本章的几条主线：

1. **类是图纸，实例是产品**——`class` 定义，`Coffee()` 造对象。
2. **`__init__` 负责初始化**——实例化时自动执行，用来接参数。
3. **`self` 是当前实例**——实例方法第一个参数固定是它，忘了就报 `TypeError`。
4. **继承复用代码**——子类用 `super()` 调用父类逻辑，`__mro__` 看查找顺序。
5. **Mixin 只加方法**——用多继承「拼装」能力，绝不单独实例化。
6. **装饰器改行为**——`classmethod` / `staticmethod` / `property`，非必要不用。

### 代码实操

完整代码见 `code/65-review.py`，一个小例子把上述要点全用上：

```python
# 第 65 讲 · 再回首：「类」单元小结
#
# 用一个小例子，把本章要点串一遍：
# 定义类、__init__ 传参、方法、staticmethod、继承 + super()、多继承 / Mixin。


class Animal:
    def __init__(self, name):  # __init__：实例化时接收参数
        self.name = name

    def speak(self):  # 方法
        print(f"  {self.name} 发出了声音")

    @staticmethod
    def about():  # staticmethod：不需要 self / cls
        print("  这是一个动物类")


class Dog(Animal):  # 继承
    def speak(self):
        super().speak()  # 复用父类方法
        print("  汪汪汪")


class SwimMixin:  # Mixin：只加方法
    def swim(self):
        print("  我还会游泳")


class Duck(Animal, SwimMixin):  # 多继承（用 Mixin 拼装能力）
    def speak(self):
        print(f"  {self.name} 嘎嘎嘎")


Animal.about()

a = Animal("小猫")
a.speak()

d = Dog("小狗")
d.speak()

duck = Duck("小鸭")
duck.speak()
duck.swim()

print("  Duck.__mro__ =", Duck.__mro__)
```

运行命令：

```bash
$ python3 65-review.py
```

本机实测输出：

```
  这是一个动物类
  小猫 发出了声音
  小狗 发出了声音
  汪汪汪
  小鸭 嘎嘎嘎
  我还会游泳
  Duck.__mro__ = (<class '__main__.Duck'>, <class '__main__.Animal'>, <class '__main__.SwimMixin'>, <class 'object'>)
```

### 课后作业

合上本章，仅凭记忆回答：

1. 类属性和实例属性的区别是什么？
2. `super()` 到底做了什么？
3. `classmethod`、`staticmethod`、`property` 分别在什么场景用？

答不上来的，回去重读对应那一讲即可——能自己讲出来，才算真会了。

---

## 本章小结

**速查表**

| 主题 | 关键点 |
| --- | --- |
| 定义类 | `class 类名:`（父类可省略，默认 `object`） |
| 实例化 | `obj = 类名(...)` |
| 类属性 | 写在类里方法外，所有实例共享 |
| 实例属性 | `self.xxx = ...`，只属于该对象 |
| 实例方法 | 第一个参数是 `self` |
| `is` / `==` | `is` 判同一对象，`==` 判值相等 |
| 继承 | `class 子类(父类):`，用 `super()` 复用父类 |
| 继承顺序 | `类名.__mro__` |
| Mixin | 只放方法的多继承，不单独实例化 |
| 类装饰器 | `@classmethod`（cls）/ `@staticmethod`（无 self）/ `@property` |
| 初始化 | `__init__(self, ...)`，实例化时自动执行 |
| 魔术方法 | `__` 开头结尾，如 `__init__`、`__call__`、`__getitem__` |
| 查魔术方法 | `dir(数据类型)` |
| 设计原则 | SOLID：单一职责 / 开闭 / 里氏替换 / 接口隔离 / 依赖倒置 |

**三句话**

1. 类和实例是「图纸与产品」：定义用 `class`，造出来用 `类名()`，第一个参数 `self` 不能忘。
2. 复用靠继承：用 `super()` 接住父类逻辑，能少用多继承就少用，Mixin 只加方法。
3. 初始化靠 `__init__`：实例化时自动执行并接收参数；扩展数据类型时先想魔术方法。

**动手练习**

1. 把 `code/58-thinking.py` 里的咖啡例子改成「面向过程」写一遍，对比哪种更好扩展。
2. 给 `code/59-class-instance.py` 的 `Coffee` 加一个 `add_milk(self)` 方法，再加一个 `latte` 实例试试。
3. 给 `code/60-inherit.py` 的 `Person` 再加一个 `WriteMixin`（方法：`write()`），观察 `__mro__` 的变化。
4. 把 `code/63-no-self.py` 和 `code/63-self-cls.py` 的报错都改对，让它们能正常输出。
5. 完成第 64 讲作业里的 `MyDict`，体会用 `__setitem__` 扩展字典。

---

## 下一章预告

第 8 章进入**模块与标准库**：学会把代码拆进模块、用 `import` 组织程序，
并认识 Python 自带的常用标准库——从此你的代码不再只写在一个文件里。

---

[← 上一章：函数](/guide/functions) ｜ [返回总目录](/) ｜ [下一章：模块与标准库 →](/guide/modules)

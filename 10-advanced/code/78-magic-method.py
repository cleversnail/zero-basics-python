# -*- coding: utf-8 -*-
"""第 78 讲 · 魔术方法：怎样通过类构造自己需要的数据类型？

本讲真跑。魔术方法是一类以「__」开头和结尾的方法，Python 在特定时机自动调用它们。
通过重写魔术方法，我们可以让自定义对象支持 +、-、len()、下标取值、像函数一样调用等行为。

运行：python3 78-magic-method.py
"""


print("=" * 50)
print("1. 基本数据类型里也藏着魔术方法")
print("=" * 50)

dict1 = {'a': 1}
print("dict1['a']             =", dict1['a'])
print("dict1.__getitem__('a') =", dict1.__getitem__('a'))  # 两者等价

# dir() 能把一个对象身上所有魔术方法列出来
magic = [m for m in dir(dict1) if m.startswith('__') and m.endswith('__')]
print("dict1 的魔术方法（前 8 个）= ", magic[:8])


print()
print("=" * 50)
print("2. 用 __add__ / __sub__ 让对象支持 + 和 -")
print("=" * 50)


class Vector:
    """一个二维向量，支持加减、打印、求长度、下标取值。"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):            # 对应 a + b
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):            # 对应 a - b
        return Vector(self.x - other.x, self.y - other.y)

    def __repr__(self):                  # print(obj) 时显示什么
        return f"Vector({self.x}, {self.y})"

    def __len__(self):                   # 对应 len(obj)
        return 2

    def __getitem__(self, index):        # 对应 obj[i]
        return (self.x, self.y)[index]


v1 = Vector(11, 22)
v2 = Vector(33, 44)
print("v1          =", v1)
print("v1 + v2     =", v1 + v2)
print("v1 - v2     =", v1 - v2)
print("len(v1)     =", len(v1))
print("v1[0],v1[1] =", v1[0], v1[1])


print()
print("=" * 50)
print("3. 对象的生命周期：__new__ / __init__ / __call__ / __del__")
print("=" * 50)


class Demo:
    def __new__(cls, *args, **kwargs):
        print("  __new__ 被调用：先创建对象")
        return super().__new__(cls)

    def __init__(self):
        print("  __init__ 被调用：再初始化对象")

    def __call__(self, x):
        return x * x

    def __del__(self):
        print("  __del__ 被调用：对象被回收时")


print("创建 Demo 实例：")
demo = Demo()
print("像函数一样调用 demo(5) =", demo(5))
print("删除 demo：")
del demo

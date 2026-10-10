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

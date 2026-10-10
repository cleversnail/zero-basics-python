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

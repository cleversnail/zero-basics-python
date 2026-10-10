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

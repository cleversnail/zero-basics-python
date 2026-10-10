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

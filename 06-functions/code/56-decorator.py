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

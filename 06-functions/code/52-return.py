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

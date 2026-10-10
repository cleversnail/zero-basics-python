# -*- coding: utf-8 -*-
"""第 51 讲 · 函数的参数：当函数操作对象不固定时怎么处理？"""


# 1. 不定长参数：* 收集位置参数，** 收集关键字参数
def address_book(name, *telphone, alias_name=None, **custom):
    print(f"name: {name}, tel: {telphone}, aname: {alias_name}, custom:{custom}")


address_book("wilson")
address_book("wilson", 1234, 4567, 5678)
address_book("wilson", 1234, 4567, 5678, home="Guangdong")
address_book("wilson", 1234, 4567, 5678, alias_name="w", aaa="bbb", home="Guangdong")


# 2. 函数文档：函数体第一行的字符串就是文档字符串（docstring）
def foo():
    """这个函数的用途、用法、注意事项都写在这里。"""
    print("test")


foo()
print(foo.__doc__)


# 3. 函数内省：用 dir() 查看函数对象自带的属性
print([d for d in dir(foo) if d in ("__call__", "__defaults__", "__doc__", "__kwdefaults__", "__name__")])
print(foo.__name__)

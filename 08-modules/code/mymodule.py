# -*- coding: utf-8 -*-
"""mymodule —— 一个自定义模块，被 68-custom-module.py 导入。

模块就是一个 .py 文件：里面定义的变量、函数、类，都能被别的程序 import 后使用。
"""

var1 = 100                    # 模块里的变量


def func1():                  # 模块里的函数
    print("func1 is called")


class Class1(object):         # 模块里的类
    def __init__(self):
        print("Class1 is instance")


# __name__ 在「直接运行本文件」时等于 "__main__"，在被别的文件 import 时等于模块名。
# 把「测试 / 调用代码」放进这个判断里，就不会在 import 时被误执行。
if __name__ == "__main__":
    print("mymodule 被直接运行（不是被导入）")
    func1()

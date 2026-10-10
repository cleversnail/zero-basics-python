# -*- coding: utf-8 -*-
"""第 81 讲配套模块：单例模式（靠 import 实现单例）。

Python 的模块在同一个进程里只会被导入（执行）一次，
因此模块级变量天然就是「进程内唯一」的，这就是最省事的单例。
"""
_name = "默认名字"


def get_name():
    return _name


def set_name(value):
    global _name
    _name = value

# -*- coding: utf-8 -*-
"""第 66 讲 · 模块的导入：如何使用其他人编写好的代码功能？

演示 5 种常见的导入写法，以及「用什么语法调用什么函数」的对应关系。
"""
import os

# ---------------------------------------------------------------
# 1. 导入整个模块：调用时写「模块名.函数()」
# ---------------------------------------------------------------
print("== 1. import os ==")
print(os.getcwd())          # getcwd = get current working directory，当前工作目录

# ---------------------------------------------------------------
# 2. 只导入模块中的某个函数：调用时直接写「函数()」
# ---------------------------------------------------------------
print("== 2. from os import getcwd ==")
from os import getcwd
print(getcwd())

# ---------------------------------------------------------------
# 3. 一次导入多个函数
# ---------------------------------------------------------------
print("== 3. from os import chdir, getcwd ==")
from os import chdir, getcwd as cwd   # getcwd 起了别名 cwd，避免和上面重名
print(cwd())

# ---------------------------------------------------------------
# 4. 给模块起别名：import 模块 as 别名
# ---------------------------------------------------------------
print("== 4. import datetime as dt ==")
import datetime as dt
print(dt.date(2026, 10, 10))

# ---------------------------------------------------------------
# 5. 从包中导入模块：包.模块.函数
# ---------------------------------------------------------------
print("== 5. from datetime import date ==")
from datetime import date
print(date(2026, 10, 10).year)

# ---------------------------------------------------------------
# 课后作业：三种 datetime 导入写法
# ---------------------------------------------------------------
print("== 课后作业：三种写法 ==")
# 格式一 datetime.date.today()
import datetime
print("格式一 datetime.date.today() ->", datetime.date.today())

# 格式二 date.today()
from datetime import date
print("格式二 date.today()          ->", date.today())

# 格式三 today()
# today() 是 date 类的方法，不是模块级名字，无法直接 from datetime import today。
# 需要先导入 date，再把 date.today 绑定成一个名字。
from datetime import date as _date
today = _date.today
print("格式三 today()               ->", today())

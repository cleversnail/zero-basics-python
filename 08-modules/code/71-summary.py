# -*- coding: utf-8 -*-
"""第 71 讲 · 再回首：「模块与标准库」单元小结

用一个小脚本把本章要点串一遍。
"""
import math
import importlib.metadata as md

# 1. 标准库：不用装，直接 import
print("标准库 math.pi =", round(math.pi, 5))

# 2. 第三方库：先 pip 安装，再 import（本机已装 sympy）
import sympy
print("第三方 sympy 版本 =", md.version("sympy"))

# 3. 模块名.成员 的调用方式小结
print("导入与调用方式：")
styles = [
    "import 模块          -> 模块.函数()",
    "from 模块 import 函数 -> 函数()",
    "import 模块 as 别名   -> 别名.函数()",
    "import 包.模块        -> 包.模块.函数()",
]
for i, s in enumerate(styles, 1):
    print(f"  {i}. {s}")

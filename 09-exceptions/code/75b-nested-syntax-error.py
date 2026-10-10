# -*- coding: utf-8 -*-
# 第 75 讲 · 避坑 4：嵌套 try-except 的「语法错误」演示
# 直接运行：python3 75b-nested-syntax-error.py
# ⚠️ 本文件【故意写错】——try 没有对应的 except，是非法的语法，会以
#    SyntaxError 退出，属于正常演示（无法用 try 在运行时捕获语法错误）。
#
# 下面的代码在「加载阶段」就会被解释器拒绝，因此整段无法执行。

try:
    print("外层 try")

# ← 这里缺了一个 except（或 finally），Python 会在解析时报语法错误

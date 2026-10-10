# 14-comments.py
# 第 14 讲 · 注释：如何写程序的说明书？
#
# 注释的标识符是井号 #，井号之后的内容会被 Python 解释器忽略。
# 注释的作用是“给人看”：说明这段代码做什么、怎么做。

# 为变量 pi 赋值为 3.14
pi = 3.14

# 变量 pi 用于计算圆的面积（描述用途，比“赋值为 3.14”更有信息量）
radius = 2
area = pi * radius * radius
print(area)

# 三重引号也可以做多行注释/说明（它本质是个字符串，只是没被使用）
"""
这是一段多行说明。
一般放在文件开头，写清这个程序是干什么的。
"""

# Python 之禅：import this 会打印 Tim Peters 写的 The Zen of Python
import this

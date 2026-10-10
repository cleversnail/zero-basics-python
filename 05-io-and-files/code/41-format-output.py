# -*- coding: utf-8 -*-
"""
第 41 讲 · 格式化输出：如何将执行结果通过屏幕输出？

三种常用的格式化输出方式：
  1. 百分号 %
  2. str.format()
  3. f-strings（下一讲细讲）

本讲重点演示前两种，第三种只做对照。
"""

# ---------- 方式一：百分号 % ----------
# %s=字符串  %d=整数  %f=浮点数；数字可控制宽度和精度
print("%s is %s than %s" % ("Beautiful", "better", "ugly"))
print("整数：%d，浮点：%f" % (42, 3.14159))
print("宽度 5、保留 1 位小数、左边补零：[%05.1f]" % 3.14)
print("宽度 5、至少 3 位数字、左对齐：[%-5.3d]" % 123.456)

# ---------- 方式二：str.format() ----------
# {} 里可以放数字索引，也可以放关键字参数
print("{} is {} than {}".format("Beautiful", "better", "ugly"))
print("{1} is {2} than {0}".format("ugly", "Beautiful", "better"))
print("{B} is {b} than {u}".format(u="ugly", B="Beautiful", b="better"))

# ---------- 方式三：f-strings（对照） ----------
u, B, b = "ugly", "Beautiful", "better"
print(f"{B} is {b} than {u}")

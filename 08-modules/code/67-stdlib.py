# -*- coding: utf-8 -*-
"""第 67 讲 · 标准库：Python 默认提供的便捷功能有哪些？

标准库 = 随 Python 一起安装、不用 pip 装就能直接 import 的模块集合。
本讲挑几个最常用的：math / json / os.path / zipfile。
"""
import math
import json
import os.path
import zipfile

# ---------------------------------------------------------------
# 1. math：数学常量与函数
# ---------------------------------------------------------------
print("== math ==")
print("math.pi        =", round(math.pi, 4))
print("math.sqrt(16)  =", math.sqrt(16))
print("math.factorial =", math.factorial(5))   # 5! = 120

# ---------------------------------------------------------------
# 2. json：在 JSON 文本和 Python 对象之间互相转换
# ---------------------------------------------------------------
print("== json ==")
person = {"name": "小明", "age": 18, "city": "北京"}
text = json.dumps(person, ensure_ascii=False)   # Python 对象 -> JSON 文本
print("json.dumps ->", text)
back = json.loads(text)                          # JSON 文本 -> Python 对象
print("json.loads ->", back["name"], back["age"])

# ---------------------------------------------------------------
# 3. os.path：拼接与拆分路径
# ---------------------------------------------------------------
print("== os.path ==")
print("os.path.join   ->", os.path.join("data", "sub", "a.txt"))
print("os.path.splitext ->", os.path.splitext("report.csv"))

# ---------------------------------------------------------------
# 4. zipfile：读 / 写 zip 压缩包（对应课后作业）
#    先建一个 a.zip，往里写 a.txt、b.txt，再把 a.txt 读出来。
# ---------------------------------------------------------------
print("== zipfile ==")
with zipfile.ZipFile("a.zip", "w") as zf:
    zf.writestr("a.txt", "这是 a.txt 里的内容\n第二行")
    zf.writestr("b.txt", "这是 b.txt 里的内容")

with zipfile.ZipFile("a.zip", "r") as zf:
    print("压缩包里的文件:", zf.namelist())
    print("a.txt 的内容如下:")
    print(zf.read("a.txt").decode("utf-8"))

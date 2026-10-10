# -*- coding: utf-8 -*-
"""
第 43 讲 · 常见常新：文件的打开

open(文件名, mode, encoding) 是操作文件的第一步。
  mode 常用值：r=读(默认)  w=覆盖写  a=追加写  b=二进制  +=读写
  encoding：文件的字符编码（macOS/Linux 默认 UTF-8）
打开成功会返回一个「文件对象」，之后所有读写都通过它进行。
"""
import os

# 以只读方式打开（默认 mode='r'，最安全，避免误覆盖）
f = open("demo1.txt", mode="r", encoding="UTF-8")

print("文件对象：", f)
print("是否可读：", f.readable(), " 是否可写：", f.writable())

# readlines()：一次性读成「行的列表」
data = f.readlines()
print("读到的每一行：", data)

# 用完要关闭，释放文件描述符
f.close()

# 路径不对会报 FileNotFoundError；用 os 模块可以查看当前工作目录
print("当前工作目录：", os.getcwd())
print("该目录下的 demo 素材文件：", sorted(n for n in os.listdir(".") if n.startswith("demo")))

# -*- coding: utf-8 -*-
"""
第 45 讲 · 常见常新：文件的读写

读取：
  read([size])      读全部（或指定大小）
  readline()        读一行
  readlines()       读成行的列表
  for line in f     迭代每一行
写入：
  write()           写内容；写到哪里由 open() 的 mode 决定
    mode='w'  清空原文件再写    mode='a'  在末尾追加
指针：
  tell()  返回当前指针位置      seek(偏移量)  移动指针
"""

# ---------- 1. 写入：mode='w' 会清空原文件，返回写入的字符数 ----------
f = open("a.txt", mode="w", encoding="UTF-8")
n = f.write("第一行\n第二行\n第三行\n")
print("写入字符数：", n)
f.close()

# ---------- 2. read() 读全部 ----------
with open("a.txt", mode="r", encoding="UTF-8") as f:
    print("read() 整体：", repr(f.read()))

# ---------- 3. readline() 逐行读 ----------
with open("a.txt", mode="r", encoding="UTF-8") as f:
    print("readline() 第 1 行：", repr(f.readline()))
    print("readline() 第 2 行：", repr(f.readline()))

# ---------- 4. readlines() 读成列表 ----------
with open("a.txt", mode="r", encoding="UTF-8") as f:
    print("readlines()：", f.readlines())

# ---------- 5. for line in f 迭代每一行 ----------
with open("a.txt", mode="r", encoding="UTF-8") as f:
    for i, line in enumerate(f, 1):
        print(f"第 {i} 行：{line.rstrip()}")

# ---------- 6. 追加：mode='a' ----------
with open("a.txt", mode="a", encoding="UTF-8") as f:
    f.write("追加的一行\n")
with open("a.txt", mode="r", encoding="UTF-8") as f:
    print("追加后共", len(f.readlines()), "行")

# ---------- 7. 只读模式下写入会报错（用 try 捕获观察） ----------
try:
    f = open("a.txt", mode="r", encoding="UTF-8")
    f.write("写不进去")
except Exception as e:            # io.UnsupportedOperation
    print("只读模式写入报错：", type(e).__name__, "-", e)

# ---------- 8. tell() / seek()：查看和移动文件指针 ----------
with open("pos.txt", mode="w", encoding="UTF-8") as f:
    f.write("hello world")
with open("pos.txt", mode="r", encoding="UTF-8") as f:
    print("初始指针位置：", f.tell())
    print("读 5 个字符：", repr(f.read(5)), " 指针位置：", f.tell())
    f.seek(0)
    print("seek(0) 后整段读回：", repr(f.read()))

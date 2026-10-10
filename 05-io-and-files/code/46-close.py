# -*- coding: utf-8 -*-
"""
第 46 讲 · 常见常新：文件的关闭

为什么必须及时关闭文件？
  - write() 写完后，内容可能还留在内存缓冲区里，没落盘；
  - 内存是「易失存储」，突然断电数据就丢了；
  - close() 会把缓冲内容刷到磁盘，并释放「文件描述符」。
两种关闭方式：
  - 手动 close()
  - with 语句：离开代码块时自动关闭（强烈推荐）
"""

# ---------- 1. with 语句：离开代码块自动关闭 ----------
with open("close.txt", mode="w", encoding="UTF-8") as f:
    f.write("用 with 语句写进来的内容\n")
print("with 块结束后，文件是否已关闭：", f.closed)

# ---------- 2. 手动 close() ----------
f2 = open("close.txt", mode="r", encoding="UTF-8")
print("手动读取内容：", f2.read().strip())
f2.close()
print("手动 close 后，文件是否已关闭：", f2.closed)

# ---------- 3. 打开不存在的文件会报 FileNotFoundError ----------
# 用 try 捕获，方便观察错误信息，同时不让程序中断
try:
    f3 = open("这个文件不存在.txt", mode="r", encoding="UTF-8")
    f3.close()
except FileNotFoundError as e:
    print("打开不存在的文件报错：", e)
    print("注意：open() 失败时不会创建文件对象，也不用（无法）调用 close()")

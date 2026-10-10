# -*- coding: utf-8 -*-
"""
第 44 讲 · 文件编码：如何解决不同操作系统的文件乱码问题？

- 计算机只能存数字，把「文本」按某种规则变成数字叫「编码」（如 GBK、UTF-8）。
- Windows 默认 GBK；Linux / macOS 默认 UTF-8。
- 用错编码去读文件，就会出现「乱码」甚至直接报 UnicodeDecodeError。
- 解决办法：open() 时用 encoding 参数指定正确的编码。
"""

# ---------- 1. 用正确编码（GBK）读 GBK 文件 ----------
with open("demo_GBK.txt", mode="r", encoding="GBK") as f:
    print("用 GBK 读 demo_GBK.txt：", f.read())

# ---------- 2. 故意用错编码（UTF-8）读同一个文件 → 报错 ----------
try:
    with open("demo_GBK.txt", mode="r", encoding="UTF-8") as f:
        print(f.read())
except UnicodeDecodeError as e:
    print("用 UTF-8 读 GBK 文件出错：", e)

# ---------- 3. 乱码是怎么产生的：编码和解码用了不一致的规则 ----------
s = "人生苦短，我用 Python"
print("原字符串：", s)
print("先按 UTF-8 编码、再按 GBK 解码：", s.encode("utf-8").decode("gbk", errors="replace"))

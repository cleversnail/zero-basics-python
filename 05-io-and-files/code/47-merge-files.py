# -*- coding: utf-8 -*-
"""
第 47 讲 · 小试牛刀：如何使用 Python 合并多个文件？

合并文件 = 逐个读取原始文件 + 追加写入一个新的目标文件。
关键点：
  1. 以只读模式打开原始文件
  2. 以写入模式打开（创建）目标文件
  3. 正确关闭文件（这里统一用 with 语句自动关闭）
"""

# ---------- 方案一：合并两个文件 ----------
with open("demo1.txt", encoding="UTF-8") as f1:
    data1 = f1.read()
with open("demo2.txt", encoding="UTF-8") as f2:
    data2 = f2.read()
with open("merge_two.txt", mode="w", encoding="UTF-8") as out:
    out.write(data1)
    out.write(data2)
print("方案一：demo1.txt + demo2.txt 已合并 -> merge_two.txt")

# ---------- 方案二：遍历列表，合并任意多个文件 ----------
files_name = ["demo1.txt", "demo2.txt", "demo3.txt"]
files_data = []

for f_name in files_name:
    with open(f_name, encoding="UTF-8") as f:
        files_data.append(f.read())

with open("merge_all.txt", mode="w", encoding="UTF-8") as out:
    for data in files_data:
        out.write(data)
print("方案二：", files_name, "已合并 -> merge_all.txt")

# ---------- 验证：读回合并结果 ----------
with open("merge_all.txt", encoding="UTF-8") as f:
    text = f.read()
print(f"合并后共 {len(text.splitlines())} 行，内容如下：")
print(text)

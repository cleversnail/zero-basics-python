# -*- coding: utf-8 -*-
"""
第 48 讲 · 再回首：本章单元小结（综合小练习）

把本章学到的四件事串成一个完整小程序：
  「输入 → 处理 → 格式化输出 → 写文件 → 读回」
"""

# ---------- 1. 输入：用固定值模拟键盘输入（真正的代码是 input()） ----------
name = "小明"
raw_scores = "90,85,100"          # 模拟用户敲入的一串成绩

# ---------- 2. 处理 ----------
scores = [int(x) for x in raw_scores.split(",")]
average = sum(scores) / len(scores)

# ---------- 3. 格式化输出（f-string，保留 2 位小数） ----------
line = f"{name} 的成绩 {scores}，平均分 {average:.2f}"
print(line)

# ---------- 4. 写文件（with 语句自动关闭） ----------
with open("report.txt", mode="w", encoding="UTF-8") as f:
    f.write(line + "\n")

# ---------- 5. 读回文件确认落盘成功 ----------
with open("report.txt", mode="r", encoding="UTF-8") as f:
    print("读回文件内容：", f.read().strip())

"""第 87 讲 · 理论盘点：数据分析的流程及对应的 Python 库

本讲以讲解为主，这个脚本用「只用标准库」的方式跑一遍数据分析的最小闭环：
    数据采集  ->  数据挖掘（清洗/统计）  ->  数据可视化（文本条形图）
目的是让你先建立整体流程的概念，后面几讲再逐个补齐真正的库（requests / re / json / matplotlib）。

运行：python3 87-overview.py
"""

# ---------- 1. 数据采集 ----------
# 真实场景里数据来自网页、数据库或 API；这里用一份「已经采集到的原始数据」代替，
# 目的是先看清流程，不引入网络依赖。
raw_data = [
    "Beijing,20220620,30",
    "Beijing,20220621,31",
    "Beijing,20220622,29",
    "Beijing,20220623,28",
    "Shanghai,20220620,32",
    "Shanghai,20220621,33",
    "Shanghai,20220622,31",
    "Shanghai,20220623,30",
]

# ---------- 2. 数据挖掘（数据准备 + 清洗 + 统计）----------
records = []  # 结构化后的数据：[(城市, 日期, 气温), ...]
for line in raw_data:
    city, day, temp = line.split(",")   # 清洗：把一行字符串按逗号拆开
    records.append((city, day, int(temp)))  # 把气温从字符串转成整数

# 按城市分组求平均气温
by_city = {}
for city, day, temp in records:
    by_city.setdefault(city, []).append(temp)

avg = {city: sum(temps) / len(temps) for city, temps in by_city.items()}

print("清洗后的数据：")
for row in records:
    print("   ", row)

print()
print("按城市统计的平均气温：")
for city, value in avg.items():
    print(f"    {city}: {value:.1f} °C")

# ---------- 3. 数据可视化（这里先用最朴素的文本条形图）----------
print()
print("文本条形图（每个 █ 代表 1 °C）：")
for city, value in avg.items():
    bar = "█" * round(value)
    print(f"    {city:<9}{bar} {value:.1f}")

print()
print("提示：第 92 讲会用 matplotlib 把这些数字画成真正的折线图。")

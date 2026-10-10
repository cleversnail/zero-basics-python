"""第 92 讲 · 小试牛刀：如何将数据进行图形化展示？

用 matplotlib 把「北京、上海一周气温」画成图，直观对比两个城市的温度变化。
最后把图保存为同目录下的 plot-demo.png，正文里的图片就是它。

运行：python3 92-plot.py
"""

import os
import matplotlib
matplotlib.use("Agg")            # 不弹窗口，直接输出图片文件（无图形界面的环境也能跑）
import matplotlib.pyplot as plt

# matplotlib 默认没有中文字体，先指定一个 macOS / 常见系统都有的中文字体，避免标题变方块
plt.rcParams["font.sans-serif"] = ["PingFang SC", "Heiti SC", "Arial Unicode MS",
                                   "Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False   # 让负号正常显示

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------- 1. 准备数据 ----------
days = ["6-20", "6-21", "6-22", "6-23", "6-24", "6-25", "6-26"]
beijing = [30, 31, 29, 28, 27, 26, 30]
shanghai = [32, 33, 31, 30, 29, 28, 31]

print("北京气温：", beijing)
print("上海气温：", shanghai)

# ---------- 2. 画布 + 坐标系 ----------
# fig 是整块画布，axs 是画布上的两个坐标系（上下排布）
fig, axs = plt.subplots(2, 1, figsize=(8, 8))

# 上：折线图，看趋势
axs[0].plot(days, beijing, marker="o", label="北京")
axs[0].plot(days, shanghai, marker="s", label="上海")
axs[0].set_title("北京、上海一周气温变化")
axs[0].set_xlabel("日期")
axs[0].set_ylabel("气温 (°C)")
axs[0].grid(True)
axs[0].legend()

# 下：柱状图，做对比
width = 0.35
idx = range(len(days))
axs[1].bar([i - width / 2 for i in idx], beijing, width=width, label="北京")
axs[1].bar([i + width / 2 for i in idx], shanghai, width=width, label="上海")
axs[1].set_xticks(list(idx))
axs[1].set_xticklabels(days)
axs[1].set_title("北京、上海一周气温对比")
axs[1].set_xlabel("日期")
axs[1].set_ylabel("气温 (°C)")
axs[1].grid(True, axis="y")
axs[1].legend()

fig.tight_layout()

# ---------- 3. 保存图片 ----------
out_path = os.path.join(HERE, "plot-demo.png")
fig.savefig(out_path, dpi=120)   # dpi 越大越清晰，文件也越大
print()
print(f"图表已保存到：{out_path}")
print("文件是否存在：", os.path.exists(out_path))

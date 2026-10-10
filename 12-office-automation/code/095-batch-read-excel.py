"""第 95 讲 · 如何批量读取 Excel 文件？

本讲真跑「批量」的两个主场景：
    1. 批量读取：用 pathlib 遍历目录，找出所有 *.xlsx，逐个读单元格
    2. 批量合并：把多个 Excel 的数据汇总到一张总表
    3. 批量拆分：把一张表按行拆成多个文件，文件名用每行第一个单元格（本讲课后作业）

为了让演示有真实数据，脚本会先在一个工作目录 work/ 里现场生成几个 xlsx，
再对它们做批量操作。每次运行都会先清空 work/，所以可以反复跑。

需要先安装依赖（本机已安装，能真跑）：pip install openpyxl

运行：python3 095-batch-read-excel.py
"""

import shutil
from pathlib import Path

from openpyxl import Workbook, load_workbook

# 演示用的工作目录：所有生成的文件都放这里，不污染别处
WORK = Path("work")
if WORK.exists():
    shutil.rmtree(WORK)      # 先清空，保证反复运行结果一致
WORK.mkdir()

print("=" * 48)
print("0) 准备数据：生成 3 个门店的销售 xlsx")
print("=" * 48)

# 每个门店一个文件：门店, 产品, 销量
store_data = {
    "北京": [["北京", "铅笔", 120], ["北京", "笔记本", 80]],
    "上海": [["上海", "铅笔", 95], ["上海", "橡皮", 60]],
    "广州": [["广州", "钢笔", 40], ["广州", "笔记本", 70]],
}
for store, rows in store_data.items():
    wb = Workbook()
    ws = wb.active
    ws.append(["门店", "产品", "销量"])
    for r in rows:
        ws.append(r)
    wb.save(WORK / f"{store}.xlsx")
    print(f"  已生成 {WORK / (store + '.xlsx')}")

print()
print("=" * 48)
print("1) 批量读取：遍历目录，找出所有 xlsx 并逐格打印")
print("=" * 48)

# 关键一行：iterdir() 遍历目录里的每一项，match('*.xlsx') 只留下 Excel 文件
# sorted() 只是为了输出稳定，和批量读取本身无关
files = sorted(x for x in WORK.iterdir() if x.match("*.xlsx"))
print("找到文件：", [f.name for f in files])
print()

for file in files:
    wb = load_workbook(file)
    ws = wb.active
    print(f"--- {file.name} ---")
    # 和遍历元组一样，用 for...in 遍历「行」，再遍历「单元格」
    for row in ws.iter_rows(values_only=True):
        print("  ", row)

print()
print("=" * 48)
print("2) 批量合并：把所有门店的数据汇总到一张总表")
print("=" * 48)

merged = Workbook()
mws = merged.active
mws.title = "汇总"
mws.append(["门店", "产品", "销量"])   # 先写表头

for file in files:
    wb = load_workbook(file)
    ws = wb.active
    # values_only 的迭代里下标 0 是表头行，跳过；其余行写入总表
    for i, row in enumerate(ws.iter_rows(values_only=True)):
        if i == 0:
            continue
        mws.append(list(row))

merged.save(WORK / "汇总.xlsx")
print("已生成", WORK / "汇总.xlsx")

# 读回汇总表看看
back = load_workbook(WORK / "汇总.xlsx")
total = 0
for row in back.active.iter_rows(values_only=True):
    print("  ", row)
    if isinstance(row[2], int):
        total += row[2]
print("总销量：", total)

print()
print("=" * 48)
print("3) 批量拆分：每行拆成一个文件，文件名用第一个单元格")
print("=" * 48)

# 准备一份「每行第一个单元格互不相同」的源表，这样拆出来才不会重名互相覆盖
split_dir = WORK / "拆分明细"
split_dir.mkdir()
src_dir = WORK / "拆分源"
src_dir.mkdir()
src_wb = Workbook()
src_ws = src_wb.active
src_ws.title = "产品"
src_ws.append(["产品", "单价", "库存"])
src_ws.append(["铅笔", 1.5, 120])
src_ws.append(["橡皮", 0.8, 200])
src_ws.append(["钢笔", 12.0, 40])
src_ws.append(["笔记本", 5.0, 80])
src_wb.save(src_dir / "产品.xlsx")

# 读这张源表，把每一行拆成一个文件
src = load_workbook(src_dir / "产品.xlsx")
rows = list(src.active.iter_rows(values_only=True))
header = rows[0]

for row in rows[1:]:
    name = str(row[0])                 # 每行第一个单元格作为文件名
    one = Workbook()
    ws = one.active
    ws.append(list(header))            # 带上表头，单文件也能看懂
    ws.append(list(row))
    out = split_dir / f"{name}.xlsx"
    one.save(out)
    print(f"  {row}  ->  {out}")

print()
print("拆分目录里的文件：", sorted(p.name for p in split_dir.iterdir()))
print()
print("提示：如果「每行第一个单元格」有重复值，拆出来的文件会互相覆盖——")
print("      实际用的时候通常再加个序号（如 铅笔-1.xlsx、铅笔-2.xlsx）来避免。")

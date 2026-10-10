# 第 12 章 · 办公自动化

> 用 Python 把表格、文档这类「办公文件」批处理起来：批量读取、批量合并拆分、格式互转，
> 再用 `collections` 扩展出更趁手的数据类型。
> **本章 5 讲（094–098）**，从「什么文件用什么库」一路走到「批量读取 → 格式转换 → 数据统计」。

## 🎯 本章目标

- 分清常见办公文件格式（xlsx / xls / docx / doc），知道它们各由哪个 Python 库读写
- 用 `openpyxl` 读写 xlsx：新建工作簿、遍历单元格、保存
- 用 `python-docx` 读写 docx：段落、表格、标题
- 用 `pathlib` 遍历目录，**批量读取**一堆 Excel 文件
- 实现 Excel 的**批量合并**与**批量拆分**
- 实现 **Word ↔ Excel 的批量格式转换**
- 用 `collections` 的 `namedtuple` / `deque` / `Counter` / `defaultdict` / `UserDict` / `UserList` 扩展数据类型

**本章代码**

> 📌 **代码约定**：正文代码块都保持**可直接运行**；所有输出都是**真实运行结果**（本机 Python 3.12.7）。
> 本章依赖第三方库 `openpyxl` 与 `python-docx`。**本机已安装**（openpyxl 3.1.5、python-docx 1.2.0），
> 所以第 94–96 讲的读写/转换示例都是**真跑**的；第 97、98 讲只用标准库 `collections`，也是**真跑**的。

| 文件 | 内容 |
| --- | --- |
| `code/094-file-types.py` | 文件格式与库的对应；用 openpyxl 写/读 xlsx、python-docx 写/读 docx，并完成「Excel 表格写入 docx」 |
| `code/095-batch-read-excel.py` | 批量读取 Excel：遍历目录、批量合并到总表、按行拆分为多文件 |
| `code/096-format-convert.py` | 批量格式转换：Word→Excel、Excel→Word |
| `code/097-collections-demo.py` | 扩展数据类型：namedtuple / deque / Counter / defaultdict / UserDict / UserList |
| `code/098-chapter-review.py` | 单元小结：统计一篇文章词频前 5（第 97 讲课后作业的综合答案） |

> 📎 `code/` 里还随附课程素材文件：`1.xlsx`、`2.xlsx`、`3.xlsx`、`sample.xlsx`、`sample.docx`
> （来自课程仓库）。第 96 讲的示例就直接读 `sample.docx`。

---

## 第 94 讲 · 理论盘点：文件类型与对应的 Python 函数库

### 本节目标

搞清一件事：**不同文件格式，要用不同的 Python 库来读写**——先记住「格式 ↔ 库」的对应关系，再动手跑一遍。

### 知识要点

**1. 文件类型就是文件的存储格式**

Windows（以及大多数系统）靠**扩展名**区分文件类型。同样是一份「内容」，存成不同格式，字节排布完全不同：

| 大类 | 常见格式 | 特点 |
| --- | --- | --- |
| 音频 | `WAV`、`MP3` | WAV 不压缩、无损但文件大；MP3 压缩、文件小 |
| Word | `docx`、`doc` | docx 是新版（基于 XML），doc 是旧版 |
| Excel | `xlsx`、`xls` | xlsx 是新版，xls 是旧版 |

**关键结论**：格式不同 → 存储方式不同 → **要用不同的软件、也就需要不同的 Python 库**去读写。

**2. Word 格式与 Python 函数库**

- 库：**`python-docx`**
- 安装：`pip install python-docx`
- 导入：`import docx`（注意：装的名字带连字符，导入的名字是 `docx`）

**3. Excel 格式与 Python 函数库**

| 格式 | 读 | 写 |
| --- | --- | --- |
| `xlsx`（新版） | `openpyxl` | `openpyxl` |
| `xls`（旧版） | `xlrd` | `xlwt` |

**记忆口诀**：**新版 xlsx 一套 openpyxl 搞定；旧版 xls 读用 xlrd、写用 xlwt。**

> ⚠️ 一句话记住本讲：**`xlsx` → `openpyxl`，`docx` → `python-docx`。**

### 代码实操

`code/094-file-types.py` 先把 xlsx、docx 各写一个再读回来，最后顺手完成本讲课后作业（把 Excel 第一张表写进 docx）。

```python
"""第 94 讲 · 理论盘点：文件类型与对应的 Python 函数库"""

from openpyxl import Workbook, load_workbook
from docx import Document

print("=" * 48)
print("1) 用 openpyxl 新建并读回一个 xlsx")
print("=" * 48)

# Workbook() 新建一个空的 Excel 工作簿；wb.active 拿到当前活动工作表
wb = Workbook()
ws = wb.active
ws.title = "订单"

# 一行一行追加数据（列表的每个元素对应一格）
ws.append(["订单号", "客户", "金额"])
ws.append([1001, "张三", 250])
ws.append([1002, "李四", 180])

# save() 才真正落盘，生成 094-demo.xlsx 文件
wb.save("094-demo.xlsx")

# load_workbook() 再把文件读回来，验证刚才真的写进去了
wb2 = load_workbook("094-demo.xlsx")
print("工作表名字：", wb2.sheetnames)
for row in wb2.active.iter_rows(values_only=True):
    print("  ", row)

print()
print("=" * 48)
print("2) 用 python-docx 新建并读回一个 docx")
print("=" * 48)

# Document() 新建一个空的 Word 文档
doc = Document()
doc.add_heading("第 94 讲演示文档", level=1)   # level=1 是一级标题
doc.add_paragraph("这一行是普通段落。")
doc.save("094-demo.docx")                     # 落盘

# 读回来：document.paragraphs 是所有段落
doc2 = Document("094-demo.docx")
for p in doc2.paragraphs:
    if p.text.strip():
        print("  段落：", p.text)

print()
print("=" * 48)
print("3) 课后作业：把 Excel 第一张表写进 docx")
print("=" * 48)

# 思路：先用 openpyxl 读 Excel 的表格 -> 再用 python-docx 写成 Word 表格
src = load_workbook("094-demo.xlsx")
rows = list(src.active.iter_rows(values_only=True))
print("从 Excel 读到的数据：")
for r in rows:
    print("  ", r)

out = Document()
out.add_heading("订单汇总", level=1)

# add_table(rows=1, cols=列数) 先建一个只有表头的表
table = out.add_table(rows=1, cols=len(rows[0]))
hdr = table.rows[0].cells
for i, name in enumerate(rows[0]):
    hdr[i].text = str(name)

# 剩下的每一行：add_row() 新增一行，再逐格填文本
for data_row in rows[1:]:
    cells = table.add_row().cells
    for i, value in enumerate(data_row):
        cells[i].text = str(value)

out.save("094-作业-excel转docx.docx")
print("已保存 094-作业-excel转docx.docx（用 Word 打开即可看到这张表）")

# 读回作业文件，确认表格真的写进去了
check = Document("094-作业-excel转docx.docx")
print("回读 094-作业-excel转docx.docx 的表格内容：")
for t in check.tables:
    for row in t.rows:
        print("  ", [c.text for c in row.cells])

print()
print("说明：xls（旧版 Excel）不能用 openpyxl，读用 xlrd、写用 xlwt——本机未装，故只讲不跑。")
```

运行命令（先装依赖，已装可跳过）：

```bash
pip install openpyxl python-docx
python3 094-file-types.py
```

本机实测输出：

```
================================================
1) 用 openpyxl 新建并读回一个 xlsx
================================================
工作表名字： ['订单']
   ('订单号', '客户', '金额')
   (1001, '张三', 250)
   (1002, '李四', 180)

================================================
2) 用 python-docx 新建并读回一个 docx
================================================
  段落： 第 94 讲演示文档
  段落： 这一行是普通段落。

================================================
3) 课后作业：把 Excel 第一张表写进 docx
================================================
从 Excel 读到的数据：
   ('订单号', '客户', '金额')
   (1001, '张三', 250)
   (1002, '李四', 180)
已保存 094-作业-excel转docx.docx（用 Word 打开即可看到这张表）
回读 094-作业-excel转docx.docx 的表格内容：
   ['订单号', '客户', '金额']
   ['1001', '张三', '250']
   ['1002', '李四', '180']

说明：xls（旧版 Excel）不能用 openpyxl，读用 xlrd、写用 xlwt——本机未装，故只讲不跑。
```

### 课后作业

请你编写程序，将 Excel 文件的第一张表格中的内容存储到 docx 文件中。

> 参考答案就是上面第 3) 段：先 `load_workbook()` 把 Excel 读成 `rows`，
> 再用 `Document()` 建文档、`add_table()` 建表、`add_row()` 逐行填、`save()` 落盘。
> 完整代码见 `code/094-file-types.py`。

---

## 第 95 讲 · 如何批量读取 Excel 文件？

### 本节目标

把「手动一个个打开表」变成「用程序一次处理一批」——学会**遍历目录找文件**、**批量读取**、**批量合并**与**批量拆分**。

### 知识要点

**1. 批量合并：先遍历拿到所有要处理的文件**

核心就一行——用 `pathlib` 遍历目录，用 `match('*.xlsx')` 只留下 Excel 文件：

```python
from pathlib import Path, PurePath
p = Path('.')
files = [x for x in p.iterdir() if PurePath(x).match('*.xlsx')]
```

- `p.iterdir()`：把目录里的每一项（文件、子目录）一个个吐出来
- `PurePath(x).match('*.xlsx')`：判断这一项的**名字**是否符合 `*.xlsx` 通配符
- 列表推导式把「符合条件的」收集成 `files` 列表，接着 `for file in files:` 就能逐个处理

**2. 批量拆分：关键是遍历所有单元格**

和遍历元组一样，Excel 也能用 `for...in` 逐行、逐格走：

```python
for row in ws.iter_rows():      # 外层遍历「行」
    for cell in row:            # 内层遍历「单元格」
        print(cell.value)       # 拿到这一格的值
```

- `ws.iter_rows()` 返回一行行数据；`values_only=True` 则直接给值、不用 `.value`
- 拆分时，每读一行就新建一个工作簿写出去，文件名可用「该行第一个单元格」来定

**3. 合并与拆分是一对反操作**

| 操作 | 方向 | 用到的能力 |
| --- | --- | --- |
| 批量合并 | 多个文件 → 一张总表 | 遍历文件 + `append()` 逐行追加 |
| 批量拆分 | 一张表 → 多个文件 | 遍历单元格 + 每条记录存一个文件 |

> 💡 两者都**依赖 for 循环**：批量读取是这一切的基础。

### 代码实操

`code/095-batch-read-excel.py` 先在一个 `work/` 目录里现场生成 3 个门店的销售表，再做批量读取、合并、拆分。

```python
"""第 95 讲 · 如何批量读取 Excel 文件？"""

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
```

运行命令：

```bash
pip install openpyxl
python3 095-batch-read-excel.py
```

本机实测输出：

```
================================================
0) 准备数据：生成 3 个门店的销售 xlsx
================================================
  已生成 work/北京.xlsx
  已生成 work/上海.xlsx
  已生成 work/广州.xlsx

================================================
1) 批量读取：遍历目录，找出所有 xlsx 并逐格打印
================================================
找到文件： ['上海.xlsx', '北京.xlsx', '广州.xlsx']

--- 上海.xlsx ---
   ('门店', '产品', '销量')
   ('上海', '铅笔', 95)
   ('上海', '橡皮', 60)
--- 北京.xlsx ---
   ('门店', '产品', '销量')
   ('北京', '铅笔', 120)
   ('北京', '笔记本', 80)
--- 广州.xlsx ---
   ('门店', '产品', '销量')
   ('广州', '钢笔', 40)
   ('广州', '笔记本', 70)

================================================
2) 批量合并：把所有门店的数据汇总到一张总表
================================================
已生成 work/汇总.xlsx
   ('门店', '产品', '销量')
   ('上海', '铅笔', 95)
   ('上海', '橡皮', 60)
   ('北京', '铅笔', 120)
   ('北京', '笔记本', 80)
   ('广州', '钢笔', 40)
   ('广州', '笔记本', 70)
总销量： 465

================================================
3) 批量拆分：每行拆成一个文件，文件名用第一个单元格
================================================
  ('铅笔', 1.5, 120)  ->  work/拆分明细/铅笔.xlsx
  ('橡皮', 0.8, 200)  ->  work/拆分明细/橡皮.xlsx
  ('钢笔', 12, 40)  ->  work/拆分明细/钢笔.xlsx
  ('笔记本', 5, 80)  ->  work/拆分明细/笔记本.xlsx

拆分目录里的文件： ['橡皮.xlsx', '笔记本.xlsx', '钢笔.xlsx', '铅笔.xlsx']

提示：如果「每行第一个单元格」有重复值，拆出来的文件会互相覆盖——
      实际用的时候通常再加个序号（如 铅笔-1.xlsx、铅笔-2.xlsx）来避免。
```

> 📌 运行后，`code/` 下会多出一个 `work/` 目录（里面是本次生成的表格），**每次运行都会先清空重建**，
> 所以可以反复跑、结果稳定。它只是演示产物，不是本章示例代码。

### 课后作业

请你编写程序，将 Excel 的每一行拆分成一个文件，并以每行第一个单元格作为文件名进行保存。

> 参考答案即上面第 3) 段：`for row in rows[1:]:` 逐行取出，`name = str(row[0])` 作为文件名，
> 新建工作簿、写入表头与这一行、`save()` 落盘。`code/095-batch-read-excel.py` 里有完整实现。

---

## 第 96 讲 · 如何实现数据的批量格式转换？

### 本节目标

把「Word 里的内容」搬进 Excel，或把「Excel 里的表」搬进 Word——掌握两个方向的双向转换。

### 知识要点

**1. Word → Excel：读 Word，写 Excel**

| 步骤 | 用什么 |
| --- | --- |
| 打开 Word、取正文/表格 | `python-docx`：`Document()`、`document.paragraphs`、`document.tables` |
| 新建 Excel、写数据 | `openpyxl`：`Workbook()`、`ws.append(列表)`、`wb.save(文件名)` |

**2. Excel → Word：读 Excel，写 Word**

| 步骤 | 用什么 |
| --- | --- |
| 打开 Excel、读单元格 | `openpyxl`：`load_workbook()`、`iter_rows(values_only=True)` |
| 新建 Word、加表格 | `python-docx`：`add_table()`、`add_row()`、`cell.text` |

> ⚠️ **提前确定格式**：一个 Excel 文件可能有多张工作表，也比 Word 表格更「宽」。
> 转换前要先想清楚：转过去要几列、多出来的表放哪、表头怎么写。

**3. 别忘了几件事**

- 不同格式转换要用**不同的库**（Word 用 docx、Excel 用 openpyxl）。
- 转换常要**同时打开多个文件**，操作完一定要 `save()` 落盘、及时释放对象，
  否则文件句柄不关，**内存占用会越来越高**。

### 代码实操

`code/096-format-convert.py` 读 `sample.docx` 转成 xlsx，再把 xlsx 的表格转回 docx。

```python
"""第 96 讲 · 如何实现数据的批量格式转换？"""

from openpyxl import Workbook, load_workbook
from docx import Document

print("=" * 48)
print("1) Word -> Excel：把 sample.docx 的文字和表格转成 xlsx")
print("=" * 48)

# 读 Word
doc = Document("sample.docx")

# 收集非空段落文本（正文）
paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
print("Word 里的段落：")
for t in paragraphs:
    print("  ", t)

# 收集表格内容
table_rows = []
for t in doc.tables:
    for row in t.rows:
        table_rows.append([c.text for c in row.cells])
print("Word 里的表格：")
for r in table_rows:
    print("  ", r)

# 写 Excel：正文一列，表格另起一张工作表
wb = Workbook()
ws1 = wb.active
ws1.title = "正文"
for t in paragraphs:
    ws1.append([t])

ws2 = wb.create_sheet("表格")
for r in table_rows:
    ws2.append(r)

wb.save("096-word转excel.xlsx")
print("已生成 096-word转excel.xlsx，工作表：", wb.sheetnames)

# 读回验证
back = load_workbook("096-word转excel.xlsx")
print("回读「正文」表：")
for row in back["正文"].iter_rows(values_only=True):
    print("  ", row)
print("回读「表格」表：")
for row in back["表格"].iter_rows(values_only=True):
    print("  ", row)

print()
print("=" * 48)
print("2) Excel -> Word：把刚才的 xlsx 表格写回一个 docx")
print("=" * 48)

# 用 openpyxl 读表格，用 python-docx 写表格（转换关键：确定好列数/列宽）
src = load_workbook("096-word转excel.xlsx")["表格"]
rows = list(src.iter_rows(values_only=True))

out = Document()
out.add_heading("由 Excel 转换而来", level=1)

cols = len(rows[0])
table = out.add_table(rows=1, cols=cols)
for i, name in enumerate(rows[0]):
    table.rows[0].cells[i].text = str(name)
for data_row in rows[1:]:
    cells = table.add_row().cells
    for i, value in enumerate(data_row):
        cells[i].text = str(value)

out.save("096-excel转word.docx")
print("已生成 096-excel转word.docx")

# 读回验证
check = Document("096-excel转word.docx")
for t in check.tables:
    for row in t.rows:
        print("  ", [c.text for c in row.cells])

print()
print("提示：格式转换常要同时开多个文件，操作完记得 save() 落盘；")
print("      openpyxl 的 workbook 对象也要及时让变量失效，否则内存占用会升高。")
```

运行命令：

```bash
pip install openpyxl python-docx
python3 096-format-convert.py
```

本机实测输出：

```
================================================
1) Word -> Excel：把 sample.docx 的文字和表格转成 xlsx
================================================
Word 里的段落：
   标题
   A plain paragraph having some bold and some italic.
   Heading, level 1
Word 里的表格：
   ['Qty', 'Id', 'Desc']
   ['3', '101', 'Spam']
   ['7', '422', 'Eggs']
   ['4', '631', 'Spam, spam, eggs, and spam']
已生成 096-word转excel.xlsx，工作表： ['正文', '表格']
回读「正文」表：
   ('标题',)
   ('A plain paragraph having some bold and some italic.',)
   ('Heading, level 1',)
回读「表格」表：
   ('Qty', 'Id', 'Desc')
   ('3', '101', 'Spam')
   ('7', '422', 'Eggs')
   ('4', '631', 'Spam, spam, eggs, and spam')

================================================
2) Excel -> Word：把刚才的 xlsx 表格写回一个 docx
================================================
已生成 096-excel转word.docx
   ['Qty', 'Id', 'Desc']
   ['3', '101', 'Spam']
   ['7', '422', 'Eggs']
   ['4', '631', 'Spam, spam, eggs, and spam']

提示：格式转换常要同时开多个文件，操作完记得 save() 落盘；
      openpyxl 的 workbook 对象也要及时让变量失效，否则内存占用会升高。
```

### 课后作业

请你编写程序，将指定 Word 文件中的文字内容，转换为同名的 Excel 文件。

> 参考答案：就是上面第 1) 段的做法——用 `Document(文件名)` 打开 Word，
> 把 `document.paragraphs` 的文本写进 `openpyxl` 的工作表；只需把输出文件名
> 取成「和输入同名、扩展名换成 `.xlsx`」即可。
> 完整代码见 `code/096-format-convert.py`。

---

## 第 97 讲 · 如何扩展数据类型？

### 本节目标

当内置的 `list`、`dict` 不够用时，用标准库 `collections` 里的几种「扩展容器」把代码写得更短、更清楚。

### 知识要点

`collections` 是 Python **标准库**（不用额外安装），提供一批比内置容器更好用的数据类型：

| 类型 | 作用 | 你多得到的能力 |
| --- | --- | --- |
| `namedtuple` 命名元组 | 给元组的位置起名字 | 用 `p.x` 取字段，比 `p[0]` 可读 |
| `deque` 双端队列 | 两端都能 O(1) 进出 | 多了 `appendleft()`、`popleft()` |
| `Counter` 计数器 | 统计元素出现次数 | `most_common(n)`、直接传入可迭代对象 |
| `defaultdict` 默认字典 | 缺 key 时自动给默认值 | 取值不必先判断 key 在不在 |
| `UserDict` / `UserList` | 字典、列表的**子类化** | 继承它们给自己的容器加功能 |

**1. 命名元组 `namedtuple`**

它是「命名元组的工厂函数」，用前先 `from collections import namedtuple`：

```python
Point = namedtuple('Point', ['x', 'y'])   # 定义一个「点」，含 x、y 两个坐标
p = Point(3, 4)
```

此时 `p.x`、`p.y` 可读性远好于下标，且它**本质上还是元组**。

**2. 双端队列 `deque`**

`deque` 是实现**双向队列**的对象，能**从左右两端**添加/移除元素，比 `list` 多了
`appendleft()`、`popleft()` 两个方法。用 `deque(maxlen=n)` 还能自动只保留最近 n 个元素。

**3. 计数器 `Counter`**

`Counter` 是「计数器工具」，可以方便地统计元素的出现次数：既可以手动 `cnt[word] += 1`，
也可以把整个列表丢进去自动计数，还能 `most_common(n)` 取出现最多的前 n 个。

**4. 字典和列表子类化 `UserDict` / `UserList`**

当你需要字典、列表的功能，但它们又**不能完全满足需要**时，
可以**继承 `UserDict` 和 `UserList`**，实现增强版的字典和列表（覆盖 `__setitem__`、加新方法等）。

> 💡 一句话：**当传统的列表、字典无法满足需要时，用命名元组、双端队列、计数器来丰富数据类型。**

### 代码实操

`code/097-collections-demo.py` 纯标准库，五种类型逐个真跑。

```python
"""第 97 讲 · 如何扩展数据类型？"""

from collections import namedtuple, deque, Counter, defaultdict, UserDict, UserList

print("=" * 48)
print("1) namedtuple：给元组的位置起名字")
print("=" * 48)

# 定义一个「点」，包含 x、y 两个坐标
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print("p       =", p)
print("p.x     =", p.x)          # 用名字取值，比 p[0] 可读
print("p.y     =", p.y)
print("p[0]    =", p[0])         # 依然可以像普通元组那样按下标取
print("它是元组吗？", isinstance(p, tuple))

print()
print("=" * 48)
print("2) deque：双端队列，左右两端都能进出")
print("=" * 48)

dq = deque("test_deq")           # 用字符串初始化，每个字符是一个元素
print("遍历 deque：")
for elements in dq:
    print("  ", elements)

# 双端队列比 list 多了 appendleft() / popleft()
dq.append("right")               # 右侧加
dq.appendleft("left")            # 左侧加（list 做不到）
print("append / appendleft 之后：", dq)

dq.pop()                         # 右侧弹出
dq.popleft()                     # 左侧弹出（list 做不到）
print("pop / popleft 之后：    ", dq)

# 一个实际用途：只用最后 3 个元素（固定长度）
recent = deque(maxlen=3)
for n in [1, 2, 3, 4, 5]:
    recent.append(n)
print("maxlen=3 只保留最后 3 个：", recent)

print()
print("=" * 48)
print("3) Counter：计数器，统计出现次数")
print("=" * 48)

cnt = Counter()
for word in ["red", "blue", "red", "green", "blue", "blue"]:
    cnt[word] += 1
print("cnt              =", cnt)
print("cnt['blue']      =", cnt["blue"])            # 直接按 key 取次数
print("most_common(2)   =", cnt.most_common(2))      # 出现最多的前 2 个

# Counter 还能直接把一个列表丢进去自动计数
c2 = Counter("abracadabra")
print("Counter('abracadabra') =", c2)

print()
print("=" * 48)
print("4) defaultdict：取值时 key 不存在也不报错")
print("=" * 48)

# 普通字典：key 不存在会 KeyError
normal = {}
# normal["a"].append(1)   # 这行会报 KeyError，所以要先 setdefault
normal.setdefault("a", []).append(1)
print("普通 dict 要 setdefault：", normal)

# defaultdict(list)：缺 key 时自动建一个空列表
dd = defaultdict(list)
dd["fruit"].append("apple")
dd["fruit"].append("banana")
dd["veggie"].append("carrot")
print("defaultdict(list)：", dict(dd))

# 也可以指定默认值为 int（默认 0）
counter = defaultdict(int)
for ch in "hello":
    counter[ch] += 1
print("defaultdict(int) 数数：", dict(counter))

print()
print("=" * 48)
print("5) UserDict / UserList：给字典、列表做二次开发")
print("=" * 48)


class UpperDict(UserDict):
    """一个「键自动变成大写」的字典"""

    def __setitem__(self, key, value):
        super().__setitem__(key.upper(), value)


ud = UpperDict()
ud["name"] = "Tom"
print("UpperDict：", dict(ud))
print("用大写键也能取到：", ud["NAME"])


class SumList(UserList):
    """在列表基础上加一个 total() 方法，边收集边求和"""

    def total(self):
        return sum(self.data)

sl = SumList([1, 2, 3])
sl.append(4)
print("SumList：", sl)
print("sl.total()：", sl.total())

print()
print("小结：需要「更像样」的容器时，先看 collections——namedtuple / deque / Counter /")
print("      defaultdict 能满足绝大多数扩展需求；真要改行为，再继承 UserDict / UserList。")
```

运行命令：

```bash
python3 097-collections-demo.py
```

本机实测输出：

```
================================================
1) namedtuple：给元组的位置起名字
================================================
p       = Point(x=3, y=4)
p.x     = 3
p.y     = 4
p[0]    = 3
它是元组吗？ True

================================================
2) deque：双端队列，左右两端都能进出
================================================
遍历 deque：
   t
   e
   s
   t
   _
   d
   e
   q
append / appendleft 之后： deque(['left', 't', 'e', 's', 't', '_', 'd', 'e', 'q', 'right'])
pop / popleft 之后：     deque(['t', 'e', 's', 't', '_', 'd', 'e', 'q'])
maxlen=3 只保留最后 3 个： deque([3, 4, 5], maxlen=3)

================================================
3) Counter：计数器，统计出现次数
================================================
cnt              = Counter({'blue': 3, 'red': 2, 'green': 1})
cnt['blue']      = 3
most_common(2)   = [('blue', 3), ('red', 2)]
Counter('abracadabra') = Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

================================================
4) defaultdict：取值时 key 不存在也不报错
================================================
普通 dict 要 setdefault： {'a': [1]}
defaultdict(list)： {'fruit': ['apple', 'banana'], 'veggie': ['carrot']}
defaultdict(int) 数数： {'h': 1, 'e': 1, 'l': 2, 'o': 1}

================================================
5) UserDict / UserList：给字典、列表做二次开发
================================================
UpperDict： {'NAME': 'Tom'}
用大写键也能取到： Tom
SumList： [1, 2, 3, 4]
sl.total()： 10

小结：需要「更像样」的容器时，先看 collections——namedtuple / deque / Counter /
      defaultdict 能满足绝大多数扩展需求；真要改行为，再继承 UserDict / UserList。
```

### 课后作业

请你编写程序，统计一篇文章中出现频率在前五的单词，并将单词和出现次数一起输出到终端。

> 参考答案见下一讲（第 98 讲）的 `code/098-chapter-review.py`：
> 用 `re.findall(r"[a-z]+", text.lower())` 取出所有单词，交给 `Counter` 计数，
> 再 `most_common(5)` 输出前五名。

---

## 第 98 讲 · 再回首：“办公自动化”单元小结

### 本节目标

把本章四讲串成一个**能解决真实问题的小工具**：读入一篇文章 → 数词频 → 取前五。它正好也是第 97 讲课后作业的答案。

### 知识要点

这一讲不再引入新知识，而是**回顾主线**：

- 第 94 讲：格式 ↔ 库——`xlsx → openpyxl`，`docx → python-docx`
- 第 95 讲：批量读取 Excel——`pathlib` 遍历目录 + `openpyxl` 合并/拆分
- 第 96 讲：批量格式转换——Word ↔ Excel 双向互转
- 第 97 讲：扩展数据类型——`collections` 的 `namedtuple` / `deque` / `Counter` / `defaultdict`

本讲的小工具把其中两块拼起来：**「读文件 + 数数」**。数据从哪来（文件）不重要，
重点是「把文本交给 `Counter`，再按频次排序输出」这套组合拳。

### 代码实操

`code/098-chapter-review.py`：

```python
"""第 98 讲 · 再回首：“办公自动化”单元小结"""

import re
from collections import Counter

# 一篇文章（这里内嵌一段英文，代表「读进来的文章文本」）
ARTICLE = """
Python is a programming language that lets you work quickly.
Python is powerful and fast and plays well with others.
Python runs on Windows, Linux and macOS.
Python is easy to learn and fun to use.
The language is simple and the community is friendly.
"""

print("=" * 48)
print("统计一篇文章中出现频率前 5 的单词")
print("=" * 48)

# 1. 预处理：统一转小写
text = ARTICLE.lower()

# 2. 用正则找出所有「单词」（连续的字母），顺便自动丢掉标点
words = re.findall(r"[a-z]+", text)
print("一共找到", len(words), "个单词")
print("前 10 个：", words[:10])

# 3. 用 Counter 数数
counter = Counter(words)

# 4. 取出现频率前 5
print()
print("出现频率前 5 的单词：")
for rank, (word, count) in enumerate(counter.most_common(5), start=1):
    print(f"  第 {rank} 名：{word:<10} {count} 次")

print()
print("本章回顾：")
print("  94  什么文件用什么库：xlsx->openpyxl，docx->python-docx")
print("  95  批量读取 Excel：pathlib 遍历 + openpyxl 合并/拆分")
print("  96  批量格式转换：Word <-> Excel 双向转换")
print("  97  扩展数据类型：collections 的 namedtuple/deque/Counter/defaultdict")
print("  98  小结：把「读文件 + 数数」组合起来，就是一个真实的小工具")
```

运行命令：

```bash
python3 098-chapter-review.py
```

本机实测输出：

```
================================================
统计一篇文章中出现频率前 5 的单词
================================================
一共找到 45 个单词
前 10 个： ['python', 'is', 'a', 'programming', 'language', 'that', 'lets', 'you', 'work', 'quickly']

出现频率前 5 的单词：
  第 1 名：is         5 次
  第 2 名：and        5 次
  第 3 名：python     4 次
  第 4 名：language   2 次
  第 5 名：to         2 次

本章回顾：
  94  什么文件用什么库：xlsx->openpyxl，docx->python-docx
  95  批量读取 Excel：pathlib 遍历 + openpyxl 合并/拆分
  96  批量格式转换：Word <-> Excel 双向转换
  97  扩展数据类型：collections 的 namedtuple/deque/Counter/defaultdict
  98  小结：把「读文件 + 数数」组合起来，就是一个真实的小工具
```

### 课后作业

把 `ARTICLE` 换成你自己电脑上的一个真实文本文件（`open(文件名).read()` 读进来），再统计前五单词。
提示：真实文章会有标点和大小写，先 `text.lower()` 再 `re.findall(r"[a-z]+", text)` 就能清洗干净。

---

## 本章小结

**速查表**

| 主题 | 关键点 |
| --- | --- |
| xlsx 读写 | `openpyxl`：`Workbook()` / `load_workbook()` / `ws.append()` / `iter_rows()` |
| xls 读写 | 读 `xlrd`、写 `xlwt`（旧版，本章只讲不跑） |
| docx 读写 | `python-docx`：`import docx`，`Document()` / `paragraphs` / `tables` / `add_table()` |
| 遍历目录找文件 | `[x for x in Path('.').iterdir() if x.match('*.xlsx')]` |
| 遍历单元格 | `for row in ws.iter_rows(values_only=True): for cell in row:` |
| 批量合并 | 遍历多个文件，逐行 `append()` 到一张总表 |
| 批量拆分 | 遍历行，每条记录 `save()` 成一个文件 |
| Word↔Excel | 读用一个库、写用另一个库，先定好列数/表头 |
| 扩展数据类型 | `collections`：`namedtuple` / `deque` / `Counter` / `defaultdict` / `UserDict` / `UserList` |
| 词频统计 | `Counter(text.split())` 或 `Counter(re.findall(r"[a-z]+", text.lower()))` |

**三句话**

1. **格式决定库**：`xlsx → openpyxl`、`docx → python-docx`，读写不同格式要用不同的库。
2. **批量 = 遍历 + 循环**：用 `pathlib` 找出文件，用 `for...in` 走行与格，合并、拆分都是它的延伸。
3. **容器不够用就找 `collections`**：数数用 `Counter`、两端进出用 `deque`、给元组命名用 `namedtuple`。

**动手练习**

1. 跑一遍 `code/094-file-types.py`，用 Word 打开生成的 `094-作业-excel转docx.docx`，看看那张表。
2. 跑一遍 `code/095-batch-read-excel.py`，打开 `work/汇总.xlsx` 和 `work/拆分明细/`，对照输出。
3. 把 `code/096-format-convert.py` 的输出文件名改成输入同名（`sample.xlsx`），体会「同名转换」。
4. 用 `Counter` 统计你某段文字里出现最多的 3 个字/词。

---

## 下一章预告

第 13 章进入 **Web 开发**：用 Django 搭起第一个网站，讲清 **MVC 架构、路由、模型与后台管理（admin）**，
把「会写脚本」升级成「能做出一个能访问的网页应用」。

> ⚠️ 第 13 章需要 Django 与数据库，属于**未实跑**单元，正文会讲清原理并给出课程完整代码。

---

[← 上一章：数据分析](/guide/data-analysis) ｜ [返回总目录](/) ｜ [下一章：Web 开发 →](/guide/web)

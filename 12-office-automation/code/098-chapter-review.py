"""第 98 讲 · 再回首：“办公自动化”单元小结

本讲把第 94–97 讲串起来，做一个综合小练习，也就是第 97 讲的课后作业：
    统计一篇文章中出现频率在前五的单词，把「单词 + 次数」输出到终端。

用到的都是本章学过的能力：
    文件读取         -> 第 95、96 讲的「读文件」思路
    collections      -> 第 97 讲的 Counter
    字符串清洗       -> 去掉标点、统一小写

纯标准库，真跑，不需要安装任何依赖。

运行：python3 098-chapter-review.py
"""

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

# 第 26 讲 · 小试牛刀：如何利用类型转换实现手机通讯录？（上）
# 本讲分两部分：先把「文章」分析成结构化数据，再把 csv 通讯录读成字典。
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------- 第一部分：把文章当成数据来分析（非结构化 → 结构化）----------
with open(os.path.join(HERE, "26-demo.txt"), encoding="utf-8") as f:
    file_data = f.readlines()   # 每一行（含换行符）作为一个元素，得到一个列表

print("文件一共", len(file_data), "行")

# 空行就是「只含换行符」的行
blank_lines = file_data.count("\n")
print("其中空行", blank_lines, "行")
print("非空行", len(file_data) - blank_lines, "行")

# 统计单词：先把所有行拼成一大段文本，再按空白切分
all_text = " ".join(file_data)
words = all_text.split()
print("单词 I 出现", words.count("I"), "次")
print("单词 you 出现", words.count("you"), "次")
print("单词 You 出现", words.count("You"), "次")
print("you 与 You 一共出现", words.count("you") + words.count("You"), "次")

# ---------- 第二部分：把 csv 通讯录读成「字典」（非结构化 → 结构化）----------
with open(os.path.join(HERE, "26-demo.csv"), encoding="utf-8") as f:
    csv_lines = f.readlines()
print("\n原始 csv 文本:", csv_lines)

contacts = []
for line in csv_lines:
    name, source, tel = line.strip().split(",")   # 按逗号切成 3 个字段
    contacts.append({"name": name, "source": source, "tel": tel})

print("转换后的通讯录（列表套字典）:")
for contact in contacts:
    print(contact)

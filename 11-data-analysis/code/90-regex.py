"""第 90 讲 · 理论盘点：非规范化数据处理的基础与正则表达式

本讲的核心是真跑：
    1. json 处理（json.dumps / json.loads）——把 Python 对象和 JSON 字符串互相转换；
    2. 正则表达式（re.split / re.sub / re.findall / re.search）——处理有规律但格式乱的数据；
    3. 完成课后作业：把带多余引号和空格的字符串转成 Python 字典。

运行：python3 90-regex.py
"""

import re
import json

line = "-" * 46

# ============================================================
# 一、json：把 Python 对象和 JSON 字符串互转
# ============================================================
print("一、json 处理")
print(line)

# Python 字典 -> JSON 字符串
dict1 = {"a": 123, "b": 456}
json_str = json.dumps(dict1)
print("dict1                :", dict1)
print("json.dumps(dict1)    :", json_str, "  （类型：", type(json_str).__name__, "）")

# JSON 字符串 -> Python 字典
json_string = '{"a": 123, "b": 456}'
back = json.loads(json_string)
print("json.loads(json_string):", back, "  （类型：", type(back).__name__, "）")
print("取回 a 的值          :", back["a"])
print()

# 真实场景：接口返回的 JSON 文本，先 loads 再按 key 取值
api_response = '''
{
    "status": 200,
    "data": {"city": "Beijing", "temp": 30, "humidity": 55}
}
'''
payload = json.loads(api_response)
print("解析接口返回：status =", payload["status"])
print("              city   =", payload["data"]["city"])
print("              temp   =", payload["data"]["temp"])
print()

# 中文默认被转成 \uXXXX，加 ensure_ascii=False 保持中文可读
print("中文转 JSON（默认）  :", json.dumps({"city": "北京"}))
print("中文转 JSON（可读）  :", json.dumps({"city": "北京"}, ensure_ascii=False))
print()

# ============================================================
# 二、正则表达式：处理「有规律但格式乱」的数据
# ============================================================
print("二、正则表达式 re")
print(line)

# 1) re.split：按「非单词字符」拆分，maxsplit=1 表示只拆一次
strings = "Words, words, words12312321321."
print("原始字符串           :", strings)
print("re.split(r'\\W+', strings, 1) :", re.split(r"\W+", strings, 1))
print()

# 2) re.sub：把匹配到的内容替换成别的
messy = "  北京  ,   20220620 , 30  "
clean = re.sub(r"\s+", "", messy)          # \s+ 匹配一个或多个空白字符
print("替换前               :", repr(messy))
print("re.sub(r'\\s+', '', messy) :", repr(clean))
print()

# 3) re.findall：找出所有符合规则的内容
html = '<img src="a.jpg"> <img src="b.png"> <img src="c.gif">'
imgs = re.findall(r'src="([^"]+)"', html)  # ([^"]+) = 捕获引号里的一串非引号字符
print("从 HTML 里找图片地址 :", imgs)
print()

# 4) re.search + 分组：只要第一处匹配，并用 () 分组取值
text = "2022-06-20 北京 30度"
m = re.search(r"(\d{4})-(\d{2})-(\d{2})", text)
print("匹配日期             :", m.group(0), "（整段）")
print("                     年 =", m.group(1), "月 =", m.group(2), "日 =", m.group(3))
print()

# 5) 常用元字符一览（配合小例子看效果）
print("常用元字符演示：")
print("  .    任意 1 个字符        re.findall(r'a.c', 'abc adc aac') ->",
      re.findall(r"a.c", "abc adc aac"))
print("  *    前一个字符 0 次或多次 re.findall(r'ab*', 'a ab abb')     ->",
      re.findall(r"ab*", "a ab abb"))
print("  +    前一个字符 1 次或多次 re.findall(r'ab+', 'a ab abb')     ->",
      re.findall(r"ab+", "a ab abb"))
print("  ?    前一个字符 0 次或 1 次 re.findall(r'ab?', 'a ab abb')    ->",
      re.findall(r"ab?", "a ab abb"))
print()

# 6) re.compile：规则要反复用时，先编译一次（也可读性更好）
pattern = re.compile(r"\d+")
print("re.compile(r'\\d+').findall('abc 12 def 345') ->",
      pattern.findall("abc 12 def 345"))
print()

# ============================================================
# 三、课后作业
#   已知 string = ' "{" hello ":" world "}" '
#   请用正则 + 相关库把它变成 Python 字典并输出
# ============================================================
print("三、课后作业：把乱格式字符串还原成字典")
print(line)

raw = ' "{" hello ":" world "}" '
print("原始字符串           :", repr(raw))

# 思路：先去掉所有单引号、空格；此时变成了合法的 JSON 文本 {...}，再用 json 解析。
# 注意：正则里的中括号字符集去空白是没问题的，但我们用 re.sub 把两头的引号先剥掉。
stripped = raw.strip()               # 去掉两端空白 -> '"{" hello ":" world "}"'
# 去掉包裹在外层的双引号
inner = stripped[1:-1]               # -> '{" hello ":" world "}"'
# 去掉键和值两侧多余的空白
inner = re.sub(r'"\s*', '"', inner)  # -> '{"hello":"world"}'
inner = re.sub(r'\s*"', '"', inner)  # -> '{"hello":"world"}'
print("整理为合法 JSON      :", inner)

result = json.loads(inner)
print("最终得到的字典       :", result)
print("按 key 取值          :", result["hello"])

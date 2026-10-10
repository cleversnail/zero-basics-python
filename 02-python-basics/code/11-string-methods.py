# 11-string-methods.py
# 第 11 讲 · 字符串（下）：Python 是如何处理单词的？
#
# 字符串自带了大量“方法”（method，就是属于字符串对象的函数），
# 本讲挑最常用的几个演示：count / isalnum / isalpha / join / split / startswith。

# count(sub)：统计子串出现次数
print("xyzxyzxyz".count("x"))
print("xyzxyzxz".count("xy"))
print("xyzxyzxz".count("a"))

# isalnum()：是否“全部由字母或数字组成且至少一个字符”
print("xyzxyzxz".isalnum())

# isalpha()：是否“全部由字母组成且至少一个字符”
print("xyzxyzxz".isalpha())

# join(iterable)：把一个可迭代对象里的字符串拼起来
print(",".join("abcdefg"))

# split(sep)：按分隔符拆成列表
print("a,b,c,d".split(","))

# startswith(prefix)：是否以某前缀开头
print("xyz".startswith("y"))

# 课后作业：统计下面这段文章中单词 better 出现的次数
text = (
    "Beautiful is better than ugly.\n"
    "Explicit is better than implicit.\n"
    "Simple is better than complex."
)
print(text.count("better"))

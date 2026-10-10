# 16-naming.py
# 第 16 讲 · 变量命名规范：如何编写优雅的程序？
#
# 合法的变量名：只能包含字母、数字、下划线，且不能以数字开头，
# 不能含空格，不能使用 Python 关键字；Python 大小写敏感。

# ---------- 一、合法命名示例 ----------
error_number = 1        # 多个单词用下划线连接（推荐写法）
name2 = "Python"        # 可以含数字，但不能以数字开头
_name = "下划线开头也合法"
print(error_number)
print(name2)
print(_name)

# ---------- 二、用 str.isidentifier() 检查一个名字是否合法 ----------
print("error_number".isidentifier())   # 合法
print("1a".isidentifier())             # 以数字开头 → 不合法
print("my name".isidentifier())        # 含空格 → 不合法

# ---------- 三、关键字不能当变量名 ----------
import keyword

print(keyword.kwlist)                 # Python 的全部关键字
print(keyword.iskeyword("for"))       # for 是关键字
print(keyword.iskeyword("hello"))     # hello 不是关键字

# ---------- 四、好的命名习惯 ----------
# 简短、描述性强、全小写、多单词用下划线连接，避免中文和 l/1/O/0 这类易混字符。
user_name = "张三"
max_count = 100
print(user_name)
print(max_count)

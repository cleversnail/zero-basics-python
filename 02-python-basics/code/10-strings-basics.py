# 10-strings-basics.py
# 第 10 讲 · 字符串（上）：Python 是如何处理单词的？
#
# 字符串（str）用于处理文本，是 Python 最常用的数据类型之一。
# 本讲讲两件事：怎样定义字符串、字符串的基本操作。

# ---------- 一、怎样定义字符串 ----------

# 1) 双引号
print("Hello Python")

# 2) 单引号（内部还能再放双引号）
print('Hello " Python " ')

# 3) 三重引号：可以跨多行
print('''
Hello
Python
''')

# ---------- 二、字符串里使用变量：f-strings ----------
x = 123
print(f"{x}： {x} 是变量 x 的值 ")

# ---------- 三、字符串的基本操作 ----------

# 成员运算：in / not in
print("xy" in "123xy456")
print("x" not in "123x456")

# 连接运算：+ 拼接，* 重复
print("abc" + "xyz")

x = "abc"
y = "xyz"
print(x + y)
print(x * 3)
print(x)
print(y)

# 切片运算：s[i] / s[i:j] / s[i:j:k]
s = "abcdefg"
print(s[0])      # 第 1 个字符（下标从 0 开始）
print(s[-1])     # 最后一个字符
print(s[1:5:2])  # 从下标 1 到 5（不含 5），步长为 2

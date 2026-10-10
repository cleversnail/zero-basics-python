# 12-numbers.py
# 第 12 讲 · 存储数字应该采用哪种数据类型？
#
# 数字类型用于数学计算和统计，主要有三种：整数 int、浮点数 float、复数 complex。

# ---------- 一、数字类型的常见运算 ----------
print(7 + 3)
print(7 - 3)
print(7 * 3)
print(7 / 3)      # 除法结果总是浮点数
print(7 // 3)     # 整除（向下取整）
print(7 % 3)      # 取余数
print(-(7))
print(+(7))

# 常用内置函数
print(abs(-5))
print(int(3.9))
print(float(3))
print(complex(3, 4))
print(divmod(7, 3))   # (商, 余数)
print(pow(2, 10))
print(2 ** 10)

# ---------- 二、用 type() 看一个值到底是什么类型 ----------
print(type(123))
print(type(3.14))

# ---------- 三、强制类型转换 ----------
print(int(123.456))       # 浮点 → 整数（直接截断小数部分）

abc = "123"
xyz = int(abc)            # 字符串 → 整数（字符串里必须全是数字）
print(type(xyz))

# str()：数字 → 字符串
print(str(456))
print(type(str(456)))

# 课后作业：让用户输入两个整数，程序算它们的和
# 讲义用 input() 读入（读到的其实是字符串），这里用固定值代替
num1 = int("12")
num2 = int("30")
print(num1 + num2)

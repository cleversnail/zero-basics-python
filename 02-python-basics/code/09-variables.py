# 09-variables.py
# 第 9 讲 · 变量：如何让计算机临时存储数据？
#
# 变量就像给内存里的数据“贴标签”：贴了什么名字，以后就用这个名字取数据。

# 1) 用变量接住输入（讲义写法是 text = input()，这里用固定值代替）
text = "hello"
print(text)
print(text)
print(text)

# 2) 直接给变量赋值
x = 123
print(x)

# 3) 变量可以随时改指向：同一个 x，先指向 123，再指向 456
x = 456
print(x)

# 4) 把一个变量的值赋给另一个变量
y = x
print(y)

# 5) 连续赋值：z、y 都指向 x 的值
z = y = x
print(z)

# 6) 一次给多个变量赋不同的值（元组解包）
a, b = 111, 222
print(a)
print(b)

# 课后作业：定义一个变量 pi，赋值为 3.14，并用 print() 输出
pi = 3.14
print(pi)

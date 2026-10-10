# 第 36 讲：语句嵌套 —— 如何处理多重循环的问题？
# 直接运行：python3 36-nested.py

# 1) 在条件语句里再写条件语句：找出 100 以内能被 7 整除的数
#    写法一：分步判断，用临时变量存储中间结果
number = 49
if number < 100:
    temp = number % 7
    if temp == 0:
        print(f"写法一：{number} 能被 7 整除")

#    写法二：把两个条件合并到一个 if 里
for number in (7, 49, 100):
    if number < 100 and number % 7 == 0:
        print(f"写法二：{number} 能被 7 整除")

# 2) 循环里嵌套条件语句，也能写成推导式
print([x * x for x in range(10) if x % 7 == 0])

# 3) 多重循环：把 3x5 的矩阵拉平成一维列表
data = [[1, 2, 1, 2, 0],
        [2, 2, 2, 1, 0],
        [1, 1, 2, 2, 0]]
list2 = []
for i in data:          # 外层循环：一行一行取
    for j in i:         # 内层循环：取行里的每个元素
        list2.append(j)
print(list2)

# 4) 课后作业：用嵌套循环在命令行打印九九乘法表
for i in range(1, 10):
    row = []
    for j in range(1, i + 1):
        row.append(f"{j}*{i}={i * j}")
    print(" ".join(row))

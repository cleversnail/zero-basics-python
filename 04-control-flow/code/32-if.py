# 第 32 讲：if 语句 —— 数据流程出现分支时，怎样编写程序？
# 直接运行：python3 32-if.py

# 1) 最简单的 if：条件为 True 才执行缩进的那一条（或那几条）语句
if True:
    print("条件为真,执行该条语句")

if False:
    print("条件为假,不执行该条语句")
print("没有缩进,不是 if 语句块中的语句,执行")

# 2) if ... else：条件为真做一件事，为假做另一件事
if True:
    print("条件为真")
else:
    print("条件为假")

# 3) if ... elif ... else：处理三种及以上情况
number = 10
if number % 2 == 1:
    print("number是奇数")
elif number % 2 == 0:
    print("number是偶数")
else:
    print(f"number 的值是 {number}")

# 4) 测试条件：相等、不相等，以及数值比较符号
print("date" == "2022-06-01")     # 是否相等
print("date" != "2022-06-01")     # 是否不相等
print(3 > 2, 3 >= 3, 2 < 1, 2 <= 2)

# 5) 课后作业：随机生成 1~100 的整数，判断能否被 3 整除
#    为了让每次运行结果一致，这里固定随机种子；去掉 seed 就是真正随机
import random

random.seed(2026)
for _ in range(5):
    number = int(random.random() * 100 + 1)
    if number % 3 == 0:
        print(f"{number} 能被 3 整除")
    else:
        print(f"{number} 不能被 3 整除")

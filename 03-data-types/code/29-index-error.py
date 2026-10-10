# 第 29 讲 · 避坑指南（1）：访问越界
# ⚠️ 本文件故意触发错误，用来演示真实报错：IndexError
numbers = [1, 2, 3]
print("合法访问:", numbers[0])
print("合法访问:", numbers[2])
print(numbers[3])   # 下标越界！

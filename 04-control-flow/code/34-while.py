# 第 34 讲：while 循环 —— 需要多次重复执行某段程序时，怎么做？
# 直接运行：python3 34-while.py

# 1) 正向计数：1、2、3
number = 1
while number <= 3:
    print(f"number is {number}")
    number += 1
print(number)   # 循环结束时 number 已经是 4

# 2) 反向计数：3、2、1
number = 3
while number >= 1:
    print(f"number is {number}")
    number -= 1

# 3) 用 break 提前跳出循环
number = 10
while number >= 1:
    print(f"number is {number}")
    number -= 1
    if number == 5:
        break

# 4) 用 continue 跳过本次剩余语句
number = 10
while number >= 1:
    number -= 1
    if number == 5:
        continue
    print(f"number is {number}")

# 5) 用 while 把循环结果放入列表
list1 = []
number = 1
while number < 5:
    list1.append(number)
    number += 1
print(list1)

# 6) 用 while 遍历列表：不断弹出末尾元素，直到列表为空
list1 = [1, 2, 3, 4, 5]
while list1:
    print(list1.pop())

# 7) 课后作业：猜数字，最多猜三次
#    交互输入无法在文档里演示，这里用固定猜测序列代替 input()
target = 42                # 相当于随机产生的正确答案
guesses = [30, 42, 88]     # 相当于用户依次输入的三个数字
index = 0
while index < 3:
    guess = guesses[index]
    index += 1
    if guess == target:
        print(f"第 {index} 次猜中，答案是 {target}，游戏结束")
        break
    print(f"第 {index} 次猜 {guess}，没猜中")
else:
    print(f"三次都没猜中，正确答案是 {target}")

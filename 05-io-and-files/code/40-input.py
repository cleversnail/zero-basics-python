# -*- coding: utf-8 -*-
"""
第 40 讲 · 输入：如何接收用户通过键盘输入的数据？

input() 是「交互式输入」函数：程序跑到这里会停下来，等你在键盘上敲一行，
按回车后，把这一行内容作为「字符串」返回。

⚠️ input() 会一直等用户敲键盘，在文档 / 自动化脚本里没法演示。
下面把真正要写的 input() 注释掉，用一个固定值代替，效果完全一样。
"""

# 真正交互时这样写（程序会停下来等你输入）：
# name = input("请输入你的名字：")
# age = input("请输入你的年龄：")

# 文档演示：用固定值代替上面的键盘输入
name = "小明"
age = "18"

print(f"你好，{name}！")
print(f"你的年龄是 {age} 岁")

# input() 返回的永远是字符串，想要数字必须自己做类型转换
# num = int(input("请输入一个数字："))
num = int("7")            # 演示：等价于用户敲入了 7
print(f"你输入的数字 + 1 = {num + 1}")
print(f"转换后的类型是：{type(num)}")

# input() 也常放在循环里，实现「按键驱动」：输入 q / quit 就退出
# 真实的写法是：
#   while True:
#       cmd = input("请输入控制指令（q 退出）：")
#       if cmd == "q":
#           break
#       print("你输入的是：", cmd)
# 演示：用一串固定指令代替用户依次敲入的内容
commands = ["s", "l", "q", "x"]
for cmd in commands:
    if cmd == "q":
        print("收到 q，退出程序")
        break
    print(f"收到指令 {cmd}：执行对应操作")

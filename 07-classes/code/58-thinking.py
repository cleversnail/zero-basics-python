# 第 58 讲 · 编程思想不同会导致怎样的代码差异？
#
# 同一个需求「做一杯美式咖啡」，用两种编程思想各写一遍，体会差异。

print("========== 面向过程：以「步骤」为核心 ==========")


def make_coffee():
    # 先 xxx，再 xxx，然后 xxx —— 完全按照时间顺序排列
    water = 200
    print(f"  1. 加水 {water} ML")
    coffee = 1
    print(f"  2. 加咖啡液 {coffee} 份")
    print("  3. 美式咖啡完成")


make_coffee()

print()
print("========== 面向对象：以「对象」为核心 ==========")


class Coffee:
    """一杯咖啡：数据（水和咖啡液的量）和动作（制作）被封装在一起。"""

    def __init__(self, water, coffee):
        self.water = water
        self.coffee = coffee

    def make(self):
        if self.water:
            print(f"  加水 {self.water} ML")
        if self.coffee:
            print(f"  加咖啡液 {self.coffee} 份")
        print("  美式咖啡完成")


americano = Coffee(water=200, coffee=1)
americano.make()

print("  再换一个对象，就是另一杯：")
another = Coffee(water=150, coffee=1)
another.make()

print()
print("========== Python 里一切都是对象：is 与 == ==========")

num = 100
num2 = num
print("  num is num2 （是同一个对象吗）  :", num is num2)
print("  num == num2 （值相等吗）        :", num == num2)

num = 456  # num 指向了一个新对象
print("  改 num 之后 num is num2         :", num is num2)
print("  num =", num, " num2 =", num2)

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print("  list1 == list2 （值相等吗）      :", list1 == list2)
print("  list1 is list2 （是同一个对象吗）:", list1 is list2)

list1.append(4)
print("  给 list1 追加 4 之后：")
print("    list1 =", list1)
print("    list2 =", list2)

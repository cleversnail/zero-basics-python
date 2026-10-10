# 第 59 讲 · 类与实例：如何使用面向对象的思想编写程序？


# class 是定义类的关键字；Coffee 是类名（约定首字母大写）
class Coffee:
    # 类属性：写在类里、方法外，被所有实例「共享」
    water = 0
    milk = 0

    # 实例方法：第一个参数固定是 self，代表「当前这个对象」
    def add_water(self):
        # self.xxx 这样写，产生的是「实例属性」，只属于调用的那个对象
        self.hot_water = 1


print("========== 1. 类的实例化 ==========")
# Coffee() 就是「实例化」：类像一张图纸，实例是按图纸造出来的具体一个
mocha = Coffee()
print("  mocha 的类型        :", type(mocha))
print("  mocha 是 Coffee 实例吗:", isinstance(mocha, Coffee))
print("  注意：类本身也是对象 :", type(Coffee))

print()
print("========== 2. 对象拥有类的属性 ==========")
print("  mocha.water =", mocha.water)
print("  mocha.milk  =", mocha.milk)

print()
print("========== 3. 调用实例方法，产生实例属性 ==========")
mocha.add_water()
print("  mocha.hot_water =", mocha.hot_water)

print()
print("========== 4. 两个实例互不干扰 ==========")
latte = Coffee()
print("  改之前：mocha.water =", mocha.water, " latte.water =", latte.water)
mocha.water = 300  # 只给 mocha 自己挂一个实例属性
print("  改之后：mocha.water =", mocha.water, " latte.water =", latte.water)
print("  类属性的原值没变：Coffee.water =", Coffee.water)

# 第 62 讲 · 小试牛刀：如何开发自动咖啡机？
#
# 一杯咖啡由三种原料调配：水、咖啡液、牛奶。
# 每种原料做成一个 Mixin（只放方法），咖啡类把它们拼装起来。
# 本程序用「固定订单」自动跑完，不需要手工输入。


class WaterMixin:
    def add_water(self, volume, temperature):
        # 水以毫升为单位，并且区分冷热
        return f"水     ：{temperature} 水 {volume} ML"


class CoffeeMixin:
    def add_coffee(self, parts):
        # 咖啡液以「份」为单位
        return f"咖啡液 ：{parts} 份"


class MilkMixin:
    def add_milk(self, volume, temperature):
        # 牛奶以毫升为单位，也区分冷热
        return f"牛奶   ：{temperature} 奶 {volume} ML"


class Coffee(WaterMixin, CoffeeMixin, MilkMixin):
    """一杯咖啡成品；某种原料传 -1 表示不放。"""

    def __init__(self, name, water=-1, water_temp="hot",
                 coffee=1, milk=-1, milk_temp="hot"):
        self.name = name
        self.recipe = []  # 配方：逐条记录加了哪种原料

        if water > 0:
            self.recipe.append(self.add_water(water, water_temp))
        if coffee > 0:
            self.recipe.append(self.add_coffee(coffee))
        if milk > 0:
            self.recipe.append(self.add_milk(milk, milk_temp))

    def show(self):
        print(f"【{self.name}】")
        for line in self.recipe:
            print("  " + line)
        print(f"  —— 共 {len(self.recipe)} 种原料")


# 固定的三张订单，程序自动处理完
orders = [
    Coffee("美式", water=200, water_temp="hot", coffee=1),
    Coffee("拿铁", water=50, water_temp="hot", coffee=1, milk=150, milk_temp="hot"),
    Coffee("冰美式", water=200, water_temp="cold", coffee=1),
]

for cup in orders:
    cup.show()
    print()

print("Coffee.__mro__ =", Coffee.__mro__)

# 第 65 讲 · 再回首：「类」单元小结
#
# 用一个小例子，把本章要点串一遍：
# 定义类、__init__ 传参、方法、staticmethod、继承 + super()、多继承 / Mixin。


class Animal:
    def __init__(self, name):  # __init__：实例化时接收参数
        self.name = name

    def speak(self):  # 方法
        print(f"  {self.name} 发出了声音")

    @staticmethod
    def about():  # staticmethod：不需要 self / cls
        print("  这是一个动物类")


class Dog(Animal):  # 继承
    def speak(self):
        super().speak()  # 复用父类方法
        print("  汪汪汪")


class SwimMixin:  # Mixin：只加方法
    def swim(self):
        print("  我还会游泳")


class Duck(Animal, SwimMixin):  # 多继承（用 Mixin 拼装能力）
    def speak(self):
        print(f"  {self.name} 嘎嘎嘎")


Animal.about()

a = Animal("小猫")
a.speak()

d = Dog("小狗")
d.speak()

duck = Duck("小鸭")
duck.speak()
duck.swim()

print("  Duck.__mro__ =", Duck.__mro__)

# 第 60 讲 · 类的继承：如何解决代码重用的问题？


print("========== 1. 父类与子类，super() 复用父类方法 ==========")


# 被继承的类叫父类，继承的类叫子类
class Father(object):
    def run(self):
        print("  run in father")


class Son(Father):
    def run(self):
        super().run()  # 先执行父类同名方法的内容
        print("  run in son")  # 再补充子类自己的行为


f = Father()
f.run()
print("  ---")
s = Son()
s.run()

print()
print("========== 2. 查看继承顺序：__mro__ ==========")
print("  Son.__mro__ =", Son.__mro__)

print()
print("========== 3. 多继承与 Mixin ==========")
# Mixin（混入）：借用多继承语法，只提供方法、不定义属性，也绝不单独实例化，
# 类名习惯以 Mixin 结尾。用它给现有类「拼装」能力，而不是构造复杂继承树。


class CookMixin:
    def cook(self):
        print("  会做饭")


class DriveMixin:
    def drive(self):
        print("  会开车")


class Person(CookMixin, DriveMixin):
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f"  我是 {self.name}")


p = Person("小明")
p.hello()
p.cook()
p.drive()
print("  Person.__mro__ =", Person.__mro__)

# 第 61 讲 · 类的装饰器：如何改变类方法的功能？


print("========== 1. classmethod：方法绑定到「类」 ==========")


class Klass:
    @classmethod
    def func(cls):  # cls 代表「当前这个类」（不是实例）
        print("  调用 classmethod，cls =", cls.__name__)


Klass.func()  # 直接用类调用
Klass().func()  # 也可以用实例调用

print()
print("========== 2. staticmethod：和类相关，但不需要 self / cls ==========")


class Tool:
    @staticmethod
    def add(a, b):  # 没有 self，也没有 cls
        return a + b


print("  Tool.add(3, 4)    =", Tool.add(3, 4))  # 不需要先实例化
print("  Tool().add(3, 4)  =", Tool().add(3, 4))  # 也可以实例调用

print()
print("========== 3. property：把方法伪装成属性 ==========")


class Klass3:
    @property
    def func(self):  # getter：读取 obj.func 时执行
        return self.__var_name

    @func.setter
    def func(self, value):  # setter：给 obj.func 赋值时执行
        self.__var_name = value


obj = Klass3()
obj.func = "123"  # 触发 setter
print("  obj.func =", obj.func)  # 触发 getter

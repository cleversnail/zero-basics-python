# -*- coding: utf-8 -*-
"""第 81 讲 · 设计模式：怎样合理组合多个函数和类？

本讲真跑。演示三种设计模式的最小实现：
  1. 单例（Singleton）：用模块（import）天然实现
  2. 单态（Monostate）：多个实例共享同一份类属性
  3. 适配器（Adapter）：让接口不兼容的类能一起工作

运行：python3 81-design-pattern.py
"""
import singleton_config   # 同目录下的模块，Python 只会导入一次


print("=" * 50)
print("1. 单例模式：靠 import 实现")
print("=" * 50)
print("第一次取:", singleton_config.get_name())
singleton_config.set_name("改过之后")
print("改完之后:", singleton_config.get_name())
# 再导入一次，拿到的还是同一个对象（模块不会被重复执行）
import singleton_config as again
print("再次导入:", again.get_name(), "（同一个模块对象，状态共享）")


print()
print("=" * 50)
print("2. 单态模式 Monostate：多个实例共享同一属性")
print("=" * 50)


class MyClass:
    _class_variable = None   # 类属性，被所有实例共享

    def __init__(self, var):
        self.get_variable = var   # 这里会触发下面的 setter

    @property
    def get_variable(self):
        return self._class_variable

    @get_variable.setter
    def get_variable(self, var):
        # 注意：写的是「类」的属性，而不是「实例」的属性
        self.__class__._class_variable = var

    def display(self):
        return self.get_variable


c1 = MyClass(1)
c2 = MyClass(2)
c2.get_variable = 3      # 改的是类属性，c1 也会看到变化
print("c1.get_variable =", c1.get_variable)
print("c1.display()    =", c1.display())


print()
print("=" * 50)
print("3. 适配器模式 Adapter：让不兼容的接口能一起用")
print("=" * 50)


class UsbTypeA:
    def getName(self):
        return "TypeA接口"

    def oneFace(self):
        return "单面"


class UsbTypeC:
    def getName(self):
        return "TypeC接口"

    def doubleFace(self):
        return "双面"


class Adapter(UsbTypeC):
    """把 TypeC 的「双面」适配成外面期望的「单面」接口。"""

    def oneFace(self):
        return self.doubleFace()


iface1 = UsbTypeA()
print("TypeA 调用 oneFace() ->", iface1.oneFace())

iface2 = Adapter()
print("适配器调用 oneFace() ->", iface2.oneFace())

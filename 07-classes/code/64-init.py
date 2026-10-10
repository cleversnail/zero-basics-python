# 第 64 讲 · init 方法：如何为对象传递参数？


print("========== 1. __init__：实例化时自动执行 ==========")


class Klass:
    def __init__(self, name, age):  # 实例化时自动调用，用来接收参数
        self.name = name
        self.age = age

    def information(self):
        print("  姓名：", self.name)
        print("  年龄：", self.age)


myself = Klass("Tom", 18)  # 参数传给 __init__
myself.information()

print()
print("========== 2. 魔术方法：以 __ 开头和结尾 ==========")


# __call__ 让「实例」也能像函数一样被调用
class Class1:
    def __call__(self):
        print("  类也可以被调用")


c1 = Class1()
c1()  # 实例后面加括号，触发 __call__

print()
print("========== 3. 用 dir() 查看一个类型有哪些魔术方法 ==========")
magic = [name for name in dir(dict) if name.startswith("__")]
print("  dict 的魔术方法个数：", len(magic))
print("  前 8 个：", magic[:8])
print("  其中就有：__init__、__call__、__getitem__ 等")

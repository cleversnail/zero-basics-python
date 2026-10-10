# 第 63 讲 · 避坑指南（1）：忘记写 self
# ⚠️ 本文件故意触发错误，用来演示真实报错：TypeError
class Coffee:
    def add_water(volume):  # 错误：第一个参数忘了写 self
        print("加水", volume)


mocha = Coffee()
mocha.add_water(200)  # 报错：实例调用时会自动多传一个 self

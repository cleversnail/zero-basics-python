# 第 28 讲 · 常见的内置数据类型都何时使用？

# 1. 哪些值代表「假」——用 bool() 一眼看穿
falsy = [None, False, 0, 0.0, "", (), [], {}, set(), range(0)]
for value in falsy:
    print(repr(value), "->", bool(value))

# 2. 不同类型的比较规则不一样
print(1 < 2)                 # 数字：按数值大小
print("apple" < "banana")    # 字符串：按首字母的 ASCII 编码
print([1, 2] < [1, 3])       # 列表：从第一个元素开始逐项比较
print((1, 2) < (1, 3))       # 元组：同理

# 3. 需要「不重复」的数据 —— 集合最省事
names = ["tom", "tom", "jerry", "tom"]
print(list(set(names)))

# 4. 想避免被误修改 —— 用不可变的元组
point = (3, 5)
print(point)

# 5. 组合出复杂结构：列表里放字典
users = [
    {"name": "tom", "age": 18},
    {"name": "jerry", "age": 20},
]
print(users[0]["name"], users[1]["age"])

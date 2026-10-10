# 第 21 讲 · 元组：如何处理一次性数据？

# 创建元组：圆括号 () —— 三种方式
color = ("r", "g", "b", "g", "b", "b")
print(type(color), color)

print(tuple("red"))        # 字符串 → 元组
print(tuple(range(1, 4)))  # range → 元组
print(tuple(["a", "b"]))   # 列表 → 元组

# 序列的通用操作（列表、元组、range 都支持）
s = (1, 2, 3, 4, 5)
print(1 in s)              # x in s
print(9 not in s)          # x not in s
print((1, 2) + (3, 4))     # s + t 拼接
print((0,) * 3)            # s * n 重复
print(s[0])                # s[i]
print(s[1:4])              # s[i:j] 切片
print(s[1:4:2])            # s[i:j:k] 带步长的切片
print(len(s))              # len(s)
print(min(s), max(s))      # min / max
print(s.index(3))          # 首次出现的索引
print(s.count(2))          # 出现次数

# 元组不可变：想「修改」只能拼一个新的
color2 = color + ("m",)
print(color2)

# 借助集合给元组去重
new_color = set(color)
print(new_color)
print(tuple(new_color))

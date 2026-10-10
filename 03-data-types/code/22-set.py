# 第 22 讲 · 常见常新：集合的常见操作

# 创建集合：花括号 {}
s1 = {'wilson', 'yin'}
print(type(s1), s1)

print(set("hello"))            # 用 set() 构造，自动去掉重复字符
print({x for x in range(5)})   # 集合推导式

# 常用操作
print(len({'a', 'b', 'c'}))        # 元素数量
print('a' in {'a', 'b'})           # 成员检测
print({'a'} <= {'a', 'b'})         # 子集（允许相等）
print({'a', 'b'} <= {'a', 'b'})    # 相等也算子集
print({'a'} < {'a', 'b'})          # 真子集
print({'a', 'b'} < {'a', 'b'})     # 相等 → 不是真子集

# 原地修改：add / remove / pop / clear
s2 = {1, 2, 3}
s2.add(4)
print(s2)

s2.remove(1)
print(s2)

s2.pop()   # 弹出任意一个元素（集合无序，弹哪个不确定）
print(s2)

s2.clear()
print(s2)

# 集合运算
a = {1, 2, 3}
b = {3, 4, 5}
print("并集:", a | b)
print("交集:", a & b)
print("差集:", a - b)
print("对称差:", a ^ b)

# 删除集合
del s1
print("s1 已被删除")

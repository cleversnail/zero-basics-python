# 第 19 讲 · 列表：如何处理同类数据？

# 创建列表：方括号 []，元素之间用逗号分隔
colours = ["red", "blue", "green"]
print(colours)
print(type(colours))

# 内置函数 list() 可以把字符串拆成「字符的列表」
print(list("red"))

# 列表推导式（第 35 讲细讲，这里先看一眼）
print([x for x in range(1, 10)])

# 索引访问：列表是有序的，下标从 0 开始，-1 表示最后一个
list1 = ["a", "b", "c", "d"]
print(list1[0])
print(list1[1])
print(list1[-1])

# 嵌套列表：元素本身也可以是列表
list2 = ["a", "b", ["c", "d"]]
print(list2[2][0])   # 第 3 个元素（一个列表）的第 1 项
print(list2[2][1])   # 想拿到字符串 'd'，就要这样两级索引

# 删除列表中的元素 / 删除整个列表
del list1[0]
print(list1)
del list1
print("list1 已被删除（再访问它会报 NameError）")

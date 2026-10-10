# 第 23 讲 · 字典：如何处理映射类型的数据？

# 创建字典：三种方式
d1 = {'one': 1, 'two': 2}
print(type(d1), d1)

d2 = dict(one=1, two=2)          # 类型构造器
print(d2)

d3 = {x: x ** 2 for x in range(5)}   # 字典推导式
print(d3)

# 由两个列表拼出字典（本讲课后作业的答案之一）
list_name = ['name1', 'name2', 'name3']
list_sn = ['1111', '2222', '3333']
name_sn = {
    list_name[0]: list_sn[0],
    list_name[1]: list_sn[1],
    list_name[2]: list_sn[2],
}
print(name_sn)

# 键的要求：必须「可哈希」；整数 1 和浮点 1.0 是同一个键
print({1: '这是 int 键', 1.0: '这行会覆盖上面那行'})

# 删除字典中的元素
del name_sn['name3']
print(name_sn)

# 删除整个字典
temp = {'x': 1}
del temp
print("temp 已被删除")

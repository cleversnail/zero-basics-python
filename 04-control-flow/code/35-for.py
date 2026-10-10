# 第 35 讲：for 循环 —— 如何遍历一个对象里的所有元素？
# 直接运行：python3 35-for.py

# 1) for 遍历元组：把每个元素挨个儿操作一遍
for temp_element in (1, 2, 3, 4):
    print(temp_element)

# 2) for + range：range(1, 5) 生成 1、2、3、4（含头不含尾）
for temp_element in range(1, 5):
    print(temp_element)

# 3) 遍历列表：对每个元素做处理
friends = ["wilson", "monica", "john", "wang"]
for friend in friends:
    print(friend.capitalize())   # 首字母大写

# 4) 遍历字典：键、值、键值对
movie1 = {"name": "Friends", "language": "En", "Sessions": 10, "Other name": "Six of One"}

print("-- 键 --")
for title in movie1.keys():
    print(title)

print("-- 值 --")
for value in movie1.values():
    print(value)

print("-- 键值对 --")
for title, value in movie1.items():
    print(title, value)

# 5) 用 enumerate 给遍历加上编号
for i in enumerate(movie1.items()):
    print(i)

for num, value in enumerate(movie1.items()):
    print(f"第 {num} 个字典元素是 {value}")

# 6) 推导式：从一个序列构造另一个序列
list1 = [i for i in (1, 2, 3, 4)]
print(list1)
list2 = [i * i for i in (1, 2, 3, 4)]
print(list2)
list3 = [i * i for i in (1, 2, 3, 4) if i > 2]
print(list3)

# 7) 课后作业：列表首字母升序排列、元素全部大写、输出序号和内容
names = ["rachel", "monica", "Phoebe", "joey"]
sorted_names = sorted(names)   # 按首字母升序
for index, name in enumerate(sorted_names):
    print(index, name.upper())

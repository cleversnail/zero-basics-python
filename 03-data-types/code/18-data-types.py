# 第 18 讲 · 内置数据类型包括哪几种？
# 用 type() 看看各种内置数据类型的「真面目」

# 数字类型
num_int = 10
num_float = 3.14
num_complex = 1 + 2j
print(type(num_int), num_int)
print(type(num_float), num_float)
print(type(num_complex), num_complex)

# 文本类型
text = "hello"
print(type(text), text)

# 序列类型：列表、元组、range
my_list = [1, 2, 3]
my_tuple = (1, "a", 3.0)
my_range = range(1, 5)
print(type(my_list), my_list)
print(type(my_tuple), my_tuple)
print(type(my_range), list(my_range))

# 集合类型
my_set = {1, 2, 3}
print(type(my_set), my_set)

# 映射类型：字典
my_dict = {"one": 1, "two": 2}
print(type(my_dict), my_dict)

# 布尔与空值
print(type(True), True)
print(type(None), None)

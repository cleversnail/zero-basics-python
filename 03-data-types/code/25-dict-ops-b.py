# 第 25 讲 · 常见常新：字典的常见操作（下）

mail_list = {'tom': 'tom@gmail.com', 'jerry': 'jerry@foxmail.com'}

# setdefault：键存在就返回它的值；不存在就插入默认值并返回
print(mail_list.setdefault('tom', 'xxx@x.com'))    # 已存在 → 返回原值，不覆盖
print(mail_list.setdefault('john', 'john@163.com'))  # 不存在 → 插入
print(mail_list)

# 合并字典：用 | 生成一个新字典（右边优先）
new_mail = {'tom': 'tom@newmail.com', 'kate': 'kate@163.com'}
merged = mail_list | new_mail
print("合并结果:", merged)
print("原字典不变:", mail_list)

# |= 原地合并（Python 3.9 及以上）
mail_list |= new_mail
print("|= 之后:", mail_list)

# zip 把两个列表「配对」成字典
names = ['name1', 'name2', 'name3']
sn = ['1111', '2222', '3333']
print(dict(zip(names, sn)))

# 数据类型之间的转换
print(list({'a': 1, 'b': 2}))   # 字典 → 键列表
print(str({'a': 1}))

# 与其他类型混合使用：字典里放列表
colors = {'red': [255, 0, 0], 'green': [0, 255, 0], 'blue': [0, 0, 255]}
print(colors['red'])

# 与其他类型混合使用：列表里放字典
color_list = [
    {'color': 'red', 'value': [255, 0, 0]},
    {'color': 'green', 'value': [0, 255, 0]},
]
print(color_list[1]['value'])

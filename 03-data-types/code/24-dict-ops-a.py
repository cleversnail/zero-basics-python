# 第 24 讲 · 常见常新：字典的常见操作（上）

mail_list = {'tom': 'tom@gmail.com', 'jerry': 'jerry@foxmail.com', 'john': 'john@163.com'}
print(mail_list)

# 访问「所有元素」：items() / keys() / values()
print(mail_list.items())
print(list(mail_list.keys()))
print(list(mail_list.values()))

# 访问「指定键」
print(mail_list.get('tom'))            # 用 get，键不存在返回 None
print(mail_list['tom'])                # 用 []，键不存在会报 KeyError
print(mail_list.get('nobody'))         # 不存在的键 → None
print(mail_list.get('nobody', '未找到'))  # 给个默认值，键不存在也不报错

# 遍历字典
for key, value in mail_list.items():
    print(key, value)

# 修改字典：新增 / 更新一个键值对
mail_list['wilson'] = 'wilson@163.com'
print(mail_list)

mail_list['wilson'] = 'wilson@new.com'   # 键已存在 → 覆盖旧值
print(mail_list)

# 返回项数 / 判断键是否存在
print(len(mail_list))
print('tom' in mail_list)

# pop：移除指定键并返回它的值
print(mail_list.pop('tom'))
print(mail_list)

# popitem：移除「最后加入」的一对键值并返回
print(mail_list.popitem())
print(mail_list)

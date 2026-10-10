# 第 20 讲 · 常见常新：列表的常见操作

list_demo = ['a', 'b', 'c', 'd', 'e', ['f', 'g']]
print(list_demo)

# 添加元素：insert（指定位置插入）
list_demo.insert(0, "first")
print(list_demo)

list_demo.insert(-1, "last")   # -1 表示插在最后一个元素之前
print(list_demo)

# 添加元素：append（在结尾追加一个元素）
list_demo.append("last_one")
print(list_demo)

# 扩展元素：extend（把可迭代对象逐个拆开追加）
list_demo.extend("last_one")   # 注意：字符串被拆成了一串单个字符
print(list_demo)

# 移除元素：remove（移除第一个匹配项）
list_demo.remove("last_one")
print(list_demo)

# 弹出元素：pop（移除并返回指定索引的元素）
result = list_demo.pop(0)
print(f"list is {list_demo}")
print(f"result is {result}")

# 反转：reverse（原地）
nums = [3, 1, 2]
nums.reverse()
print(nums)

# 复制：copy（浅拷贝，改副本不影响原列表）
nums_copy = nums.copy()
nums_copy.append(99)
print("原列表:", nums)
print("副本:", nums_copy)

# 清空：clear（原地）
nums.clear()
print("clear 之后:", nums)

# 计算长度：len
print(len("abc"))          # 字符串的长度
print(len([1, 2, 3]))      # 列表的长度

# 统计出现次数：count
print([1, 2, 2, 3, 2].count(2))

# 排序：sorted() 返回新列表，原列表不变
data = [3, 1, 2]
sorted_data = sorted(data)
print("sorted 返回新列表:", sorted_data, "原列表不变:", data)

# 排序：list.sort() 原地排序
data.sort()
print("sort 原地排序:", data)

data.sort(reverse=True)
print("reverse=True 降序:", data)

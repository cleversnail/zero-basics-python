# 第 31 讲 · 再回首：内置数据类型单元小结

# 一表回顾：本章 6 种核心数据类型
summary = {
    "数字": "int / float / complex —— 参与算术运算",
    "字符串": "str —— 不可变、有序，处理文本",
    "列表": "list —— 可变、有序，[]，存放同类数据",
    "元组": "tuple —— 不可变、有序，()，存放一次性数据",
    "集合": "set —— 可变、无序、元素唯一，{}",
    "字典": "dict —— 键值对映射，{键: 值}",
}
for key, value in summary.items():
    print(f"{key}：{value}")

# 各类型的典型操作串一遍
scores = [90, 85, 90]
print("列表:", scores, "→ 去重并排序:", sorted(set(scores)))

info = (("tom", 18), ("jerry", 20))
print("元组:", info)

mail = dict(info)
print("元组转字典:", mail)

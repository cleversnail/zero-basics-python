# 第 29 讲 · 避坑指南（4）：对只读类型做写入
# ⚠️ 本文件故意触发错误，用来演示真实报错：AttributeError
t = (1, 2, 3)
print("先确认它是元组:", type(t))
t.append("new_element")   # 元组没有 append 方法！

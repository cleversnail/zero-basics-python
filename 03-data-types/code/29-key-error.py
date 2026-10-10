# 第 29 讲 · 避坑指南（2）：访问不存在的键
# ⚠️ 本文件故意触发错误，用来演示真实报错：KeyError
mail_list = {"tom": "tom@gmail.com"}
print("存在的键:", mail_list["tom"])
print(mail_list["jerry"])   # 字典里没有 jerry 这个键！

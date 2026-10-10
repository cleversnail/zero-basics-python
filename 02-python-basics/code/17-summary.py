# 17-summary.py
# 第 17 讲 · 告别新手村：Python 编程基础知识（总结）
#
# 把本章学过的三块内容串一遍：变量、数据类型、输入输出。

# 1) 变量：给数据贴标签，随时可改
name = "小明"
print(name)
name = "小红"          # 变量的值可以改
print(name)

# 2) 数据类型：变量指向的数据有类型，用 type() 查看
age = 18               # 整数 int
height = 1.75          # 浮点数 float
city = "北京"          # 字符串 str
print(type(age))
print(type(height))
print(type(city))

# 3) 输入输出：input() 读入的是字符串，要参与计算需先转换
#    讲义写法是 age_str = input(...)，这里用固定值代替
age_str = "18"
age_num = int(age_str)
print(type(age_str))
print(type(age_num))

# 4) 字符串方法：类型自带常用方法，方便操作
print(city.startswith("北"))
print("a,b,c".split(","))

# 5) 用 f-string 把变量拼进一句话，输出最终结果
print(f"{name}今年{age}岁，身高{height}米，来自{city}。")

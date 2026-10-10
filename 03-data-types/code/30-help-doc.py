# 第 30 讲 · 内置数据类型参考：如何使用官方文档与帮助？

# help() 是「提醒式」帮助：把对象的用法直接打出来
help(str.count)

# 判断一个对象是不是「迭代器」
it = iter([1, 2, 3, 4])
print("it 的类型:", type(it))
print("it 有 __next__ 方法吗:", hasattr(it, "__next__"))
print("逐个取出元素:")
print(next(it))
print(next(it))

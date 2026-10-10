# 第 38 讲 · 避坑 2：遍历过程中修改列表，导致误操作
# 直接运行：python3 38-pitfalls-pop.py
# 本文件【故意触发错误】，会以 IndexError 退出，属于正常演示。

# 列表在执行 pop() 之后长度会减少，
# 而 range(len(list1)) 在一开始就按「原长度 4」定好了，
# 于是索引越走越界，最终报 IndexError。
list1 = ["a", "b", "c", "d"]
for i in range(len(list1)):
    list1.pop(i)

print(list1)

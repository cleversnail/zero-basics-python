# 第 38 讲 · 避坑 3：循环嵌套中的缩进，会让执行结果出现差别
# 直接运行：python3 38-pitfalls-indent.py

# 缩进决定了「这句话属于哪一层循环」：
#   与内层循环体对齐  → 内层、外层循环都会执行
#   与内层 while 对齐 → 每次外层循环执行一次
#   与外层 while 对齐 → 只在循环全部结束后执行一次

outer = 1
while outer <= 2:
    inner = 1
    while inner <= 2:
        print(f"内外层都执行：outer={outer}, inner={inner}")
        inner += 1
    print(f"只有外层每次执行一次：outer={outer}")
    outer += 1          # 别忘了让外层循环前进，否则会死循环

print("循环全部结束后才执行一次")

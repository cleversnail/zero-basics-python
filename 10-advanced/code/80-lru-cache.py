# -*- coding: utf-8 -*-
"""第 80 讲 · 怎样将已有算法改造成符合项目的特定算法？

本讲真跑。用斐波那契数列演示「算法改造」：
朴素的递归算法时间复杂度是 O(2^n)，非常慢；
加上 functools 的缓存装饰器（LRU 思想）后，复杂度降到 O(n)，速度天差地别。

运行：python3 80-lru-cache.py
"""
import time
from functools import lru_cache, cache


# ---------- 改造前：朴素递归，没有缓存 ----------
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


# ---------- 改造后：加上 lru_cache 装饰器，自动缓存结果 ----------
@lru_cache(maxsize=None)   # maxsize=None 表示缓存容量不设上限
def fib_cached(n):
    if n < 2:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)


# ---------- 用 functools.cache 更简洁（Python 3.9+，等价于 lru_cache(None)）----------
@cache
def fib_cache(n):
    if n < 2:
        return n
    return fib_cache(n - 1) + fib_cache(n - 2)


def timeit(func, n):
    start = time.perf_counter()
    result = func(n)
    cost = time.perf_counter() - start
    return result, cost


print("=" * 56)
print("朴素递归 vs 加缓存：同样的结果，完全不同的速度")
print("=" * 56)

n1 = 30
r1, t1 = timeit(fib, n1)
print(f"fib({n1})        无缓存 = {r1:>12}   耗时 {t1:.6f} 秒")

r2, t2 = timeit(fib_cached, n1)
print(f"fib_cached({n1}) 有缓存 = {r2:>12}   耗时 {t2:.6f} 秒")

# 加大到 n=40：有缓存依然是「瞬间」，无缓存则慢得无法接受（这里不跑，避免长时间等待）
r3, t3 = timeit(fib_cached, 40)
print(f"fib_cached(40)   有缓存 = {r3:>12}   耗时 {t3:.6f} 秒")

print()
print("结论：结果一样（fib(30)=832040），但复杂度从 O(2^n) 降到 O(n)。")


print()
print("=" * 50)
print("cache_info()：查看缓存命中情况")
print("=" * 50)
print("fib_cached 的缓存统计：", fib_cached.cache_info())
print("fib_cache  的缓存统计：", fib_cache.cache_info())


print()
print("=" * 50)
print("动手试一试：同一个参数，第二次调用直接返回缓存")
print("=" * 50)
_ = fib_cached(40)              # 再算一次 40
print("再算一次 fib_cached(40) 后：", fib_cached.cache_info())
print("可以看到 hits（命中）增加了，说明第二次直接从缓存返回，没有重复计算。")

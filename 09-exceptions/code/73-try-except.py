# -*- coding: utf-8 -*-
"""
第 73 讲 · 异常捕获：出现异常时，如何利用程序进行处理？

运行命令：python3 73-try-except.py

本讲要点：
  1. try-except 捕获异常；
  2. try-except-else-finally 实现更完整的流程控制；
  3. 一个 try 可以配多个 except，按「从上到下」匹配；
  4. try-except 可以嵌套。
"""
import os
import tempfile

print("=" * 56)
print("示例 1：最基本的 try-except")
print("=" * 56)
try:
    num = 1
    num2 = 0
    print("尝试计算 1 / 0 ...")
    print(num / num2)          # 这里会引发 ZeroDivisionError
except ZeroDivisionError as e:
    print("上一段程序有异常：", e)
print()

print("=" * 56)
print("示例 2：try-except-else-finally 完整流程")
print("=" * 56)


def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"  divide({a}, {b}) → except：{e}")
    else:
        # else：只有 try 里没出异常才会执行
        print(f"  divide({a}, {b}) → else ：结果 = {result}")
    finally:
        # finally：无论出不出异常，都会执行
        print(f"  divide({a}, {b}) → finally：这一段一定执行")


divide(10, 2)   # 正常：走 else + finally
divide(10, 0)   # 异常：走 except + finally
print()

print("=" * 56)
print("示例 3：捕获多个异常（多个 except，按顺序匹配）")
print("=" * 56)


def to_int(text):
    try:
        return int(text)
    except ValueError:
        print(f"  '{text}' 不是合法整数（ValueError）")
    except TypeError:
        print(f"  {text!r} 类型不对，无法转换（TypeError）")


for t in ["123", "abc", None]:
    r = to_int(t)
    if r is not None:
        print(f"  '{t}' 转换成功，结果是 {r}")
print()

print("=" * 56)
print("示例 4：嵌套 try-except")
print("=" * 56)
try:
    print("  外层 try 开始")
    try:
        print("  内层 try 开始")
        x = 1 / 0                  # 在内层引发异常
    except ZeroDivisionError as e:
        print("  内层捕获：", e)
    print("  内层处理完了，外层继续往下走")
except Exception as e:
    print("  外层捕获：", e)
print()

print("=" * 56)
print("示例 5：课后作业 —— 打开文件时的异常捕获")
print("=" * 56)


def read_file(path):
    """打开文件：出错时给出提示；无论如何都保证文件被关闭。"""
    f = None
    try:
        f = open(path, mode="r", encoding="utf-8")
        return f.readlines()
    except FileNotFoundError as e:
        return f"文件不存在，无法打开：{e.filename}"
    finally:
        # 只要文件打开过（f 不是 None），就一定关掉，防止数据丢失
        if f is not None:
            f.close()


with tempfile.TemporaryDirectory() as d:
    missing = os.path.join(d, "不存在的文件.txt")
    print("① 打开一个「不存在」的文件：")
    print("   ", read_file(missing))

    exist = os.path.join(d, "demo.txt")
    with open(exist, "w", encoding="utf-8") as w:
        w.write("你好，异常处理！\n第二行。\n")
    print("② 打开一个「存在」的文件（正常读取）：")
    print("   ", read_file(exist))

# -*- coding: utf-8 -*-
"""
第 72 讲 · 初识异常：异常的产生与分类

运行命令：python3 72-exceptions.py

本讲要点：
  1. 异常是「错误自动引发、且无法被解释器自动处理」的特殊对象；
  2. 引发异常时，所在代码块会中断；
  3. 异常有层次结构，写捕获时拿不准就用基类 Exception。

为了让脚本正常退出（exit=0），下面所有会报错的地方都用 try/except 包住了，
用 traceback 模块把真实的「栈回溯信息」打印出来给你看。
"""
import traceback

print("=" * 56)
print("示例 1：异常会让代码「中断」")
print("=" * 56)
print("第一行：程序开始")
try:
    # 1 / 0 会在这里引发 ZeroDivisionError（除零错误）
    result = 1 / 0
    print("这一行永远不会执行 —— 因为上面一行已经把代码块「中断」了")
except ZeroDivisionError as e:
    print(f"捕获到异常：{e}  （类型：{type(e).__name__}）")
print("最后一行：异常被处理后，程序还能继续往下走")
print()

print("=" * 56)
print("示例 2：未被处理的异常会打印「栈回溯（Traceback）」")
print("=" * 56)
num = 1
num2 = 0
try:
    num / num2
except Exception as e:
    print("上一段程序有异常")
    print(e)
    print("---- 完整栈回溯（真实报错长这样）----")
    print(traceback.format_exc())
print()

print("=" * 56)
print("示例 3：异常是「对象」")
print("=" * 56)
e = ZeroDivisionError("division by zero")
print("异常对象本身：", repr(e))
print("它的类型       ：", type(e))
print("转成字符串     ：", str(e))
print("是 BaseException 的实例？", isinstance(e, BaseException))
print("是 Exception 的实例？     ", isinstance(e, Exception))
print()

print("=" * 56)
print("示例 4：常见异常类型一览")
print("=" * 56)
samples = [
    ("除零",      lambda: 1 / 0),
    ("下标越界",  lambda: [1, 2, 3][5]),
    ("键不存在",  lambda: {"a": 1}["b"]),
    ("类型错误",  lambda: "abc" + 1),
    ("值错误",    lambda: int("abc")),
]
for name, fn in samples:
    try:
        fn()
    except Exception as exc:
        print(f"  {name:6s} → {type(exc).__name__}: {exc}")
print()

print("=" * 56)
print("示例 5：异常的层次结构（用 issubclass 验证）")
print("=" * 56)
pairs = [
    (ZeroDivisionError, ArithmeticError),
    (IndexError,        LookupError),
    (KeyError,          LookupError),
    (LookupError,       Exception),
    (ValueError,        Exception),
    (Exception,         BaseException),
]
for child, parent in pairs:
    print(f"  {child.__name__:18s} 是 {parent.__name__:15s} 的子类？ {issubclass(child, parent)}")
print("  SystemExit 是 Exception 的子类？   ", issubclass(SystemExit, Exception))
print("  SystemExit 是 BaseException 的子类？", issubclass(SystemExit, BaseException))
print()

print("=" * 56)
print("示例 6：FileNotFoundError 的继承链（MRO）")
print("=" * 56)
print(" -> ".join(cls.__name__ for cls in FileNotFoundError.__mro__))
print()

print("=" * 56)
print("示例 7：用 raise 主动引发一个异常")
print("=" * 56)
try:
    raise ValueError("value error !!!!")
except ValueError as exc:
    print("主动 raise 的异常被捕获：", exc)

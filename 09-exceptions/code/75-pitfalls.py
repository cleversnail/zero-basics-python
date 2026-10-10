# -*- coding: utf-8 -*-
"""
第 75 讲 · 避坑指南：编写捕获异常程序时经常出现的问题

运行命令：python3 75-pitfalls.py

本讲要点（PPT 归纳为四类坑）：
  1. 捕获位置设置不当 —— try 设得太晚，程序已经报错退出；
  2. 捕获范围设置不当 —— 一上来就用 Exception 基类，原因不明确；
  3. 捕获处理设置不当 —— 只 print 一句，不告知原因、不关闭文件；
  4. 嵌套 try-except 语法错误 —— try 与 except 必须成对出现。

本文件把所有「坑」都放在 try 里跑或演示成对比，因此可以正常退出（exit=0）。
第 4 类「语法错误」无法在运行时捕获，单独放在 75b-nested-syntax-error.py 里演示。
"""

print("=" * 56)
print("坑 1：捕获位置设置不当 —— try 设得太晚")
print("=" * 56)


def unprotected():
    """错误在 try 之前就抛出了，后面的 try 根本没机会接住。"""
    data = [1, 2, 3]
    print("  准备访问 data[5]（这里会出错）...")
    print(data[5])          # ← 错误在这里发生，程序当场中断
    try:
        pass
    except IndexError:
        print("  这句永远不会执行，因为陷阱设晚了")


try:
    unprotected()
except IndexError as e:
    print(f"  正确做法：把 try 设在错误发生之前，才能在错误处接住它 → {e}")
print()

print("=" * 56)
print("坑 2：捕获范围设置不当 —— 用 Exception 一把抓")
print("=" * 56)


def loose(items, index):
    # ❌ 反面：把所以异常都吞掉，连哪儿错了都看不出来
    try:
        total = 0
        for i in range(index + 1):
            total += items[i]
        return total
    except Exception as e:
        return f"出错了：{type(e).__name__}（太宽泛，看不出原因）"


def strict(items, index):
    # ✅ 正面：精确捕获 IndexError，其余异常照常暴露
    try:
        return sum(items[i] for i in range(index + 1))
    except IndexError as e:
        return f"精确捕获：IndexError: {e}"


print("  宽泛捕获结果：", loose([1, 2], 5))
print("  精确捕获结果：", strict([1, 2], 5))
print()

print("=" * 56)
print("坑 2b：except Exception 不会捕获 KeyboardInterrupt")
print("=" * 56)
try:
    try:
        raise KeyboardInterrupt()
    except Exception:
        print("  不该看到这行（Exception 抓不到 KeyboardInterrupt）")
except KeyboardInterrupt:
    print("  KeyboardInterrupt 穿透了 except Exception，被外层接住 —— ")
    print("  正因如此，不要写「裸」的 except:，否则连 Ctrl+C 都按不动")
print()

print("=" * 56)
print("坑 3：捕获处理设置不当 —— 只说「出错了」，不告知原因/不关文件")
print("=" * 56)


class FileMissingError(Exception):
    """把底层异常包装成更友好的业务提示。"""
    pass


def read_report(path):
    """好的处理方式：① 明确告知原因；② 保证文件被关闭。"""
    f = None
    try:
        f = open(path, encoding="utf-8")
        return f.read().strip()
    except FileNotFoundError:
        raise FileMissingError(f"找不到报表文件「{path}」，请先上传后再试")
    finally:
        if f is not None:
            f.close()


try:
    read_report("根本不存在的报表.txt")
except FileMissingError as e:
    print("  友好提示：", e)
print()

print("=" * 56)
print("坑 4：嵌套 try-except —— 正确的写法")
print("=" * 56)
# 语法错误（try 没配 except）会在「加载阶段」就被解释器拦下，无法用 try 捕获，
# 见 75b-nested-syntax-error.py。下面是语法正确的嵌套写法：
try:
    print("  外层 try")
    try:
        int("abc")
    except ValueError as e:
        print("  内层已处理：", e)
    print("  内层处理完，外层若无异常继续")
except Exception as e:
    print("  外层兜底：", e)
print()

print("小结：位置、范围、处理方式三处用错，是异常处理里最常见的错误；")
print("      嵌套时务必保证 try 与 except 成对出现，靠 IDE 的自动缩进/检查来避免语法错误。")

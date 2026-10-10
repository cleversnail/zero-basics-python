# -*- coding: utf-8 -*-
"""
第 74 讲 · 自定义异常捕获：如何定义业务异常？

运行命令：python3 74-custom-exception.py

本讲要点：
  1. 自定义异常必须继承 Exception（或它的子类）；
  2. 自定义异常用 raise 主动引发，用 except 捕获，可携带业务信息；
  3. with 语句是「语法糖」，背后靠上下文管理器的 __enter__ / __exit__ 实现。
"""
import os
import tempfile

print("=" * 56)
print("示例 1：定义一个最简单的业务异常")
print("=" * 56)


class NameForbiddenError(Exception):
    """业务异常：用户名不允许使用某些敏感词。"""

    def __init__(self, message):
        self.message = message
        super().__init__(message)      # 交给父类保存，便于 str(e) 输出

    @property
    def msg(self):
        return f"名字不允许使用「{self.message}」"


name = "jerry"
try:
    if name == "jerry":
        raise NameForbiddenError(name)
except NameForbiddenError as ne:
    print("捕获到自定义异常：", ne.msg)
    print("str(ne) 得到的原始信息：", str(ne))
print()

print("=" * 56)
print("示例 2：用自定义异常表达业务规则（银行取款）")
print("=" * 56)


class InsufficientBalanceError(Exception):
    """业务异常：余额不足。"""

    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        gap = amount - balance
        super().__init__(f"余额 {balance} 元，不足以取出 {amount} 元（还差 {gap} 元）")


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError(balance, amount)
    return balance - amount


for bal, amt in [(100, 30), (100, 250)]:
    try:
        rest = withdraw(bal, amt)
    except InsufficientBalanceError as e:
        print(f"  取款失败：{e}")
    else:
        print(f"  取款成功：余额 {bal} → {rest}")
print()

print("=" * 56)
print("示例 3：with 语句与上下文管理器（__enter__ / __exit__）")
print("=" * 56)


class MyClass:
    def __enter__(self):
        print("  __enter__ 被调用：进入 with 代码块，返回值交给 as 后面的变量")
        return self

    def __exit__(self, exc_type, exc_value, tb):
        print("  __exit__ 被调用：with 代码块结束（正常或异常都会走这里）")
        return False   # 返回 False：不吞异常，照常往外抛

    def hello(self):
        print("  hello() 被调用：我正在 with 代码块里工作")


with MyClass() as mc:
    mc.hello()
print()

print("=" * 56)
print("示例 4：__exit__ 如何收到 with 里的异常")
print("=" * 56)


class DemoCM:
    def __enter__(self):
        print("  进入 with")
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            print(f"  退出时发现异常：{exc_type.__name__}: {exc_value}")
        else:
            print("  正常退出")
        return True   # 返回 True：异常已被处理，不再向外抛出


with DemoCM():
    print("  准备 raise ...")
    raise ValueError("我在 with 里出错啦")
print("  程序没有崩溃，继续执行")
print()

print("=" * 56)
print("示例 5：with open(...) 自动关闭文件")
print("=" * 56)
with tempfile.TemporaryDirectory() as d:
    path = os.path.join(d, "note.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write("with 会在代码块结束后自动关闭文件，省去了手写 close()。\n")
    with open(path, encoding="utf-8") as f:
        print("  读到的内容：", f.readline().strip())
    print("  离开 with 后文件是否已关闭：", f.closed)
print()

print("=" * 56)
print("示例 6：课后作业 —— 文件过小则抛自定义异常")
print("=" * 56)


class FileTooSmallError(Exception):
    """自定义异常：文件内容太少。"""
    pass


def read_file(path, min_chars=10):
    with open(path, encoding="utf-8") as f:
        content = f.read()
    if len(content) < min_chars:
        raise FileTooSmallError(f"文件只有 {len(content)} 个字符，少于要求的 {min_chars} 个")
    return content


with tempfile.TemporaryDirectory() as d:
    small = os.path.join(d, "small.txt")
    big = os.path.join(d, "big.txt")
    with open(small, "w", encoding="utf-8") as f:
        f.write("太短")
    with open(big, "w", encoding="utf-8") as f:
        f.write("这是一个够长的文件内容，已经超过十个字符了。")

    for p in (small, big):
        try:
            print("  正常输出：", read_file(p))
        except FileTooSmallError as e:
            print(f"  抛出异常：{e}")

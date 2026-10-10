# -*- coding: utf-8 -*-
"""
第 76 讲 · 再回首：「异常处理」单元小结

运行命令：python3 76-summary.py

这是一个把本章知识点串起来的小程序：
  认识异常 → try-except 捕获 → 自定义业务异常 → 用 with 自动清理。
"""
import tempfile
import os

print("=" * 56)
print("单元小结：异常处理四步走")
print("=" * 56)

# 1) 自定义一个业务异常（继承 Exception）
class AgeTooSmallError(Exception):
    """业务异常：年龄不合法。"""


def check_age(age):
    # 2) 用 raise 主动引发异常，携带明确的业务信息
    if age < 0:
        raise AgeTooSmallError(f"年龄不能为负数，收到的是 {age}")
    return f"年龄 {age} 合法"


# 3) 用 try-except-finally 捕获并保证清理
print("\n[1] 捕获自定义异常 + finally 清理：")
for age in (18, -3):
    try:
        print("   ", check_age(age))
    except AgeTooSmallError as e:
        print("    捕获异常：", e)
    finally:
        print("    finally：不管成功失败，这一步都执行")

# 4) with 语句：范围越大越省心，自动关闭资源
print("\n[2] with 语句自动管理资源：")
with tempfile.TemporaryDirectory() as d:
    path = os.path.join(d, "summary.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write("用 with 打开文件，离开代码块就自动关闭。\n")
    with open(path, encoding="utf-8") as f:
        content = f.read().strip()
    print("    读取：", content)
    print("    文件已关闭？", f.closed)

# 5) 关键结论回顾
print("\n[3] 关键结论：")
print("    · 异常是错误自动引发、无法被解释器自动处理的特殊对象")
print("    · 拿不准要捕获什么，就用基类 Exception 兜底")
print("    · 自定义异常必须继承 Exception，用 raise 引发、except 捕获")
print("    · with 语句靠 __enter__ / __exit__ 实现，简化资源清理")
print("    · 捕获要「位置准、范围窄、处理明」，避免吞掉异常")

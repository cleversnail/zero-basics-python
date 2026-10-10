# -*- coding: utf-8 -*-
"""
第 40 讲 · 命令行参数（argparse）—— 非交互式输入

把参数直接写在命令后面，程序启动时就拿到，不用停下来等键盘。
    python3 40-args.py -number 100
    python3 40-args.py -number1 5 -number2 7
不写参数时，带 default 的用默认值，不带的则是 None。

argparse 需要 Python 3.2 以上版本（本机 3.12.7 完全支持）。
"""
import argparse

parser = argparse.ArgumentParser(description="这个程序用来演示命令行参数处理")

# 可选参数：名字前面带 -，不写时值为 None
parser.add_argument("-number", help="输入一个数字")

# 带类型转换和默认值的可选参数
parser.add_argument("-number1", type=int, default=10, help="第一个数字")
parser.add_argument("-number2", type=int, default=20, help="第二个数字")

# 解析参数；没有传参数时用默认值
args = parser.parse_args()

print(f"你输入的 number 参数是 {args.number}")
print(f"两数之和是 {args.number1 + args.number2}")

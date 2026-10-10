# -*- coding: utf-8 -*-
"""第 77 讲 · 扩展数据类型：怎样使用更复杂的数据类型？

本讲真跑。用 collections 模块里的四种扩展类型，弥补普通 list / dict / tuple 的不足：
namedtuple（命名元组）、deque（双端队列）、Counter（计数器）、UserDict / UserList（子类化）。

运行：python3 77-namedtuple.py
"""
from collections import namedtuple, deque, Counter, UserDict, UserList


print("=" * 50)
print("1. 命名元组 namedtuple —— 给每个位置起个名字")
print("=" * 50)

# 定义一个「点」，包含 x 和 y 两个坐标
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(11, y=22)

print("p1            =", p1)
print("p1.x          =", p1.x)          # 用名字取值
print("p1[0]         =", p1[0])         # 也可以用下标取值
print("p1.x == p1[0] =", p1.x == p1[0])  # 两种取法等价
print("p1 是元组吗   =", isinstance(p1, tuple))  # 它本身就是元组

# 命名元组不可变：像元组一样，一旦创建就不能改
try:
    p1.x = 99
except AttributeError as e:
    print("p1.x = 99 失败 ->", type(e).__name__, e)


print()
print("=" * 50)
print("2. 双端队列 deque —— 两端都能进出的队列")
print("=" * 50)

dq = deque([1, 2, 3])
dq.appendleft(0)   # 从左端加入
dq.append(4)       # 从右端加入
print("加入两端后    =", list(dq))

left = dq.popleft()  # 从左端弹出
right = dq.pop()     # 从右端弹出
print("popleft 弹出  =", left)
print("pop 弹出      =", right)
print("剩下          =", list(dq))


print()
print("=" * 50)
print("3. 计数器 Counter —— 统计元素出现次数")
print("=" * 50)

c = Counter("abracadabra")
print("统计结果      =", c)
print("出现最多的 2 个 =", c.most_common(2))
print("字母 a 出现   =", c["a"], "次")


print()
print("=" * 50)
print("4. 子类化 UserDict —— 给字典加规则")
print("=" * 50)


class MyDict(UserDict):
    """继承 UserDict，重写 __setitem__：遇到重复 key 就报错，不覆盖。"""

    def __setitem__(self, key, value):
        if key in self.data:
            print(f'赋值错误，key "{key}" 已存在，放弃赋值。')
        else:
            self.data[str(key)] = value


d = MyDict()
d['a'] = 1
d['a'] = 2            # 第二次给同一个 key 赋值 —— 被拦下
print("d['a'] 的值   =", d['a'])  # 仍然是 1，没被覆盖

# UserList 同理，可以给列表加自定义规则
class MyList(UserList):
    """只允许追加偶数。"""

    def append(self, item):
        if item % 2 == 0:
            super().append(item)
        else:
            print(f"{item} 是奇数，拒绝加入列表")


ml = MyList([2, 4])
ml.append(6)
ml.append(7)
print("MyList 内容   =", list(ml))

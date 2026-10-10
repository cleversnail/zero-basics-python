"""第 97 讲 · 如何扩展数据类型？

collections 是 Python 标准库，提供了几种「比内置 list / dict 更好用」的数据类型。
本讲全部真跑（纯标准库，不需要安装任何东西）：
    1. namedtuple  命名元组     —— 给元组的每个位置起名字
    2. deque       双端队列     —— 两端都能 O(1) 进出
    3. Counter     计数器       —— 数数神器
    4. defaultdict 默认字典      —— 取值不用先判断 key 在不在
    5. UserDict / UserList       —— 给字典、列表做「二次开发」

运行：python3 097-collections-demo.py
"""

from collections import namedtuple, deque, Counter, defaultdict, UserDict, UserList

print("=" * 48)
print("1) namedtuple：给元组的位置起名字")
print("=" * 48)

# 定义一个「点」，包含 x、y 两个坐标
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print("p       =", p)
print("p.x     =", p.x)          # 用名字取值，比 p[0] 可读
print("p.y     =", p.y)
print("p[0]    =", p[0])         # 依然可以像普通元组那样按下标取
print("它是元组吗？", isinstance(p, tuple))

print()
print("=" * 48)
print("2) deque：双端队列，左右两端都能进出")
print("=" * 48)

dq = deque("test_deq")           # 用字符串初始化，每个字符是一个元素
print("遍历 deque：")
for elements in dq:
    print("  ", elements)

# 双端队列比 list 多了 appendleft() / popleft()
dq.append("right")               # 右侧加
dq.appendleft("left")            # 左侧加（list 做不到）
print("append / appendleft 之后：", dq)

dq.pop()                         # 右侧弹出
dq.popleft()                     # 左侧弹出（list 做不到）
print("pop / popleft 之后：    ", dq)

# 一个实际用途：只用最后 3 个元素（固定长度）
recent = deque(maxlen=3)
for n in [1, 2, 3, 4, 5]:
    recent.append(n)
print("maxlen=3 只保留最后 3 个：", recent)

print()
print("=" * 48)
print("3) Counter：计数器，统计出现次数")
print("=" * 48)

cnt = Counter()
for word in ["red", "blue", "red", "green", "blue", "blue"]:
    cnt[word] += 1
print("cnt              =", cnt)
print("cnt['blue']      =", cnt["blue"])            # 直接按 key 取次数
print("most_common(2)   =", cnt.most_common(2))      # 出现最多的前 2 个

# Counter 还能直接把一个列表丢进去自动计数
c2 = Counter("abracadabra")
print("Counter('abracadabra') =", c2)

print()
print("=" * 48)
print("4) defaultdict：取值时 key 不存在也不报错")
print("=" * 48)

# 普通字典：key 不存在会 KeyError
normal = {}
# normal["a"].append(1)   # 这行会报 KeyError，所以要先 setdefault
normal.setdefault("a", []).append(1)
print("普通 dict 要 setdefault：", normal)

# defaultdict(list)：缺 key 时自动建一个空列表
dd = defaultdict(list)
dd["fruit"].append("apple")
dd["fruit"].append("banana")
dd["veggie"].append("carrot")
print("defaultdict(list)：", dict(dd))

# 也可以指定默认值为 int（默认 0）
counter = defaultdict(int)
for ch in "hello":
    counter[ch] += 1
print("defaultdict(int) 数数：", dict(counter))

print()
print("=" * 48)
print("5) UserDict / UserList：给字典、列表做二次开发")
print("=" * 48)


class UpperDict(UserDict):
    """一个「键自动变成大写」的字典"""

    def __setitem__(self, key, value):
        super().__setitem__(key.upper(), value)


ud = UpperDict()
ud["name"] = "Tom"
print("UpperDict：", dict(ud))
print("用大写键也能取到：", ud["NAME"])


class SumList(UserList):
    """在列表基础上加一个 total() 方法，边收集边求和"""

    def total(self):
        return sum(self.data)

sl = SumList([1, 2, 3])
sl.append(4)
print("SumList：", sl)
print("sl.total()：", sl.total())

print()
print("小结：需要「更像样」的容器时，先看 collections——namedtuple / deque / Counter /")
print("      defaultdict 能满足绝大多数扩展需求；真要改行为，再继承 UserDict / UserList。")

# -*- coding: utf-8 -*-
"""第 69 讲 · 第三方模块的使用：如何使用其他人编写的代码？

第三方模块 = 别人发布到 PyPI 上的包，用 pip 安装后才能 import。
本机已安装 requests、numpy，这里直接真跑。
"""
# ---------------------------------------------------------------
# 1. 第三方模块装好后，import 方式和标准库完全一样
# ---------------------------------------------------------------
import requests
import numpy as np

print("requests 版本:", requests.__version__)
print("numpy 版本:   ", np.__version__)

# ---------------------------------------------------------------
# 2. 用第三方模块 numpy 做一次真实计算
# ---------------------------------------------------------------
arr = np.array([1, 2, 3, 4, 5])
print("数组:   ", arr)
print("平均值: ", arr.mean())
print("每个元素的平方:", arr ** 2)
print("数组之和:", arr.sum())

# ---------------------------------------------------------------
# 3. 查看某个第三方包「装在哪、版本多少」
# ---------------------------------------------------------------
import importlib.metadata as md
print("numpy 包名:", md.distribution("numpy").metadata["Name"])
print("numpy 版本:", md.version("numpy"))
print("requests 版本:", md.version("requests"))

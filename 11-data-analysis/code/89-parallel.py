"""第 89 讲 · 理论盘点：任务的并行执行原理

本讲以讲解为主，这个脚本用标准库 concurrent.futures 真跑一遍，
让你亲眼看到：面对不同的任务类型，单进程 / 多线程 / 多进程 的耗时差别。

    任务 A（I/O 密集型）：大部分时间在「等」（比如等网络、等磁盘）—— threading 有效
    任务 B（CPU 密集型）：大部分时间在「算」——          multiprocessing 有效

运行：python3 89-parallel.py
"""

import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# ---------- 两个模拟任务 ----------

def io_task(n):
    """模拟一次网络请求：真实下载图片时，程序大部分时间都在等待。"""
    time.sleep(0.2)          # 睡 0.2 秒，代表「等待服务器响应」
    return n


def cpu_task(n):
    """模拟一次纯计算：占用 CPU 反复算，代表数据清洗/建模里的密集运算。"""
    total = 0
    for i in range(8_000_000):
        total += i * i
    return total


def timeit(label, func, tasks, workers=None):
    """统一计时的小工具：串行跑，或用线程池/进程池跑。"""
    start = time.perf_counter()
    if workers is None:                      # 串行：一个一个来
        for t in tasks:
            func(t)
    else:                                    # 并行：按指定并发数跑
        with workers as pool:
            list(pool.map(func, tasks))
    cost = time.perf_counter() - start
    print(f"{label:<28}{cost:.2f} 秒")
    return cost


if __name__ == "__main__":
    # Windows / macOS 用进程池时，必须把「真正执行」的代码放进 if __name__ == "__main__"
    io_tasks = list(range(6))
    cpu_tasks = list(range(6))

    print("任务 A（I/O 密集型，6 个任务，每个 sleep 0.2 秒）")
    timeit("  串行（一个接一个）", io_task, io_tasks)
    timeit("  多线程（4 线程池）", io_task, io_tasks,
           ThreadPoolExecutor(max_workers=4))
    timeit("  多进程（4 进程池）", io_task, io_tasks,
           ProcessPoolExecutor(max_workers=4))
    print("  => 结论：I/O 等待时线程能同时等待，多线程明显更快。")
    print()

    print("任务 B（CPU 密集型，6 个任务，每个反复做大量乘法）")
    timeit("  串行（一个接一个）", cpu_task, cpu_tasks)
    timeit("  多线程（4 线程池）", cpu_task, cpu_tasks,
           ThreadPoolExecutor(max_workers=4))
    timeit("  多进程（4 进程池）", cpu_task, cpu_tasks,
           ProcessPoolExecutor(max_workers=4))
    print("  => 结论：受 GIL 限制，多线程无法加速纯计算；多进程才能真正并行。")

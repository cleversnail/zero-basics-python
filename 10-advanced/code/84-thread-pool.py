# -*- coding: utf-8 -*-
"""第 84 讲 · 计算资源充足时，如何通过并行设计提高效率？

本讲真跑。并发（Concurrency）指宏观上多个任务同时推进；并行（Parallelism）指同一时刻
真的有多个任务在跑。这里用「线程池」把 6 个「耗时任务」并发执行，和「一个接一个地串行执行」对比。

⚠️ 为了不依赖网络，本示例把「下载网页」换成了 time.sleep 的模拟任务（等价于等待 I/O）。
   PPT 里的原始例子是并发访问 http://www.baidu.com，改动只在 load 函数内部。

运行：python3 84-thread-pool.py
"""
import time
from concurrent.futures import ThreadPoolExecutor, as_completed


# 6 个任务，每个「耗时」0.5 秒（模拟一次网络请求）
TASKS = [(1, 0.5), (2, 0.5), (3, 0.5), (4, 0.5), (5, 0.5), (6, 0.5)]
MAX_WORKERS = 2   # 线程池里最多同时跑 2 个线程


def load_page(task_id, seconds):
    """模拟一次耗时请求：睡一会儿，再返回「页面大小」。"""
    time.sleep(seconds)
    fake_page = f"page-{task_id}" * 100   # 假装是下载回来的内容
    return task_id, len(fake_page)


print("=" * 56)
print("1. 串行执行：一个任务做完再做下一个")
print("=" * 56)

start = time.perf_counter()
for task_id, seconds in TASKS:
    tid, size = load_page(task_id, seconds)
    print(f"  任务 {tid} 完成，页面大小 {size} 字节")
serial_cost = time.perf_counter() - start
print(f"串行总耗时：{serial_cost:.2f} 秒")


print()
print("=" * 56)
print(f"2. 并发执行：线程池，最多 {MAX_WORKERS} 个线程同时跑")
print("=" * 56)

start = time.perf_counter()
with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
    # submit() 把任务提交给线程池，返回一个 future（未来的结果）
    future_to_task = {
        executor.submit(load_page, task_id, seconds): task_id
        for task_id, seconds in TASKS
    }
    # as_completed：谁先做完就先处理谁
    for future in as_completed(future_to_task):
        task_id = future_to_task[future]
        try:
            tid, size = future.result()
        except Exception as exc:   # noqa: BLE001
            print(f"  任务 {task_id} 出错：{exc}")
        else:
            print(f"  任务 {tid} 完成，页面大小 {size} 字节")
parallel_cost = time.perf_counter() - start
print(f"并发总耗时：{parallel_cost:.2f} 秒")

print()
print(f"对比：串行 {serial_cost:.2f} 秒 -> 并发 {parallel_cost:.2f} 秒，"
      f"提速约 {serial_cost / parallel_cost:.1f} 倍。")

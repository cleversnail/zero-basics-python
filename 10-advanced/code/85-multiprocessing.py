# -*- coding: utf-8 -*-
"""第 85 讲 · 多进程间如何通信？

本讲真跑。多个进程各有各的内存，变量不能直接共享，需要用操作系统提供的机制交换数据。
本示例演示三种方式：
  1. Queue（队列）：一个进程放，另一个进程取
  2. Pipe（管道）：双向通道，两端都能 send / recv
  3. Pool（进程池）：把函数并发地跑在多核上

⚠️ macOS / Windows 上的多进程默认用 spawn 启动方式，进程会重新导入本模块，
   因此所有「创建进程」的代码都必须写在 if __name__ == '__main__': 里面，否则会无限重跑。

运行：python3 85-multiprocessing.py
"""
from multiprocessing import Process, Queue, Pipe, Pool


# ---------- 1. 队列 ----------
def producer(q, n):
    """生产者：把 1~n 依次放进队列，最后放一个 None 作为结束信号。"""
    for i in range(1, n + 1):
        q.put(i)
    q.put(None)   # 哨兵：告诉消费者「没有更多数据了」


def consumer(q):
    """消费者：不断从队列取值，能被 7 整除的就打印出来。"""
    while True:
        item = q.get()
        if item is None:      # 收到哨兵，结束
            break
        if item % 7 == 0:
            print(f"  消费者：{item} 能被 7 整除")


# ---------- 2. 管道 ----------
def child_process(conn):
    """子进程：先打个招呼，等父进程回复，再回一句。"""
    conn.send("你好，父进程")
    reply = conn.recv()
    conn.send(f"子进程收到：{reply}")
    conn.close()


# ---------- 3. 进程池 ----------
def square(x):
    return x * x


def main():
    print("=" * 50)
    print("1. Queue：一个进程产生 1~30，另一个进程挑出 7 的倍数")
    print("=" * 50)
    q = Queue()
    p_producer = Process(target=producer, args=(q, 30))
    p_consumer = Process(target=consumer, args=(q,))
    p_producer.start()
    p_consumer.start()
    p_producer.join()
    p_consumer.join()
    print("  队列通信结束。")

    print()
    print("=" * 50)
    print("2. Pipe：父子进程一来一回")
    print("=" * 50)
    parent_conn, child_conn = Pipe()   # 默认是双向管道
    p = Process(target=child_process, args=(child_conn,))
    p.start()
    print("  父进程收到：", parent_conn.recv())
    parent_conn.send("收到，合作愉快")
    print("  父进程再次收到：", parent_conn.recv())
    p.join()

    print()
    print("=" * 50)
    print("3. Pool：把 square 并发地跑在多个进程上")
    print("=" * 50)
    with Pool(4) as pool:   # 开 4 个进程
        results = pool.map(square, [1, 2, 3, 4, 5])
    print("  pool.map(square, [1,2,3,4,5]) =", results)


if __name__ == '__main__':
    main()

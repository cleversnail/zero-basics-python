# -*- coding: utf-8 -*-
"""第 82 讲 · Redis 数据库：怎样使用 NoSQL 数据库？

⚠️ 本节为说明，未实跑，因为本机没有运行 Redis 服务（也没有安装 redis-py 客户端）。
   为了不让脚本直接报错退出，下面做了「能连上就真跑、连不上就打印说明」的兜底处理。

要真正运行，需要两步：
  1. 安装 Python 客户端：  pip3 install redis
  2. 启动 Redis 服务，例如用 Docker：
        docker run -d -p 6379:6379 --name myredis redis
     启动后，再运行本脚本：  python3 82-redis.py

运行：python3 82-redis.py
"""
import sys


# 第一步：先看有没有装 redis-py
try:
    import redis
except ImportError:
    print("[未实跑] 本机没有安装 redis-py 客户端，无法连接 Redis。")
    print("         安装命令：pip3 install redis")
    sys.exit(0)


def demo(conn):
    """真正读写 Redis 的完整示例。"""
    # ---- 字符串 ----
    conn.set('name', 'Alice')
    print("读取 name        =", conn.get('name'))          # 返回 b'Alice'

    # ---- 字符串（带过期时间，单位秒）----
    conn.set('code', '8888', ex=60)
    print("读取 code        =", conn.get('code'))

    # ---- 哈希表：一个 key 下存多个字段 ----
    conn.hset('user:1', mapping={'name': 'Bob', 'age': 30})
    print("读取 user:1      =", conn.hgetall('user:1'))

    # ---- 列表：当简易消息队列用（顺序存储、顺序读取）----
    conn.rpush('jobs', 'job1', 'job2', 'job3')   # 从右端推入
    print("队列 jobs        =", conn.lrange('jobs', 0, -1))
    print("取出队首         =", conn.lpop('jobs'))          # 从左端弹出
    print("剩余 jobs        =", conn.lrange('jobs', 0, -1))

    # ---- 计数器：原子自增 ----
    conn.incr('visits')
    conn.incr('visits')
    print("访问计数 visits  =", conn.get('visits'))

    # 清理演示数据
    conn.delete('name', 'code', 'user:1', 'jobs', 'visits')
    print("演示数据已清理。")


def main():
    try:
        # 连接数据库：host, port, password, db
        conn = redis.Redis(host='localhost', port=6379, db=0,
                           socket_connect_timeout=2)
        conn.ping()   # 主动探活；连不上会抛异常
    except Exception as exc:   # noqa: BLE001
        print(f"[未实跑] 无法连接本机 Redis 服务（{type(exc).__name__}: {exc}）。")
        print("         启动 Redis 服务后，再运行本脚本即可真正读写。")
        return

    print("已连接 Redis，开始读写演示：")
    demo(conn)


if __name__ == '__main__':
    main()

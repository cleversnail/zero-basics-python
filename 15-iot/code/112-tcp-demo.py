#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第 112 讲 · TCP 协议演示：一个脚本里同时跑「服务端」和「客户端」。

场景：模拟物联网里的一台「温度传感器节点」（服务端）与一部「手机」
（客户端）通过 TCP 通信——手机问「现在几度？」，节点把温度读数回给它。

💡 为什么服务端和客户端写在一个文件里？
   真实物联网里，服务端和客户端是两块板子（或两台机器），要开两个终端分别运行。
   为了让文档里一条命令就能看到完整通信过程，这里用 threading 在后台线程里
   起服务端，主线程当客户端。脚本跑完会自动关闭，**不会常驻、不会卡住**。

运行：  python3 112-tcp-demo.py
"""
import socket
import threading
import time

HOST = "127.0.0.1"   # 回环地址：等价于「自己跟自己通信」，不依赖真实网络
PORT = 65432         # 端口号，取 >1024 的值可避免权限问题

# 模拟温度传感器的「连续读数」：每被问一次，就吐出一个新温度
READINGS = [25.3, 25.5, 25.4, 25.8, 26.1]

# 一个「信号灯」：服务端真正 listen 成功后点亮，客户端据此等待，避免抢跑
server_ready = threading.Event()


def sensor_server() -> None:
    """温度传感器节点（服务端）：监听端口，收到请求就回一个温度。"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
        # 端口复用：脚本反复运行时，避免「Address already in use」
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind((HOST, PORT))
        srv.listen()
        print(f"[传感器节点] 已启动，监听 {HOST}:{PORT}")
        server_ready.set()                     # 告诉客户端：可以连了

        # 一共只服务 len(READINGS) 次请求，然后退出
        for temp in READINGS:
            conn, addr = srv.accept()          # 阻塞，等客户端来连
            with conn:
                request = conn.recv(1024)      # 收客户端发来的请求
                print(f"[传感器节点] 收到来自 {addr[0]}:{addr[1]} 的请求：{request!r}")
                reply = str(temp).encode()     # 组装回复（bytes）
                conn.sendall(reply)            # 发回去
                print(f"[传感器节点] 已回复温度：{reply.decode()} °C")


def phone_client() -> None:
    """手机客户端：连上节点，发请求，打印收到的温度。"""
    if not server_ready.wait(timeout=5):       # 等服务端真正就绪
        raise RuntimeError("服务端启动超时")
    for i in range(len(READINGS)):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cli:
            cli.connect((HOST, PORT))          # 发起 TCP 连接（三次握手）
            cli.sendall(b"TEMP?")              # 发请求：字符串要 encode 成 bytes
            data = cli.recv(1024)              # 等回复
            print(f"[手机] 第 {i + 1} 次查询 → 收到 {data.decode()} °C")
            time.sleep(0.2)                    # 稍等，让日志顺序更好读


def main() -> None:
    # 后台线程起服务端
    server = threading.Thread(target=sensor_server, name="sensor-server")
    server.start()

    # 主线程当客户端，连上去问 5 次
    phone_client()

    server.join()                              # 等服务端线程收尾
    print("通信结束：服务端与客户端均已关闭（脚本未常驻）。")


if __name__ == "__main__":
    main()

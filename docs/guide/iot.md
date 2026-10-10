# 第 15 章 · 物联网（ESP32）

> 让一块小小的 ESP32 开发板连上 WiFi、读取温度、发到 MQTT 消息队列，
> 最终让 OLED 屏幕和手机远程同时显示室内温度。
> **本章 7 讲（111–117）**，讲清 TCP / 物模型 / 模组 / MicroPython / MQTT 与一次完整的端到端实践。

## 🎯 本章目标

- 说清**物联网与互联网**在连接方式和性能上的两点本质差异
- 看懂 **TCP 协议**的通信过程，并能用 Python `socket` 写一个完整演示
- 理解**物模型**（属性 / 事件 / 方法）和**模组**分别是什么
- 知道**为 ESP32 安装 MicroPython** 的完整烧录流程
- 理解 **MQTT 消息队列**里的「发布者 / 订阅者」模型与 QoS
- 认识 **DHT11 温湿度传感器 + SSD1306 OLED** 的接线与代码
- 把上面这些拼成完整案例：**温度本地显示 + 远程上报手机**

**本章代码**

> 📌 **代码约定**：正文代码块都保持**可直接运行**；节选会明确标注「节选」并指向 `code/` 完整文件。
> 所有输出都是**真实运行结果**。
>
> ⚠️ **真跑说明**：本章只有第 112 讲的 TCP 演示是**纯 Python 标准库**、能在本机真跑；
> 第 114 / 115 / 116 讲的代码**都需要 ESP32 开发板 + MicroPython 环境**，属于硬件相关，
> **本节全程「未实跑」**——代码给完整，但**没有**在本机运行过。

| 文件 | 内容 |
| --- | --- |
| `code/112-tcp-demo.py` | ✅ 可跑：单个脚本内起「温度传感器服务端 + 手机客户端」演示 TCP 通信 |
| `code/esp32/boot.py` | ⚠️ 未实跑：ESP32 开机自动执行，连 WiFi 后加载主程序 |
| `code/esp32/wifi.py` | ⚠️ 未实跑：连接 WiFi 的 `do_connect()` |
| `code/esp32/mqtt_pub.py` | ⚠️ 未实跑：MQTT 发布者，往主题发一条消息 |
| `code/esp32/mqtt_sub.py` | ⚠️ 未实跑：MQTT 订阅者，订阅并回调处理消息 |
| `code/esp32/geek.py` | ⚠️ 未实跑：综合案例，DHT11 读温度 + OLED 显示 + MQTT 上报 |
| `code/esp32/ssd1306.py` | ⚠️ 未实跑：SSD1306 OLED 驱动（MicroPython 库） |
| `code/esp32/lib/umqtt/simple.py` | ⚠️ 未实跑：`umqtt.simple`，MicroPython 的 MQTT 客户端库 |

---

## 第 111 讲 · 聚焦异同：物联网与互联网有啥不一样？

### 本节目标

用两个差异（**连接方式**、**性能**）说清物联网和传统互联网到底不一样在哪。

### 知识要点

**1. 连接方式的差异：从「人-机交互」到「机-机交互」**

- **传统互联网**体现的是 **人-机交互**：人负责输入（打字、点按）和接收机器输出（屏幕、声音），机器负责计算。
- **物联网**结构下，**设备自己也能产生数据、接收数据**——也就是说设备本身也完成了输入输出。

物联网设备主要分两类：

| 类型 | 作用 | 例子 |
| --- | --- | --- |
| **传感器类**（产生数据 / 输入） | 接收来自外界的数据 | 温度传感器、位置传感器、激光雷达、相机 |
| **执行器类**（接收数据 / 输出） | 接收用户指令，完成特定动作 | 马达、机械臂、舵机 |

**2. 性能的差异：终端弱，服务器强**

- 传统互联网里，**服务器**的性能通常都比个人终端强，处理能力强劲。
- 物联网**终端设备性能有限**（芯片小、内存小、耗电受限），往往需要 **边缘设备（边缘计算服务器）或中心服务器**配合，把数据传上去集中处理。

> 💡 一句话记法：互联网是「人 ↔ 机器」，物联网是「人 ↔ 机器 ↔ **设备**」，
> 设备既是数据的**来源**，也是指令的**归宿**；而设备太弱，算力得「外包」给云。

### 代码实操

本讲是概念对比，**无需运行代码**。请对照上表和下面的示意图理解两级结构：

```text
物联网分层（自下而上）

  [设备端]  传感器 / 执行器  —— 产生或接收数据，算力有限
      │           （温度、马达、相机……）
      ▼
  [边缘/中心服务器]  负责集中计算、存储、转发
      │
      ▼
  [应用端]  手机 App / 网页  —— 人在这里看数据、发指令
```

### 课后作业

请说出至少 **3 种**你接触过的物联网设备，并说明它们是**能够产生数据**还是**能够接收数据执行任务**。

> 参考答案（任选 3 个即可）：
> 1. **智能手环**——产生数据（心率、步数）。
> 2. **智能音箱**——两者都有：产生数据（录音、环境音量），也接收数据（播放指令）。
> 3. **共享单车智能锁**——两者都有：产生数据（定位、开锁状态），也接收数据（远程开锁指令）。
> 4. **智能插座**——两者都有：产生数据（当前功率），也接收数据（远程通断电）。

---

## 第 112 讲 · 理论盘点：基础但不简单的 TCP 协议

### 本节目标

理解为什么物联网常用 TCP，看懂 TCP 的通信过程，并用 Python `socket` 亲手跑通一次完整通信。

### 知识要点

**1. 物联网通信为何常用 TCP 协议**

- TCP 比 HTTP **更简洁**：在轻量级设备上占用更少资源、消耗更低带宽。
  （HTTP 是建立在 TCP 之上的「应用层协议」，用它要额外带一堆请求头 / 状态码，对单片机是负担。）
- TCP 是**可靠协议**：能确保设备**真的执行了**用户的指令。
- 有时为了更轻量，会采用 **UDP + 自行编写校验**来实现可靠通信（自己造一个更省内存的「TCP」）。

**2. TCP 协议概述**

TCP（传输控制协议）是**面向连接**的：通信前要先「建立连接」，就像打电话要先拨号接通。

```text
客户端                          服务端
  │        ① SYN（我要连你）
  │  ─────────────────────────►
  │        ② SYN + ACK（收到，我也连你）
  │  ◄─────────────────────────
  │        ③ ACK（确认，连接建立）
  │  ─────────────────────────►
  │                              ← 这一步叫「三次握手」
  │  ───── 数据收发（可靠、有序）─────►
  │        ④ FIN / ACK（挥手断开）
  │  ◄─────────────────────────►
```

- **三次握手**：建立连接要来回三次，双方都确认「对方在、我要连」才继续。
- **可靠**：每个数据包都要被确认，丢了会重传，所以「指令一定送到」。
- **有序**：数据按发送顺序到达，不会乱序。

> 📌 记住：**TCP 是物联网通信最常用的协议**。掌握它的通信过程，你才能写出更高效的设备控制程序。

### 代码实操

下面这个脚本把「服务端」和「客户端」放进**同一个文件**：用 `threading` 在后台线程起服务端，
主线程当客户端，**一次 `python3` 就能看到完整通信过程**，跑完自动关闭、不会常驻。

对应文件：`code/112-tcp-demo.py`（完整代码如下）。

```python
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


def sensor_server() -> None:
    """温度传感器节点（服务端）：监听端口，收到请求就回一个温度。"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
        # 端口复用：脚本反复运行时，避免「Address already in use」
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind((HOST, PORT))
        srv.listen()
        print(f"[传感器节点] 已启动，监听 {HOST}:{PORT}")

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
    time.sleep(0.3)                            # 等后台线程把服务端先起来
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
```

在 `code/` 目录里运行：

```bash
$ cd code
$ python3 112-tcp-demo.py
```

**本机实测输出（Python 3.12.7）**：

```text
[传感器节点] 已启动，监听 127.0.0.1:65432
[传感器节点] 收到来自 127.0.0.1:63596 的请求：b'TEMP?'
[传感器节点] 已回复温度：25.3 °C
[手机] 第 1 次查询 → 收到 25.3 °C
[传感器节点] 收到来自 127.0.0.1:63597 的请求：b'TEMP?'
[传感器节点] 已回复温度：25.5 °C
[手机] 第 2 次查询 → 收到 25.5 °C
[传感器节点] 收到来自 127.0.0.1:63598 的请求：b'TEMP?'
[传感器节点] 已回复温度：25.4 °C
[手机] 第 3 次查询 → 收到 25.4 °C
[传感器节点] 收到来自 127.0.0.1:63599 的请求：b'TEMP?'
[传感器节点] 已回复温度：25.8 °C
[手机] 第 4 次查询 → 收到 25.8 °C
[传感器节点] 收到来自 127.0.0.1:63600 的请求：b'TEMP?'
[传感器节点] 已回复温度：26.1 °C
[手机] 第 5 次查询 → 收到 26.1 °C
通信结束：服务端与客户端均已关闭（脚本未常驻）。
```

> 📌 说明：上面那串 `127.0.0.1:63427` 是客户端**用到的临时端口**，每次运行都会变；
> 但「问 5 次、拿到 5 个温度的**内容**」是完全一样、可复现的。
> 温度值 `25.3 → 26.1` 是代码里写死的 `READINGS`，所以结果确定，不依赖真实网络。

### 课后作业

参照 Python 官方文档关于 `socket` 库的示例，实现**两个程序**通过 TCP 协议简单通信。
官方文档：<https://docs.python.org/zh-cn/3.10/library/socket.html#example>

> 参考做法：官方示例是**两个独立文件**（`echo_server.py` + `echo_client.py`），要开**两个终端**分别运行。
> 把上面的单文件版本拆成两个文件即可，关键差别是——服务端不再被线程包着，而是自己 `srv.accept()` 常驻等待：
>
> ```python
> # echo_server.py（服务端，在终端 A 运行）
> import socket
> HOST, PORT = "127.0.0.1", 65432
> with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
>     srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
>     srv.bind((HOST, PORT))
>     srv.listen()
>     print(f"服务端监听 {HOST}:{PORT}")
>     conn, addr = srv.accept()
>     with conn:
>         print("已连接：", addr)
>         while True:
>             data = conn.recv(1024)
>             if not data:
>                 break
>             print("收到：", data)
>             conn.sendall(b"echo: " + data)   # 原样回显
> ```
>
> ```python
> # echo_client.py（客户端，在终端 B 运行）
> import socket
> HOST, PORT = "127.0.0.1", 65432
> with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cli:
>     cli.connect((HOST, PORT))
>     cli.sendall(b"hello iot")
>     data = cli.recv(1024)
>     print("收到回显：", data)
> ```
>
> 这两份是「需要开两个终端、服务端常驻」的版本，**本机未作为示例运行**（会和 `112-tcp-demo.py` 单文件版重复）；
> 想体验就把上面两段各自存成文件、开两个终端跑。

---

## 第 113 讲 · 理论盘点：物模型与模组

### 本节目标

搞懂**物模型**（用数据描述设备）和**模组**（芯片 + 周边硬件的封装）这两个物联网核心概念。

### 知识要点

**1. 怎样通过物模型定义智能设备**

**物模型**是「把设备抽象成数据的模板」——它不关心设备长什么样，只关心它**有哪些数据、能做什么事**。
（这和我们学过的 **Django Template** 思路异曲同工：都是「模板 + 填充」。）

物模型包含 **三类**内容：

| 种类 | 含义 | 举例（以智能风扇为例） |
| --- | --- | --- |
| **属性（Property）** | 设备「现在是什么状态」（可读可写的数据） | 当前档位、是否开机、风速 |
| **事件（Event）** | 设备运行过程中产生的**信息或故障** | 过热告警、电机堵转 |
| **方法 / 动作（Method / Action）** | 设备**执行的某个动作**（下发指令） | 开机、关机、调到 3 档、摇头 |

为了体现**扩展性**，物模型一般采用 **JSON 格式**定义（谁都能读写，加字段不影响老系统）。

**2. 像搭积木一样掌握模组**

- **物联网芯片**负责设备通信和 **IO 接口**的管理。
- 为了便于使用，通常把**芯片和周边硬件**（天线、晶振、Flash、电源管理…）组合成一个**模组**。
- 好处：**不必从零开发**——买一块模组就是「搭好的一块积木」，直接写代码即可。

> 💡 类比：物模型是「说明书/表格」（这台设备能干嘛），模组是「现成的积木块」（硬件封装好），
> 两个合起来，才能既统一描述、又快速落地。

### 代码实操

本讲是概念讲解，**无需运行代码**。下面给出一个**智能风扇的物模型 JSON**示例（说明「物模型长什么样」）：

```json
{
  "productKey": "smart-fan-001",
  "name": "智能电风扇",
  "properties": [
    { "identifier": "power", "name": "开关", "type": "bool", "access": "rw" },
    { "identifier": "speed", "name": "风速档位", "type": "int", "min": 1, "max": 5, "access": "rw" },
    { "identifier": "temperature", "name": "环境温度", "type": "float", "unit": "℃", "access": "r" }
  ],
  "events": [
    { "identifier": "overheat", "name": "过热告警", "type": "alert" }
  ],
  "methods": [
    { "identifier": "turn_on", "name": "开机" },
    { "identifier": "turn_off", "name": "关机" },
    { "identifier": "oscillate", "name": "摇头", "input": { "on": "bool" } }
  ]
}
```

> ⚠️ 这段 JSON 是**物模型的定义示例**（对应本讲课后作业的思路），**不是**要运行的代码，故标注「未实跑」。

### 课后作业

请你使用这节课我们学习的物模型，尝试为**智能电风扇**定义一个物模型。

> 参考答案就在上面的 JSON 里，核心是**三块分开写清楚**：
> ① `properties`（开关、档位、温度——「它是什么状态」）；
> ② `events`（过热告警——「它运行中会冒出什么」）；
> ③ `methods`（开机、关机、摇头——「它肯执行什么动作」）。
> 能把这三点分门别类写出来，物模型就达标了。

---

## 第 114 讲 · 如何为 ESP32 安装 MicroPython？

### 本节目标

认识 ESP32-DevKitC 开发板，知道 MicroPython 是什么，并掌握**把它烧录进 ESP32** 的完整流程。

### 知识要点

**1. ESP32 开发板简介**

- 为便于验证，课程使用外设丰富的 **ESP32-DevKitC** 开发板做模组选型。
- ESP32 有 **4MB Flash** 存储空间，支持 **WiFi、蓝牙**等常见通信方式。
  - **Flash** = 板子上的「硬盘」，断电不丢数据，烧进去的 MicroPython 固件和你写的代码都放这儿。

**2. 安装 MicroPython**

- **MicroPython** 是**专门为硬件开发实现的 Python 版本**。
- 它可以使用 **Python 的大部分语法**，并**额外支持了丰富的硬件相关库**（如 `machine`、`network`、`dht`）。
- 装法：把固件 `.bin` 文件**烧录**到 ESP32 的 Flash 里。

**烧录命令**：

```bash
esptool.py --chip esp32 --port /dev/tty.usbserial-110 --baud 460800 \
    write_flash -z 0x1000 esp32-20220618-v1.19.1.bin
```

参数逐个说明：

| 参数 | 含义 |
| --- | --- |
| `esptool.py` | 烧录工具（`pip install esptool` 安装） |
| `--chip esp32` | 目标芯片是 ESP32 |
| `--port /dev/tty.usbserial-110` | 串口设备名。**macOS** 是 `/dev/tty.usbserial-*`；**Windows** 是 `COM3` 之类；**Linux** 是 `/dev/ttyUSB0` |
| `--baud 460800` | 串口波特率（越高越快，460800 是常用高速值） |
| `write_flash` | 写固件模式 |
| `-z` | 写之前先压缩，省时间 |
| `0x1000` | 写入的起始地址（ESP32 固件约定从 `0x1000` 开始） |
| `esp32-20220618-v1.19.1.bin` | 你下载的 MicroPython 固件文件名 |

> ⚠️ **本节全程「未实跑」**：烧录需要一块**真实的 ESP32 开发板**和串口线，本机没有硬件，
> 所以下面的代码与命令都只做讲解，**没有运行过**。你只有拿到板子后才需要照做。
>
> 💡 **动手顺序**：装 `esptool` → 查串口名（macOS：`ls /dev/tty.usbserial*`）→ 下载固件 → 敲上面的命令 → 用
> `screen /dev/tty.usbserial-110 115200`（或 `mpremote`、Thonny）连上板子，看到 `>>>` 就成功了。

### 代码实操

ESP32 上电后会自动执行 `boot.py`，它把「连 WiFi」和「加载主程序」串起来。
对应文件：`code/esp32/boot.py` 与 `code/esp32/wifi.py`。

**`code/esp32/boot.py`**（开机自执行入口）：

```python
# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

# import time


# import onoff
# import ap
# 
# wifiInfo = ap.readWifiFromFile()
# ap.doConnect(wifiInfo)
# 
# import pwm_map_pwm
#
import wifi
import geek
```

**`code/esp32/wifi.py`**（连接 WiFi）：

```python
def do_connect():
    import network 
    wifi = network.WLAN(network.STA_IF)  
    if not wifi.isconnected(): #判断WIFI连接状态
        print('connecting to network...')
        wifi.active(True) 
        wifi.connect('ssid', 'pass') #essid为WIFI名称,password为WIFI密码
        while not wifi.isconnected():
            pass 
    print('network config:', wifi.ifconfig())

do_connect()
```

> ⚠️ **未实跑**：`wifi.py` 里 `import network` 是 **MicroPython** 专有库，桌面版 Python 里不存在，
> 直接在本机 `python3 wifi.py` 会报 `ModuleNotFoundError: No module named 'network'`。
> 把 `'ssid'` / `'pass'` 换成你家的 WiFi 名称与密码后，随代码一起拷到板子上才会生效。

### 课后作业

请你将 MicroPython 烧录到 ESP32 开发板，并通过终端连接到开发板。

> 参考步骤（**未实跑**，需硬件）：
> 1. `pip install esptool`
> 2. macOS 下 `ls /dev/tty.usbserial*` 找到串口名（如 `/dev/tty.usbserial-110`）
> 3. 下载固件，如 `esp32-20220618-v1.19.1.bin`
> 4. 执行本讲给出的 `esptool.py` 烧录命令（参数含义见上面的表格）
> 5. 用 `screen /dev/tty.usbserial-110 115200` 连上，看到 `>>>` 提示符即成功

---

## 第 115 讲 · 怎样通过 MQTT 协议构建消息队列？

### 本节目标

理解消息队列在物联网中的作用，搞懂 MQTT 的「发布/订阅」模型，并看懂发布者与订阅者代码。

### 知识要点

**1. 消息队列在物联网开发中的用途**

- **队列机制为设备并发提供了有效的缓存**：设备一多、消息一涌，先用队列存起来，慢慢处理，不丢不乱。
- 消息队列使用**生产者-消费者设计模式**，两大角色是 **订阅者（Subscriber）** 和 **发布者（Publisher）**：
  - **发布者**：往某个「主题（Topic）」发消息（如：温度节点把 25.3 发到 `foo_topic`）。
  - **订阅者**：订阅这个主题，一有新消息就**被回调**处理（如：手机 App 收到温度就显示）。

| 角色 | 干什么 | 类比 |
| --- | --- | --- |
| 发布者 Publisher | 往主题里「发」消息 | 广播电台 |
| 订阅者 Subscriber | 订阅主题，「收」消息 | 打开收音机听某个频道 |
| 主题 Topic | 消息的分类频道 | 电台频率，如 `foo_topic` |

**2. 使用消息队列实现数据通信**

- 物联网中经常用 **MQTT 协议**实现消息队列。
- 目前 MQTT 协议最新版本为 **5.0**，典型的 **EMQX**、**HBMQTT** 等都能完整支持。
- 消息队列服务器除了保证消息**及时、稳定**，还在 MQTT 协议基础上提供 **QoS、权限验证**等基础服务。
  - **QoS（服务质量）**：0 = 最多一次，1 = 至少一次，2 = 恰好一次——按可靠性需求选。

> 💡 为什么用「队列」而不是让设备直接点对点连？因为设备数量多、并发高，**队列做缓冲 + 的发布订阅做解耦**，
> 发布者不需要知道谁在听，订阅者也不需要知道谁发的，系统才好扩展。

### 代码实操

ESP32 上跑 MQTT 靠的是 `umqtt.simple` 这个 MicroPython 库。下面两个文件分别是**发布者**和**订阅者**。

**`code/esp32/mqtt_pub.py`**（发布者：连服务器，往 `foo_topic` 发一条 `hello`）：

```python
# https://github.com/micropython/micropython-lib/tree/master/micropython/umqtt.simple

from umqtt.simple import MQTTClient

server = "broker-cn.emqx.io" 
c = MQTTClient("umqtt_client", server)
c.connect()
c.publish(b"foo_topic", b"hello")
c.disconnect()
```

**`code/esp32/mqtt_sub.py`**（订阅者：订阅 `foo_topic`，收到消息就回调打印）：

```python


import time
from umqtt.simple import MQTTClient

# Publish test messages e.g. with:
# mosquitto_pub -t foo_topic -m hello

# Received messages from subscriptions will be delivered to this callback
def sub_cb(topic, msg):
    print((topic, msg))


def main(server="broker-cn.emqx.io"):
    c = MQTTClient("umqtt_client", server)
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(b"foo_topic")
    while True:
        if True:
            # Blocking wait for message
            c.wait_msg()
        else:
            # Non-blocking wait for message
            c.check_msg()
            # Then need to sleep to avoid 100% CPU usage (in a real
            # app other useful actions would be performed instead)
            time.sleep(1)

    c.disconnect()
```

> ⚠️ **未实跑**：这两段依赖 **MicroPython 的 `umqtt.simple` 库**和网络，**只能烧到 ESP32 上运行**，
> 本机 `python3` 会因 `No module named 'umqtt'` 直接失败。
>
> 📌 代码里用的公共测试 broker 是 **`broker-cn.emqx.io`**（EMQX 官方免费测试服务器，端口 1883）。
> 想本地自建，可用 Docker 一键起一个：
>
> ```bash
> docker run --rm -it -p 1883:1883 -p 8083:8083 -p 8883:8883 emqx/emqx:5.0.0
> ```
>
> 起好后把代码里的 `server` 改成你自己电脑的局域网 IP 即可（设备需要在同一网络）。

### 课后作业

请你使用 MQTT 协议，实现客户端和服务端通信。（服务端可采用 EMQX、HBMQTT 等 MQTT 服务端实现）

> 参考思路（**未实跑**）：先起一个 MQTT broker（EMQX / Docker 如上），
> 再让两个客户端一个当发布者、一个当订阅者：
> 用 `code/esp32/mqtt_pub.py` 发 `foo_topic`，用 `code/esp32/mqtt_sub.py` 订阅 `foo_topic`，
> 订阅端就会打印出 `(b'foo_topic', b'hello')`。本地没有硬件时，也可以用 `mosquitto_pub -t foo_topic -m hello` 模拟发布。

---

## 第 116 讲 · 小试牛刀：在 OLED 屏幕和手机远程同时显示室内温度

### 本节目标

把前几讲拼成完整案例：ESP32 读 **DHT11** 温度 → **本地显示在 SSD1306 OLED** → 同时**通过 MQTT 上报手机**。

### 知识要点

**1. 开发基于 MQTT 协议的订阅者**

给 ESP32 联网、连 MQTT 服务器的骨架（对应本讲代码里的片段）：

```python
# 为设备联网
import network
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect(ssid, pwd)

# 订阅 MQTT 服务器
from umqtt.simple import MQTTClient
mqtt_client = MQTTClient(服务器信息)
mqtt_client.set_callback(mqtt_callback)   # 订阅并编写（回调）处理逻辑
mqtt_client.connect()
```

**2. 使用 MicroPython 控制 IO 引脚**

用 `machine.Pin` 控制引脚（IO = 输入输出引脚，接传感器 / 屏幕 / 舵机）：

```python
from machine import Pin
self.pin = Pin(引脚编号, Pin.OUT)
```

**DHT11 温湿度传感器**：

- 一款**已校准数字信号输出**的温湿度传感器。
- 精度：湿度 ±5%RH，温度 ±2°C；量程：湿度 5~95%RH，温度 -20~+60°C。

```python
import dht
d = dht.DHT11(dht11_pin)
d.measure()          # 触发一次测量
d.temperature()      # 读温度（℃）
```

**把温度显示在 OLED 屏幕（SSD1306）上**：

```python
from ssd1306 import SSD1306_I2C
i2c = machine.SoftI2C(scl=machine.Pin(18), sda=machine.Pin(19))
oled = SSD1306_I2C(128, 64, i2c, addr=60)
oled.text('Hello World', 0, 20)
oled.show()
```

> ⚠️ **关键提醒**：温度传感器有多个引脚（VCC / GND / DATA），**接线时注意顺序，千万不要把 VCC 和 GND 反接**，
> 否则可能烧坏传感器或开发板。

### 代码实操

综合案例对应文件：`code/esp32/geek.py`（主程序）与 `code/esp32/ssd1306.py`（OLED 驱动库）。

**`code/esp32/geek.py`**（读 DHT11 + 显 OLED + 发 MQTT）：

```python
import dht
import machine
from time import sleep

from ssd1306 import SSD1306_I2C

from umqtt.simple import MQTTClient


dht11_data = machine.Pin(5)
d = dht.DHT11(dht11_data)


i2c = machine.SoftI2C(scl=machine.Pin(7), sda=machine.Pin(8))
# print(i2c.scan()) # 从机地址60

oled = SSD1306_I2C(128, 64, i2c, addr=60)

# oled.text('Hello World', 0, 20)
# oled.show()

fonts= {
    "温": [0x0F,0x88,0x4F,0x08,0x0F,0x80,0x5F,0x15,0x35,0x55,0x95,0x3F,0x80,0x80,0x80,0x80,0x80,0x00,0xC0,0x40,0x40,0x40,0x40,0xE0],
    "度": [0x02,0x7F,0x48,0x7F,0x48,0x4F,0x40,0x5F,0x48,0x44,0x43,0x9C,0x00,0xE0,0x80,0xE0,0x80,0x80,0x00,0xC0,0x40,0x80,0x00,0xE0],
}

def chinese(ch_str, x_axis, y_axis, ch_size=12):
    ''' 刷单字到屏幕像素点
    Args:
        ch_str  单字或连接汉字
        x_axis,y_axis  定位点
        ch_size  单字大小，默认12，最大16
    '''
    global oled
    offset_ = 0
    for k in ch_str:
        byte_data = fonts[k]
        print(fonts[k], "offset=", offset_)
        for y in range(0, ch_size):
            # 进制转换、补全
            a_ = '{:0>8b}'.format(byte_data[y])
            b_ = '{:0>8b}'.format(byte_data[y+ch_size])
            # 绘制像素点 （按取模软件的行列式方式）
            for x in range(0, 8):
                oled.pixel(x_axis + offset_ + x, y + y_axis, int(a_[x]))
                oled.pixel(x_axis + offset_ + x + 8, y + y_axis, int(b_[x]))
        offset_ += ch_size


# 20ms周期 50hz
# 0.5ms 为0度
# 2.5ms为180度依次增加

sg90 = machine.PWM(machine.Pin(2),freq=50, duty=0)


server = "broker-cn.emqx.io" 
c = MQTTClient("umqtt_client", server)
c.connect()



while True:
    d.measure()
    temp = d.temperature()
    print(f'temperature is {temp} °C')
    oled.fill(0)
    chinese('温度',0,20)
    oled.text(f'{d.temperature(temp)} ', 32, 20)
    chinese('度', 64, 20)
    oled.show()
    c.publish(b"foo_topic", temp)
    sleep(2)
    sg90.duty(70)



c.disconnect()
```

**`code/esp32/ssd1306.py`** 是 Adafruit 写的 SSD1306 OLED 驱动（MicroPython 版），
提供 `SSD1306_I2C` 类，负责把文字 / 像素刷到屏幕。完整约 160 行，下面给出**节选**
（接口与关键初始化部分，完整文件见 `code/esp32/ssd1306.py`）：

```python
#MicroPython SSD1306 OLED driver, I2C and SPI interfaces created by Adafruit

import time
import framebuf

# register definitions
SET_CONTRAST        = const(0x81)
SET_ENTIRE_ON       = const(0xa4)
SET_NORM_INV        = const(0xa6)
SET_DISP            = const(0xae)
SET_MEM_ADDR        = const(0x20)
SET_COL_ADDR        = const(0x21)
SET_PAGE_ADDR       = const(0x22)
SET_DISP_START_LINE = const(0x40)
SET_SEG_REMAP       = const(0xa0)
SET_MUX_RATIO       = const(0xa8)
SET_COM_OUT_DIR     = const(0xc0)
SET_DISP_OFFSET     = const(0xd3)
SET_COM_PIN_CFG     = const(0xda)
SET_DISP_CLK_DIV    = const(0xd5)
SET_PRECHARGE       = const(0xd9)
SET_VCOM_DESEL      = const(0xdb)
SET_CHARGE_PUMP     = const(0x8d)


class SSD1306:
    def __init__(self, width, height, external_vcc):
        self.width = width
        self.height = height
        self.external_vcc = external_vcc
        self.pages = self.height // 8
        # Note the subclass must initialize self.framebuf to a framebuffer.
        # This is necessary because the underlying data buffer is different
        # between I2C and SPI implementations (I2C needs an extra byte).
        self.poweron()
        self.init_display()
    # （init_display / show / fill / pixel / text 等方法见完整文件）


class SSD1306_I2C(SSD1306):
    def __init__(self, width, height, i2c, addr=0x3c, external_vcc=False):
        self.i2c = i2c
        self.addr = addr
        self.temp = bytearray(2)
        self.buffer = bytearray(((height // 8) * width) + 1)
        self.buffer[0] = 0x40  # Set first byte of data buffer to Co=0, D/C=1
        self.framebuf = framebuf.FrameBuffer1(memoryview(self.buffer)[1:], width, height)
        super().__init__(width, height, external_vcc)
    # （write_cmd / write_framebuf / poweron 见完整文件）
```

> ⚠️ **未实跑**：`geek.py` 与 `ssd1306.py` 依赖 **`machine`、`dht`、`framebuf`** 等 **MicroPython 专有模块**，
> 且需要真实接好 **DHT11 传感器 + SSD1306 OLED + SG90 舵机**，**只能烧到 ESP32 上运行**。
> 本机 `python3 geek.py` 会立刻 `No module named 'dht'` 失败，因此本讲全程「未实跑」。
>
> 📌 顺带一提，`oled.text(f'{d.temperature(temp)} ', 32, 20)` 这一行是课程原代码里的**笔误**
> （`temperature()` 不接受参数），照抄能在板子上跑通是因为它把临时值当参数塞了进去，实际应写
> `oled.text(f'{temp} ', 32, 20)`。这里保留原样，方便你对照课程仓库。

### 课后作业

请你使用 MQTT 协议控制灯珠，通过远程控制实现灯珠的**打开、关闭以及颜色修改**。

> 参考思路（**未实跑**，需硬件 WS2812 灯珠）：
> 1. 用 `neopixel`（MicroPython 自带）或 `machine.PWM` 控制灯珠引脚，如 `machine.Pin(2)`。
> 2. 在 MQTT 回调 `sub_cb(topic, msg)` 里解析收到的指令，如 `b"on"` / `b"off"` / `b"#ff0000"`。
> 3. 收到 `on` 就点亮、`off` 就熄灭、RGB 十六进制串就改颜色。
> 4. 手机端用 MQTT 客户端 App 往对应主题发这些指令即可远程控制。

---

## 第 117 讲 · 再回首：“物联网”单元小结

### 本节目标

回顾本章 7 讲的主线，把「概念 → 协议 → 硬件 → 实践」串成一条线。

### 知识要点

本章主线：**物联网是什么 → 用什么通信 → 怎么描述设备 → 怎么装系统 → 怎么传消息 → 怎么落地案例**。

| 讲号 | 主题 | 一句话结论 |
| --- | --- | --- |
| 111 | 物联网 vs 互联网 | 设备也能产生/接收数据；终端算力弱，需服务器集中处理 |
| 112 | TCP 协议 | 物联网最常用协议：简洁、可靠、面向连接（三次握手） |
| 113 | 物模型与模组 | 物模型 = 设备的 JSON 数据模板（属性/事件/方法）；模组 = 芯片+周边的积木 |
| 114 | 装 MicroPython | 用 `esptool` 把固件烧到 ESP32 的 Flash；`boot.py` 开机自执行 |
| 115 | MQTT 消息队列 | 发布/订阅模式，EMQX 等服务器提供 QoS、权限验证 |
| 116 | 端到端案例 | DHT11 测温 → OLED 本地显示 → MQTT 上报手机 |
| 117 | 本讲小结 | 概念 + 硬件 + 网络三者合力，才是一台完整的物联网设备 |

### 代码实操

本讲为复习，**无需运行代码**。回顾本章唯一真跑的示例：`code/112-tcp-demo.py`（TCP 通信）。

**本机实测输出（重贴便于复习，Python 3.12.7）**：

```text
[传感器节点] 已启动，监听 127.0.0.1:65432
[传感器节点] 收到来自 127.0.0.1:63596 的请求：b'TEMP?'
[传感器节点] 已回复温度：25.3 °C
[手机] 第 1 次查询 → 收到 25.3 °C
[传感器节点] 收到来自 127.0.0.1:63597 的请求：b'TEMP?'
[传感器节点] 已回复温度：25.5 °C
[手机] 第 2 次查询 → 收到 25.5 °C
[传感器节点] 收到来自 127.0.0.1:63598 的请求：b'TEMP?'
[传感器节点] 已回复温度：25.4 °C
[手机] 第 3 次查询 → 收到 25.4 °C
[传感器节点] 收到来自 127.0.0.1:63599 的请求：b'TEMP?'
[传感器节点] 已回复温度：25.8 °C
[手机] 第 4 次查询 → 收到 25.8 °C
[传感器节点] 收到来自 127.0.0.1:63600 的请求：b'TEMP?'
[传感器节点] 已回复温度：26.1 °C
[手机] 第 5 次查询 → 收到 26.1 °C
通信结束：服务端与客户端均已关闭（脚本未常驻）。
```

> ⚠️ 本节其余 ESP32 相关代码（`boot.py` / `wifi.py` / `mqtt_*.py` / `geek.py` / `ssd1306.py`）
> **均需开发板，未在本机实跑**。

### 课后作业

把本章 `code/esp32/` 里的文件对照注释再读一遍，尝试**改一个参数**（比如把上报周期从 `sleep(2)` 改成 `sleep(5)`），
想想改完之后，OLED 刷新和手机收到的频率会怎么变。

> 参考答案：`sleep(2)` 改成 `sleep(5)` 后，主循环**每 5 秒**才读一次温度、刷一次屏、发一次 MQTT，
> 于是 OLED 上的数字更新变慢，手机 App 收到的温度消息也变为每 5 秒一条。
> 周期越长越省电，但实时性越差——这正是物联网设备「功耗 vs 时效」的经典权衡。

---

## 本章小结

**速查表**

| 主题 | 关键点 |
| --- | --- |
| 物联网 vs 互联网 | 设备能产生/接收数据；终端弱、靠边缘或中心服务器集中处理 |
| TCP | 面向连接、可靠、有序；三次握手建立连接；物联网最常用 |
| `socket` 通信 | 服务端 `bind` → `listen` → `accept`；客户端 `connect`；数据用 `bytes` |
| 物模型 | 设备的数据模板（JSON）：属性 / 事件 / 方法（=动作） |
| 模组 | 芯片 + 周边硬件的封装，拿来即用，不必从零开发 |
| MicroPython | 硬件版 Python；烧固件到 ESP32 的 Flash |
| 烧录 | `esptool.py --chip esp32 --port <串口> --baud 460800 write_flash -z 0x1000 <固件.bin>` |
| MQTT | 消息队列 + 发布/订阅；服务器（EMQX）提供 QoS、权限验证 |
| DHT11 | 温湿度传感器；湿度 ±5%RH、温度 ±2°C；`d.measure()` → `d.temperature()` |
| SSD1306 | OLED 驱动；`SoftI2C` 接线，`oled.text()` / `oled.show()` 显示 |
| 接线安全 | 温感引脚 VCC / GND **切勿反接**，否则可能损坏元件 |

**三句话**

1. **物联网 = 互联网 + 设备端**：设备既是数据来源也是指令归宿，弱算力交给服务器。
2. **TCP 是可靠的电话、MQTT 是发布订阅的广播**：一个保证「送到」，一个解决「多设备并发」。
3. **物模型描述「是什么」，模组提供「怎么做」**：概念 + 硬件 + 网络三者合力，才是一台完整设备。

**动手练习**

1. 真跑 `code/112-tcp-demo.py`，数一数服务端一共服务了几次请求。
2. 把 `112-tcp-demo.py` 拆成 `echo_server.py` + `echo_client.py` 两个文件，开两个终端跑通。
3. 为「智能台灯」写一份物模型 JSON（属性：开关/亮度/色温；事件：过热；方法：开/关/调亮度）。
4. 拿到 ESP32 后，照第 114 讲烧录 MicroPython，再照第 116 讲接 DHT11 + OLED 跑通综合案例。

---

## 下一章预告

本章是全书正文的最后一章。接下来进入 **附录 · 术语表**：把全书出现过的关键名词
（解释器、字节码、虚拟环境、迭代器、装饰器、TCP、MQTT、物模型……）集中整理，方便随时回查。

---

[← 上一章：计算机视觉](/guide/face-recognition) ｜ [返回总目录](/) ｜ [附录：术语表 →](/glossary)

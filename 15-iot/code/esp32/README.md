# code/esp32 · ESP32 硬件代码（未实跑）

这里的文件是第 114 / 115 / 116 讲的 **ESP32 + MicroPython** 代码，从课程原始仓库
（`_source/code/ch15/`）拷贝而来，内容**保持原样**，方便你直接拷到开发板上运行。

⚠️ **本节全程「未实跑」**：这些代码 `import` 了 `machine`、`network`、`dht`、`framebuf`、
`umqtt.simple` 等 **MicroPython 专有模块**，在电脑上的桌面版 Python 里**不存在**，
直接 `python3 boot.py` 会报 `ModuleNotFoundError`。

> 因此它们被放在 `code/esp32/` **子目录**里：
> 全仓校验脚本 `scripts/verify-examples.py` 只扫描 `code/` 顶层的 `.py`，不递归子目录，
> 这样既保留了完整的硬件代码，又不会让「需开发板」的脚本被误判为失败。

## 文件对照

| 文件 | 讲号 | 作用 |
| --- | --- | --- |
| `boot.py` | 114 | 开机自执行入口：连 WiFi（`import wifi`）后加载主程序（`import geek`） |
| `wifi.py` | 114 | `do_connect()`：连接 WiFi（`network.WLAN`） |
| `mqtt_pub.py` | 115 | MQTT 发布者：连 `broker-cn.emqx.io`，往 `foo_topic` 发 `hello` |
| `mqtt_sub.py` | 115 | MQTT 订阅者：订阅 `foo_topic`，收到消息触发 `sub_cb` 回调 |
| `geek.py` | 116 | 综合案例：DHT11 读温度 → SSD1306 OLED 显示 → MQTT 上报 |
| `ssd1306.py` | 116 | SSD1306 OLED 驱动（MicroPython，Adafruit 版） |
| `lib/umqtt/simple.py` | 115 | `umqtt.simple`：MicroPython 的 MQTT 客户端库 |

用法：把 `esp32/` 下的 `.py`（含 `lib/` 目录结构）整体拷到 ESP32 的文件系统里，
上电后 `boot.py` 会自动执行。

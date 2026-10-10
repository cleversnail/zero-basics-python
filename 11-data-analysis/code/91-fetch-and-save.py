"""第 91 讲 · 如何获取网页上的数据并存储到文件？

本讲分两部分：

  1. 【未实跑】从真实网页抓取数据 —— 需要联网，本节只给完整代码，标注「本节为说明，未实跑」。
  2. 【实跑】从一段本地 HTML 文本里提取数据并存成文件 —— 不联网，逻辑与抓网页完全一样，
     而且能直接运行观察结果。

运行：python3 91-fetch-and-save.py
"""

import os
import re

# ============================================================
# 第一部分：从真实网页抓取并保存（本节为说明，未实跑）
# 这段代码需要联网，且目标网站可能改版，因此不在文档里运行。
# ============================================================
import requests

HERE = os.path.dirname(os.path.abspath(__file__))


def fetch_html(url, save_as=None):
    """用 HTTP 的 GET 方式抓取一个网页，返回网页源代码文本。

    真实采集里会加 User-Agent，让服务器把我们当成普通浏览器，而不是脚本。
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
    }
    r = requests.get(url, headers=headers, timeout=10)
    r.encoding = "utf-8"          # 中文网页一般用 utf-8，避免乱码
    if save_as:                   # 顺带把原始网页存一份，方便以后反复分析
        with open(save_as, "w", encoding="utf-8") as f:
            f.write(r.text)
    return r.text


# 【本节为说明，未实跑】下面这行需要联网，正式跑时取消注释即可：
# html = fetch_html("https://www.weather.com.cn/weather/101010100.shtml",
#                   save_as=os.path.join(HERE, "beijing_weather.html"))


# ============================================================
# 第二部分：从本地 HTML 文本里提取数据并存成文件（实跑）
# 网页本质上就是一坨字符串，提取逻辑与抓真网页一致，只是数据来源换成了本地的 html 变量。
# ============================================================
html = """
<html>
  <body>
    <h1>某城市一周天气</h1>
    <table>
      <tr><td>2022-06-20</td><td>晴</td><td>30</td></tr>
      <tr><td>2022-06-21</td><td>多云</td><td>31</td></tr>
      <tr><td>2022-06-22</td><td>阴</td><td>29</td></tr>
      <tr><td>2022-06-23</td><td>小雨</td><td>28</td></tr>
      <tr><td>2022-06-24</td><td>晴</td><td>27</td></tr>
      <tr><td>2022-06-25</td><td>晴</td><td>26</td></tr>
      <tr><td>2022-06-26</td><td>多云</td><td>30</td></tr>
    </table>
    <img src="sun.png">
    <img src="cloud.png">
  </body>
</html>
"""

# 1) 提取所有 <td>...</td> 里的文字，再每 3 个一组（日期、天气、气温）
cells = re.findall(r"<td>(.*?)</td>", html)
rows = [cells[i:i + 3] for i in range(0, len(cells), 3)]

print("从 HTML 中提取到的表格数据：")
for day, weather, temp in rows:
    print(f"    {day}  {weather}  最高 {temp}°C")

# 2) 提取所有 <img> 的图片地址
imgs = re.findall(r'<img src="([^"]+)"', html)
print()
print("从 HTML 中提取到的图片地址：", imgs)

# 3) 存成文本文件（追加/写入模式），一行一条记录
out_path = os.path.join(HERE, "weather.txt")
with open(out_path, "w", encoding="utf-8") as f:
    f.write("日期,天气,最高气温\n")           # 表头
    for day, weather, temp in rows:
        f.write(f"{day},{weather},{temp}\n")  # 每条记录一行，用逗号分隔

print()
print(f"数据已保存到：{out_path}")
print("文件内容：")
with open(out_path, "r", encoding="utf-8") as f:
    print(f.read().rstrip())
print()
print("提示：把 html 换成 fetch_html(...) 抓回来的真实网页文本，这套提取逻辑同样适用。")

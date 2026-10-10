"""第 88 讲 · 理论盘点：数据采集的方法与 HTTP 协议

本讲讲 HTTP 协议本身。为了不依赖网络，这个脚本做两件完全离线的事：
    1. 用 urllib.parse 拆解一个 URL，看清「请求地址」由哪几部分组成；
    2. 用 requests 的 PreparedRequest 组装一个 GET 请求，
       看它在真正发出去之前长什么样（这一步不发网络请求）。

运行：python3 88-http-demo.py
"""

from urllib.parse import urlparse, parse_qs, urlencode
from requests import Request

# ---------- 1. 拆解 URL ----------
# URL 是「统一资源定位符」，一个典型的 URL 长这样：
#   https://time.geekbang.org/resource?plus=0&sort=2&order=desc
url = "https://time.geekbang.org/resource?plus=0&m=0&d=3&c=12&sort=2&order=desc"

parsed = urlparse(url)
print("原始 URL：", url)
print("scheme（协议）  :", parsed.scheme)
print("netloc（主机名）:", parsed.netloc)
print("path（路径）    :", parsed.path)
print("query（查询参数）:", parsed.query)
print()

# 把查询参数拆成字典，方便程序取值
params = parse_qs(parsed.query)
print("拆解后的查询参数：", params)
print("只取 sort 参数   ：", params["sort"][0])
print()

# 反过来：把字典拼回查询字符串
new_query = urlencode({"city": "beijing", "days": 7})
print("重新拼接的查询字符串：", new_query)
print()

# ---------- 2. 组装一个 GET 请求（不发网络）----------
# requests.Request 只是「描述」一个请求；.prepare() 把它变成真正可发送的样子。
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
}
req = Request("GET", url, headers=headers).prepare()

print("即将发送的请求：")
print("    方法(method)   :", req.method)
print("    地址(url)      :", req.url)
print("    请求头(headers):")
for key, value in req.headers.items():
    print(f"        {key}: {value}")
print()
print("说明：真正的 requests.get(...) 会把这个请求发到服务器，服务器返回状态码 + 响应体。")
print("      常见状态码：200 成功 / 301 永久重定向 / 404 找不到 / 500 服务器错误。")

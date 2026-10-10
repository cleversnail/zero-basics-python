# 第 33 讲：match 语句 —— 如何通过 match 关键字来处理程序的分支逻辑？
# match 语句需要 Python 3.10 及以上版本
# 直接运行：python3 33-match.py

# 1) 基本用法：变量名 _ 是通配符，保证 match 一定能匹配成功
http_response_status = 500

match http_response_status:
    case 400:
        print("Bad request")
    case 404:
        print("Not found")
    case 418:
        print("I'm a teapot")
    case _:
        print("Something's wrong with the internet")

# 2) 模式组合：用 "|" 在一个模式里组合多个字面值
#    注意：PPT 里写法是 "case 500 or 501 or 503"，但在真实 Python 里
#    case 模式只认 "|"，写成 "or" 会直接 SyntaxError（见避坑说明）
http_response_status = 404

match http_response_status:
    case 400 | 403 | 404:
        print("4xx error")
    case 500 | 501 | 503:
        print("5xx error")
    case _:
        print("其他状态码")

# 3) 课后作业：根据月份输出季节
month = 7

match month:
    case 3 | 4 | 5:
        print("春季")
    case 6 | 7 | 8:
        print("夏季")
    case 9 | 10 | 11:
        print("秋季")
    case 12 | 1 | 2:
        print("冬季")
    case _:
        print("月份不合法")

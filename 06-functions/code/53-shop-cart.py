# -*- coding: utf-8 -*-
"""第 53 讲 · 小试牛刀：如何利用函数实现电商购物车功能？

原课程用 input() 让用户在现场一次次输入商品与数量，文档里无法演示交互输入。
这里改成「固定购物序列」，程序一次跑完，功能与讲义完全一致。
"""

# 商品表：每行是 [商品编号, 名称, 类目, 单价]
products = [
    [1000, "iphone", "phone", 12000],
    [1001, "ipad", "pad", 15000],
    [1002, "macbook", "laptop", 20000],
]

# 购物车：{商品编号: 数量}
cart = {1000: 5, 1001: 2}


def idtoname(product_id):
    """商品编号 -> 商品名称"""
    for product in products:
        if product[0] == product_id:
            return product[1]


def idtoprice(product_id):
    """商品编号 -> 单价"""
    for product in products:
        if product[0] == product_id:
            return product[3]


def show_cart():
    """展示购物车里的商品，并统计总费用"""
    total = 0
    for product_id in cart:
        print(f"购买商品 {idtoname(product_id)} 的数量为 {cart[product_id]}")
        total += idtoprice(product_id) * cart[product_id]
    print(f"总费用为: {total}")


def add_product(product_id, number):
    """加入购物车：已有就累加数量，没有就新增"""
    if product_id in cart:
        cart[product_id] += number
    else:
        cart[product_id] = number


def del_product(product_id):
    """购物车里某商品数量减 1，减到 0 就把它移除"""
    if product_id in cart:
        cart[product_id] -= 1
        if cart[product_id] == 0:
            cart.pop(product_id)


def clean_cart():
    """清空购物车"""
    cart.clear()


print("=== 初始购物车 ===")
show_cart()

print("=== 加入 15 台 macbook 后 ===")
add_product(1002, 15)
show_cart()

print("=== 从购物车减去 1 台 ipad 后 ===")
del_product(1001)
show_cart()

print("=== 清空购物车后 ===")
clean_cart()
show_cart()

# -*- coding: utf-8 -*-
"""第 83 讲 · 关系型数据库：如何使用关系型数据库？

⚠️ 本节为说明，未实跑，因为本机没有运行 MySQL 服务（也没有安装 PyMySQL 客户端）。
   为了不让脚本直接报错退出，下面做了「能连上就真跑、连不上就打印说明」的兜底处理。

要真正运行，需要三步：
  1. 安装 Python 客户端：  pip3 install PyMySQL
  2. 准备一个 MySQL 服务，并在里面建好库和表：
        CREATE DATABASE db;
        CREATE TABLE `users` (
            `id` int(11) NOT NULL AUTO_INCREMENT,
            `email` varchar(255) NOT NULL,
            `password` varchar(255) NOT NULL,
            PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
  3. 把下面的 user / password 改成你自己的，再运行：python3 83-mysql.py

运行：python3 83-mysql.py
"""
import sys


# 第一步：先看有没有装 PyMySQL
try:
    import pymysql.cursors
except ImportError:
    print("[未实跑] 本机没有安装 PyMySQL 客户端，无法连接 MySQL。")
    print("         安装命令：pip3 install PyMySQL")
    sys.exit(0)


# 数据库连接参数（请改成你自己的）
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'rootroot',
    'database': 'db',
    'cursorclass': pymysql.cursors.DictCursor,   # 查询结果用字典返回
}


def main():
    # 连接数据库
    try:
        connection = pymysql.connect(**DB_CONFIG)
    except Exception as exc:   # noqa: BLE001
        print(f"[未实跑] 无法连接本机 MySQL 服务（{type(exc).__name__}: {exc}）。")
        print("         准备好 MySQL 与 db.users 表后，再运行本脚本即可真正读写。")
        return

    try:
        with connection:
            with connection.cursor() as cursor:
                # 建立一条记录（用 %s 占位符，避免 SQL 注入）
                sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
                cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

            # connection 不能自动提交数据，必须手动提交
            connection.commit()

            with connection.cursor() as cursor:
                # 读取记录
                sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
                cursor.execute(sql, ('webmaster@python.org',))
                result = cursor.fetchone()
                print("查询结果：", result)

            with connection.cursor() as cursor:
                # 更新数据
                sql = "UPDATE `users` SET `password`=%s WHERE `email`=%s"
                cursor.execute(sql, ('new-secret', 'webmaster@python.org'))
            connection.commit()
            print("更新完成。")
    except Exception:                 # noqa: BLE001
        connection.rollback()         # 出错就回滚
        print("操作失败，已回滚。")
    finally:
        connection.close()            # 别忘了关闭连接


if __name__ == '__main__':
    main()

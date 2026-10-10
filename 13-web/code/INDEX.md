# 第 13 章 · code/ 目录说明（Web 开发 / Django）

> ⚠️ **本章代码全程「未实跑」**——Django 工程需要安装 Django、并连接数据库（SQLite / MySQL）才能运行。
> 本目录只**原样保存**课程仓库的 Django 项目源码，供你复制到自己电脑上运行；本机未执行过任何 `manage.py` 命令。
>
> 📌 本目录**顶层故意不放 `.py` 文件**：Django 的 `manage.py` 必须在装了 Django 的环境中才能运行，
> 直接 `python3 manage.py` 会因缺 Django 报错。因此所有 `.py` 都收在**子目录**里，
> 全仓校验脚本（`npm run verify`）只扫描各章 `code/*.py`（顶层），不会误跑到它们。

## 目录结构

```
code/
├── INDEX.md                ← 本文件
├── 本章命令速查.md          ← 由 97.txt / 98.txt / 100.txt 整理的有序命令清单
├── key-files/              ← 关键文件集中版（最常看的几个文件）
│   ├── mysite/             (Blog 项目：models / views / admin / urls / settings / templates)
│   ├── mysite98/           (最小站点)
│   └── mysite99/           (最小站点，带 "Hello Django" 视图)
├── mysite/                 ← 第 102–103 讲：个人 Blog 完整工程
├── mysite98/               ← 第 101 讲：最小站点完整工程
└── mysite99/               ← 第 101 讲：最小站点完整工程（路由闭环）
```

## 三个工程分别是什么 / 怎么跑

| 工程 | 对应讲号 | 跑起来后看到什么 |
| --- | --- | --- |
| `mysite98/` | 101 | 一个只有内置 admin 的空站点 |
| `mysite99/` | 101 | 访问 `/myapp99/` 返回纯文本 `Hello Django` |
| `mysite/` | 102–103 | 后台录入文章，访问 `/myblog/` 展示文章列表 |

**通用运行步骤（示例，未实跑）：**

```bash
cd code/mysite99
pip3 install django==4.1.2
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
# 浏览器打开 http://127.0.0.1:8000/myapp99/
```

`mysite/` 额外事项：它默认连 **MySQL**，并且模板用了 `django-bootstrap4`。
- 想省事：把 `mysite/mysite/settings.py` 的 `DATABASES` 改回 SQLite 默认配置，并把模板里的
  `{% load bootstrap4 %}` 那行去掉（详见本章 README 第 103 讲给的纯净版模板）。
- 想照原样：`pip3 install django-bootstrap4 mysqlclient`，并在 MySQL 里 `create database django;`。

## key-files/ 里有什么

| 文件 | 来源 | 内容 |
| --- | --- | --- |
| `key-files/mysite/myblog/models.py` | `mysite/myblog/models.py` | Article 模型定义 |
| `key-files/mysite/myblog/views.py` | `mysite/myblog/views.py` | 取文章并渲染模板的视图 |
| `key-files/mysite/myblog/admin.py` | `mysite/myblog/admin.py` | 注册后台 + `list_display` |
| `key-files/mysite/myblog/urls.py` | `mysite/myblog/urls.py` | 应用级路由 |
| `key-files/mysite/mysite/urls.py` | `mysite/mysite/urls.py` | 项目级路由 |
| `key-files/mysite/mysite/settings.py` | `mysite/mysite/settings.py` | 数据库与应用配置 |
| `key-files/mysite/myblog/templates/blog.html` | `mysite/myblog/templates/blog.html` | 文章展示模板 |
| `key-files/mysite98/myapp98/views.py` | `mysite98/myapp98/views.py` | 空视图（仅注释） |
| `key-files/mysite98/mysite98/urls.py` | `mysite98/mysite98/urls.py` | 项目级路由 |
| `key-files/mysite98/mysite98/settings.py` | `mysite98/mysite98/settings.py` | 最小配置 |
| `key-files/mysite99/myapp99/views.py` | `mysite99/myapp99/views.py` | 返回 `Hello Django` 的视图 |
| `key-files/mysite99/myapp99/urls.py` | `mysite99/myapp99/urls.py` | 应用级路由 |
| `key-files/mysite99/mysite99/urls.py` | `mysite99/mysite99/urls.py` | 项目级路由（挂载 myapp99） |
| `key-files/mysite99/mysite99/settings.py` | `mysite99/mysite99/settings.py` | 最小配置 |

（`mysite98` 没有 `myapp98/urls.py`，因为它的项目级路由只挂了 admin，尚未用到应用级路由。）

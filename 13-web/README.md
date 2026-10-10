# 第 13 章 · Web 开发

> 从「浏览器和服务器到底在干什么」讲起，理解 MVC / MTV 分层思想，再用 Python 最知名的
> Django 框架，一步步搭出一个属于自己的个人 Blog（后台发文 + 前台展示）。
> **本章 6 讲（099–104）**，从 Web 原理 → MVC 模型 → 搭最小服务器 → admin 上传 → 前台发布 → 单元小结。

## 🎯 本章目标

- 分清 **Web 客户端**（浏览器）与 **Web 服务端**各自负责什么
- 知道 Web 服务端要处理的**三类数据**：HTTP 协议头、HTTP 包体、HTTP 状态码
- 用 Python 内置的 `http.server` 模块，把任意目录发布成网页
- 理解 **Web 框架**为什么要存在，以及 **MVC** 三层（Model / View / Controller）的含义
- 说清 Django 的 **MTV**（Model / Template / View）与 MVC 的对应关系
- 跑通 Django 的「建项目 → 建应用 → 改路由 → 写视图 / 模型 / 模板」完整流程
- 用 **Django-admin** 后台实现文章上传，并优化列表显示字段
- 用模板把数据库里的文章**发布**到网页上

**本章代码**

> ⚠️ **本章全程「未实跑」**。
> Django 的运行需要一个装了 Django 的 Python 环境，还要有数据库（SQLite 或 MySQL）才能建表、起服务。
> 我们在写这本书的沙箱里**没有真跑过任何一条 Django 命令**——因此本章**不会出现任何伪造的终端输出**
> （比如 `Watching for file changes with StatReloader`、`System check identified no issues` 这类信息，
> 都是「通常会看到」，不是我们跑出来的）。
>
> ✅ 但每个代码块后面都给足了「**你自己怎么跑起来**」的完整步骤：装包、建项目、改哪个文件的哪一行、
> 敲哪条命令、浏览器该打开什么地址。代码全部照抄课程仓库（`mysite/`、`mysite98/`、`mysite99/`）。

| 文件 / 目录 | 内容 |
| --- | --- |
| `code/mysite98/` | 第 101 讲的最小站点示例（`startproject mysite98` + `startapp myapp98`） |
| `code/mysite99/` | 第 101 讲的最小站点示例，多一个「视图返回 Hello Django」的完整路由闭环 |
| `code/mysite/` | 第 102–103 讲的个人 Blog（`myblog` 应用：模型 + admin + 模板 + 视图） |
| `code/key-files/` | 从上面三个项目里挑出的**关键文件**（models / views / urls / settings / templates），集中放一处方便查阅 |
| `code/本章命令速查.md` | 把 `97.txt` / `98.txt` / `100.txt` 里的命令整理成的有序速查表 |

> 📎 说明：课程仓库 `_source/code/ch13/` 里只有 `97.txt`、`98.txt`、`100.txt` 三个命令记录文件
> （**没有** `99.txt`），本章速查表按实际存在的文件整理。

---

## 第 99 讲 · 理论盘点：Web 客户端与服务端

### 本节目标

先不写框架，把「上网」这件事拆成两半：**浏览器做什么**、**服务器做什么**；
再用 Python 自带的 `http.server` 亲手把一个目录发布成网页，获得第一手的「服务端」体验。

### 知识要点

**1. Web 客户端和服务端，各管什么？**

| 角色 | 典型代表 | 主要职责 |
| --- | --- | --- |
| **Web 客户端** | Chrome、Firefox、Edge 等浏览器 | 解决**用户与服务器的交互**：把用户的请求提交给服务器；再解释服务器返回的图片、代码，展示给用户 |
| **Web 服务端** | 一台跑着 Web 程序的服务器 | 接收客户端请求 → 向上游**数据库**请求数据 → 经中间件处理 → 以特定形式返回给浏览器 |

一句话：**客户端负责「展示和收集输入」，服务端负责「处理请求、组织数据」**。

**2. Web 服务端需要处理的主要数据**

| 数据 | 含义 |
| --- | --- |
| **HTTP 协议头** | 又分「请求方式」和「请求内容」两部分 |
| **HTTP 包体** | 请求真正携带的数据（如表单内容、上传的文件） |
| **HTTP 返回状态码** | 服务器告诉浏览器「这次请求结果如何」，如 200（成功）、404（找不到） |

HTTP 协议头里最需要注意的是**请求方式**：最常用的是 **GET** 和 **POST** 两种。

- **GET**：把参数拼在 URL 后面，用来「取」数据（如 `?id=1`）。
- **POST**：把数据放在包体里，用来「提交」数据（如登录、发文章）。

请求内容主要以 **URL** 为主，此外还有浏览器版本、主机名等，服务器也会据此做不同处理。

**3. 用 `http.server` 模块构建简单 Web 服务器**

Python **内置**了一个极简 Web 服务器模块 —— `http.server`。想发布哪个目录，
就在那个目录里运行：

```bash
python3 -m http.server
```

它会把当前目录当作网站根目录，默认监听 **8000** 端口。

### 代码实操

> ⚠️ **本节为说明，未实跑（需在本机执行并保持进程运行）**。下面命令的执行效果是「起一个前台服务、
> Ctrl+C 才停」，属于交互式长时间运行，不适合在文档里贴出「运行输出」。

在你想发布的目录里（例如 `/tmp`）敲：

```bash
# 默认发布当前目录到 8000 端口
python3 -m http.server

# 或者指定端口 8080
python3 -m http.server 8080
```

**你自己怎么跑：**

1. 打开终端，`cd /tmp`（或任意目录）。
2. 敲 `python3 -m http.server 8080`（**不要**用 `python`，避免落到 Python 2）。
3. 终端会停在那里不返回——这是**正常**的，它正在前台监听。
4. 打开浏览器访问 `http://127.0.0.1:8080/`，你会看到该目录的文件列表，点进去就能下载 / 预览。
5. 回到终端按 **Ctrl+C** 停止服务。

> 💡 这个内置服务器**只适合开发调试和临时分享**，不安全、性能也弱，**不要**拿它对外提供正式服务。

### 课后作业

请你使用 `http.server` 模块，将目录 `/tmp` 通过 HTTP 协议发布到 **8080** 端口，并通过浏览器验证是否发布成功。

**参考做法：**

```bash
cd /tmp
python3 -m http.server 8080
# 浏览器打开 http://127.0.0.1:8080/ ，能看到 /tmp 下的文件列表即发布成功
```

---

## 第 100 讲 · 理论盘点：MVC 模型是什么？

### 本节目标

理解「为什么需要 Web 框架」，掌握 **MVC** 三层分工，并弄清 Django 的 **MTV** 与 MVC 的对应关系。

### 知识要点

**1. 没有 Web 框架之前，会遇到什么问题？**

手动写 Web 服务端逻辑，通常是这样的流程：用户登录 → 查询数据库 → 返回页面；
匿名用户 → 查询数据库 → 返回另一个页面……**大量逻辑重复**。由此带来三个麻烦：

| 问题 | 说明 |
| --- | --- |
| **大量重复逻辑** | 每加一个页面都要重写一遍「连库、拼 HTML」 |
| **耦合紧密** | 一处修改可能引发另一处 Bug |
| **依赖关系不清晰** | 代码之间谁依赖谁说不清楚，难维护 |

**2. Web 框架的作用**

> Web 框架就像盖楼时的**结构框架**，确保 Web 服务器代码**有层次、松耦合、不累赘**。

常见的 Web 框架分为 **MVC** 和 **MTV** 两种模式，**它们的本质相同**。

**3. MVC 模型是什么**

MVC 把 Web 后端代码分成**三个层次**：

| 层 | 全称 | 职责 |
| --- | --- | --- |
| **M** | Model 模型层 | 实现**业务对象**和**数据库对象**之间的映射（用 Python 类描述一张表） |
| **V** | View 视图层 | 负责**业务逻辑**和**用户交互**（收到请求要做的主逻辑） |
| **C** | Controller 控制层 | 实现**用户请求**到**视图层**的调用（决定「哪个 URL 找哪个视图」） |

**4. Django 的 MTV 与 MVC 的区别**

Python 最知名的框架 **Django** 实现了 **MTV** 模型。它与 MVC 在**定义上**不同，但在
**解耦和依赖解决**方面采用相同的处理逻辑：

| Django（MTV） | 对应 MVC 的哪一层 | 说明 |
| --- | --- | --- |
| **M**：Model 模型层 | Model | 同上，对象与数据库的映射 |
| **T**：Template 页面模板 | 相当于 View（展示部分） | 负责「页面长什么样」，HTML 模板 |
| **V**：View 视图层 | 相当于 Controller（控制部分） | 负责接收请求、处理逻辑、选用模板 |

Django 的数据处理顺序：

```
用户请求 → URL 控制器 → view 视图 → [Model 模型] → Template 模板 → 返回 HTML
```

> 📌 记忆要点：**MVC 与 MTV 只是「叫法」和「切分位置」不同，目标都是「分层 + 松耦合」。**

### 代码实操

本讲是概念讲解，没有需要自己写的逻辑代码。课程把「装 Django 并启动」作为本讲的动手作业。

> ⚠️ **本节为说明，未实跑（需 Django 环境）**。下面是安装并启动 Django 的完整步骤，请你本机操作。

```bash
# 1) 安装 Django（课程用 4.1.2）
pip3 install django==4.1.2

# 2) 用版本号确认装上了
python3 -m django --version

# 3) 建一个项目并启动，验证 Django 工作正常
django-admin startproject mysite98
cd mysite98
python3 manage.py runserver 0.0.0.0:8000
# 浏览器访问 http://127.0.0.1:8000/ —— 能看到 Django 的欢迎页（一枚小火箭），即安装启动成功
```

### 课后作业

请你使用 `pip` 安装并启动 Django 框架，并使用浏览器访问 Django 监听的端口。根据网页的返回信息，验证 Django 是否被成功安装和启动。

**参考做法：** 见上方「代码实操」的三步；看到 Django 欢迎页即为成功。

---

## 第 101 讲 · 如何使用 Django 搭建简单的 Web 服务器？

### 本节目标

走通 Django 的**最小闭环**：建项目 → 建应用 → 注册应用 → 写视图 → 配路由 → 起服务。

### 知识要点

Django 的 Web 框架包含四大主要部分，本讲先把它们认全：

| 部分 | 作用 |
| --- | --- |
| **URL 处理** | 把用户请求的 URL 映射到对应的视图 |
| **视图（View）** | 处理用户逻辑（收到请求后干什么） |
| **模型（Model）** | 把 Python 对象映射到数据库对象 |
| **模板（Template）** | 把特定信息的样式展示给用户 |

**1. 创建项目**

```bash
django-admin startproject myproject
```

**2. 创建应用（app）**

一个项目可以包含多个应用；应用才是真正放业务代码的地方：

```bash
python3 manage.py startapp testapp
```

**3. 运行 Django（开发服务器）**

```bash
python3 manage.py runserver 8888
```

**4. 处理 URL**

`urls.py` 里的 `urlpatterns` 列表，就是「URL → 视图」的映射表：

```python
urlpatterns = [
    path('admin/', admin.site.urls),
]
```

**5. 视图返回内容**

最简单的视图，直接返回一段文本（来自 `mysite99/myapp99/views.py` 的思路）：

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Django")
```

### 代码实操

> ⚠️ **本节代码为说明，未实跑（需 Django + 数据库环境）**。下面代码**逐字照抄**课程仓库
> `_source/code/ch13/` 下的 `mysite99/` 工程，你可以直接在本章 `code/mysite99/` 里对照。

**第一步：建项目和应用**（对应 `mysite98/`、`mysite99/`）

```bash
# 建项目（生成 mysite99/ 目录）
django-admin startproject mysite99
cd mysite99

# 建应用（生成 myapp99/ 目录）
python3 manage.py startapp myapp99
```

**第二步：把应用注册进 `settings.py`**

打开 `mysite99/mysite99/settings.py`，在 `INSTALLED_APPS` 里加上 `'myapp99'`：

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp99',          # ← 新加这一行
]
```

**第三步：写视图 `myapp99/views.py`**（完整文件）

```python
from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

# 接收用户的请求，采用标准的httpreponse返回数据
def index(request):
    # 这里处理模型
    return HttpResponse("Hello Django") # 模版
```

**第四步：配应用级路由 `myapp99/urls.py`**（完整文件，新建此文件）

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
]
```

**第五步：配项目级路由 `mysite99/mysite99/urls.py`**（完整文件）

```python
"""mysite99 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.urls import include

urlpatterns = [
    path('myapp99/', include('myapp99.urls')),
    path('admin/', admin.site.urls),
]
```

**第六步：起服务**

```bash
python3 manage.py runserver 0.0.0.0:8000
```

**你自己怎么跑：**

1. `cd 13-web/code/mysite99`
2. 确认已装 Django 4.1.2（见第 100 讲）。
3. 敲 `python3 manage.py migrate`（初始化内置表）。
4. 敲 `python3 manage.py runserver`。
5. 浏览器访问 `http://127.0.0.1:8000/myapp99/`，页面会显示纯文本 **Hello Django**。
6. Ctrl+C 停服务。

> 📌 注意第 5 步为什么不是 `/` 而是 `/myapp99/`：项目级路由里写的是
> `path('myapp99/', include('myapp99.urls'))`，应用级路由里 `path('', views.index)` 是**空字符串**，
> 二者拼起来才是 `/myapp99/`。

**附：PPT 里的模型与模板示例（polls 投票应用）**

下面是 PPT 用来演示「模型」和「模板」的经典例子，供你理解 `models.py` 和模板长什么样
（同样**未实跑**）：

模型 `models.py`：

```python
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

模板片段：

```html
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
           <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```

### 课后作业

请你将**所在地区的气温、天气**存入数据库，并利用 Django 框架，将数据库中的天气信息进行展示。

**思路：** 参照本章第 102、103 讲——先在 `models.py` 里定义一个 `Weather` 模型（字段如城市、
气温、天气状况、日期），`makemigrations` + `migrate` 建表，用 admin 后台或 `manage.py shell`
录入数据，再写视图 + 模板把它展示出来。

---

## 第 102 讲 · 如何使用 Django-admin 实现文章上传？

### 本节目标

为 Blog 定义**文章模型**，把它**注册到 admin 后台**，并通过后台界面上传（录入）文章数据；
同时学会用 `list_display` 优化后台列表的显示字段。

### 知识要点

**1. 文章对象模型应当包含哪些字段**

按课程 PPT：文章模型应包含 **文章标题、文章类别、文章作者、发布时间、文章内容**。
字段类型参考官方文档：<https://docs.djangoproject.com/zh-hans/4.0/ref/models/fields/>

| Django 字段类型 | 用途 |
| --- | --- |
| `CharField(max_length=200)` | 短文本（标题、作者） |
| `TextField()` | 长文本（正文内容） |
| `DateTimeField()` | 日期时间（发布时间） |
| `verbose_name="文章标题"` | 给字段起一个中文别名，后台会显示这个别名 |

> ⚠️ **切记要把 model 注册到管理后台**，否则模型**不会**出现在后台界面里。

**2. 从管理后台上传数据**

管理界面地址：`http://127.0.0.1/admin`（课程里实际用的是 `http://127.0.0.1:8080/admin/`）。
登录后即可在后台对文章进行「增 / 删 / 改 / 查」——这就是「上传文章」。

**3. 优化显示字段**

后台列表页默认**不显示全部字段**，通过一个继承 `admin.ModelAdmin` 的类来指定：

```python
class blogAdmin(admin.ModelAdmin):
    list_display = (字段名称,)

# 注册管理类到管理界面：
admin.site.register(blog, blogAdmin)
```

### 代码实操

> ⚠️ **本节代码为说明，未实跑（需 Django + 数据库环境）**。以下代码照抄课程仓库 `mysite/myblog/`。

**第一步：建项目和应用**（对应 `mysite/`）

```bash
django-admin startproject mysite
cd mysite
python3 manage.py startapp myblog
```

**第二步：定义模型 `myblog/models.py`**（完整文件）

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="文章标题")
    pub_date = models.DateTimeField(verbose_name="发布日期")
    data = models.TextField(max_length=200, verbose_name="文章内容")

```

> 💡 课程仓库里的 `Article` 只写了 3 个字段。PPT 建议加上「文章类别、文章作者」，你可以自己补：
>
> ```python
> class Article(models.Model):
>     title = models.CharField(max_length=200, verbose_name="文章标题")
>     category = models.CharField(max_length=100, verbose_name="文章类别", default="未分类")
>     author = models.CharField(max_length=100, verbose_name="文章作者", default="匿名")
>     pub_date = models.DateTimeField(verbose_name="发布日期")
>     data = models.TextField(verbose_name="文章内容")
> ```

**第三步：注册模型到后台 `myblog/admin.py`**（完整文件）

```python
from django.contrib import admin

# Register your models here.
from myblog.models import Article


# 设置admin界面展示的样式
class ArticleAdmin(admin.ModelAdmin):
    list_display  = ("title",)

admin.site.register(Article, ArticleAdmin)
```

**第四步：修改 `mysite/settings.py`**（关键片段）

课程用的是 MySQL。如果不改数据库、用默认 SQLite，也要**把应用注册进去**：

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap4',
    'myblog'
]
```

数据库配置（课程用 MySQL，来自 `mysite/mysite/settings.py`）：

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',       # 连接的数据库
        'HOST': '127.0.0.1',    # mysql 的 ip 地址
        'PORT': 3306,           # mysql 的端口
        'USER': 'root',         # mysql 的用户名
        'PASSWORD': 'rootroot'  # mysql 的密码
    }
}
```

> ⚠️ 不想装 MySQL？把 `DATABASES` 换回 `startproject` 生成的 SQLite 默认配置即可：
>
> ```python
> DATABASES = {
>     'default': {
>         'ENGINE': 'django.db.backends.sqlite3',
>         'NAME': BASE_DIR / 'db.sqlite3',
>     }
> }
> ```
>
> 另外 `mysite` 的模板用到了 `{% load bootstrap4 %}`，需要 `pip3 install django-bootstrap4`；
> 不想装，就把模板顶部那行和 bootstrap 相关标签删掉（见第 103 讲给出的纯净版模板）。

**第五步：建表 + 建后台管理员 + 起服务**

```bash
# 先建库里默认的表
python3 manage.py migrate

# 创建超级管理员（按提示输入用户名 / 邮箱 / 密码）
python3 manage.py createsuperuser

# 因为中途改了 models.py，生成并应用迁移
python3 manage.py makemigrations
python3 manage.py migrate

# 起服务
python3 manage.py runserver 127.0.0.1:8080
```

**你自己怎么跑：**

1. `cd 13-web/code/mysite`
2. 装依赖：`pip3 install django==4.1.2 django-bootstrap4 mysqlclient`（用 MySQL）或 `pip3 install django==4.1.2 django-bootstrap4`（并改用 SQLite）。
3. 若用 MySQL：先在 MySQL 里 `create database django;`，再核对 settings 里的账号密码。
4. 依次执行上面的 `migrate` / `createsuperuser` / `makemigrations` / `migrate` / `runserver`。
5. 浏览器打开 `http://127.0.0.1:8080/admin/`，用刚建的超管账号登录。
6. 在后台点 **Article**，点右上角 **Add**，填标题、发布日期、内容，**Save**——文章就存进数据库了。

### 课后作业

请你根据这节课内容，通过 Django-admin 实现 **Blog 的文章上传**功能。

**提示：** 关键在第三、四步——`admin.py` 里 `admin.site.register(Article, ArticleAdmin)` 那一行不能少，
否则后台看不到 Article 模型，就没法上传。

---

## 第 103 讲 · 如何使用 Django 实现文章发布？

### 本节目标

把数据库里的文章**展示到网页上**：做模板（Templates）→ 写视图（View）→ 配 URL → 刷新页面看到文章列表。

### 知识要点

**1. 制作模板**

- 模板放在应用的 `templates` 文件夹里，用 **HTML** 展示给用户。
- 模板除内容外，还能承载**样式（CSS）**以及 **JS** 等前端脚本实现的逻辑。
- Django 模板有自己的语法：`{% %}` 是**标签**（逻辑），<code v-pre>{{ }}</code> 是**变量**（取值）。

**2. 修改视图**

- 根据上一讲创建的 Blog 模型，创建展示用的视图：从数据库取出文章 → 交给模板渲染。
- ⚠️ **创建视图后，必须修改 `urls.py`**，把用户请求的 URL 映射到指定的视图，否则页面 404。

**3. 刷新与重启**

- 以**开发模式**运行 Django（`runserver`）：改完代码**刷新浏览器**就能看到最新页面。
- 以**生产模式**运行：需要**重启 Django 进程**才能生效。

### 代码实操

> ⚠️ **本节代码为说明，未实跑（需 Django + 数据库环境）**。代码照抄课程仓库 `mysite/`。

**第一步：写视图 `myblog/views.py`**（完整文件）

```python
from django.shortcuts import render

# Create your views here.
from .models import Article

# 参考 
# https://docs.djangoproject.com/zh-hans/4.1/intro/tutorial03/#a-shortcut-render

def index(request):
    blog_list = Article.objects.order_by('title')
    context = {'blog_list':blog_list}
    return render(request, 'blog.html', context)
```

**第二步：配应用级路由 `myblog/urls.py`**（完整文件）

```python
from django.urls import path

from . import views

app_name = 'myblog'
urlpatterns = [
    path('', views.index, name='index'),
]
```

**第三步：配项目级路由 `mysite/mysite/urls.py`**（完整文件）

```python
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('myblog/', include('myblog.urls')),
    path('admin/', admin.site.urls),
]
```

**第四步：写模板 `myblog/templates/blog.html`**（完整文件，课程仓库原版）

```html
{% load bootstrap4 %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width,initial-scale=1">
        <title>Learning Log</title>
        {% bootstrap_css %}
        {% bootstrap_javascript %}
      </head>

<body>
{% block content %}

    {% if blog_list %}
        
        {% for blog in blog_list %}
        <ul>
            <h2> {{blog.title}} </h2>
            <li> {{blog.pub_date}} </li>
            <h4> {{blog.data}} </h4>
        </ul>
        {% endfor %}
        
    {% endif %}

{% endblock content %}
</body>
```

> 💡 上面原版依赖 `django-bootstrap4`。如果你没装，用下面这个**不依赖任何第三方**的等价模板，
> 效果一样（就是少了 Bootstrap 的样式）：

```html
<!DOCTYPE html>
<html lang="zh-CN">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width,initial-scale=1">
        <title>我的 Blog</title>
    </head>
<body>
    {% if blog_list %}
        {% for blog in blog_list %}
        <ul>
            <h2> {{blog.title}} </h2>
            <li> {{blog.pub_date}} </li>
            <h4> {{blog.data}} </h4>
        </ul>
        {% endfor %}
    {% else %}
        <p>还没有文章，去 /admin/ 上传一篇吧。</p>
    {% endif %}
</body>
</html>
```

**你自己怎么跑：**

1. 确认前几讲已完成：模型已建表、后台已录入至少一篇文章。
2. 按上面四步把视图、两个 `urls.py`、模板就位。
3. `python3 manage.py runserver 127.0.0.1:8080`。
4. 浏览器访问 `http://127.0.0.1:8080/myblog/`——你在后台录入的文章标题、发布日期、内容就会显示出来。
5. 再回 `http://127.0.0.1:8080/admin/` 添一篇，刷新 `/myblog/` 页面即可看到新文章（开发模式自动重载）。

### 课后作业

请你将 Blog 的**文章标题、分类、时间和内容**展示到网页上。

**提示：** 若你按第 102 讲给 `Article` 加了 `category`（类别）字段，只需在模板里补一行：

```html
<p>分类：{{ blog.category }}</p>
```

---

## 第 104 讲 · 再回首：“Web 开发”单元小结

### 本节目标

把本单元零散的知识点串成一条线：**HTTP 原理 → MVC/MTV 分层 → Django 四大件 → Blog 全流程**，
并留下一份可操作的命令速查表。

### 知识要点

**1. 一条主线：请求是怎么变成页面的**

```
浏览器发请求
   │
   ▼
URL 控制器（urls.py）        —— 决定「哪个 URL 交给哪个视图」
   │
   ▼
视图 View（views.py）        —— 处理业务逻辑，向 Model 要数据
   │
   ▼
模型 Model（models.py）      —— 把 Python 对象映射成数据库里的一行行记录
   │
   ▼
模板 Template（*.html）      —— 把数据套进 HTML，生成页面
   │
   ▼
返回 HTML 给浏览器展示
```

**2. 本单元三个「必须记住」**

1. **角色分工**：客户端负责交互与展示，服务端负责处理请求、组织数据。
2. **分层思想**：MVC / MTV 都是「分层 + 松耦合」，Django 用的是 MTV。
3. **Django 四件套**：URL 处理、视图、模型、模板——四者缺一，页面就跑不起来。

**3. Django 项目结构速查**

| 位置 | 是什么 | 你通常改什么 |
| --- | --- | --- |
| `manage.py` | 命令行入口 | 几乎不改 |
| `mysite/settings.py` | 全局配置 | `INSTALLED_APPS`、`DATABASES` |
| `mysite/urls.py` | **项目级**路由 | 用 `include()` 挂载各应用的路由 |
| `myblog/models.py` | 模型（表结构） | 定义你的数据类 |
| `myblog/admin.py` | 后台注册 | `admin.site.register(Article, ArticleAdmin)` |
| `myblog/views.py` | 视图（逻辑） | 取数据、选模板 |
| `myblog/urls.py` | **应用级**路由 | 把 URL 映射到视图 |
| `myblog/templates/*.html` | 模板（页面） | HTML + <code v-pre>{{ 变量 }}</code> |

### 代码实操

本讲不引入新代码，而是把前五讲串起来。完整的命令与文件清单见：

- 项目源码：`code/mysite98/`、`code/mysite99/`（最小站点）、`code/mysite/`（Blog）
- 关键文件集中版：`code/key-files/`
- 命令速查：`code/本章命令速查.md`

> ⚠️ **本节所有命令均为说明，未实跑**——原因同本章开头：需要 Django + 数据库环境。

**从零到 Blog 跑起来的完整清单（照着做）：**

```bash
# 0. 装环境
pip3 install django==4.1.2 django-bootstrap4

# 1. 建项目与应用
django-admin startproject mysite
cd mysite
python3 manage.py startapp myblog

# 2. 把 myblog 写进 settings.py 的 INSTALLED_APPS

# 3. 定义 models.py（Article），再注册到 admin.py

# 4. 建表 / 建超管
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py makemigrations
python3 manage.py migrate

# 5. 写 views.py + 两个 urls.py + templates/blog.html

# 6. 起服务
python3 manage.py runserver 127.0.0.1:8080
# 后台：http://127.0.0.1:8080/admin/    前台：http://127.0.0.1:8080/myblog/
```

### 课后作业

请你把本章的 Blog 项目完整跑一遍：**在后台录入至少两篇文章，在 `/myblog/` 页面看到它们按标题排序展示**。
进阶：给 `Article` 补上「类别、作者」字段，并重跑 `makemigrations` + `migrate`。

---

## 本章小结

**速查表**

| 主题 | 关键点 |
| --- | --- |
| Web 客户端 / 服务端 | 客户端 = 浏览器（交互 + 展示）；服务端 = 处理请求、查库、返回数据 |
| HTTP 三样数据 | 协议头（含 GET/POST 请求方式）、包体、状态码 |
| 起静态服务器 | `python3 -m http.server [端口]`（Python 内置 `http.server`） |
| Web 框架作用 | 让代码有层次、松耦合、不累赘；MVC 与 MTV 本质相同 |
| MVC | Model（对象↔数据库）/ View（逻辑+交互）/ Controller（请求→视图） |
| Django MTV | Model（同 MVC）、Template（页面）、View（≈ 控制器） |
| Django 四件套 | URL 处理、视图、模型、模板 |
| 建项目 / 建应用 | `django-admin startproject X`；`python3 manage.py startapp Y` |
| 注册应用 | 在 `settings.py` 的 `INSTALLED_APPS` 里加 `'Y'` |
| 模型迁移 | 改 `models.py` → `makemigrations` → `migrate` |
| 注册后台 | `admin.py` 里 `admin.site.register(Model, ModelAdmin)` |
| 优化后台列表 | `list_display = ("字段名",)` |
| 视图渲染 | `render(request, '模板.html', context)` |
| 路由映射 | `path('前缀/', include('app.urls'))` + `path('', views.index)` |
| 起服务 | `python3 manage.py runserver [IP:端口]` |

**三句话**

1. **客户端管展示、服务端管处理**——一切 Web 开发都从这条分工出发。
2. **Django 用 MTV 分层**：模型管数据、模板管页面、视图管逻辑，URL 负责把请求接进来。
3. **跑通 Blog 就四步**：建项目应用 → 写 model 并迁移 → 注册 admin 传数据 → 写 view+template 展示。

**动手练习**

1. 用 `http.server` 把某目录发布到 8080 端口，用手机（同一局域网）访问验证。
2. 把本章 `mysite98` 起的服务器截图，确认 Django 欢迎页。
3. 给 `mysite/myblog` 的 `Article` 增加「类别、作者」字段，迁移后在新版本后台录入并展示。
4. 把 `/myblog/` 的展示逻辑改成「按发布日期倒序」，让最新的文章排最上面。

---

## 下一章预告

下一章进入 **计算机视觉**：用 Python + OpenCV 打开摄像头，做**人脸识别**。
你会学到读取视频流、加载人脸分类器、在画面上框出人脸——同样需要摄像头等硬件，届时的示例也会照实标注是否实跑。

---

[← 上一章：办公自动化](/guide/office-automation) ｜ [返回总目录](/) ｜ [下一章：计算机视觉 →](/guide/face-recognition)

# 零基础学 Python 中文精读

> 把开源课程《零基础学 Python》（<https://gitee.com/wilsonyin/zero-basics-python>）的 **PPT + 配套代码**，按官方 117 讲目录重排成一本中文电子书。

- 🌐 在线电子书：<https://cleversnail.github.io/zero-basics-python/>
- 📦 源码仓库（二选一，内容一致）：
  - GitHub：<https://github.com/cleversnail/zero-basics-python>
  - Gitee：<https://gitee.com/snail_wn/zero-basics-python>
- 📄 原始课程仓库：<https://gitee.com/wilsonyin/zero-basics-python>（PPT / 代码，LGPL-2.1）

## 这本书是什么

原课程是 117 讲视频，每一讲配一份 PPT 和一节代码。这份电子书把它们逐讲整理成**可读、可查、可复现**的图文：

- **每讲一节**：本节目标 → 知识要点 → 代码实操 → 避坑提示 → 课后作业
- **讲号与课程完全一致**：第 12 讲就是视频里的第 12 讲
- **每个示例都给完整代码 + 运行命令 + 真实终端输出**，不用 `...` 省略
- 全中文，照顾**没写过代码**的人：环境安装、IDE、查官方文档、读报错都在第一章讲透

## 目录（15 章 · 117 讲）

| 章 | 标题 | 讲号 | 讲数 |
| --- | --- | --- | --- |
| 开篇 | 课程综述 | — | — |
| 第 1 章 | 入门的第一道门槛 —— 非计算机专业学习编程的第一道门槛 | 001–007 | 7 |
| 第 2 章 | Python 编程基础知识 | 008–017 | 10 |
| 第 3 章 | 内置数据类型 | 018–031 | 14 |
| 第 4 章 | 判断与循环 | 032–039 | 8 |
| 第 5 章 | 输入输出与文件操作 | 040–048 | 9 |
| 第 6 章 | 函数 | 049–057 | 9 |
| 第 7 章 | 类 | 058–065 | 8 |
| 第 8 章 | 模块与标准库 | 066–071 | 6 |
| 第 9 章 | 异常 | 072–076 | 5 |
| 第 10 章 | 高级数据类型与算法 | 077–086 | 10 |
| 第 11 章 | 数据分析：数据采集、处理与展示 | 087–093 | 7 |
| 第 12 章 | 办公自动化：批量文件处理 | 094–098 | 5 |
| 第 13 章 | Web 开发：编写自己的个人 Blog | 099–104 | 6 |
| 第 14 章 | 计算机视觉：使用 Python 进行人脸识别 | 105–110 | 6 |
| 第 15 章 | 物联网：通过手机远程获取室内温度 | 111–117 | 7 |

## 快速开始

```bash
# 1. 克隆源码（GitHub / Gitee 二选一，两个仓库内容一致，都是同名目录 zero-basics-python）
git clone https://github.com/cleversnail/zero-basics-python.git
# git clone https://gitee.com/snail_wn/zero-basics-python.git
cd zero-basics-python

# 2. 本地看文档
npm install
npm run docs:dev            # → http://localhost:5173

# 3. 跑某一章的示例
cd 03-data-types/code
python3 19-list.py

# 4. 全量校验所有示例是否真能跑通
cd ../.. && npm run verify
```

## 怎么读

1. **完全没写过代码**：从 [开篇 · 课程综述](./00-intro/README.md) 和第 1 章读起，先把环境装好。
2. **有点基础想查漏**：直接跳到对应章，每讲末尾都有速查表。
3. **只想做项目**：第 11–15 章是五个实战方向，挑感兴趣的看。

## 运行环境

- **Python 3.10 及以上**（推荐 3.11 / 3.12）
  - 第 14 章人脸识别部分，课程用的是 Python 3.9（OpenCV 相关依赖对版本敏感），会在该章说明
- 依赖按章安装，各章 `code/requirements.txt` 里列了需要额外安装的第三方库
- 基础语法章节（第 1–9 章）**不需要**任何第三方依赖，装了 Python 就能跑

## 仓库结构

```
zero-basics-python-cn/
├── 00-intro/                 开篇 · 课程综述
├── 01-getting-started/       第 1 章：环境、IDE、官方文档、Git、调试
│   ├── README.md               本章正文（一讲一节）
│   └── code/                   本章示例代码
├── ...                       第 2–15 章结构同上
├── GLOSSARY.md               术语表（中英对照 + 易混淆概念）
├── docs/                     VitePress 站点
├── scripts/                  同步 / 校验 / 部署脚本
└── README.md                 本文件
```

## 本地运行

```bash
# 1. 看文档站点
npm install
npm run docs:dev          # 打开 http://localhost:5173

# 2. 跑示例代码（以第 1 章为例）
cd 01-getting-started/code
python3 01-hello.py

# 3. 全量校验示例是否都能跑通
npm run verify
```

## 许可

- **原始课程的 PPT 与代码**：LGPL-2.1，来自 <https://gitee.com/wilsonyin/zero-basics-python>
- **本中文精读版**：是上述课程内容的整理、重排与复现（衍生作品），因此沿用同一许可证
  **LGPL-2.1**，全文见 [LICENSE](./LICENSE)。正文文字为本项目原创撰写，代码示例源自并改造自原课程仓库。

> ⚠️ 如需商用，请先阅读 LGPL-2.1 条款，并自行确认上游课程内容的授权范围。

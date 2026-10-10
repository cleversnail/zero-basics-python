---
layout: home

hero:
  name: 零基础学 Python
  text: 中文精读笔记
  tagline: 15 章 · 117 讲 · 每讲配中文讲解与真实可运行的代码
  actions:
    - theme: brand
      text: 从课程综述开始
      link: /guide/intro
    - theme: alt
      text: 术语表
      link: /glossary

features:
  - icon: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>'
    title: 按讲精读
    details: 严格对齐课程目录：15 章 117 讲，每讲一节，讲号与课程一致，方便边看视频边对照。

  - icon: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>'
    title: 代码真能跑
    details: 每个示例都给完整代码 + 运行命令 + 真实终端输出，不用「…」省略，复制就能跑。

  - icon: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 8v4l3 2"/></svg>'
    title: 从零门槛讲起
    details: 环境安装、IDE 选择、官方文档怎么查、报错怎么读，第一步就照顾没写过代码的人。

  - icon: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2 2 7l10 5 10-5-10-5z"/><path d="m2 17 10 5 10-5"/><path d="m2 12 10 5 10-5"/></svg>'
    title: 基础知识全覆盖
    details: 变量、数据类型、判断循环、函数、类、模块、异常——一门语言真正要用的东西都在。

  - icon: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>'
    title: 五个实战项目
    details: 数据分析、办公自动化、Django 博客、人脸识别、ESP32 物联网，学完能做出东西。

  - icon: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>'
    title: 避坑与小试牛刀
    details: 每个知识单元都有「避坑指南」讲常见错误、「小试牛刀」用一个小项目把知识点串起来。
---

## 这本书是什么

这是把开源课程《零基础学 Python》的 **PPT 与配套代码**，按官方目录重排成的中文电子书。

原课程的开源仓库在 Gitee：<https://gitee.com/wilsonyin/zero-basics-python>（PPT / 代码，LGPL-2.1）。

原课程是 117 讲视频；这本书把它们逐讲整理成可读、可查、可复现的图文：

- **每讲一节**：本节目标 → 知识要点 → 代码实操 → 避坑提示 → 课后作业
- **讲号与课程一致**：第 12 讲就是视频里的第 12 讲，方便对照着看
- **代码全部来自课程仓库**，整理成可直接运行的脚本，并附真实运行输出

## 怎么用这本书

1. **完全没写过代码**：从 [课程综述](/guide/intro) 和第 1 章读起，先装好环境。
2. **有点基础想查漏**：直接跳到对应章，每讲末尾都有速查表。
3. **只想做项目**：第 11–15 章是五个实战方向，可以挑感兴趣的看。

> 💡 全书假设你用的是 **Python 3.10 及以上**。第 14 章人脸识别部分课程用的是 Python 3.9，会在对应章节说明。

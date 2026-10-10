import { defineConfig } from "vitepress";

/**
 * VitePress 配置 —— 参考 vuejs.org 官方站点的信息架构：
 * 顶栏导航 + 左侧目录 + 右侧大纲 + 本地搜索。
 *
 * 内容来源：开源课程《零基础学 Python》的 PPT 与配套代码
 * （gitee.com/wilsonyin/zero-basics-python），按官方 117 讲目录重排为中文电子书。
 */
export default defineConfig({
  lang: "zh-CN",
  title: "零基础学 Python 中文精读",
  description:
    "跟着开源课程《零基础学 Python》走一遍：15 章 117 讲，从环境搭建到物联网，每讲配中文讲解与真实可运行的 Python 代码。",

  // 始终使用浅色（青绿主题）。设为 false = 关闭深色模式。
  appearance: false,

  // base 取决于部署目标，用环境变量控制，避免不同平台互相打架：
  //   GitHub Pages 项目站点 = 子路径
  //   自有域名 / 腾讯云 CloudBase = 根路径，构建时设 DOCS_BASE=/
  base: process.env.DOCS_BASE ?? "/zero-basics-python/",

  cleanUrls: true,

  // 死链检查：默认严格（有死链就构建失败）。
  // 写书过程中章节尚未补齐时，可用 DOCS_IGNORE_DEADLINKS=1 临时放宽；成书后必须不带该变量构建。
  ignoreDeadLinks: process.env.DOCS_IGNORE_DEADLINKS === "1",

  markdown: {
    lineNumbers: true,
    theme: { light: "github-light", dark: "github-dark" },
  },

  head: [["meta", { name: "theme-color", content: "#0d9488" }]],

  themeConfig: {
    logo: "/logo.svg",

    nav: [
      { text: "首页", link: "/" },
      { text: "教程", link: "/guide/intro", activeMatch: "/guide/" },
      { text: "术语表", link: "/glossary" },
      { text: "源码", link: "https://github.com/cleversnail/zero-basics-python" },
    ],

    sidebar: {
      "/guide/": [
        {
          text: "开始",
          items: [
            { text: "开篇 · 课程综述", link: "/guide/intro" },
            { text: "第 1 章 · 入门的第一道门槛", link: "/guide/getting-started" },
          ],
        },
        {
          text: "编程基础",
          items: [
            { text: "第 2 章 · Python 编程基础知识", link: "/guide/python-basics" },
            { text: "第 3 章 · 内置数据类型", link: "/guide/data-types" },
            { text: "第 4 章 · 判断与循环", link: "/guide/control-flow" },
          ],
        },
        {
          text: "输入输出与函数",
          items: [
            { text: "第 5 章 · 输入输出与文件操作", link: "/guide/io-and-files" },
            { text: "第 6 章 · 函数", link: "/guide/functions" },
          ],
        },
        {
          text: "面向对象与模块",
          items: [
            { text: "第 7 章 · 类", link: "/guide/classes" },
            { text: "第 8 章 · 模块与标准库", link: "/guide/modules" },
            { text: "第 9 章 · 异常", link: "/guide/exceptions" },
          ],
        },
        {
          text: "进阶",
          items: [
            { text: "第 10 章 · 高级数据类型与算法", link: "/guide/advanced" },
          ],
        },
        {
          text: "项目实战",
          items: [
            { text: "第 11 章 · 数据分析", link: "/guide/data-analysis" },
            { text: "第 12 章 · 办公自动化", link: "/guide/office-automation" },
            { text: "第 13 章 · Web 开发（Django）", link: "/guide/web" },
            { text: "第 14 章 · 计算机视觉（人脸识别）", link: "/guide/face-recognition" },
            { text: "第 15 章 · 物联网（ESP32）", link: "/guide/iot" },
          ],
        },
        {
          text: "附录",
          items: [{ text: "术语表", link: "/glossary" }],
        },
      ],
    },

    outline: {
      level: [2, 3],
      label: "本页目录",
    },

    search: {
      provider: "local",
      options: {
        translations: {
          button: { buttonText: "搜索文档", buttonAriaLabel: "搜索文档" },
          modal: {
            noResultsText: "没有找到相关结果",
            resetButtonTitle: "清除查询条件",
            footer: {
              selectText: "选择",
              navigateText: "切换",
              closeText: "关闭",
            },
          },
        },
      },
    },

    docFooter: { prev: "上一章", next: "下一章" },
    returnToTopLabel: "回到顶部",
    sidebarMenuLabel: "目录",
    darkModeSwitchLabel: "主题",
    lightModeSwitchTitle: "切换到浅色模式",
    darkModeSwitchTitle: "切换到深色模式",

    footer: {
      message:
        "内容基于开源课程《零基础学 Python》的 PPT 与配套代码（gitee.com/wilsonyin/zero-basics-python，LGPL-2.1）整理并重排为中文学习路径",
      copyright: "本中文版仅供学习使用",
    },
  },
});

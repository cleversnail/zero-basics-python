#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
把各章 README.md 同步到 VitePress 站点目录 docs/guide/。

为什么需要它：
  章节目录里的 README.md 是「仓库里读到」的版本，末尾导航行用的是仓库内相对路径
  （如 ../01-getting-started/README.md）；而站点里的同一篇要用站点路径（如 /guide/getting-started）。
  两边内容必须一致，手工维护必然漂移，所以用脚本做单一事实源同步。

用法：
  python3 scripts/sync-docs.py      （或 npm run docs:sync）

规则：
  - 逐章读取 <章节目录>/README.md，写入 docs/guide/<slug>.md
  - 只改写「末尾那一行导航」，正文一个字不动
  - GLOSSARY.md → docs/glossary.md（只改指向仓库文件的相对链接，正文不动）
"""
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (章节目录, 站点 slug, 上一章文本, 上一章链接, 下一章文本, 下一章链接)
CHAPTERS = [
    ("00-intro",              "intro",             None,                   None,
                              "入门的第一道门槛",      "/guide/getting-started"),
    ("01-getting-started",    "getting-started",   "课程综述",              "/guide/intro",
                              "Python 编程基础知识",   "/guide/python-basics"),
    ("02-python-basics",      "python-basics",     "入门的第一道门槛",      "/guide/getting-started",
                              "内置数据类型",          "/guide/data-types"),
    ("03-data-types",         "data-types",        "Python 编程基础知识",   "/guide/python-basics",
                              "判断与循环",            "/guide/control-flow"),
    ("04-control-flow",       "control-flow",      "内置数据类型",          "/guide/data-types",
                              "输入输出与文件操作",    "/guide/io-and-files"),
    ("05-io-and-files",       "io-and-files",      "判断与循环",            "/guide/control-flow",
                              "函数",                  "/guide/functions"),
    ("06-functions",          "functions",         "输入输出与文件操作",    "/guide/io-and-files",
                              "类",                    "/guide/classes"),
    ("07-classes",            "classes",           "函数",                  "/guide/functions",
                              "模块与标准库",          "/guide/modules"),
    ("08-modules",            "modules",           "类",                    "/guide/classes",
                              "异常",                  "/guide/exceptions"),
    ("09-exceptions",         "exceptions",        "模块与标准库",          "/guide/modules",
                              "高级数据类型与算法",    "/guide/advanced"),
    ("10-advanced",           "advanced",          "异常",                  "/guide/exceptions",
                              "数据分析",              "/guide/data-analysis"),
    ("11-data-analysis",      "data-analysis",     "高级数据类型与算法",    "/guide/advanced",
                              "办公自动化",            "/guide/office-automation"),
    ("12-office-automation",  "office-automation", "数据分析",              "/guide/data-analysis",
                              "Web 开发",              "/guide/web"),
    ("13-web",                "web",               "办公自动化",            "/guide/office-automation",
                              "计算机视觉",            "/guide/face-recognition"),
    ("14-face-recognition",   "face-recognition",  "Web 开发",              "/guide/web",
                              "物联网",                "/guide/iot"),
    ("15-iot",                "iot",               "计算机视觉",            "/guide/face-recognition",
                              "术语表",                "/glossary"),
]

NAV_RE = re.compile(
    r"^\[(?:(← 上一章：.*?)｜\s*)?\[返回总目录\]\([^)]*\)(?:\s*｜\s*\[下一章：.*?→\]\([^)]*\))?\s*$"
)

# 章节正文里的图片引用：`![说明](code/xxx.png)`。
# 仓库里读得通，但站点 docs/guide/ 下没有 code/ 目录，必须重写到 /img/ 并同步文件。
IMG_RE = re.compile(r"\]\(\.?/?(code/[^)\s]+\.(?:png|jpe?g|gif|webp|svg))\)")
IMG_SRC_RE = re.compile(r"\.?/?(code/[^)\s]+\.(?:png|jpe?g|gif|webp|svg))")


def rewrite_images(text: str) -> str:
    """把仓库内相对图片路径重写成站点路径 /img/<文件名>。"""
    return IMG_RE.sub(lambda m: "](/img/" + os.path.basename(m.group(1)) + ")", text)


# 《提问的智慧》在本站是独立页面，仓库里指向它的相对链接要改写成站点路径
LINKS = [
    ("](./How-To-Ask-Questions-The-Smart-Way.md)", "(/guide/how-to-ask-questions)"),
    ("](How-To-Ask-Questions-The-Smart-Way.md)", "(/guide/how-to-ask-questions)"),
]


def rewrite_links(text: str) -> str:
    for old, new in LINKS:
        text = text.replace(old, new)
    return text


def sync_howto():
    """把《提问的智慧》发布到站点。

    这份第三方文档自带几个指向它自己 GitHub 仓库的小链接（README.md / history.md /
    两个邮件地址），在本站没有对应页面，会触发 VitePress 死链检查；发布时把它们
    降级为纯文本（原文链接语义仍在，只是不再可点）。
    """
    src = os.path.join(ROOT, "00-intro", "How-To-Ask-Questions-The-Smart-Way.md")
    dst = os.path.join(ROOT, "docs", "guide", "how-to-ask-questions.md")
    if not os.path.exists(src):
        return None
    text = open(src, encoding="utf-8").read()
    for bad in ("README.md", "history.md", "esr@thyrsus.com", "respond-auto@linuxmafia.com"):
        text = text.replace(f"[{bad}]({bad})", bad)
        text = text.replace(f"[繁體中文版]({bad})", "繁體中文版")
        text = text.replace(f"[原文版本历史]({bad})", "原文版本历史")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    return dst


def sync_images(chapter_readmes):
    """把章节 README 里引用到的 code/ 图片拷进 docs/public/img/。"""
    outdir = os.path.join(ROOT, "docs", "public", "img")
    os.makedirs(outdir, exist_ok=True)
    copied, missing = [], []
    for dirname in chapter_readmes:
        readme = os.path.join(ROOT, dirname, "README.md")
        if not os.path.exists(readme):
            continue
        text = open(readme, encoding="utf-8").read()
        for rel in IMG_SRC_RE.findall(text):
            src = os.path.join(ROOT, dirname, rel)
            if os.path.exists(src):
                shutil.copy2(src, os.path.join(outdir, os.path.basename(rel)))
                copied.append(os.path.basename(rel))
            else:
                missing.append(f"{dirname}/{rel}")
    return copied, missing


def build_nav(prev_text, prev_link, next_text, next_link) -> str:
    parts = []
    if prev_text and prev_link:
        parts.append(f"[← 上一章：{prev_text}]({prev_link})")
    parts.append("[返回总目录](/)")
    if next_text and next_link:
        label = "附录" if next_text == "术语表" else "下一章"
        parts.append(f"[{label}：{next_text} →]({next_link})")
    return " ｜ ".join(parts)


def sync_chapter(dirname, slug, prev_text, prev_link, next_text, next_link):
    src = os.path.join(ROOT, dirname, "README.md")
    dst = os.path.join(ROOT, "docs", "guide", slug + ".md")
    if not os.path.exists(src):
        print(f"  ⏭  {dirname}/README.md 尚未编写，跳过")
        return None, None
    with open(src, encoding="utf-8") as f:
        lines = f.read().rstrip("\n").split("\n")

    nav = build_nav(prev_text, prev_link, next_text, next_link)
    if lines and lines[-1].lstrip().startswith("[") and "返回总目录" in lines[-1]:
        lines[-1] = nav
    else:
        lines += ["", "---", "", nav]

    body = rewrite_links(rewrite_images("\n".join(lines)))
    with open(dst, "w", encoding="utf-8") as f:
        f.write(body + "\n")
    return dst, nav


def sync_glossary():
    src = os.path.join(ROOT, "GLOSSARY.md")
    dst = os.path.join(ROOT, "docs", "glossary.md")
    with open(src, encoding="utf-8") as f:
        text = f.read()
    text = text.replace("](../README.md)", "](/")
    text = text.replace("](../GLOSSARY.md)", "](/glossary)")
    # 《提问的智慧》在站点里是独立页面
    text = text.replace(
        "(./How-To-Ask-Questions-The-Smart-Way.md)", "(/guide/how-to-ask-questions)"
    )
    for dirname, slug, *_ in CHAPTERS:
        text = text.replace(f"](../{dirname}/README.md)", f"](/guide/{slug})")
        text = text.replace(f"](../{dirname}/README.md#", f"](/guide/{slug}#")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    return dst


def main():
    made = []
    for ch in CHAPTERS:
        dst, nav = sync_chapter(*ch)
        if dst is None:
            continue
        made.append(dst)
        print(f"  ✅ {os.path.relpath(dst, ROOT)}")
        print(f"     └─ {nav}")
    dst = sync_glossary()
    made.append(dst)
    print(f"  ✅ {os.path.relpath(dst, ROOT)}")

    dst = sync_howto()
    if dst:
        made.append(dst)
        print(f"  ✅ {os.path.relpath(dst, ROOT)}")

    copied, missing = sync_images([c[0] for c in CHAPTERS])
    if copied:
        print(f"  🖼  图片同步到 docs/public/img/：{', '.join(sorted(set(copied)))}")
    if missing:
        print(f"  ⚠️  引用但找不到的图片：{', '.join(missing)}")

    print(f"\n共同步 {len(made)} 个文件。")
    return 0


if __name__ == "__main__":
    sys.exit(main())

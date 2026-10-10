#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
站点内容体检：在 npm run docs:build 之前先抓出「能构建通过、但页面会坏/会缺内容」的坑。

目前检查一条（都是真实踩过的）：
  行内代码里的 Vue 插值：`{{ xxx }}`
    VitePress 只对**围栏代码块**自动加 v-pre，行内 `<code>{{ }}</code>` 会被 Vue 当表达式求值。
    轻则渲染成空白，重则 SSR 直接抛错、**页面内容被截断**（第 13 章就整页丢过一半）。
    正确写法：<code v-pre>{{ 变量 }}</code>
    或者干脆改成围栏代码块。

用法：
  python3 scripts/lint-docs.py     （全量检查所有章节目录的 README.md）
  npm run lint
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTER_RE = re.compile(r"^(\d\d)-")

FENCE_RE = re.compile(r"^\s*(```|~~~)")
INLINE_CODE_RE = re.compile(r"`[^`]*\{\{[^`]*`[^`]*`")
ANY_INTERP_RE = re.compile(r"\{\{")


def check_file(path):
    problems = []
    in_fence = False
    for lineno, line in enumerate(open(path, encoding="utf-8"), 1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        # 已经被 v-pre 保护的不算问题
        if "v-pre" in line:
            continue
        if ANY_INTERP_RE.search(line):
            problems.append(
                (lineno, line.strip()[:110])
            )
    return problems


def main():
    targets = [os.path.join(ROOT, "README.md"), os.path.join(ROOT, "GLOSSARY.md")]
    for name in sorted(os.listdir(ROOT)):
        if not CHAPTER_RE.match(name) or not os.path.isdir(os.path.join(ROOT, name)):
            continue
        readme = os.path.join(ROOT, name, "README.md")
        if os.path.exists(readme):
            targets.append(readme)

    total = 0
    for path in targets:
        problems = check_file(path)
        if problems:
            total += len(problems)
            print(f"❌ {os.path.relpath(path, ROOT)}")
            for lineno, text in problems:
                print(f"     L{lineno}: {text}")
    if total:
        print(
            f"\n共 {total} 处行内 Vue 插值 `{{{{ }}}}`——会被 Vue 当表达式求值，"
            "可能导致页面内容缺失。改用 <code v-pre>…</code> 或围栏代码块。"
        )
        return 1
    print(f"✅ 体检通过：{len(targets)} 个文件，无行内 Vue 插值风险。")
    return 0


if __name__ == "__main__":
    sys.exit(main())

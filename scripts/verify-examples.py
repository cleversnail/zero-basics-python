#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
逐个真跑各章 code/*.py，判定「书里的示例到底能不能跑通」。

三档判定（沿用本系列前两本的标准）：
  ✅ PASS    exit=0，且（若脚本里有 print）确实有输出
  ⚠️ SUSPECT exit=0 但脚本里明明有 print 却一行都没输出 —— 这类 bug 不报错、只是安静地错
  ❌ FAIL    非零退出 / 超时 / 运行时报错

有些示例是「故意演示错误」（语法错误、异常捕获、避坑指南），非零退出是**正常**的，
把它们登记在 ALLOW_FAIL 里放行；需要外部服务/硬件的示例登记在 SKIP 里默认跳过。

用法：
  python3 scripts/verify-examples.py            # 全量
  python3 scripts/verify-examples.py 03         # 只跑第 3 章
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 「故意演示错误」的示例：非零退出属正常
ALLOW_FAIL = {
    "01-getting-started/code/02-syntax-error.py",
    # 第 3 章 29 讲「避坑指南」：每个文件故意触发一种内置数据类型错误
    "03-data-types/code/29-index-error.py",
    "03-data-types/code/29-key-error.py",
    "03-data-types/code/29-type-error.py",
    "03-data-types/code/29-attr-error.py",
    "03-data-types/code/29-unhashable.py",
    # 第 4 章 38 讲「避坑指南」：遍历中 pop 导致索引越界
    "04-control-flow/code/38-pitfalls-pop.py",
    # 第 7 章 63 讲「避坑指南」：忘记写 self / staticmethod 误用 self
    "07-classes/code/63-no-self.py",
    "07-classes/code/63-self-cls.py",
    # 第 9 章 75 讲「避坑指南」：try 缺 except 的语法错误演示（解析阶段即失败）
    "09-exceptions/code/75b-nested-syntax-error.py",
}

# 需要外部服务 / 硬件 / 需手动交互的示例：默认跳过（在正文里标注「未实跑」）
SKIP = {
    # pdb 是交互式调试器，非交互喂 stdin 会以 BdbQuit 退出；正文里给的是真实手工会话
    "01-getting-started/code/03-pdb-demo.py",
}

TIMEOUT = 30


def find_examples(only=None):
    out = []
    for name in sorted(os.listdir(ROOT)):
        m = re.match(r"^(\d\d)-", name)
        if not m or not os.path.isdir(os.path.join(ROOT, name)):
            continue
        if only and not name.startswith(only):
            continue
        codedir = os.path.join(ROOT, name, "code")
        if not os.path.isdir(codedir):
            continue
        for fn in sorted(os.listdir(codedir)):
            if fn.endswith(".py"):
                out.append(os.path.relpath(os.path.join(codedir, fn), ROOT))
    return out


def run(rel):
    path = os.path.join(ROOT, rel)
    src = open(path, encoding="utf-8", errors="replace").read()
    has_print = bool(re.search(r"\bprint\s*\(", src))
    try:
        p = subprocess.run(
            [sys.executable, os.path.basename(path)],
            cwd=os.path.dirname(path),
            input="",
            capture_output=True,
            text=True,
            timeout=TIMEOUT,
        )
        out = (p.stdout or "") + (p.stderr or "")
        rc = p.returncode
    except subprocess.TimeoutExpired:
        return "FAIL", "超时（可能卡在 input() 或服务监听）"
    except Exception as e:  # noqa: BLE001
        return "FAIL", f"无法运行：{e}"

    if rc != 0:
        if rel in ALLOW_FAIL:
            return "ALLOW", "故意演示错误，非零退出属正常"
        first = [l for l in out.splitlines() if l.strip()][-1:] or ["(无输出)"]
        return "FAIL", f"exit={rc} · {first[0][:90]}"

    if has_print and not out.strip():
        return "SUSPECT", "exit=0 但脚本里有 print 却无任何输出"
    return "PASS", out.strip().splitlines()[-1][:70] if out.strip() else "(无输出)"


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    examples = find_examples(only)
    if not examples:
        print("没找到任何 code/*.py")
        return 1

    counts = {"PASS": 0, "SUSPECT": 0, "FAIL": 0, "ALLOW": 0, "SKIP": 0}
    bad = []
    for rel in examples:
        if rel in SKIP:
            counts["SKIP"] += 1
            print(f"  ⏭️  SKIP    {rel}")
            continue
        status, msg = run(rel)
        counts[status] += 1
        icon = {"PASS": "✅", "SUSPECT": "⚠️", "FAIL": "❌", "ALLOW": "🟡"}[status]
        print(f"  {icon} {status:7s} {rel}  —— {msg}")
        if status in ("FAIL", "SUSPECT"):
            bad.append((rel, status, msg))

    print("\n" + "=" * 60)
    print(
        f"共 {len(examples)} 个示例："
        f"✅ {counts['PASS']} 通过 · "
        f"🟡 {counts['ALLOW']} 故意报错 · "
        f"⚠️ {counts['SUSPECT']} 可疑 · "
        f"❌ {counts['FAIL']} 失败 · "
        f"⏭️ {counts['SKIP']} 跳过"
    )
    if bad:
        print("\n需要处理：")
        for rel, status, msg in bad:
            print(f"  {status}: {rel} —— {msg}")
        return 1
    print("全部达标 🎉")
    return 0


if __name__ == "__main__":
    sys.exit(main())

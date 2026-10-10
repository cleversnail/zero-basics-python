#!/bin/bash
# 构建并发布 VitePress 站点到腾讯云 CloudBase 静态托管
#
# 用法：npm run deploy:tencent  或  bash scripts/deploy-tencent.sh
# 前置：本机已装 tcb CLI 并登录过（tcb login），且已有环境（env）。
#
# 两个坑（都实测踩过）：
#   1. 本机 npm 全局前缀是 /usr/local，`npm install -g` 会报 EACCES；
#      也不要裸跑 `npx @cloudbase/cli`（找不到 bin，可执行名是 tcb）。
#      统一用：npx --yes -p @cloudbase/cli tcb ...
#   2. 未登录的 tcb **不会报错**，而是进入设备授权流程、一直卡住（实测静默挂 7 分钟）。
#      所以先探一次 `tcb env list`，探不通就退出并给出提示。
set -euo pipefail
cd "$(dirname "$0")/.."

ENV_ID="${TCB_ENV_ID:-}"
if [ -z "$ENV_ID" ]; then
  echo "⚠️ 请先设置环境 ID：TCB_ENV_ID=<你的环境id> npm run deploy:tencent"
  exit 1
fi

TCB() { npx --yes -p @cloudbase/cli tcb "$@"; }

echo "▶ [0/5] 探测 tcb 登录状态（未登录会进入设备授权并卡住，必须先探）"
if ! timeout 20 npx --yes -p @cloudbase/cli tcb env list >/tmp/tcb-probe.txt 2>&1; then
  echo "❌ tcb 未登录或不可用。请先在本机执行："
  echo "     npx --yes -p @cloudbase/cli tcb login"
  echo "   然后重跑本脚本。探测输出："
  sed 's/^/     /' /tmp/tcb-probe.txt | head -5
  exit 1
fi
echo "  ✅ tcb 可用"

echo "▶ [1/5] 同步文档"
python3 scripts/sync-docs.py

echo "▶ [2/5] 构建站点（CloudBase 是根路径，所以 DOCS_BASE=/）"
DOCS_BASE=/ npm run docs:build

echo "▶ [3/5] 部署 docs/.vitepress/dist 到环境 $ENV_ID"
TCB hosting deploy docs/.vitepress/dist -e "$ENV_ID" --verify

echo "▶ [4/5] 完成"
echo ""
echo "✅ 已发布到腾讯云 CloudBase（环境：$ENV_ID）"
echo "   静态托管默认域名形如：https://<envId>.tcloudbaseapp.com/"
echo "   提示：CDN 生效通常还要 1~3 分钟。"

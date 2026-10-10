#!/bin/bash
# 配好 Gitee + GitHub 双远端，并把 main 推上去
#
# 用法：
#   bash scripts/setup-gitee-remote.sh https://gitee.com/<你的用户名>/zero-basics-python.git
#
# 做的事：
#   1. 确认 Gitee 仓库真的存在（存在才继续，不存在直接报错退出，不会建空远端）
#   2. origin 配成「一次 push 双发 Gitee + GitHub」
#   3. 推 main，并核对两个远端的 SHA 是否一致
#
# 注意：Gitee 凭据走 macOS 钥匙串（git credential-osxkeychain），
#       不要把令牌写进 argv 或 .git/config。
set -euo pipefail
cd "$(dirname "$0")/.."

GITEE_URL="${1:-}"
GH_SLUG="cleversnail/zero-basics-python"
GH_URL="https://github.com/${GH_SLUG}.git"

if [ -z "$GITEE_URL" ]; then
  echo "用法：bash scripts/setup-gitee-remote.sh https://gitee.com/<用户名>/zero-basics-python.git"
  exit 1
fi

echo "▶ [1/4] 确认 Gitee 仓库存在：$GITEE_URL"
if ! git ls-remote --heads "$GITEE_URL" >/dev/null 2>&1; then
  echo "❌ 读不到这个仓库（名字不对 / 还没创建 / 凭据无效）。"
  echo "   请先在 https://gitee.com/projects/new 创建空仓库（不要勾选自动生成 README，保持空倉）。"
  exit 1
fi
echo "  ✅ 仓库可访问"

echo "▶ [2/4] 配置 origin（一条 push 同时发 Gitee + GitHub）"
git remote set-url origin "$GITEE_URL"
git remote set-url --add --push origin "$GITEE_URL"
git remote set-url --add --push origin "$GH_URL"
git remote set-url github "$GH_URL"
echo "  origin:"
git remote -v | sed 's/^/    /'

echo "▶ [3/4] 推送 main 到两个远端"
git push origin main

echo "▶ [4/4] 核对两端 SHA"
LOCAL=$(git rev-parse main)
G=$(git ls-remote origin main | awk '{print $1}')
H=$(git ls-remote github main | awk '{print $1}')
printf '  本地      %s\n  Gitee     %s\n  GitHub    %s\n' "${LOCAL:0:7}" "${G:0:7}" "${H:0:7}"
if [ "$LOCAL" = "$G" ] && [ "$LOCAL" = "$H" ]; then
  echo "  ✅ 三处 SHA 一致"
else
  echo "  ⚠️ SHA 不一致，请检查推送输出"
  exit 1
fi

echo ""
echo "✅ 双远端就绪。以后一条命令即可双发：git push origin main"

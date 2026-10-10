#!/bin/bash
# 构建并发布 VitePress 站点到 GitHub Pages（gh-pages 分支）
#
# 用法：npm run deploy:github  或  bash scripts/deploy-github.sh
#
# 为什么不用 GitHub Actions：
#   本系列上一本（lang-chain-js-cn）配过工作流，但作业始终拿不到 runner
#   （runner_name / steps 均为空、几秒即失败），Actions 设置本身正常。
#   因此沿用「本地构建 → 推 gh-pages 分支」的做法，完全不依赖 Actions。
set -euo pipefail
cd "$(dirname "$0")/.."

# 换仓库名只改这一行
REPO_SLUG="cleversnail/zero-basics-python"
BRANCH_NAME="${REPO_SLUG#*/}"
SITE_URL="https://${REPO_SLUG%/*}.github.io/${BRANCH_NAME}/"

echo "▶ [0/6] 同步文档（章节目录 → docs/guide）"
python3 scripts/sync-docs.py

echo "▶ [1/6] 构建站点（base = /${BRANCH_NAME}/，GitHub Pages 子路径）"
npm run docs:build

echo "▶ [2/6] 暂存产物"
DIST=$(mktemp -d)
cp -R docs/.vitepress/dist/. "$DIST/"

echo "▶ [3/6] 准备 gh-pages 分支"
if git show-ref --verify --quiet refs/heads/gh-pages; then
  echo "  本地已有 gh-pages"
elif git ls-remote --exit-code --heads github gh-pages >/dev/null 2>&1; then
  echo "  从远端拉取 gh-pages"
  git fetch github gh-pages:gh-pages
else
  echo "  首次发布：新建 gh-pages 分支"
  git branch gh-pages
fi

WT=$(mktemp -d)
rmdir "$WT"
git worktree remove "$WT" --force 2>/dev/null || true
git worktree add -f "$WT" gh-pages >/dev/null

(
  cd "$WT"
  git rm -rq --ignore-unmatch .          # 清掉旧产物（含哈希名已变的旧资源）
  cp -R "$DIST/." .
  touch .nojekyll                        # 防止 Jekyll 干扰
  git add -A
  # 注意：VitePress 构建是**非确定性**的 —— 同样的输入，app.js 的分块哈希每次都会变。
  # 所以「无变化就跳过」的判断基本不会命中，每次发布会各产生一个提交。
  # 这无害（gh-pages 上的历史只用于发布，不影响站点内容）。
  if git diff --cached --quiet; then
    echo "  （站点内容无变化，跳过提交）"
  else
    git -c user.name="蜗牛" -c user.email="652501825@qq.com" \
        commit -q -m "deploy: 重新发布站点 $(date '+%Y-%m-%d %H:%M')"
    git push github gh-pages
    echo "  ✅ 已推送 gh-pages"
  fi
)
git worktree remove "$WT" --force
rm -rf "$DIST"

echo "▶ [4/6] 确认 Pages 已开启"
if gh api "repos/$REPO_SLUG/pages" >/dev/null 2>&1; then
  echo "  已开启"
else
  echo "  Pages 尚未开启，正在开启（source = gh-pages 分支根目录）"
  if gh api -X POST "repos/$REPO_SLUG/pages" \
       -f 'source[branch]=gh-pages' -f 'source[path]=/' >/dev/null 2>&1; then
    echo "  ✅ 已开启"
  else
    echo "  ⚠️ 自动开启失败，请去仓库 Settings → Pages 手动选 gh-pages 分支"
  fi
fi

echo "▶ [5/6] 触发 Pages 构建"
if gh api -X POST "repos/$REPO_SLUG/pages/builds" >/dev/null 2>&1; then
  echo "  已触发构建"
else
  echo "  ⚠️ 触发失败（可稍等自动构建，或去仓库 Pages 页手动重试）"
fi

echo "▶ [6/6] 等待发布结果（最多 90 秒）"
# 注意：一次发布会触发**两条**构建记录 —— 一条是 GitHub 重复触发、duration=0 立刻 errored，
# 另一条才是真正构建。所以不能只读一次状态（会读到那条假失败），要轮询到最新构建不再是
# building 为止。
build_status="unknown"
for _ in $(seq 1 18); do
  sleep 5
  build_status=$(gh api "repos/$REPO_SLUG/pages/builds?per_page=1" --jq '.[0].status' 2>/dev/null || echo "unknown")
  if [ "$build_status" != "building" ] && [ "$build_status" != "queued" ]; then
    break
  fi
  printf "."
done
echo ""
echo "  最新一次构建：$build_status"
gh api "repos/$REPO_SLUG/pages" --jq '"  Pages 站点状态: " + .status + "   url: " + .html_url' 2>/dev/null || true
if [ "$build_status" != "built" ]; then
  echo "  ⚠️ 构建未成功。去 Actions / Settings → Pages 看详情，或重跑 npm run deploy:github。"
fi

echo ""
echo "✅ 发布流程结束"
echo "   线上地址：$SITE_URL"
echo "   （CDN 生效通常还要 1~3 分钟；刚构建完时静态资源可能先 404 后恢复，属正常）"

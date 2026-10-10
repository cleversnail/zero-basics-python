# 部署

这本电子书的站点用 VitePress 构建，可以发布到多个静态托管平台。`base` 路径由环境变量
`DOCS_BASE` 控制，一份配置同时服务所有目标：

| 部署目标 | base | 说明 |
| --- | --- | --- |
| GitHub Pages（项目站点） | `/zero-basics-python/`（默认） | 子路径 |
| 腾讯云 CloudBase / 自有域名 | `/` | 根路径，构建时设 `DOCS_BASE=/` |

## 本地预览

```bash
npm install
npm run docs:dev          # 开发模式，热更新 → http://localhost:5173
# 或者
npm run docs:build && npm run docs:preview   # 预览构建产物 → http://localhost:4173/zero-basics-python/
```

## 发布前必做

```bash
npm run lint              # 站点内容体检（行内 Vue 插值等坑）
npm run verify            # 全量实跑所有 code/*.py
npm run docs:sync         # 章节目录 README → docs/guide（**改完正文必须跑**）
npm run docs:build        # 严格构建（有死链就失败）
```

> ⚠️ `docs/guide/*.md` 是从各章 `README.md` **生成**的副本。改了章节正文却忘了 `docs:sync`，
> 线上就会继续显示旧内容。把它和 `docs:build` 当成一个原子动作。

## GitHub Pages

```bash
npm run deploy:github
```

脚本做的事：同步 → 构建 → 把 `docs/.vitepress/dist/` 推进 `gh-pages` 分支 → 确认 Pages 已开启 →
触发构建 → 轮询到最新构建结束。

线上地址：<https://cleversnail.github.io/zero-basics-python/>

两个已知但无害的现象：

- **一次发布会触发两条构建记录**：一条是 GitHub 自动触发的 `duration: 0` / `errored` 假失败，
  另一条才是真构建。脚本读的是「最新一条」，所以不会被假失败误导。
- **构建完 1~3 分钟内，静态资源可能先 404 再恢复**：CDN 还没分发完，属正常。

## 腾讯云 CloudBase

```bash
TCB_ENV_ID=<你的环境id> npm run deploy:tencent
```

需要先 `npx --yes -p @cloudbase/cli tcb login`。脚本会先探一次登录状态——**未登录的 `tcb`
不报错，而是进入设备授权并一直卡住**，所以这一步不能省。

> CloudBase 是根路径托管，脚本会自动带上 `DOCS_BASE=/` 构建。

## 双远端（Gitee + GitHub）

本系列的习惯是**一次 push 同时发两个远端**。本仓库已配好：

```bash
# 已经配好了，下面是配置命令（换仓库名时才需要重跑）
git remote set-url --push origin https://gitee.com/snail_wn/zero-basics-python.git
git remote set-url --add --push origin https://github.com/cleversnail/zero-basics-python.git

git remote -v          # origin 应显示两条 (push)
git push origin main   # 一条命令 → Gitee + GitHub
```

首次换机器/换仓库名时，可用现成脚本一次配好并核对 SHA：

```bash
bash scripts/setup-gitee-remote.sh https://gitee.com/snail_wn/zero-basics-python.git
```

推送后**核对三个 SHA 是否一致**（本地 / Gitee / GitHub），"我推了"不算证据，SHA 一致才算。
这次两个远端的仓库名恰好相同，`git clone` 生成的本地目录都是 `zero-basics-python`；
若将来两端名字不同，写克隆说明时要**每个远端配各自的 `cd` 目标**。

# 博客项目路径说明

## 问题发现

2026-03-01 发现博客文章底部按钮样式不一致：
- 2 月 28 日（数字噪音）和 3 月 1 日（静默的必要性）使用单按钮样式
- 之前文章使用双按钮样式（← 返回博客列表 + 首页）

## 根本原因

### 1. 两个项目路径

博客项目存在于两个路径：
- `/home/admin/.openclaw/workspace/roco33.github.io` - OpenClaw 工作区路径
- `/home/admin/projects/roco33.github.io` - Cron 任务使用的路径

### 2. Cron 任务配置

Cron 任务（每日博客发布 - 05:23）配置使用 `/home/admin/projects/roco33.github.io`，但：
- AI 子代理创建文章时参考了旧文章作为模板
- 旧文章（2 月 18 日之前）使用单按钮样式（site-nav）
- 导致新文章继承了错误的样式

### 3. 路径同步问题

两个路径是同一个 Git 仓库的副本，但：
- 手动操作通常在 workspace 路径
- 自动任务在 projects 路径
- 需要定期同步

## 修正措施

### 1. 修正现有文章
已修正以下文章的底部按钮样式：
- `blog/2026/02/28/digital-noise/index.html`
- `blog/2026/03/01/silence-value/index.html`

### 2. 更新 Cron 任务提示词
在 Cron 任务提示词中明确要求使用正确的双按钮样式：
```html
<nav class="pagination">
  <a href="/blog/">← 返回博客列表</a>
  <a href="/">首页</a>
</nav>
```

### 3. 统一路径建议
建议未来操作使用：
- **自动任务**：`/home/admin/projects/roco33.github.io`
- **手动操作**：`/home/admin/.openclaw/workspace/roco33.github.io`
- 操作完成后记得同步（git pull）

## 文章底部按钮规范

所有博客文章底部必须使用以下双按钮样式：

```html
<nav class="pagination">
  <a href="/blog/">← 返回博客列表</a>
  <a href="/">首页</a>
</nav>
```

**不要使用：**
```html
<nav class="site-nav">
  <a href="/">← 首页</a>
</nav>
```

## Cron 任务信息

- 任务名称：每日博客发布 - 05:23
- 运行时间：每天 05:23（北京时间）
- 项目路径：`/home/admin/projects/roco33.github.io`
- 任务 ID：`2573dcb0-e66f-4322-9df3-c84d7e891393`

## 相关提交

- `e68f749` - 更新网站标题和导航样式（统一为双按钮）
- `09ab6c5` - 修正文章底部按钮样式（workspace路径）
- `f0fae50` - 修正文章底部按钮样式（projects路径，已 rebase）

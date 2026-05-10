# My Awesome Skills

这是一个精选的 Claude Agent Skills 集合，通过 Git Submodules 的方式引入了各领域的优质 skills。

## What are Skills?

Skills 是模块化的指令包，为 AI 编程代理提供领域专业知识。它们将 Claude 从通用代理转变为具备特定领域专业知识的专用代理。

## 包含的技能集合

### 官方技能库
- **[anthropic-official](skills/anthropic-official/)** - Anthropic 官方技能库
  - 来源: [anthropics/skills](https://github.com/anthropics/skills)
  - 官方实现，包含经过 Anthropic 团队验证的核心技能

### 社区技能集合

#### [alirezarezvani-collection](skills/alirezarezvani-collection/)
- 来源: [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)
- **232+ Claude Code skills & agent plugins**
- 涵盖多个领域的模块化指令包

#### [jeffallan-collection](skills/jeffallan-collection/)
- 来源: [jeffallan/claude-skills](https://github.com/jeffallan/claude-skills)
- **66 个专业技能**
- 跨越 12 个类别：
  - 编程语言
  - 前端/后端框架
  - 基础设施
  - APIs
  - 测试
  - DevOps
  - 安全
  - 数据/机器学习
  - 更多...

#### [glebis-collection](skills/glebis-collection/)
- 来源: [glebis/claude-skills](https://github.com/glebis/claude-skills)
- 生产工作流技能
- 每个技能指导 Claude 完成特定任务的可执行配方

#### [cybersecurity-collection](skills/cybersecurity-collection/)
- 来源: [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)
- **754 个结构化网络安全技能**
- 覆盖 26 个安全领域
- 遵循 agentskills.io 开放标准

## 快速开始

### 克隆仓库

```bash
git clone --recurse-submodules https://github.com/your-username/my-awesome-skills.git
```

### 如果已经克隆，初始化子模块

```bash
git submodule update --init --recursive
```

### 更新子模块到最新版本

```bash
git submodule update --remote --merge
```

## 技能领域概览

| 领域 | 相关技能集合 |
|------|-------------|
| 文档处理 | alirezarezvani-collection, glebis-collection |
| 前端开发 | alirezarezvani-collection, jeffallan-collection |
| 后端开发 | jeffallan-collection, anthropic-official |
| 网络安全 | cybersecurity-collection |
| 测试 | jeffallan-collection |
| DevOps | jeffallan-collection, glebis-collection |
| 数据/ML | jeffallan-collection, alirezarezvani-collection |
| APIs | jeffallan-collection |

## 如何使用 Skills

Skills 需要安装到 Claude Code 的插件路径中才能使用。通常路径为：

- **Windows**: `%USERPROFILE%\.claude\plugins\`
- **macOS/Linux**: `~/.claude/plugins/`

你可以将需要的技能文件夹复制到插件目录，或者创建符号链接：

```bash
# 创建符号链接（示例）
ln -s /path/to/my-awesome-skills/skills/anthropic-official/document-skills ~/.claude/plugins/
```

## 动画素材生成器

项目中的 `animation/` 目录包含使用 Puppeteer 录制 HTML 动画的工具。

### 使用方法

```bash
cd animation
npm install
node capture.js
```

### 注意事项

**JavaScript 动画需要特殊处理**

Puppeteer 通过 `window.seekTo(time)` 函数跳转到指定时间点进行逐帧录制。这个函数默认只能控制 **CSS 动画**（通过设置 `animation-delay`）。

如果你的动画使用 JavaScript 实现（如 `setTimeout`、`requestAnimationFrame`），需要在 `seekTo` 函数中手动处理：

```javascript
window.seekTo = function(time) {
    // 控制 CSS 动画
    styleEl.textContent = `* { animation-delay: -${time}s !important; }`;

    // 手动控制 JavaScript 动画状态
    // 根据时间计算并设置动画元素的当前状态
    const progress = (time - startTime) / duration;
    element.textContent = text.substring(0, Math.floor(progress * text.length));
};
```

**透明背景录制**

使用 `omitBackground: true` 保留透明通道：

```javascript
await page.screenshot({
    path: framePath,
    omitBackground: true  // 保留透明背景
});
```

**生成透明视频**

```bash
ffmpeg -framerate 30 -i frames/frame_%04d.png -c:v libvpx-vp9 -pix_fmt yuva420p output.webm
```

## 资源链接

- [Agent Skills 官方标准](https://agentskills.io)
- [Claude Code 文档](https://claude.ai/code)
- [Awesome Agent Skills](https://github.com/VoltAgent/awesome-agent-skills)

## 贡献

欢迎提交 PR 添加更多优质的技能集合！

## 许可

各技能集合遵循其原始仓库的许可证。

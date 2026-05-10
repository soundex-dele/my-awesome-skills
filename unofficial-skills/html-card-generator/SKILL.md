---
name: html-card-generator
description: 当用户需要为社交媒体视频、分镜序列或带有动画文本/图形的视频内容生成HTML动画卡片，并与jianying-editor工作流集成时使用
---

# HTML卡片生成器

## 概述

为社交媒体视频生成可直接用于生产的HTML动画卡片序列。每张卡片都是一个包含CSS动画和JavaScript的独立HTML文件，与剪映编辑器(jianying-editor)的web-vfx系统兼容，可用于视频录制。

**核心原则：** 将用户需求（分镜+风格描述）转换为可执行的HTML动画，无需手动编写HTML/CSS/JS代码。

## 使用时机

```
用户需要视频内容？→ 涉及动画卡片？→ 社交媒体格式？→ 使用此技能
        ↓                ↓                   ↓
    产品演示          文字动画            抖音/TikTok
    教程              动态图形            短视频
    演示文稿          场景转换            移动端优先
```

**适用场景：**
- 用户提到"视频卡片"、"HTML动画"、"动态图形"
- 用户提供分镜或场景分解
- 目标平台是社交媒体（抖音、TikTok、Instagram Reels）
- 输出需要与剪映编辑器集成
- 用户需要动画文本/图形序列

**不适用于：**
- 静态图片幻灯片（使用更简单的工具）
- 复杂3D场景（使用专业3D工具）
- 实拍视频素材（这是用于叠加内容）

## 工作流程

### 步骤1：解析用户需求

从用户输入中提取：
- **分镜**：逐场景内容分解
- **风格**：视觉美学（科技、简约、活力等）
- **方向**：横屏（1920x1080）或竖屏（1080x1920）
- **时长**：每场景时间（默认3-5秒）

### 步骤2：选择风格模板

从**8种预设风格**中选择（见下方风格库）或从用户描述推断：
- 关键词："现代"、"简洁" → `minimal`
- 关键词："科技"、"数字"、"AI" → `tech`
- 关键词："有趣"、"活力" → `vibrant`
- 等等

### 步骤3：生成场景卡片

对分镜中的每个场景：
1. 确定场景类型（封面、内容、特性、引用、代码、号召、结尾）
2. 应用风格模板（颜色、排版、动画模式）
3. 生成包含内嵌CSS/JS的完整HTML
4. 确保符合动画规范（见动画规则）

### 步骤4：输出文件序列

按命名规范生成文件：`card_{序号:02d}_{场景类型}.html`

## 风格库

| 风格 | 颜色（CSS变量） | 视觉特征 | 适用场景 |
|-------|------------------------|-----------------|----------|
| **tech** | `--primary: #00f2fe`, `--secondary: #4facfe` | 玻璃拟态、脉冲动画、网格背景 | 科技产品、AI工具、软件演示 |
| **minimal** | `--bg: #ffffff`, `--text: #1a1a1a`, `--accent: #333333` | 简洁排版、淡入过渡、充足留白 | 奢侈品牌、艺术内容、专业演示 |
| **vibrant** | `--primary: #ff6b6b`, `--secondary: #ffc04d`, `--accent: #6c5ce7` | 弹跳动画、高对比度、渐变叠加 | 娱乐、青年内容、生活方式 |
| **business** | `--primary: #2c3e50`, `--secondary: #3498db` | 结构化布局、滑动动画、专业图标 | 企业演示、B2B营销、培训 |
| **retro** | `--primary: #e67e22`, `--secondary: #d35400`, `--bg: #f5e6d3` | 复古字体、胶片颗粒效果、经典边框 | 怀旧主题、经典产品、复古内容 |
| **cute** | `--primary: #ffb6b9`, `--secondary: #feca57`, `--accent: #ff9ff3` | 圆角、弹性动画、可爱图标 | 儿童内容、宠物、生活方式、育儿 |
| **premium** | `--primary: #c0c0c0`, `--gold: #d4af37`, `--bg: #1a1a1a` | 金属渐变、光泽效果、优雅排版 | 奢侈品、高端服务、独家优惠 |
| **dark** | `--bg: #0a0a0a`, `--primary: #00ff88`, `--accent: #ff00ff` | 霓虹发光效果、赛博元素、高对比度 | 游戏、电竞、夜生活、科技 |

## 场景类型与模板

### 1. cover - 封面/片头

**用途：** 带有主标题和副标题的开场标题卡片

**结构：**
```html
<div class="cover-container">
  <div class="tag-line">[标签/分类]</div>
  <h1 class="main-title">[主标题]</h1>
  <p class="subtitle">[副标题/描述]</p>
  <div class="decoration"></div>
</div>
```

**动画：** 标题缩放进入、副标题淡入上移、装饰元素脉冲

### 2. content - 内容页

**用途：** 带有标题和正文的信息内容

**结构：**
```html
<div class="content-container">
  <h2 class="section-title">[章节标题]</h2>
  <div class="content-body">
    <p>[段落内容]</p>
    <p>[根据需要添加更多段落]</p>
  </div>
  <div class="visual-element"></div>
</div>
```

**动画：** 标题滑入、段落层叠淡入

### 3. features - 特性列表

**用途：** 带有图标和描述的功能项网格

**结构：**
```html
<div class="features-grid">
  <div class="feature-item">
    <div class="feature-icon">[图标/表情]</div>
    <h3 class="feature-title">[功能名称]</h3>
    <p class="feature-desc">[描述]</p>
  </div>
  <!-- 每个功能重复（通常3-4项） -->
</div>
```

**动画：** 项目依次淡入并带缩放效果

### 4. quote - 金句/引用

**用途：** 居中显示的大号引用或关键信息

**结构：**
```html
<div class="quote-container">
  <div class="quote-mark">"</div>
  <p class="quote-text">[引用内容]</p>
  <div class="quote-author">— [作者/来源]</div>
</div>
```

**动画：** 文字揭示、缩放脉冲、作者淡入

### 5. code - 代码展示

**用途：** 带语法高亮的代码显示

**结构：**
```html
<div class="code-container">
  <div class="code-header">
    <span class="lang-tag">[语言]</span>
  </div>
  <pre class="code-block"><code>[代码内容]</code></pre>
</div>
```

**动画：** 打字机效果或逐行揭示

### 6. cta - 号召行动

**用途：** 带有按钮和提示的行动号召

**结构：**
```html
<div class="cta-container">
  <h2 class="cta-title">[行动提示]</h2>
  <p class="cta-subtitle">[支持文本]</p>
  <button class="cta-button">[按钮文本]</button>
  <div class="cta-decorations"></div>
</div>
```

**动画：** 按钮脉冲进入、文字弹跳、装饰元素旋转

### 7. ending - 结尾

**用途：** 感谢和关注提示的结束卡片

**结构：**
```html
<div class="ending-container">
  <h2 class="thanks-text">感谢观看！</h2>
  <p class="follow-text">[关注/订阅提示]</p>
  <div class="social-icons">[社交媒体图标/表情]</div>
</div>
```

**动画：** 爱心弹跳、图标旋转、柔和淡入

## 动画规范（剪映编辑器兼容性）

**关键：** 所有生成的HTML必须遵守以下规则：

```javascript
// 1. 必需：动画结束时设置完成信号
window.animationFinished = true;

// 2. 必需：透明背景用于视频叠加
body {
  background: transparent;
  margin: 0;
  overflow: hidden;
}

// 3. 时长：每张卡片默认3-5秒
const ANIMATION_DURATION = 3000; // 毫秒，按场景调整

// 4. 使用requestAnimationFrame实现流畅动画
requestAnimationFrame(animate);

// 5. 可选：通过CDN加载外部库
// <script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>
```

**文件格式要求：**
- 单文件（HTML + CSS + JS内联）
- UTF-8编码
- 无外部资源（CDN库除外）
- 不使用`alert()`或阻塞操作
- 适应方向（横屏/竖屏）

## 尺寸适配

### 横屏（1920x1080）- 默认

```css
:root {
  --width: 1920px;
  --height: 1080px;
}
body {
  width: var(--width);
  height: var(--height);
  font-size: 48px; /* 基础字号 */
}
```

### 竖屏（1080x1920）

```css
:root {
  --width: 1080px;
  --height: 1920px;
}
body {
  width: var(--width);
  height: var(--height);
  font-size: 42px; /* 移动端调整 */
}
/* 调整布局以适应垂直堆叠 */
```

**提示：** 使用CSS变量和相对单位（rem、%、vw/vh）便于适配。

## 完整示例

### 用户输入

```
制作一个剪映AI剪辑介绍视频的卡片序列：

分镜：
1. 封面：标题"剪映AI自动化剪辑"，副标题"让视频创作更简单"
2. 功能页：展示3个核心功能
   - 智能剪辑 🎬
   - 自动字幕 ✨
   - AI旁白 🎙️
3. 结尾：号召行动"立即体验"

风格：科技感，横屏
```

### 生成的输出

**card_01_cover.html:**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<style>
:root {
  --primary: #00f2fe;
  --secondary: #4facfe;
  --width: 1920px;
  --height: 1080px;
}
body {
  margin: 0;
  width: var(--width);
  height: var(--height);
  background: linear-gradient(135deg, #0a1628 0%, #1a2a4a 100%);
  font-family: 'PingFang SC', 'Microsoft YaHei', sans-serif;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}
.cover-container {
  text-align: center;
  position: relative;
}
.tag-line {
  color: var(--primary);
  font-size: 32px;
  letter-spacing: 8px;
  margin-bottom: 30px;
  opacity: 0;
  animation: fade-in 0.8s ease-out 0.3s forwards;
}
.main-title {
  font-size: 120px;
  font-weight: 800;
  background: linear-gradient(90deg, var(--primary), var(--secondary));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin: 0 0 40px 0;
  transform: scale(0.8);
  opacity: 0;
  animation: scale-in 1s ease-out 0.5s forwards;
}
.subtitle {
  font-size: 48px;
  color: rgba(255,255,255,0.8);
  margin: 0;
  opacity: 0;
  animation: fade-up 0.8s ease-out 1s forwards;
}
.decoration {
  position: absolute;
  width: 400px;
  height: 400px;
  border: 3px solid var(--primary);
  border-radius: 50%;
  opacity: 0.1;
  animation: pulse 3s ease-in-out infinite;
}
@keyframes scale-in {
  to { transform: scale(1); opacity: 1; }
}
@keyframes fade-up {
  from { transform: translateY(30px); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
}
@keyframes fade-in {
  to { opacity: 1; }
}
@keyframes pulse {
  0%, 100% { transform: scale(1); opacity: 0.1; }
  50% { transform: scale(1.1); opacity: 0.2; }
}
</style>
</head>
<body>
<div class="cover-container">
  <div class="tag-line">AI 创作工具</div>
  <h1 class="main-title">剪映AI自动化剪辑</h1>
  <p class="subtitle">让视频创作更简单</p>
  <div class="decoration"></div>
</div>
<script>
// 动画完成信号
setTimeout(() => {
  window.animationFinished = true;
}, 3000);
</script>
</body>
</html>
```

**card_02_features.html:**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<style>
:root {
  --primary: #00f2fe;
  --secondary: #4facfe;
  --width: 1920px;
  --height: 1080px;
}
body {
  margin: 0;
  width: var(--width);
  height: var(--height);
  background: linear-gradient(135deg, #0a1628 0%, #1a2a4a 100%);
  font-family: 'PingFang SC', sans-serif;
  display: flex;
  align-items: center;
  justify-content: center;
}
.features-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 80px;
  padding: 100px;
}
.feature-item {
  background: rgba(255,255,255,0.05);
  border: 2px solid rgba(79, 172, 254, 0.3);
  border-radius: 24px;
  padding: 60px 40px;
  text-align: center;
  backdrop-filter: blur(10px);
  opacity: 0;
  transform: translateY(40px) scale(0.9);
  animation: item-appear 0.8s ease-out forwards;
}
.feature-item:nth-child(1) { animation-delay: 0.3s; }
.feature-item:nth-child(2) { animation-delay: 0.5s; }
.feature-item:nth-child(3) { animation-delay: 0.7s; }
.feature-icon {
  font-size: 80px;
  margin-bottom: 30px;
}
.feature-title {
  font-size: 42px;
  color: var(--primary);
  margin: 0 0 20px 0;
  font-weight: 700;
}
.feature-desc {
  font-size: 28px;
  color: rgba(255,255,255,0.7);
  margin: 0;
}
@keyframes item-appear {
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}
</style>
</head>
<body>
<div class="features-grid">
  <div class="feature-item">
    <div class="feature-icon">🎬</div>
    <h3 class="feature-title">智能剪辑</h3>
    <p class="feature-desc">AI自动识别精彩片段</p>
  </div>
  <div class="feature-item">
    <div class="feature-icon">✨</div>
    <h3 class="feature-title">自动字幕</h3>
    <p class="feature-desc">语音转文字一键生成</p>
  </div>
  <div class="feature-item">
    <div class="feature-icon">🎙️</div>
    <h3 class="feature-title">AI旁白</h3>
    <p class="feature-desc">智能配音专业呈现</p>
  </div>
</div>
<script>
setTimeout(() => {
  window.animationFinished = true;
}, 3000);
</script>
</body>
</html>
```

**card_03_ending.html:**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<style>
:root {
  --primary: #00f2fe;
  --secondary: #4facfe;
}
body {
  margin: 0;
  width: 1920px;
  height: 1080px;
  background: linear-gradient(135deg, #0a1628 0%, #1a2a4a 100%);
  font-family: 'PingFang SC', sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.cta-title {
  font-size: 96px;
  color: var(--primary);
  margin: 0 0 40px 0;
  opacity: 0;
  animation: bounce-in 1s ease-out 0.3s forwards;
}
.cta-button {
  font-size: 48px;
  padding: 30px 80px;
  background: linear-gradient(90deg, var(--primary), var(--secondary));
  border: none;
  border-radius: 60px;
  color: #0a1628;
  font-weight: 700;
  cursor: pointer;
  animation: pulse-btn 2s ease-in-out infinite 1.5s;
  opacity: 0;
  animation: fade-in 0.8s ease-out 0.8s forwards, pulse-btn 2s ease-in-out 1.5s infinite;
}
@keyframes bounce-in {
  0% { transform: scale(0.3); opacity: 0; }
  50% { transform: scale(1.05); }
  100% { transform: scale(1); opacity: 1; }
}
@keyframes fade-in {
  to { opacity: 1; }
}
@keyframes pulse-btn {
  0%, 100% { transform: scale(1); box-shadow: 0 0 20px rgba(0, 242, 254, 0.4); }
  50% { transform: scale(1.05); box-shadow: 0 0 40px rgba(0, 242, 254, 0.8); }
}
</style>
</head>
<body>
<h2 class="cta-title">立即体验</h2>
<button class="cta-button">开始创作 →</button>
<script>
setTimeout(() => {
  window.animationFinished = true;
}, 3000);
</script>
</body>
</html>
```

## 输出格式

### 文件命名规范

```
card_{序号:02d}_{场景类型}.html

示例：
- card_01_cover.html
- card_02_features.html
- card_03_ending.html
```

### 返回格式

生成卡片后，提供：

```
已生成 {N} 张卡片：
{文件列表}

与剪映编辑器配合使用：
```python
from jy_wrapper import JyProject

project = JyProject("我的视频")

for i, html_file in enumerate([{文件列表}]):
    project.add_web_asset_safe(
        html_path=html_file,
        start_time=f"{i * 3}s",
        duration="3s"
    )

project.save()
```

## 剪映编辑器集成

生成的HTML卡片**直接兼容**剪映编辑器工作流：

```python
from jy_wrapper import JyProject

# 创建新项目
project = JyProject("社交媒体视频")

# 批量导入卡片
cards = [
    "card_01_cover.html",
    "card_02_content.html",
    "card_03_features.html",
    "card_04_ending.html"
]

for i, card in enumerate(cards):
    # 每张卡片播放3-5秒
    start = f"{i * 3}s"
    project.add_web_asset_safe(
        html_path=card,
        start_time=start,
        duration="3s"
    )

# 导出视频
project.export(output_path="最终视频.mp4")
```

**集成优势：**
- 自动录制HTML动画
- 透明背景便于叠加
- 精确时间控制
- 无需手动编码

## 方向指南

### 横屏（1920×1080）

**关键原则：**
- 使用相对单位（`vw`、`vh`、`%`）而非固定像素
- Body: `width: 100vw; height: 100vh;`
- 内容内边距：`5vh 5vw` 保持安全边距
- 所有字体、间距、动画使用视口单位

**模板结构：**
```css
body {
  width: 100vw;
  height: 100vh;
  margin: 0;
  overflow: hidden;
}

.container {
  padding: 5vh 5vw;
  max-width: 90vw;
  max-height: 90vh;
}

/* 排版 - 相对于视口 */
h1 { font-size: 7vw; }
p { font-size: 2.5vw; }
```

**最佳实践：**
- ✅ 使用`vw`作为水平尺寸
- ✅ 使用`vh`作为垂直尺寸
- ✅ 在容器上设置`max-width/max-height`
- ✅ 使用`%`实现响应式网格
- ❌ 避免使用固定`px`作为尺寸
- ❌ 避免硬编码宽度/高度

### 竖屏（1080×1920）

**关键挑战：** 垂直内容必须旋转-90°才能在横屏显示

**旋转模式：**
```css
body {
  width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}

.card-wrapper {
  width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}

.card {
  width: 1080px;
  height: 1920px;
  transform: rotate(-90deg);
  max-width: 100vh;
  max-height: 100vw;
  object-fit: contain;
}
```

**⚠️ 关键：安全区域与单位选择**

**问题：** 旋转-90°后，`vh`/`vw`单位会根据**错误的视口轴**计算，导致内容溢出或错位。此外，短视频平台（抖音、TikTok）会在顶部/底部预留约10%的屏幕空间用于UI元素（点赞/评论按钮）。

**解决方案：**
1. **将最大尺寸缩小到90%**（而非100%）以创建安全区域
2. **使用固定像素（px）** 而非`vh`/`vw`，确保旋转后尺寸一致
3. **使用固定内边距**（80-100px）而非视口相对内边距

**正确模式：**
```css
.card {
  width: 1080px;
  height: 1920px;
  transform: rotate(-90deg);
  max-width: 90vh;   /* 不是100vh - 两侧各留5% */
  max-height: 90vw;  /* 不是100vw - 两侧各留5% */
  padding: 80px 60px; /* 固定像素，不是vh/vw */
}
```

**关键设置：**

| 属性 | 值 | 用途 |
|----------|-------|---------|
| `transform: rotate(-90deg)` | -90度 | 将垂直旋转为水平 |
| `max-width: 90vh` | 视口高度的90% | **关键：** 限制宽度 + 创建安全区域 |
| `max-height: 90vw` | 视口宽度的90% | **关键：** 限制高度 + 创建安全区域 |
| `padding: 80px 60px` | 固定像素 | **使用px而非vh/vw** 确保间距一致 |
| `overflow: hidden` | 隐藏 | 裁剪多余内容 |

**背景处理：**
```css
/* 背景填充整个屏幕 */
body {
  background: linear-gradient(135deg, #0a1628 0%, #1a2a4a 100%);
}

/* 卡片背景 */
.card {
  background: transparent; /* 或匹配的渐变 */
}
```

**内容布局：**
- **在卡片内使用固定像素（px）** 作为所有尺寸
- **避免使用vh/vw单位** - 旋转后计算错误
- 内边距：`80px 60px` 用于竖屏特定间距
- 字号：标题`80-100px`，正文`28-40px`
- 使用`flex-direction: column`垂直堆叠

**常见竖屏陷阱：**

| 问题 | 原因 | 解决方案 |
|-------|-------|----------|
| **边缘内容被裁剪** | `max-width/max-height: 100vh/100vw` 未留安全区域 | 使用`90vh/90vw`为平台UI预留10% |
| **VH/VW单位错位** | 旋转后，`vh`测量宽度，`vw`测量高度 | 所有尺寸、内边距、字号**使用固定像素（px）** |
| **顶部/底部内容被遮挡** | 平台UI叠加（如点赞按钮、评论） | 将重要内容保持在80%中心区域内 |
| 方向错误 | 缺少旋转 | 添加`transform: rotate(-90deg)` |
| 溢出 | 无尺寸约束 | 在包装器上添加`overflow: hidden` |
| 内容变形 | 宽高不匹配 | 确保基准尺寸为1080×1920 |

**测试清单：**
- [ ] 背景填充整个屏幕
- [ ] 内容正确旋转
- [ ] 无水平滚动条
- [ ] **顶部/底部10%安全区域无关键内容**
- [ ] **所有尺寸使用固定像素（而非vh/vw）**
- [ ] 文字在缩放下可读
- [ ] 动画正确播放
- [ ] 卡片在视口居中，四周有边距

### 响应式设计技巧

**使用CSS变量保持一致性：**
```css
:root {
  --safe-margin: 5vh 5vw;
  --title-size: 7vw;
  --body-size: 2.5vw;
}
```

**媒体查询（可选）：**
```css
@media (max-aspect-ratio: 16/9) {
  /* 适配较窄屏幕 */
  :root {
    --title-size: 6vw;
  }
}
```

## 常见错误

| 错误 | 修正 |
|---------|-----|
| 缺少`window.animationFinished` | 始终在动画结束时设置此信号 |
| 非透明背景 | 使用`background: transparent`或渐变叠加 |
| 仅使用固定尺寸 | 使用CSS变量实现方向灵活性 |
| **在竖屏卡片中使用vh/vw** | **使用固定像素（px）- vh/vw旋转后失效** |
| **max-width/max-height: 100vh/100vw** | **使用90vh/90vw为平台UI预留安全区域** |
| 阻塞操作（alert、prompt） | 动画代码中绝不使用阻塞调用 |
| 外部本地资源 | 使用CDN或全部内联 |

## CDN库（可选）

使用这些库增强动画：

```html
<!-- GSAP用于复杂时间轴 -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>

<!-- Three.js用于3D效果 -->
<script src="https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.min.js"></script>

<!-- Anime.js用于简化动画 -->
<script src="https://cdn.jsdelivr.net/npm/animejs@3.2.1/lib/anime.min.js"></script>
```

**谨慎使用** - 简单动画首选原生CSS/JS。

## 快速参考

```
故事 → 解析 → 风格 → 生成 → 输出
  ↓       ↓       ↓         ↓         ↓
输入  提取  选择  创建    文件
```

**风格选择启发式：**
- 科技/AI/SaaS → `tech`
- 奢侈/艺术 → `minimal` 或 `premium`
- 儿童/家庭 → `cute`
- 商务/企业 → `business`
- 游戏/电竞 → `dark`
- 美食/生活方式 → `vibrant`
- 怀旧 → `retro`

---
name: md-to-html
description: Markdown 转微信公众号 HTML 工具。基于预设模板生成兼容微信公众号的精美 HTML，支持 5 种设计风格，无需脚本直接由 LLM 生成。
version: 3.0
---

# Markdown 转微信公众号 HTML Skill

## 功能概述

基于**预设设计模板**，将 Markdown 文档转换为**兼容微信公众号**的精美 HTML 页面。LLM 直接读取模板并替换内容，无需运行脚本。

### 核心特点

- 📱 **微信公众号兼容** - 所有模板专为微信公众号富文本编辑器设计
- 🎨 **5 种预设设计风格** - 专业设计师精心打造
- 📝 **模板化生成** - LLM 读取模板并替换变量
- 🚀 **零脚本依赖** - 不需要 Python 或其他工具
- ✅ **仅使用内联样式** - 移除 `<style>` 标签，确保公众号兼容
- 🎯 **即用即走** - 直接生成可粘贴到公众号的 HTML 代码

---

## 微信公众号 HTML 限制

### 支持的特性
- ✅ 基础标签：`<p>`, `<h1>`~`<h3>`, `<ul>`, `<ol>`, `<li>`
- ✅ 文本格式：`<strong>`, `<em>`, `<u>`, `<del>`
- ✅ 媒体：`<img>`, `<table>`
- ✅ **内联样式** (`style` 属性)：`color`, `font-size`, `padding`, `margin`, `border`, `border-radius` 等
- ✅ `<section>` 容器标签

### 不支持的特性（已移除）
- ❌ `<style>` 标签和外部 CSS
- ❌ CSS 变量 (`:root`, `var(--xxx)`)
- ❌ 伪元素/伪类 (`::before`, `::after`, `:hover`, `:nth-child`)
- ❌ JavaScript、iframe、form
- ❌ 复杂布局（flexbox, grid）
- ❌ 动画和过渡效果
- ❌ 渐变背景

---

## 可用模板

### 1. 极简科技风（minimal-tech.html）

**适用场景：** 技术文档、API 文档、开发教程

**设计特点：**
- 深色主题，护眼舒适
- 霓虹配色（青色、紫色、绿色）
- 等宽字体，代码友好
- 简洁的边框和分隔线

**颜色方案：**
```css
背景: #0d1117 (深灰)
文字: #c9d1d9 (浅灰)
强调: #58a6ff (青色)、#3fb950 (绿色)、#bc8cff (紫色)
```

### 2. 现代博客风（modern-blog.html）

**适用场景：** 个人博客、技术文章、教程

**设计特点：**
- 白色卡片背景
- 蓝粉配色
- 圆角设计
- 柔和阴影效果

**颜色方案：**
```css
背景: #f8f9fa (浅灰)
卡片: #ffffff (白色)
强调: #3498db (蓝色)、#e74c3c (粉色)
```

### 3. 优雅杂志风（elegant-magazine.html）

**适用场景：** 正式文章、出版物、文学内容

**设计特点：**
- 衬线字体，经典优雅
- 大量留白，高级感
- 金色装饰元素
- 简约分隔线

**颜色方案：**
```css
背景: #faf9f7 (米白)
文字: #2c3e50 (深灰)
强调: #c9a959 (金色)、#8b9a7d (鼠尾草绿)
```

### 4. 温暖日系风（warm-japanese.html）

**适用场景：** 生活博客、随笔、轻松内容

**设计特点：**
- 柔和的暖色调
- 圆角卡片，手绘感
- 日文装饰元素（✦ 🌸）
- 可爱风格

**颜色方案：**
```css
背景: #fff9f0 (暖白)
文字: #5d513c (暖棕)
强调: #f4a688 (珊瑚色)、#8fbc8f (鼠尾草绿)
```

### 5. 专业文档风（professional-doc.html）

**适用场景：** 技术文档、用户手册、API 参考

**设计特点：**
- 简洁清爽
- GitHub 风格配色
- 支持警告框样式
- 表格和代码优化

**颜色方案：**
```css
背景: #ffffff (白色)
强调: #0366d6 (蓝色)、#28a745 (绿色)、#6f42c1 (紫色)
```

---

## 使用流程

### 步骤 1：选择模板

根据内容类型选择合适的模板：

| 内容类型 | 推荐模板 | 原因 |
|---------|---------|------|
| 技术文档/代码 | minimal-tech.html | 深色护眼，代码友好 |
| 技术博客/教程 | modern-blog.html | 卡片式，易阅读 |
| 正式文章/出版物 | elegant-magazine.html | 优雅专业 |
| 生活随笔/轻松内容 | warm-japanese.html | 温馨可爱 |
| API 文档/手册 | professional-doc.html | 结构清晰 |

### 步骤 2：读取模板并创建生成计划

**2.1 读取模板文件**

使用 `read` 工具读取模板文件：

```json
{
  "tool_name": "read",
  "params": {
    "file_path": "/Users/xiesongde/workspace/agent/video_player/engine/agent/skills/superpowers-writer/md-to-html/templates/minimal-tech.html"
  }
}
```

**2.2 分析模板结构，创建生成计划**

根据模板结构，将生成任务拆分为多个步骤，每个步骤生成一部分内容并立即写入文件。

**生成计划示例：**

```
生成计划：微信公众号 HTML 文档
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

步骤 1: 创建文件并写入文档头部
  - 写入 <!DOCTYPE html> 和 <html> 标签
  - 写入 <head> 部分（meta、title、style）
  - 写入 <body> 开始标签

步骤 2: 写入头部区域（header）
  - 替换 {{title}} 为实际标题
  - 替换 {{author}}、{{date}} 等变量
  - 生成完整的 header 结构

步骤 3: 逐段写入内容
  - 转换 Markdown 为 HTML（带内联样式）
  - 每段内容立即追加写入文件
  - 包括：标题、段落、列表、代码块、引用、表格等

步骤 4: 写入页脚区域（footer）
  - 生成 footer 结构
  - 闭合 </body> 和 </html> 标签

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
总计 4 个步骤，每步完成后立即写入文件
```

### 步骤 3：执行生成计划（逐个生成，立即写入）

**核心原则：逐个生成，立即写入**

- ✅ 每个步骤生成的内容**立即使用 `write` 工具写入文件**
- ✅ 每次写入都覆盖或追加到同一个输出文件
- ✅ 避免在内存中累积大量内容
- ✅ 每个步骤完成后报告进度

**写入策略：**

```json
// 步骤 1: 创建文件并写入头部
{
  "tool_name": "write",
  "params": {
    "file_path": "/path/to/output.html",
    "content": "<!DOCTYPE html>\n<html>\n<head>...</head>\n<body>"
  }
}

// 步骤 2: 追加 header
{
  "tool_name": "write",
  "params": {
    "file_path": "/path/to/output.html",
    "content": "<header>...</header>\n<main>"
  }
}

// 步骤 3: 追加内容段落（重复多次）
{
  "tool_name": "write",
  "params": {
    "file_path": "/path/to/output.html",
    "content": "<section>...</section>\n<section>...</section>"
  }
}

// 步骤 4: 追加 footer 并闭合标签
{
  "tool_name": "write",
  "params": {
    "file_path": "/path/to/output.html",
    "content": "</main>\n<footer>...</footer>\n</body>\n</html>"
  }
}
```

### 步骤 4：Markdown 到 HTML 转换规则

**逐段转换时遵循以下规则：**

#### Markdown → HTML 映射

| Markdown | HTML |
|----------|------|
| `# 标题` | `<h1 style="...">标题</h1>` |
| `## 标题` | `<h2 style="...">标题</h2>` |
| `### 标题` | `<h3 style="...">标题</h3>` |
| `**粗体**` | `<strong style="...">粗体</strong>` |
| `*斜体*` | `<em style="...">斜体</em>` |
| `- 列表` | `<ul style="..."><li style="...">列表</li></ul>` |
| `` `代码` `` | `<code style="...">代码</code>` |
| ```` ```语言 ```` | `<pre style="..." data-lang="语言"><code style="...">代码</code></pre>` |
| `> 引用` | `<blockquote style="..."><p>引用</p></blockquote>` |
| `[链接](url)` | `<a style="..." href="url">链接</a>` |
| `![alt](img)` | `<img style="..." src="img" alt="alt">` |
| `---` | `<hr style="...">` |

#### 代码块格式（带内联样式）

```html
<pre data-lang="python" style="background-color: #f6f8fa; padding: 16px; border-radius: 6px; overflow-x: auto;"><code style="font-family: monospace; font-size: 14px; color: #24292e;">def hello():
    print("Hello, World!")
</code></pre>
```

#### 表格格式（带内联样式）

```html
<table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
    <thead>
        <tr style="background-color: #f6f8fa; border-bottom: 2px solid #e1e4e8;">
            <th style="padding: 12px; text-align: left; font-weight: 600;">列1</th>
            <th style="padding: 12px; text-align: left; font-weight: 600;">列2</th>
        </tr>
    </thead>
    <tbody>
        <tr style="border-bottom: 1px solid #e1e4e8;">
            <td style="padding: 12px;">数据1</td>
            <td style="padding: 12px;">数据2</td>
        </tr>
    </tbody>
</table>
```

### 步骤 5：模板变量替换

模板中的占位符需要在生成时替换为实际内容：

| 变量 | 说明 | 示例 |
|------|------|------|
| `{{title}}` | 文档标题 | "我的第一篇博客" |
| `{{subtitle}}` | 副标题（可选） | "技术分享系列" |
| `{{author}}` | 作者 | "张三" |
| `{{date}}` | 日期 | "2026-03-23" |
| `{{description}}` | 文档描述 | "这是一篇关于..." |
| `{{content}}` | HTML 内容 | 逐段转换的 HTML |
| `{{readTime}}` | 阅读时间（可选） | "5 分钟" |

---

## 完整示例

### 示例 1：生成技术文档（极简科技风）

**用户请求：**
```
将这个 Markdown 文档转换为微信公众号 HTML，使用极简科技风格
```

**处理步骤：**

**1. 读取模板并创建生成计划**
```json
{
  "tool_name": "read",
  "params": {
    "file_path": "/Users/xiesongde/workspace/agent/video_player/engine/agent/skills/superpowers-writer/md-to-html/templates/minimal-tech.html"
  }
}
```

**生成计划：**
```
步骤 1: 写入文档头部和容器开始
步骤 2: 写入 header（替换 {{title}}, {{author}}, {{date}}）
步骤 3: 逐段转换 Markdown 为 HTML 并写入
  - 标题转换为 <h2 style="...">
  - 段落转换为 <p style="...">
  - 代码块转换为 <pre style="..."><code>
步骤 4: 写入 footer 并闭合所有标签
```

**2. 执行步骤 1：写入头部**
```json
{
  "tool_name": "write",
  "params": {
    "file_path": "/tmp/python-guide.html",
    "content": "<section style=\"padding: 20px; background-color: #0d1117;\">\n<section style=\"max-width: 750px; margin: 0 auto;\">\n<section style=\"padding: 40px;\">"
  }
}
```
**✅ 步骤 1 完成：头部已写入**

**3. 执行步骤 2：写入 header**
```json
{
  "tool_name": "write",
  "params": {
    "file_path": "/tmp/python-guide.html",
    "content": "<header style=\"text-align: center; margin-bottom: 40px;\">\n<h1 style=\"font-size: 28px; color: #58a6ff;\">Python 异步编程指南</h1>\n<section style=\"margin-top: 15px;\">\n<span style=\"color: #8b949e;\">2026-03-23</span>\n<span style=\"color: #8b949e; margin-left: 20px;\">技术团队</span>\n</section>\n</header>\n<main>"
  }
}
```
**✅ 步骤 2 完成：header 已写入**

**4. 执行步骤 3：逐段写入内容（重复多次）**
```json
{
  "tool_name": "write",
  "params": {
    "file_path": "/tmp/python-guide.html",
    "content": "<section style=\"margin-bottom: 30px;\">\n<h2 style=\"font-size: 22px; color: #58a6ff; margin-bottom: 15px;\">什么是异步编程？</h2>\n<p style=\"color: #c9d1d9; line-height: 1.8;\">异步编程是一种编程范式...</p>\n</section>"
  }
}
```
**✅ 步骤 3 完成（第 1/3 段）：第一段已写入**

```json
{
  "tool_name": "write",
  "params": {
    "file_path": "/tmp/python-guide.html",
    "content": "<section style=\"margin-bottom: 30px;\">\n<h2 style=\"font-size: 22px; color: #58a6ff; margin-bottom: 15px;\">Python asyncio 示例</h2>\n<pre style=\"background-color: #161b22; padding: 16px; border-radius: 6px;\"><code style=\"font-family: monospace; color: #c9d1d9;\">import asyncio\n\nasync def hello():\n    print(\"Hello, World!\")\n</code></pre>\n</section>"
  }
}
```
**✅ 步骤 3 完成（第 2/3 段）：第二段已写入**

```json
{
  "tool_name": "write",
  "params": {
    "file_path": "/tmp/python-guide.html",
    "content": "<section style=\"margin-bottom: 30px;\">\n<h2 style=\"font-size: 22px; color: #58a6ff; margin-bottom: 15px;\">总结</h2>\n<p style=\"color: #c9d1d9; line-height: 1.8;\">异步编程可以显著提高 I/O 密集型任务的性能...</p>\n</section>"
  }
}
```
**✅ 步骤 3 完成（第 3/3 段）：第三段已写入**

**5. 执行步骤 4：写入 footer 并闭合标签**
```json
{
  "tool_name": "write",
  "params": {
    "file_path": "/tmp/python-guide.html",
    "content": "</main>\n<footer style=\"margin-top: 50px; padding-top: 25px; border-top: 1px solid #30363d; text-align: center; color: #8b949e;\">\n<p>感谢阅读 💻</p>\n</footer>\n</section>\n</section>\n</section>"
  }
}
```
**✅ 步骤 4 完成：文档已生成**

**✅ 全部完成！文件已保存至 `/tmp/python-guide.html`**

### 示例 2：生成博客文章（温暖日系风）

**用户请求：**
```
帮我写一篇关于 Docker 的博客，生成微信公众号 HTML，使用温暖日系风格
```

**处理步骤：**

1. **读取模板**：`warm-japanese.html`
2. **创建生成计划**：拆分为 4 个步骤
3. **执行计划**：
   - 步骤 1：写入容器结构 ✅
   - 步骤 2：写入 header（替换标题、作者、日期） ✅
   - 步骤 3：逐段写入内容（简介、核心概念、使用示例、总结） ✅
   - 步骤 4：写入 footer 并闭合标签 ✅
4. **输出**：`/tmp/docker-blog.html`

**每个步骤完成后立即使用 `write` 工具写入文件，避免在内存中累积大量内容。**

---

## 模板路径速查

```
/Users/xiesongde/workspace/agent/video_player/engine/agent/skills/superpowers-writer/md-to-html/templates/

├── minimal-tech.html       # 极简科技风
├── modern-blog.html        # 现代博客风
├── elegant-magazine.html   # 优雅杂志风
├── warm-japanese.html      # 温暖日系风
└── professional-doc.html   # 专业文档风
```

---

## 重要提醒

### ✅ 必须遵守的规则

1. **创建生成计划** - 读取模板后，必须先创建生成计划，明确拆分为哪些步骤
2. **逐个生成，立即写入** - 每个步骤完成后**立即**使用 `write` 工具写入文件，避免在内存中累积
3. **完整读取模板** - 必须使用 `read` 工具读取完整的模板文件
4. **正确转换语法** - 严格按照 Markdown → HTML 映射规则转换
5. **替换所有变量** - 确保所有 `{{变量}}` 都被替换为实际内容
6. **保留 HTML 结构** - 不要修改模板的 HTML 结构和内联样式
7. **使用内联样式** - 所有样式必须是 `style="..."` 属性形式
8. **生成完整代码** - 输出的 HTML 必须可直接粘贴到微信公众号编辑器
9. **报告进度** - 每个步骤完成后报告进度（如：✅ 步骤 1 完成）

### ⚠️ 常见错误

| 错误 | 原因 | 解决方案 |
|------|------|---------|
| HTML 无法显示 | 没有完整读取模板 | 使用 `read` 工具读取完整文件 |
| 样式丢失 | 修改了内联样式或 HTML 结构 | 只替换 `{{变量}}`，不修改结构 |
| 变量未替换 | 遗漏了某些占位符 | 检查所有 `{{}}` 并全部替换 |
| 代码块不显示 | 没有使用正确的 `<pre data-lang="">` 格式 | 使用 `<pre data-lang="python" style="..."><code>` 格式 |
| 微信公众号不显示 | 使用了 `<style>` 标签或不支持的 CSS | 确保只使用内联样式 |
| 复杂布局失效 | 使用了 flexbox、grid 等 | 使用简单的 `<section>` 和内联样式 |

### 🎯 最佳实践

1. **遵循增量生成策略**
   - 正确顺序：读取模板 → 创建计划 → **逐个生成并立即写入**
   - 不要在内存中累积整个 HTML 文档
   - 每个步骤独立完成，便于调试和恢复

2. **创建清晰的生成计划**
   - 读取模板后，先分析结构
   - 将任务拆分为 3-6 个步骤
   - 每个步骤聚焦于一个独立的部分

3. **保持原始结构**
   - 只替换 `{{变量}}` 内容，不修改 HTML 标签和内联样式

4. **测试输出**
   - 生成后建议先在浏览器中预览，再粘贴到微信公众号后台测试

5. **选择合适的模板**
   - 技术内容用 `minimal-tech.html`
   - 文章内容用 `modern-blog.html` 或 `warm-japanese.html`
   - 正式内容用 `elegant-magazine.html`

6. **图片处理**
   - 图片需先上传到微信公众号图床
   - 使用微信CDN链接替换 `src` 属性

7. **大文档处理**
   - 对于长文档，每 2-3 个元素就执行一次写入
   - 避免单次写入内容过大（建议不超过 5000 字符）

---

## 快速参考

### 常用 Markdown → HTML 转换

```markdown
# 一级标题
## 二级标题
### 三级标题

**粗体文本**
*斜体文本*

- 无序列表1
- 无序列表2

1. 有序列表1
2. 有序列表2

`行内代码`

\```python
def hello():
    print("Hello")
\```

> 引用文本

[链接文字](https://example.com)

![图片描述](image.jpg)

---

| 列1 | 列2 |
|-----|-----|
| A   | B   |
```

对应 HTML（带内联样式）：

```html
<h1 style="...">一级标题</h1>
<h2 style="...">二级标题</h2>
<h3 style="...">三级标题</h3>

<strong style="...">粗体文本</strong>
<em style="...">斜体文本</em>

<ul style="...">
    <li style="...">无序列表1</li>
    <li style="...">无序列表2</li>
</ul>

<ol style="...">
    <li style="...">有序列表1</li>
    <li style="...">有序列表2</li>
</ol>

<code style="...">行内代码</code>

<pre data-lang="python" style="..."><code style="...">def hello():
    print("Hello")
</code></pre>

<blockquote style="..."><p>引用文本</p></blockquote>

<a style="..." href="https://example.com">链接文字</a>

<img style="..." src="image.jpg" alt="图片描述">

<hr style="...">

<table style="...">
    <thead>
        <tr style="...">
            <th style="...">列1</th>
            <th style="...">列2</th>
        </tr>
    </thead>
    <tbody>
        <tr style="...">
            <td style="...">A</td>
            <td style="...">B</td>
        </tr>
    </tbody>
</table>
```

---

## 总结

使用这个 skill 的核心流程：

1. **选择合适的模板**
2. **使用 `read` 工具读取模板文件**
3. **创建生成计划** - 分析模板结构，拆分为多个步骤
4. **执行生成计划** - **逐个生成，每个步骤立即使用 `write` 工具写入文件**
5. **将 Markdown 内容转换为 HTML（带内联样式）**
6. **替换模板中的 `{{变量}}` 占位符**

**关键原则：增量生成，立即写入，避免内存累积！** 🎉

**生成流程图：**

```
开始
  ↓
读取模板文件
  ↓
创建生成计划（3-6 个步骤）
  ↓
┌─────────────────────────────┐
│  步骤 1: 生成头部           │ → 立即写入 ✅
├─────────────────────────────┤
│  步骤 2: 生成 header        │ → 立即写入 ✅
├─────────────────────────────┤
│  步骤 3: 生成内容段落 1     │ → 立即写入 ✅
├─────────────────────────────┤
│  步骤 4: 生成内容段落 2     │ → 立即写入 ✅
├─────────────────────────────┤
│  步骤 5: 生成 footer        │ → 立即写入 ✅
└─────────────────────────────┘
  ↓
完成！文件已生成
```

**无需任何脚本，LLM 直接生成微信公众号兼容的 HTML！** 🎉

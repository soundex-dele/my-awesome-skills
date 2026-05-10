# HyperFrames 提示词模板

此模板定义了如何将视频脚本转换为结构化的HyperFrames合成提示词。

## 提示词结构

### 1. 项目概述

```
创建一个 [时长] 的 [内容类型] 视频
目标受众：[从脚本提取]
核心信息：[从脚本的核心卖点提取]
```

### 2. 设计系统

```
## 设计系统

### 视觉风格
- 情绪：[根据BGM风格推断 - 如：现代/科技感/轻松/专业]
- 风格参考：[匹配house-style.md中的预设风格]

### 色彩方案
- 主色：[品牌色或根据情绪推荐]
- 强调色：[用于关键词高亮]
- 背景：[深色/浅色，根据情绪决定]

### 排版
- 标题字号：[根据视频尺寸，60px+]
- 正文字号：[20px+]
- 字体：[内建字体或design.md指定]

### 动画特征
- 节奏模式：[如：快-快-慢-快-着色器-保持]
- 能量水平：[高/中/低]
- 主要缓动函数：[至少3种不同的easing]
```

### 3. 场景分解模板

对每个场景，使用以下模板：

```
## 场景 N：[场景名称] ([开始时间]s - [结束时间]s)

### 画面布局
- [描述主要元素和位置]
- 布局类型：[居中/左右分割/卡片堆叠等]

### 元素
- [元素1名称]：[样式描述]
- [元素2名称]：[样式描述]

### 进场动画
```javascript
// [元素1]
tl.from("[selector]", {
  y: 50,
  opacity: 0,
  duration: 0.6,
  ease: "power3.out"
}, [起始偏移]);

// [元素2]
tl.from("[selector]", {
  x: -40,
  opacity: 0,
  scale: 0.9,
  duration: 0.5,
  ease: "expo.out"
}, [交错偏移]);
```

### 字幕/台词
"[内容]"

### 音频
- BGM：[风格描述]
- 音效：[特定音效]
- 配音：[如有]

### 转场至下一场景
- 类型：[淡入淡出/擦除/着色器转场]
- 持续时间：[秒]
```

### 4. 技术规格

```
## 技术要求

### 输出格式
- 分辨率：[1920x1080 / 1080x1920 / 其他]
- 帧率：[通常30fps]
- 时长：[从脚本提取的总时长]

### 必须遵循的规则
1. 所有场景必须使用转场（无跳跃剪辑）
2. 每个元素必须有进场动画（gsap.from）
3. 除最终场景外，不使用退出动画
4. 时间线必须注册到 window.__timelines
5. 使用确定性动画（无 Math.random()）
```

### 5. 特殊效果映射

根据脚本中的描述映射到HyperFrames技术：

| 脚本描述 | HyperFrames实现 |
|---------|----------------|
| "文字炸开/炸裂出现" | gsap.from({ scale: 0, opacity: 0, ease: "elastic.out(1, 0.5)" }) |
| "从侧边滑入" | gsap.from({ x: [distance], ease: "power3.out" }) |
| "弹性行进" | ease: "elastic.out" 或 "back.out" |
| "淡入" | gsap.from({ opacity: 0 }) |
| "旋转问号" | gsap.from({ rotation: -180, opacity: 0 }) |
| "卡片弹出" | gsap.from({ scale: 0.8, opacity: 0, ease: "back.out" }) |
| "音频驱动/律动" | 使用 audio-reactive.md 模式 |
| "波形可视化" | Canvas 2D 或 SVG 绘制，音频驱动 |

### 6. 常见场景模式

#### 开场文字炸裂
```javascript
tl.from(".title", {
  scale: 0,
  opacity: 0,
  rotation: -15,
  duration: 0.8,
  ease: "elastic.out(1, 0.5)"
}, 0.3);
```

#### 痛点对比（左右分割）
```javascript
// 左侧
tl.from(".pain-left", {
  x: -100,
  opacity: 0,
  duration: 0.6,
  ease: "power2.out"
}, 0.2);

// 右侧
tl.from(".pain-right", {
  x: 100,
  opacity: 0,
  duration: 0.6,
  ease: "power2.out"
}, 0.4);
```

#### 解决方案揭示（中心放大）
```javascript
tl.from(".solution", {
  scale: 0.5,
  opacity: 0,
  duration: 0.7,
  ease: "back.out(1.7)"
}, 0.3);
```

#### 优势卡片依次弹出
```javascript
tl.from(".benefit-card:nth-child(1)", {
  y: 60,
  opacity: 0,
  duration: 0.5,
  ease: "power3.out"
}, 0);
tl.from(".benefit-card:nth-child(2)", {
  y: 60,
  opacity: 0,
  duration: 0.5,
  ease: "power3.out"
}, 0.15);
tl.from(".benefit-card:nth-child(3)", {
  y: 60,
  opacity: 0,
  duration: 0.5,
  ease: "power3.out"
}, 0.3);
```

## 完整示例

基于示例脚本的提示词：

```
创建一个3分钟的工具介绍视频，介绍HyperFrames——用网页技术做视频动画的工具

目标受众：内容创作者、电商团队、视频制作小白
核心信息：不用专业软件，会打字就能做视频动画

## 设计系统

### 视觉风格
- 情绪：现代、科技感、轻松
- 风格参考：类似house-style中的现代科技风格

### 色彩方案
- 主色：#6366f1 (Indigo - 科技感)
- 强调色：#f59e0b (Amber - 关键词高亮)
- 背景：深色 #0f172a

### 排版
- 标题：80-120px
- 正文：24-32px
- 代码演示：18px monospace

### 动画特征
- 节奏：开场快速(0-30s) → 演示中速(30-150s) → CTA收尾(150-175s)
- 缓动：power3.out, expo.out, back.out, elastic.out

## 场景分解

### 场景1：开场炸裂 (0-3s)
标题："给视频加动画，不用学AE，不用装软件！"
动画：文字从中心炸裂出现，配合音效
GSAP：scale 0→1, opacity 0→1, elastic.out

### 场景2：痛点展示 (3-8s)
左右分割布局：左侧"专业软件太复杂"，右侧"在线模板太死板"
台词："你有好素材，但想做点特效动画，却发现..."

[... 按此模板继续每个场景 ...]

## 技术要求

- 分辨率：1920x1080 (横屏)
- 所有场景使用淡入淡出或擦除转场
- 每个文字元素必须有进场动画
- 字幕使用<span>标签包裹关键词，应用强调色
```

## 转换技巧

1. **时间计算**：将脚本的"X-Ys"转换为data-start和data-duration
2. **元素识别**：从"画面"描述中提取需要创建的DOM元素
3. **动画选择**：根据"文字动效"描述选择GSAP模式
4. **音频规划**：根据"音效/备注"规划audio tracks和转场点
5. **样式应用**：从"字幕重点"提取需要加粗/变色的文本

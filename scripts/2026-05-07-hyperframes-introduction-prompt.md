# HyperFrames 合成提示词：HyperFrames 介绍视频

## 项目概述
在现有视频基础上添加动态文字、转场特效和视觉强调元素
- 时长：175秒（2分55秒）
- 基础层：已有录屏视频
- 叠加层：文字动画、卡片、图标、特效元素

---

## 设计系统

### 视觉风格
- 情绪：现代、科技感、轻松、专业
- 风格参考：现代科技产品介绍风格

### 色彩方案
- 主色：`#6366f1` (Indigo - HyperFrames品牌色)
- 强调色：`#f59e0b` (Amber - 关键词高亮)
- 成功色：`#10b981` (Emerald - 成功提示)
- 警告色：`#ef4444` (Red - 痛点问题)
- 背景：半透明深色遮罩 `rgba(15, 23, 42, 0.85)`

### 排版
- 标题字号：80-120px，字重700
- 副标题：40-60px，字重600
- 字幕：28-36px，字重500
- 代码演示：20px monospace
- 字体：系统内置 sans-serif

### 动画特征
- 节奏模式：快速-中速-快速
- 能量水平：高
- 主要缓动：`power3.out`, `expo.out`, `back.out(1.7)`, `elastic.out(1, 0.5)`

---

## 场景分解

### 场景1：文字动效开场 (0-3s)

**画面布局**
- 全屏居中大标题
- 背景视频略微调暗

**元素**
- `.hero-title`: "给视频加动画，不用学AE，不用装软件！"
  - 颜色：白色
  - 字号：100px
  - 字重：700
  - 文字阴影：0 0 30px rgba(99, 102, 241, 0.5)

**进场动画**
```javascript
tl.from(".hero-title", {
  scale: 0,
  opacity: 0,
  rotation: -10,
  duration: 0.8,
  ease: "elastic.out(1, 0.5)"
}, 0.3);
```

**字幕**
"**给视频加动画，不用学AE，不用装软件！**"

**音效**
- 炸裂/冲击音效配合文字出现

**转场**
- 淡出 + 缩小，0.5s

---

### 场景2：痛点展示 (3-8s)

**画面布局**
- 左右分割布局
- 左侧：红色警告卡片
- 右侧：红色警告卡片

**元素**
- `.pain-left`: "专业软件太复杂"
  - 背景渐变：linear-gradient(135deg, #ef4444, #dc2626)
  - 白色文字
  - 圆角：16px
  - 阴影：0 10px 40px rgba(239, 68, 68, 0.3)

- `.pain-right`: "在线模板太死板"
  - 相同样式

- `.pain-subtitle`: "你有好素材，但想做点特效动画，却发现..."
  - 居中下方
  - 白色文字

**进场动画**
```javascript
// 左侧痛点卡片
tl.from(".pain-left", {
  x: -150,
  opacity: 0,
  rotation: -5,
  duration: 0.6,
  ease: "power2.out"
}, 0.2);

// 右侧痛点卡片
tl.from(".pain-right", {
  x: 150,
  opacity: 0,
  rotation: 5,
  duration: 0.6,
  ease: "power2.out"
}, 0.4);

// 副标题
tl.from(".pain-subtitle", {
  y: 30,
  opacity: 0,
  duration: 0.5,
  ease: "power2.out"
}, 0.6);
```

**字幕**
"你有好素材，但想做点特效动画，却发现..."

**转场**
- 向上擦除 + 淡出，0.6s

---

### 场景3：解决方案揭示 (8-12s)

**画面布局**
- 居中大字
- 品牌色强调

**元素**
- `.solution-text`: "会打字 = 会做视频动画"
  - 字号：80px
  - 颜色：白色
  - "=" 符号使用品牌色高亮

- `.highlight-key`: "会打字"
  - 颜色：#f59e0b
  - 下划线动画

**进场动画**
```javascript
tl.from(".solution-text", {
  scale: 0.5,
  opacity: 0,
  duration: 0.7,
  ease: "back.out(1.7)"
}, 0.3);

// 关键词强调
tl.from(".highlight-key", {
  color: "#ffffff",
  duration: 0.3,
  ease: "power2.out"
}, 0.8);
```

**字幕**
"其实，**会打字就会做视频动画**"

**音效**
- "叮"的成功提示音

**转场**
- 中心扩散 + 淡出，0.5s

---

### 场景4：问题场景动画 (12-30s)

**画面布局**
- 中央：视频素材图标
- 周围：旋转的问号元素
- 气泡："想加特效？"

**元素**
- `.video-icon`: SVG视频图标
  - 尺寸：120x120px
  - 颜色：品牌色

- `.question-mark`: 多个问号元素
  - 随机分布
  - 不同大小
  - 旋转动画

- `.bubble-text`: "想加特效？"
  - 气泡对话框样式
  - 白色背景
  - 深色文字

**进场动画**
```javascript
// 视频图标
tl.from(".video-icon", {
  scale: 0,
  opacity: 0,
  duration: 0.5,
  ease: "back.out"
}, 0.2);

// 问号元素 - 交错出现
document.querySelectorAll(".question-mark").forEach((el, i) => {
  tl.from(el, {
    rotation: -180,
    opacity: 0,
    scale: 0.5,
    duration: 0.4,
    ease: "power2.out"
  }, 0.4 + i * 0.1);
});

// 气泡文字
tl.from(".bubble-text", {
  y: 20,
  opacity: 0,
  duration: 0.5,
  ease: "power2.out"
}, 0.8);
```

**字幕**
"你有视频素材，产品展示、Vlog片段...想加文字动效、转场特效，但专业软件太复杂，在线模板又太死板"

**音效**
- 问号出现音效

**转场**
- 左侧擦除 + 淡出，0.6s

---

### 场景5：HyperFrames界面演示 (30-60s)

**画面布局**
- 顶部：标题 "HyperFrames"
- 中央：保留原有录屏
- 底部：滚动文字说明

**元素**
- `.product-title`: "HyperFrames"
  - 品牌色
  - 字号：60px
  - 字重：700
  - 带光晕效果

- `.product-subtitle`: "用网页技术做视频动画"
  - 白色文字

- `.scrolling-text`: 底部滚动字幕
  - "你的视频 + 简单配置 = 专业级动画效果"

**进场动画**
```javascript
// 产品标题
tl.from(".product-title", {
  y: -50,
  opacity: 0,
  duration: 0.6,
  ease: "power3.out"
}, 0.2);

// 副标题
tl.from(".product-subtitle", {
  y: -30,
  opacity: 0,
  duration: 0.5,
  ease: "power2.out"
}, 0.4);

// 滚动文字
tl.from(".scrolling-text", {
  x: -100,
  opacity: 0,
  duration: 0.8,
  ease: "power2.out"
}, 0.6);
```

**字幕**
"今天给你介绍HyperFrames——用网页技术做视频动画的工具。你的视频，加上简单配置，就能得到专业级动画效果"

**转场**
- 淡出 + 模糊，0.5s

---

### 场景6：场景1演示 (60-85s)

**画面布局**
- 保留原有录屏
- 左侧：代码高亮标注
- 右侧：效果标注箭头

**元素**
- `.demo-title`: "文字进场动画"
  - 白色文字
  - 左上角定位

- `.time-badge`: "3秒钟搞定"
  - 背景：#10b981
  - 圆角胶囊形状
  - 右上角

- `.code-highlight`: 代码高亮框
  - 边框：2px solid #f59e0b
  - 圆角：8px
  - 半透明背景

- `.success-check`: 成功勾选图标
  - 绿色
  - 动画弹出

**进场动画**
```javascript
// 演示标题
tl.from(".demo-title", {
  x: -50,
  opacity: 0,
  duration: 0.5,
  ease: "power2.out"
}, 0.2);

// 时间徽章
tl.from(".time-badge", {
  scale: 0,
  opacity: 0,
  duration: 0.4,
  ease: "back.out"
}, 0.4);

// 代码高亮框
tl.from(".code-highlight", {
  opacity: 0,
  borderColor: "transparent",
  duration: 0.3,
  ease: "power2.out"
}, 1.5);

// 成功勾选
tl.from(".success-check", {
  scale: 0,
  rotation: -180,
  duration: 0.5,
  ease: "elastic.out(1, 0.3)"
}, 2);
```

**字幕**
"看这个，文字进场动画，**3秒钟**就搞定。不用关键帧，不用时间轴，写几行配置就好"

**音效**
- "叮"成功音效

**转场**
- 向右擦除，0.5s

---

### 场景7：场景2演示 (85-110s)

**画面布局**
- 保留原有录屏
- 转场箭头指示
- 代码行高亮

**元素**
- `.demo-title-2`: "视频转场特效"
  - 白色文字

- `.code-badge`: "一行代码"
  - 背景：#f59e0b
  - 白色文字

- `.transition-indicator`: 转场箭头
  - 左右箭头图标
  - 动画移动

- `.cinematic-label`: "电影级切换"
  - 金色文字
  - 带闪光效果

**进场动画**
```javascript
// 标题
tl.from(".demo-title-2", {
  x: -50,
  opacity: 0,
  duration: 0.5,
  ease: "power2.out"
}, 0.2);

// 代码徽章
tl.from(".code-badge", {
  scale: 0,
  duration: 0.4,
  ease: "back.out"
}, 0.4);

// 转场指示箭头 - 循环动画
tl.from(".transition-indicator", {
  x: -200,
  opacity: 0,
  duration: 0.6,
  ease: "power2.out"
}, 0.6);

// 电影级标签
tl.from(".cinematic-label", {
  y: 30,
  opacity: 0,
  duration: 0.5,
  ease: "power2.out"
}, 1);
```

**字幕**
"视频之间要加转场？**一行代码**，就能做出这种电影级的切换效果"

**音效**
- 转场 swoosh 音效

**转场**
- 波纹擦除，0.6s

---

### 场景8：场景3演示 (110-135s)

**画面布局**
- 保留原有录屏
- 音频波形可视化
- 节拍指示器

**元素**
- `.demo-title-3`: "音频驱动动画"
  - 白色文字

- `.waveform`: 音频波形
  - Canvas 绘制
  - 品牌色渐变
  - 音频响应式律动

- `.beat-indicator`: 节拍指示
  - 圆形指示器
  - 随节拍闪烁

- `.vibe-label`: "氛围感拉满"
  - 白色文字
  - 脉冲动画

**进场动画**
```javascript
// 标题
tl.from(".demo-title-3", {
  x: -50,
  opacity: 0,
  duration: 0.5,
  ease: "power2.out"
}, 0.2);

// 波形
tl.from(".waveform", {
  scaleY: 0,
  opacity: 0,
  duration: 0.6,
  ease: "power2.out"
}, 0.4);

// 节拍指示器 - 持续脉冲
tl.from(".beat-indicator", {
  scale: 0.5,
  opacity: 0,
  duration: 0.4,
  ease: "back.out"
}, 0.6);

// 氛围感标签 - 持续脉冲
tl.from(".vibe-label", {
  scale: 0.8,
  opacity: 0,
  duration: 0.5,
  ease: "back.out"
}, 0.8);

// 持续脉冲动画
tl.to(".beat-indicator, .vibe-label", {
  scale: 1.1,
  duration: 0.3,
  ease: "power1.inOut",
  repeat: -1,
  yoyo: true
}, 0);
```

**字幕**
"最牛的是这个——音频驱动动画。画面跟着音乐节奏动起来，氛围感直接拉满"

**音频**
- 音乐节奏同步

**转场**
- 音频波形淡出，0.6s

---

### 场景9：三大优势 (135-150s)

**画面布局**
- 三个优势卡片横向排列
- 交错弹出动画

**元素**
- `.benefit-card-1`: "批量生产"
  - 背景：linear-gradient(135deg, #6366f1, #8b5cf6)
  - 白色文字
  - 图标：批量/队列

- `.benefit-card-2`: "随时修改"
  - 背景：linear-gradient(135deg, #10b981, #059669)
  - 白色文字
  - 图标：编辑/修改

- `.benefit-card-3`: "团队协作"
  - 背景：linear-gradient(135deg, #f59e0b, #d97706)
  - 白色文字
  - 图标：团队/协作

**进场动画**
```javascript
// 三个卡片依次弹出
tl.from(".benefit-card-1", {
  y: 80,
  opacity: 0,
  scale: 0.9,
  duration: 0.5,
  ease: "power3.out"
}, 0);

tl.from(".benefit-card-2", {
  y: 80,
  opacity: 0,
  scale: 0.9,
  duration: 0.5,
  ease: "power3.out"
}, 0.15);

tl.from(".benefit-card-3", {
  y: 80,
  opacity: 0,
  scale: 0.9,
  duration: 0.5,
  ease: "power3.out"
}, 0.3);

// 卡片持续轻微浮动
tl.to(".benefit-card", {
  y: -5,
  duration: 2,
  ease: "sine.inOut",
  repeat: -1,
  yoyo: true,
  stagger: 0.3
}, 1);
```

**字幕**
"**批量生产**、**随时修改**、**团队协作**，这些全都能搞定"

**音效**
- 卡片弹出音效 x3

**转场**
- 向下擦除 + 淡出，0.5s

---

### 场景10：适用人群轮播 (150-165s)

**画面布局**
- 三个场景快速切换
- 底部标签指示

**元素**
- `.audience-scene-1`: "内容创作者"
  - 背景：视频编辑图标
  - 标签：快速包装视频

- `.audience-scene-2`: "电商团队"
  - 背景：购物图标
  - 标签：批量生成产品视频

- `.audience-scene-3`: "教育机构"
  - 背景：教育图标
  - 标签：制作课件动画

- `.scene-indicator`: 底部指示器
  - 三个点
  - 当前场景高亮

**进场动画**
```javascript
// 场景快速切换 - 每个场景 5秒
const scenes = [".audience-scene-1", ".audience-scene-2", ".audience-scene-3"];

scenes.forEach((scene, i) => {
  // 进入
  tl.from(scene, {
    x: 100,
    opacity: 0,
    duration: 0.4,
    ease: "power2.out"
  }, i * 5);

  // 退出
  tl.to(scene, {
    x: -100,
    opacity: 0,
    duration: 0.4,
    ease: "power2.in"
  }, i * 5 + 4.5);
});

// 指示器同步高亮
scenes.forEach((scene, i) => {
  tl.to(`.scene-indicator .dot:nth-child(${i + 1})`, {
    scale: 1.5,
    backgroundColor: "#6366f1",
    duration: 0.2,
    ease: "power2.out"
  }, i * 5);

  tl.to(`.scene-indicator .dot:nth-child(${i + 1})`, {
    scale: 1,
    backgroundColor: "#475569",
    duration: 0.2,
    ease: "power2.out"
  }, i * 5 + 4.5);
});
```

**字幕**
"内容创作者快速包装视频，电商团队批量生成产品视频，教育机构制作课件动画"

**转场**
- 淡出，0.5s

---

### 场景11：CTA画面 (165-175s)

**画面布局**
- 居中大标题
- 底部小字

**元素**
- `.cta-title`: "关注我"
  - 白色文字
  - 字号：80px

- `.cta-subtitle`: "下期：5分钟做第一个动画"
  - 品牌色
  - 字号：40px

- `.cta-footer`: "从零开始"
  - 底部小字
  - 半透明白色

- `.highlight-5min`: "5分钟"
  - 强调色：#f59e0b
  - 放大效果

**进场动画**
```javascript
// 主标题
tl.from(".cta-title", {
  scale: 0.8,
  opacity: 0,
  duration: 0.6,
  ease: "back.out"
}, 0.2);

// 副标题
tl.from(".cta-subtitle", {
  y: 30,
  opacity: 0,
  duration: 0.5,
  ease: "power2.out"
}, 0.5);

// 5分钟强调
tl.from(".highlight-5min", {
  scale: 1.5,
  color: "#ffffff",
  duration: 0.4,
  ease: "power2.out"
}, 0.9);

// 底部小字
tl.from(".cta-footer", {
  y: 20,
  opacity: 0,
  duration: 0.4,
  ease: "power2.out"
}, 1);
```

**字幕**
"想知道怎么做出这些动画？关注我，下期视频，手把手教你从零开始，第一个视频动画只要**5分钟**"

**音频**
- BGM收尾上扬

**结束**
- 保持到结尾

---

## 技术要求

### 输出格式
- 分辨率：1920x1080 (横屏)
- 帧率：30fps
- 总时长：175秒

### 必须遵循的规则
1. 所有场景使用转场（无跳跃剪辑）
2. 每个文字元素必须有进场动画
3. 除最终场景外，不使用退出动画
4. 时间线必须注册到 `window.__timelines`
5. 使用确定性动画（无 `Math.random()`）
6. 关键词使用 `<span class="highlight">` 包裹应用强调色

### 音频轨道
- Track 1: BGM (轻快、现代、科技感)
- Track 2: 音效 (炸裂、叮、swoosh、弹出)
- Track 3: 画外音配音

### 背景视频层
- 使用现有视频作为 `data-video-background`
- 场景5-8 保留完整录屏
- 其他场景添加暗色遮罩 `rgba(15, 23, 42, 0.6)`

---

## 关键词高亮映射

| 原文 | 高亮样式 |
|------|----------|
| 不用学AE、不用装软件 | `<span class="highlight">不用学AE</span>、`<span class="highlight">不用装软件</span>` |
| 会打字就会做 | `<span class="highlight">会打字就会做</span>` |
| 3秒钟、一行代码 | `<span class="highlight">3秒钟</span>`、`<span class="highlight">一行代码</span>` |
| 批量生产、随时修改 | `<span class="highlight">批量生产</span>`、`<span class="highlight">随时修改</span>` |
| HyperFrames | `<span class="brand">HyperFrames</span>` |
| 5分钟 | `<span class="highlight-number">5分钟</span>` |

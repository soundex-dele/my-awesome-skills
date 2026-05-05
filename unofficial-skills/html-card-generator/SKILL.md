---
name: html-card-generator
description: Use when user needs HTML animation cards for social media videos, storyboard sequences, or video content with animated text/graphics that integrate with jianying-editor workflow
---

# HTML Card Generator

## Overview

Generate production-ready HTML animation card sequences for social media videos. Each card is a self-contained HTML file with CSS animations and JavaScript, compatible with jianying-editor's web-vfx system for video recording.

**Core principle:** Transform user requirements (storyboard + style description) into executable HTML animations without manual HTML/CSS/JS coding.

## When to Use

```
User needs video content? → Animated cards involved? → Social media format? → Use this skill
        ↓                        ↓                           ↓
   Product demo            Text animations          Douyin/TikTok
   Tutorial                Motion graphics          Short videos
   Presentation            Scene transitions        Mobile-first
```

**Use this skill when:**
- User mentions "video cards", "HTML animations", "motion graphics"
- User provides storyboard or scene-by-scene breakdown
- Target platform is social media (Douyin, TikTok, Instagram Reels)
- Output needs to integrate with jianying-editor
- User wants animated text/graphic sequences

**Don't use for:**
- Static image slides (use simpler tools)
- Complex 3D scenes (use specialized 3D tools)
- Live-action video footage (this is for overlay content)

## Workflow

### Step 1: Parse User Requirements

Extract from user input:
- **Storyboard**: Scene-by-scene content breakdown
- **Style**: Visual aesthetic (tech, minimal, vibrant, etc.)
- **Orientation**: Landscape (1920x1080) or Portrait (1080x1920)
- **Duration**: Per-scene timing (default 3-5 seconds)

### Step 2: Select Style Template

Choose from **8 preset styles** (see Style Library below) or infer from user description:
- Keywords: "modern", "clean" → `minimal`
- Keywords: "tech", "digital", "AI" → `tech`
- Keywords: "fun", "energetic" → `vibrant`
- etc.

### Step 3: Generate Scene Cards

For each scene in storyboard:
1. Determine scene type (cover, content, features, quote, code, cta, ending)
2. Apply style template (colors, typography, animation patterns)
3. Generate complete HTML with embedded CSS/JS
4. Ensure animation contract compliance (see Animation Rules)

### Step 4: Output File Sequence

Generate files with naming convention: `card_{序号:02d}_{场景类型}.html`

## Style Library

| Style | Colors (CSS variables) | Visual Features | Best For |
|-------|------------------------|-----------------|----------|
| **tech** | `--primary: #00f2fe`, `--secondary: #4facfe` | Glassmorphism, pulse animations, grid backgrounds | Tech products, AI tools, software demos |
| **minimal** | `--bg: #ffffff`, `--text: #1a1a1a`, `--accent: #333333` | Clean typography, fade transitions, generous whitespace | Luxury brands, art content, professional presentations |
| **vibrant** | `--primary: #ff6b6b`, `--secondary: #ffc04d`, `--accent: #6c5ce7` | Bounce animations, high contrast, gradient overlays | Entertainment, youth content, lifestyle |
| **business** | `--primary: #2c3e50`, `--secondary: #3498db` | Structured layouts, slide animations, professional icons | Corporate presentations, B2B marketing, training |
| **retro** | `--primary: #e67e22`, `--secondary: #d35400`, `--bg: #f5e6d3` | Vintage fonts, film grain effects, classic borders | Nostalgic themes, classic products, throwback content |
| **cute** | `--primary: #ffb6b9`, `--secondary: #feca57`, `--accent: #ff9ff3` | Rounded corners, elastic animations, playful icons | Kids content, pets, lifestyle, parenting |
| **premium** | `--primary: #c0c0c0`, `--gold: #d4af37`, `--bg: #1a1a1a` | Metallic gradients, shine effects, elegant typography | Luxury goods, high-end services, exclusive offers |
| **dark** | `--bg: #0a0a0a`, `--primary: #00ff88`, `--accent: #ff00ff` | Neon glow effects, cyber elements, high contrast | Gaming, eSports, nightlife, tech |

## Scene Types & Templates

### 1. cover - 封面/片头

**Purpose:** Opening title card with main heading and subtitle

**Structure:**
```html
<div class="cover-container">
  <div class="tag-line">[Tag/Category]</div>
  <h1 class="main-title">[Main Title]</h1>
  <p class="subtitle">[Subtitle/Description]</p>
  <div class="decoration"></div>
</div>
```

**Animation:** Title scale-in, subtitle fade-up, decoration pulse

### 2. content - 内容页

**Purpose:** Informational content with heading and body text

**Structure:**
```html
<div class="content-container">
  <h2 class="section-title">[Section Title]</h2>
  <div class="content-body">
    <p>[Paragraph content]</p>
    <p>[Additional paragraphs as needed]</p>
  </div>
  <div class="visual-element"></div>
</div>
```

**Animation:** Title slide-in, paragraphs cascade-fade

### 3. features - 特性列表

**Purpose:** Grid of feature items with icons and descriptions

**Structure:**
```html
<div class="features-grid">
  <div class="feature-item">
    <div class="feature-icon">[Icon/Emoji]</div>
    <h3 class="feature-title">[Feature Name]</h3>
    <p class="feature-desc">[Description]</p>
  </div>
  <!-- Repeat for each feature (typically 3-4 items) -->
</div>
```

**Animation:** Items stagger-fade-in with scale effect

### 4. quote - 金句/引用

**Purpose:** Large centered quote or key message

**Structure:**
```html
<div class="quote-container">
  <div class="quote-mark">"</div>
  <p class="quote-text">[Quote content]</p>
  <div class="quote-author">— [Author/Source]</div>
</div>
```

**Animation:** Text reveal, scale pulsing, author fade-in

### 5. code - 代码展示

**Purpose:** Display code with syntax highlighting

**Structure:**
```html
<div class="code-container">
  <div class="code-header">
    <span class="lang-tag">[Language]</span>
  </div>
  <pre class="code-block"><code>[Code content]</code></pre>
</div>
```

**Animation:** Typewriter effect or line-by-line reveal

### 6. cta - 号召行动

**Purpose:** Call-to-action with button and prompt

**Structure:**
```html
<div class="cta-container">
  <h2 class="cta-title">[Action Prompt]</h2>
  <p class="cta-subtitle">[Supporting text]</p>
  <button class="cta-button">[Button Text]</button>
  <div class="cta-decorations"></div>
</div>
```

**Animation:** Button pulse-in, text bounce, decorations rotate

### 7. ending - 结尾

**Purpose:** Closing card with thanks and follow prompt

**Structure:**
```html
<div class="ending-container">
  <h2 class="thanks-text">Thank You!</h2>
  <p class="follow-text">[Follow/Subscribe prompt]</p>
  <div class="social-icons">[Social media icons/emojis]</div>
</div>
```

**Animation:** Heart bounce, icons spin, gentle fade

## Animation Contract (jianying-editor compatibility)

**CRITICAL:** All generated HTML MUST comply with these rules:

```javascript
// 1. REQUIRED: Set completion signal when animation finishes
window.animationFinished = true;

// 2. REQUIRED: Transparent background for video overlay
body {
  background: transparent;
  margin: 0;
  overflow: hidden;
}

// 3. Duration: Default 3-5 seconds per card
const ANIMATION_DURATION = 3000; // ms, adjust per scene

// 4. Use requestAnimationFrame for smooth animations
requestAnimationFrame(animate);

// 5. OPTIONAL: Load external libraries via CDN
// <script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>
```

**File format requirements:**
- Single file (HTML + CSS + JS inline)
- UTF-8 encoding
- No external resources (except CDN libraries)
- No `alert()` or blocking operations
- Responsive to orientation (landscape/portrait)

## Size Adaptation

### Landscape (1920x1080) - Default

```css
:root {
  --width: 1920px;
  --height: 1080px;
}
body {
  width: var(--width);
  height: var(--height);
  font-size: 48px; /* Base font size */
}
```

### Portrait (1080x1920)

```css
:root {
  --width: 1080px;
  --height: 1920px;
}
body {
  width: var(--width);
  height: var(--height);
  font-size: 42px; /* Adjusted for mobile */
}
/* Adjust layouts for vertical stacking */
```

**Tip:** Use CSS variables and relative units (rem, %, vw/vh) for easier adaptation.

## Complete Example

### User Input

```
制作一个剪映AI剪辑介绍视频的卡片序列：

故事板：
1. 封面：标题"剪映AI自动化剪辑"，副标题"让视频创作更简单"
2. 功能页：展示3个核心功能
   - 智能剪辑 🎬
   - 自动字幕 ✨
   - AI旁白 🎙️
3. 结尾：号召行动"立即体验"

风格：科技感，横屏
```

### Generated Output

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
// Animation completion signal
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

## Output Format

### File Naming Convention

```
card_{序号:02d}_{场景类型}.html

Examples:
- card_01_cover.html
- card_02_features.html
- card_03_ending.html
```

### Return Format

After generating cards, provide:

```
Generated {N} cards:
{file_list}

Usage with jianying-editor:
```python
from jy_wrapper import JyProject

project = JyProject("MyVideo")

for i, html_file in enumerate([{files}]):
    project.add_web_asset_safe(
        html_path=html_file,
        start_time=f"{i * 3}s",
        duration="3s"
    )

project.save()
```

## jianying-editor Integration

Generated HTML cards are **directly compatible** with jianying-editor workflow:

```python
from jy_wrapper import JyProject

# Create new project
project = JyProject("SocialMediaVideo")

# Batch import cards
cards = [
    "card_01_cover.html",
    "card_02_content.html",
    "card_03_features.html",
    "card_04_ending.html"
]

for i, card in enumerate(cards):
    # Each card plays for 3-5 seconds
    start = f"{i * 3}s"
    project.add_web_asset_safe(
        html_path=card,
        start_time=start,
        duration="3s"
    )

# Export video
project.export(output_path="final_video.mp4")
```

**Integration benefits:**
- Automatic recording of HTML animations
- Transparent background for layering
- Precise timing control
- No manual encoding needed

## Orientation Guidelines

### Landscape (横屏 1920×1080)

**Key Principles:**
- Use relative units (`vw`, `vh`, `%`) instead of fixed pixels
- Body: `width: 100vw; height: 100vh;`
- Content padding: `5vh 5vw` for safe margins
- All fonts, spacing, animations in viewport units

**Template Structure:**
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

/* Typography - relative to viewport */
h1 { font-size: 7vw; }
p { font-size: 2.5vw; }
```

**Best Practices:**
- ✅ Use `vw` for horizontal dimensions
- ✅ Use `vh` for vertical dimensions
- ✅ Set `max-width/max-height` on containers
- ✅ Use `%` for responsive grids
- ❌ Avoid fixed `px` for dimensions
- ❌ Avoid hardcoded widths/heights

### Portrait (竖屏 1080×1920)

**Key Challenge:** Vertical content must be rotated -90° for landscape display

**Rotation Pattern:**
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

**⚠️ CRITICAL: Safe Area & Unit Selection**

**Problem:** After rotating -90°, `vh`/`vw` units calculate against the **wrong viewport axis**, causing content overflow or misalignment. Additionally, short-form video platforms (Douyin, TikTok) reserve ~10% of screen space at top/bottom for UI elements (like/comment buttons).

**Solution:**
1. **Reduce max dimensions** to 90% (not 100%) to create safe area
2. **Use fixed pixels (px)** instead of `vh`/`vw` for consistent sizing after rotation
3. **Apply fixed padding** (80-100px) rather than viewport-relative padding

**Correct Pattern:**
```css
.card {
  width: 1080px;
  height: 1920px;
  transform: rotate(-90deg);
  max-width: 90vh;   /* NOT 100vh - leaves 5% on each side */
  max-height: 90vw;  /* NOT 100vw - leaves 5% on each side */
  padding: 80px 60px; /* Fixed pixels, NOT vh/vw */
}
```

**Critical Settings:**

| Property | Value | Purpose |
|----------|-------|---------|
| `transform: rotate(-90deg)` | -90deg | Rotate vertical to horizontal |
| `max-width: 90vh` | 90% of viewport height | **Critical:** Limits width + creates safe area |
| `max-height: 90vw` | 90% of viewport width | **Critical:** Limits height + creates safe area |
| `padding: 80px 60px` | Fixed pixels | **Use px NOT vh/vw** for consistent spacing |
| `overflow: hidden` | hidden | Clip excess content |

**Background Handling:**
```css
/* Background fills entire screen */
body {
  background: linear-gradient(135deg, #0a1628 0%, #1a2a4a 100%);
}

/* Card background */
.card {
  background: transparent; /* Or matching gradient */
}
```

**Content Layout:**
- **Use fixed pixels (px)** for all measurements inside card
- **AVOID vh/vw units** - they calculate incorrectly after rotation
- Padding: `80px 60px` for portrait-specific spacing
- Font sizes: `80-100px` for titles, `28-40px` for body text
- Stack vertically with `flex-direction: column`

**Common Portrait Pitfalls:**

| Issue | Cause | Solution |
|-------|-------|----------|
| **Content cut off at edges** | `max-width/max-height: 100vh/100vw` leaves no safe area | Use `90vh/90vw` to reserve 10% for platform UI |
| **VH/VW units misaligned** | After rotation, `vh` measures width, `vw` measures height | Use **fixed pixels (px)** for all sizes, padding, fonts |
| **Top/bottom content clipped** | Platform UI overlays (like button, comments) | Keep important content within 80% center area |
| Wrong orientation | Missing rotate | Add `transform: rotate(-90deg)` |
| Overflow | No size constraints | Add `overflow: hidden` to wrapper |
| Distorted content | Width/height mismatch | Ensure 1080×1920 base size |

**Testing Checklist:**
- [ ] Background fills entire screen
- [ ] Content is properly rotated
- [ ] No horizontal scrollbars
- [ ] **Top/bottom 10% safe area is free of critical content**
- [ ] **Fixed pixels used (not vh/vw) for all sizes**
- [ ] Text is readable at scale
- [ ] Animations play correctly
- [ ] Card centers in viewport with margin on all sides

### Responsive Design Tips

**Use CSS Variables for Consistency:**
```css
:root {
  --safe-margin: 5vh 5vw;
  --title-size: 7vw;
  --body-size: 2.5vw;
}
```

**Media Queries (Optional):**
```css
@media (max-aspect-ratio: 16/9) {
  /* Adjust for narrower screens */
  :root {
    --title-size: 6vw;
  }
}
```

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Missing `window.animationFinished` | Always set this signal at animation end |
| Non-transparent background | Use `background: transparent` or gradient overlays |
| Fixed dimensions only | Use CSS variables for orientation flexibility |
| **Using vh/vw in portrait cards** | **Use fixed pixels (px) - vh/vw break after rotation** |
| **max-width/max-height: 100vh/100vw** | **Use 90vh/90vw to reserve safe area for platform UI** |
| Blocking operations (alert, prompt) | Never use blocking calls in animation code |
| External local resources | Use CDNs or inline everything |

## CDN Libraries (Optional)

Enhance animations with these libraries:

```html
<!-- GSAP for complex timelines -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>

<!-- Three.js for 3D effects -->
<script src="https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.min.js"></script>

<!-- Anime.js for simplified animations -->
<script src="https://cdn.jsdelivr.net/npm/animejs@3.2.1/lib/anime.min.js"></script>
```

**Use sparingly** - vanilla CSS/JS is preferred for simple animations.

## Quick Reference

```
Story → Parse → Style → Generate → Output
  ↓       ↓       ↓         ↓         ↓
Input  Extract  Select  Create    Files
```

**Style selection heuristic:**
- Tech/AI/SaaS → `tech`
- Luxury/Art → `minimal` or `premium`
- Kids/Family → `cute`
- Business/Corp → `business`
- Gaming/Esports → `dark`
- Food/Lifestyle → `vibrant`
- Nostalgic → `retro`

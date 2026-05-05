---
name: script-to-jianying
description: Convert video scripts to Jianying (CapCut) draft files using YAML format specification
---

# Script to Jianying Converter

This skill converts video scripts into Jianying (CapCut) draft files using a structured YAML format.

## Workflow

### Phase 1: Read and Understand Input

1. **Read the video script** from the user-specified file path
   - Ask the user for the script file path if not provided
   - Read and parse the script content
   - Identify the script structure (scenes, segments, timing, etc.)

2. **Read the YAML specification** from `/Users/xiesongde/workspace/video/pyJianYingDraft/YAML_SPECIFICATION.md`
   - This specification defines the required YAML format
   - Pay special attention to:
     - Document structure (metadata + elements)
     - Time range format: `"Xs-Ys"` where Y is **duration**, not end time
     - Element types: audio, video, image, text
     - Required and optional fields for each element type
     - Constraints (no overlapping tracks, valid ranges, etc.)

### Phase 2: Generate YAML Conversion Plan

3. **Analyze the script** and create a conversion plan:

   Check for media asset availability:
   - Ask user if they have video/image/audio files ready
   - If **NO**, use placeholder files on correct tracks (see Asset Placeholder Strategy)
   - If **YES**, ask for asset directory path

   Present a structured plan to the user:

   ```
   📋 YAML文件生成计划

   脚本信息:
   - 标题: <title>
   - 总时长: <duration>
   - 场景数量: <count>
   - 分辨率: <resolution>

   素材策略: <使用占位符 / 使用实际素材>

   元素统计:
   - 音频: <audio_count> 个
   - 视频: <video_count> 个
   - 图片: <image_count> 个
   - 文字: <text_count> 个

   输出:
   - YAML文件: <output_file_path>
   - 剪映草稿目录: <draft_folder>
   ```

4. **Get user confirmation** before proceeding:
   - Use `AskUserQuestion` to confirm the plan
   - Options:
     - "确认生成" (Proceed with generation)
     - "修改计划" (Modify the plan)
     - "取消" (Cancel)

### Phase 3: Generate and Convert

5. **Generate the YAML file**:
   - Create complete YAML content based on the specification
   - Include required metadata (title, width, height, fps)
   - Create elements array with proper time ranges
   - **⚠️ CRITICAL: Every element MUST include `track_name` field (multi-track mode required)**
   - Ensure all constraints are met
   - Validate against the specification rules

6. **Write the YAML file** to disk:
   - Save to the specified output path
   - Confirm file creation

7. **Convert to Jianying draft** using the conversion script:

   **Important**: Handle paths with spaces properly using one of these methods:

   Method 1 - Use double quotes (recommended):
   ```bash
   python yaml_to_draft.py examples/agent_intro.yaml "/Users/xiesongde/Movies/JianyingPro/User Data/Projects/com.lveditor.draft"
   ```

   Method 2 - Use single quotes:
   ```bash
   python yaml_to_draft.py examples/agent_intro.yaml '/Users/xiesongde/Movies/JianyingPro/User Data/Projects/com.lveditor.draft'
   ```

   Method 3 - Use backslash escape:
   ```bash
   python yaml_to_draft.py examples/agent_intro.yaml \
     /Users/xiesongde/Movies/JianyingPro/User\ Data/Projects/com.lveditor.draft
   ```

   When using the Bash tool, **always use Method 1 (double quotes)** for reliability.

8. **Report completion**:
   ```
   ✅ 转换完成!

   生成的文件:
   ✓ YAML: <yaml_file_path>
   ✓ 剪映草稿: <draft_path>

   请在剪映中打开项目查看效果。
   ```

## Asset Placeholder Strategy

⚠️ **When media assets are not available**, use text elements on separate tracks with `track_name`.

### Placeholder Format

Use `type: text` with different `track_name` values for each media type:

```yaml
# Video placeholder → on "视频占位符" track
- type: text
  content: "[VIDEO] intro.mp4 - 开场视频"
  time_range: "0s-5s"
  track_name: "视频占位符"  # Separate track for video placeholders
  style:
    color: "#ff0000"  # Red color to mark as placeholder
    position:
      x: 0
      y: 0

# Image placeholder → on "图片占位符" track
- type: text
  content: "[IMAGE] screenshot.png - 界面截图"
  time_range: "2s-3s"
  track_name: "图片占位符"  # Separate track for image placeholders
  style:
    color: "#ff9900"  # Orange for images
    position:
      x: 0
      y: 0

# Audio placeholder → on "音频占位符" track
- type: text
  content: "[AUDIO] bgm.mp3 - 背景音乐"
  time_range: "0s-15s"
  track_name: "音频占位符"  # Separate track for audio placeholders
  style:
    color: "#0099ff"  # Blue for audio
    position:
      x: 0
      y: 0.5

# Regular text → on default track or "文字" track
- type: text
  content: "正常文字内容"
  time_range: "1s-4s"
  # No track_name = default track, or use track_name: "文字"
  style:
    color: "#ffffff"
```

### Placeholder Track Naming

**Recommended track names**:
- 视频占位符 → `track_name: "视频占位符"`
- 图片占位符 → `track_name: "图片占位符"`
- 音频占位符 → `track_name: "音频占位符"`
- 普通文字 → `track_name: "文字"` or omit (use default)

### Benefits of Separate Tracks

✅ **Easy to identify**: Each placeholder type is on its own track in Jianying
✅ **No overlap conflicts**: Different tracks can overlap in time
✅ **Simple replacement**: Select entire track and replace with real media
✅ **Color coding**: Each track uses different colors for visual clarity

### Placeholder Color Coding

- **🔴 Red (#ff0000)**: Video placeholders on "视频占位符" track
- **🟠 Orange (#ff9900)**: Image placeholders on "图片占位符" track
- **🔵 Blue (#0099ff)**: Audio placeholders on "音频占位符" track
- **⚪ White (#ffffff)**: Regular text on default or "文字" track

### Conversion to Real Assets

After generating the draft with separate placeholder tracks:

1. **Open in Jianying**
   - Launch Jianying and open the generated project
   - You'll see separate tracks for each placeholder type

2. **Identify placeholder tracks**
   - 🔴 "视频占位符" track - Red text, video placeholders
   - 🟠 "图片占位符" track - Orange text, image placeholders
   - 🔵 "音频占位符" track - Blue text, audio placeholders
   - ⚪ "文字" track - White text, regular content

3. **Replace each placeholder**
   - Select the entire placeholder track or individual elements
   - Note the filename and timing from the text content
   - Delete the placeholder text element
   - Import and add the actual media file
   - Set the same time_range
   - Apply the same animations/transitions if needed

### Example with Placeholders (Multi-Track)

```yaml
metadata:
  title: "Demo Video with Placeholders"
  width: 1920
  height: 1080
  fps: 30

elements:
  # Audio placeholder track
  - type: text
    content: "[AUDIO] background.mp3 - 背景音乐"
    time_range: "0s-15s"
    track_name: "音频占位符"
    style:
      color: "#0099ff"
      position:
        x: 0
        y: 0.5

  # Video placeholder track
  - type: text
    content: "[VIDEO] intro.mp4 - 开场"
    time_range: "0s-5s"
    track_name: "视频占位符"
    style:
      color: "#ff0000"
      font: 文轩体
      position:
        x: 0
        y: 0
    animations:
      - type: intro
        subtype: 向上滑动

  # Regular text track
  - type: text
    content: "标题文字"
    time_range: "1s-4s"
    track_name: "文字"
    style:
      color: "#ffffff"
      font: 文轩体
      position:
        x: 0
        y: -0.3

  # Image placeholder track
  - type: text
    content: "[IMAGE] diagram.png - 流程图"
    time_range: "5s-3s"
    track_name: "图片占位符"
    style:
      color: "#ff9900"
      position:
        x: 0
        y: 0
```

## Important Rules

### ⚠️ MANDATORY: Multi-Track Mode with track_name

**🚨 CRITICAL REQUIREMENT: ALL elements MUST include `track_name` field**

**必须包含 track_name，使用多轨道模式！**

Every element in the YAML **MUST** have a `track_name` field. Do NOT use numeric `track` values - always use named tracks.

#### Required Format (✅ CORRECT):

```yaml
elements:
  # Video on "main_video" track
  - type: video
    content: intro.mp4
    time_range: "0s-5s"
    track_name: "main_video"  # ✅ REQUIRED - Must use track_name

  # Audio on "background_music" track
  - type: audio
    content: bgm.mp3
    time_range: "0s-15s"
    track_name: "background_music"  # ✅ REQUIRED - Must use track_name

  # Text on "subtitles" track
  - type: text
    content: "欢迎"
    time_range: "1s-3s"
    track_name: "subtitles"  # ✅ REQUIRED - Must use track_name
```

#### Invalid Format (❌ WRONG):

```yaml
elements:
  # ❌ WRONG: Missing track_name entirely
  - type: video
    content: intro.mp4
    time_range: "0s-5s"
    # No track_name - THIS WILL FAIL!

  # ❌ WRONG: Using numeric track instead of track_name
  - type: audio
    content: bgm.mp3
    time_range: "0s-15s"
    track: 0  # Do NOT use numeric track values!
```

#### Track Naming Best Practices:

Use descriptive, meaningful track names:

| Track Purpose | Recommended track_name | Example |
|--------------|------------------------|---------|
| Main video content | `"main_video"` or `"视频"` | Background video, main footage |
| Background music | `"bgm"` or `"背景音乐"` | Background audio |
| Sound effects | `"sfx"` or `"音效"` | Sound effects |
| Voiceover/narration | `"voiceover"` or `"旁白"` | Voice narration |
| Subtitles/captions | `"subtitles"` or `"字幕"` | Text captions |
| Titles/headings | `"titles"` or `"标题"` | Title text |
| Overlays | `"overlays"` or `"叠加"` | Overlay graphics/text |
| Placeholders | `"placeholders"` or `"占位符"` | Placeholder elements |

#### Multi-Track Architecture:

```
Jianying Timeline Structure:
┌─────────────────────────────────────────────┐
│ Track: "bgm" (背景音乐)                      │
│  ├─ [bgm.mp3] 0s────────────────────30s     │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ Track: "main_video" (主视频)                 │
│  ├─ [intro.mp4] 0s───────5s                 │
│  ├─ [demo.mp4]  5s──────10s                 │
│  └─ [outro.mp4] 10s────15s                  │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ Track: "subtitles" (字幕)                   │
│  ├─ "欢迎"     1s───3s                      │
│  ├─ "智能助手" 6s───8s                      │
│  └─ "开始使用" 11s──14s                     │
└─────────────────────────────────────────────┘
```

#### Benefits of Multi-Track Mode:

✅ **Clear organization**: Each track has a specific purpose
✅ **Easy editing**: Select entire track to modify all related elements
✅ **No overlap confusion**: Different tracks can overlap in time
✅ **Professional workflow**: Matches industry-standard video editing practices
✅ **Simple maintenance**: Easy to identify and modify specific element types

#### Validation Checklist:

Before finalizing YAML, verify EVERY element has:
- [ ] `track_name` field is present
- [ ] `track_name` is a string (not a number)
- [ ] `track_name` is descriptive and meaningful
- [ ] Elements with same `track_name` do NOT overlap in time
- [ ] Elements with different `track_name` CAN overlap in time

**Remember**: `track_name` is **MANDATORY** for ALL elements. Never omit it!

### Time Range Format

⚠️ **CRITICAL**: Time ranges use `"start-duration"` format, NOT `"start-end"`:

- ✅ `"0s-5s"` = starts at 0s, lasts 5 seconds, ends at 5s
- ✅ `"2s-3s"` = starts at 2s, lasts 3 seconds, ends at 5s
- ❌ `"0s-5s"` is NOT "from 0s to 5s"

### 🚨 CRITICAL: No Overlapping Segments on Same Track

**⚠️ THIS IS THE MOST IMPORTANT RULE - VIOLATING THIS WILL CAUSE CONVERSION ERRORS**

**同一轨道上的片段，时间绝对不能重叠！**

Elements on the **same track** must **never overlap in time**. Each segment must end before the next one begins on that track.

#### Examples of Invalid Overlaps (❌ DO NOT DO THIS):

```yaml
# ❌ WRONG: Two videos on same track overlapping in time
elements:
  - type: video
    content: intro.mp4
    time_range: "0s-5s"    # Starts at 0s, ends at 5s
    track: 0               # Same track!

  - type: video
    content: demo.mp4
    time_range: "3s-5s"    # Starts at 3s, ends at 8s
    track: 0               # Same track! OVERLAP from 3s-5s! ❌
```

#### Examples of Valid Non-Overlapping Segments (✅ CORRECT):

```yaml
# ✅ CORRECT: Segments on same track, sequential timing
elements:
  - type: video
    content: intro.mp4
    time_range: "0s-5s"    # Starts at 0s, ends at 5s
    track: 0

  - type: video
    content: demo.mp4
    time_range: "5s-5s"    # Starts at 5s, ends at 10s
    track: 0               # Same track, but NO overlap ✅

  - type: video
    content: outro.mp4
    time_range: "10s-5s"   # Starts at 10s, ends at 15s
    track: 0               # Same track, sequential ✅
```

#### How to Handle Simultaneous Content (Use Different Tracks):

```yaml
# ✅ CORRECT: Different tracks allow time overlap
elements:
  # Video on track 0
  - type: video
    content: background.mp4
    time_range: "0s-10s"   # 0s to 10s
    track: 0

  # Audio on track 1 (can overlap with video)
  - type: audio
    content: bgm.mp3
    time_range: "0s-10s"   # Same time range, different track ✅
    track: 1

  # Text on track 2 (can overlap with both)
  - type: text
    content: "Title"
    time_range: "2s-3s"    # Overlaps with others, different track ✅
    track: 2
```

#### Track-Specific Rules:

| Track Type | Overlap Allowed? | Notes |
|------------|------------------|-------|
| **Audio** | ❌ NO | Only one audio element at a time per track |
| **Video** | ❌ NO | Only one video element at a time per track |
| **Image** | ❌ NO | Only one image element at a time per track |
| **Text** | ✅ YES | Multiple text elements can overlap on same track |

#### Validation Checklist for Each Track:

Before finalizing the YAML, verify for **each track**:

```bash
# Track 0 (Video):
#   Segment 1: 0s → 5s  ✓
#   Segment 2: 5s → 8s  ✓ (starts exactly when previous ends)
#   Segment 3: 8s → 10s ✓ (sequential, no overlap)

# Track 1 (Audio):
#   Segment 1: 0s → 15s ✓
#   Segment 2: 15s → 20s ✓ (sequential, no overlap)
```

**Remember**: `track_name` creates separate tracks. Elements with different `track_name` values can overlap in time. Elements with the same `track_name` (or same `track` number) must **never** overlap!

### Element Constraints

1. **⚠️ MANDATORY track_name field**:
   - **EVERY element MUST have `track_name` field**
   - **Do NOT use numeric `track` values**
   - Use descriptive names like `"main_video"`, `"bgm"`, `"subtitles"`, etc.

2. **Track overlap**:
   - 🚫 **Audio elements cannot overlap on same `track_name`**
   - 🚫 **Video/image elements cannot overlap on same `track_name`**
   - ✅ **Text elements CAN overlap on same `track_name`**
   - ✅ **Different `track_name` values CAN overlap in time**

3. **Required fields**:
   - **ALL elements**: `type`, `time_range`, `track_name` ⚠️
   - Audio/Video/Image: `content` (file path)
   - Text: `content` (text string)

4. **Metadata requirements**:
   - `title` (required)
   - `width` (required)
   - `height` (required)
   - `fps` (optional, default: 30)

### File Path Handling

- Use relative paths when possible (relative to YAML file location)
- Or use absolute paths if assets are in different locations
- Warn users if asset files don't exist

### Common Resolution Presets

- **横屏 (Landscape)**: 1920x1080
- **竖屏 (Portrait/TikTok)**: 1080x1920
- **正方形 (Square/Instagram)**: 1080x1080
- **4K**: 3840x2160

## User Interaction

### Initial Questions

Before starting, ask the user:

1. **Script file path**: Where is the video script located?
2. **Asset availability**: Do you have video/image/audio files ready, or should we use text placeholders?
   - If placeholders: Will use text elements on separate tracks with track_name
   - If real assets: Provide the assets directory path
3. **Output YAML file**: Where should the YAML file be saved? (default: `examples/<script_name>.yaml`)
4. **Draft folder**: Where is the Jianying draft folder?
   - Default: `/Users/xiesongde/Movies/JianyingPro/User Data/Projects/com.lveditor.draft`

### Progress Updates

Provide clear progress feedback:

```
📝 正在生成YAML文件...
✓ YAML内容已生成
✓ 已保存到: /path/to/file.yaml

🎬 正在生成剪映草稿...
✓ 草稿已创建
```

## Example Conversion

### Input Script (with placeholders)

```
Title: Agent Intro
Duration: 15 seconds
Resolution: 1920x1080 (landscape)

Note: No media assets available yet, use placeholders

Timeline:
0-5s:
  - Audio: bgm.mp3 (placeholder)
  - Video: intro.mp4 (placeholder)
  - Text: "欢迎来到Agent世界" (center, animated)

5-10s:
  - Video: demo.mp4 (placeholder)
  - Text: "智能助手" (top center)

10-15s:
  - Video: outro.mp4 (placeholder)
  - Text: "开始使用" (center, outro animation)
```

### Output YAML (with placeholders)

```yaml
metadata:
  title: "Agent Intro"
  width: 1920
  height: 1080
  fps: 30

elements:
  # Audio placeholder (on "音频占位符" track)
  - type: text
    content: "[AUDIO] bgm.mp3 - 背景音乐"
    time_range: "0s-15s"
    track_name: "音频占位符"
    style:
      color: "#0099ff"
      font: 文轩体
      position:
        x: 0
        y: 0.5

  # Scene 1: 0-5s
  # Video placeholder (on "视频占位符" track)
  - type: text
    content: "[VIDEO] intro.mp4 - 开场动画"
    time_range: "0s-5s"
    track_name: "视频占位符"
    style:
      color: "#ff0000"
      font: 文轩体
      position:
        x: 0
        y: 0
    animations:
      - type: intro
        subtype: 向上滑动

  # Regular text (on default "文字" track)
  - type: text
    content: "欢迎来到Agent世界"
    time_range: "0.5s-4s"
    track_name: "文字"
    style:
      font: 文轩体
      color: "#ffffff"
      position:
        x: 0
        y: -0.3
    animations:
      - type: intro
        subtype: 动感放大

  # Scene 2: 5-10s
  # Video placeholder (on "视频占位符" track)
  - type: text
    content: "[VIDEO] demo.mp4 - 演示视频"
    time_range: "5s-5s"
    track_name: "视频占位符"
    style:
      color: "#ff0000"
      font: 文轩体
      position:
        x: 0
        y: 0
    animations:
      - type: intro
        subtype: 放大

  # Regular text (on "文字" track)
  - type: text
    content: "智能助手"
    time_range: "5.5s-9s"
    track_name: "文字"
    style:
      font: 文轩体
      color: "#ffffff"
      position:
        x: 0
        y: -0.5

  # Scene 3: 10-15s
  # Video placeholder (on "视频占位符" track)
  - type: text
    content: "[VIDEO] outro.mp4 - 结尾画面"
    time_range: "10s-5s"
    track_name: "视频占位符"
    style:
      color: "#ff0000"
      font: 文轩体
      position:
        x: 0
        y: 0
    animations:
      - type: intro
        subtype: 向下甩入

  # Regular text (on "文字" track)
  - type: text
    content: "开始使用"
    time_range: "10.5s-14s"
    track_name: "文字"
    style:
      font: 文轩体
      color: "#ffff00"
      position:
        x: 0
        y: 0
    animations:
      - type: intro
        subtype: 弹性伸缩
```

### Conversion Command

```bash
cd /Users/xiesongde/workspace/video/pyJianYingDraft
python yaml_to_draft.py examples/agent_intro.yaml \
  "/Users/xiesongde/Movies/JianyingPro/User Data/Projects/com.lveditor.draft"
```

**Note**: Use double quotes around the path to handle spaces properly.

## Validation Checklist

Before writing the YAML file, verify:

### Metadata (基础元数据)
- [ ] Metadata has title, width, height
- [ ] fps is specified or can use default (30)

### Element Requirements (元素要求)
- [ ] **ALL elements have `track_name` field** ⚠️ **MANDATORY**
- [ ] All elements have `type` and `time_range`
- [ ] No elements use numeric `track` values (use `track_name` only)

### Time Format (时间格式)
- [ ] Time ranges use "Xs-Ys" format (start-duration, NOT start-end)
- [ ] Duration values are positive numbers
- [ ] Time values are within reasonable bounds (not negative)

### Track Validation (轨道验证)
- [ ] **For each `track_name`: verify no overlapping segments** (except text)
- [ ] Audio elements on same track_name don't overlap
- [ ] Video/Image elements on same track_name don't overlap
- [ ] Track names are descriptive and meaningful

### Asset Validation (素材验证)
- [ ] All file paths are valid or warnings issued
- [ ] File paths use proper format (relative or absolute)
- [ ] Audio/video files have supported extensions

### Style Validation (样式验证)
- [ ] Animations use valid Chinese names
- [ ] Colors are in valid format (#hex, [r,g,b], or name)
- [ ] Positions are in range (-1.0 to 1.0)
- [ ] Volumes are in range (0.0 to 1.0)
- [ ] Font sizes are reasonable (not too large/small)

## Tools and Commands

Use these tools during execution:

1. **Read** - Read the script file and YAML specification
2. **AskUserQuestion** - Get confirmation and preferences
3. **Write** - Write the YAML file
4. **Bash** - Execute the conversion script

## Error Handling

If any step fails:

1. **Script parsing error**:
   - Report the specific error
   - Ask user to fix the script or provide more details

2. **YAML generation error**:
   - Report the specific validation error
   - Ask user if they want to: fix manually, or abort

3. **Draft conversion error**:
   - Report the error from yaml_to_draft.py
   - YAML file is still saved
   - Suggest checking file paths and trying manually

## Manual Asset Replacement Guide

After generating the draft with separate placeholder tracks, follow these steps to replace with real assets:

### Step-by-Step Process

1. **Open in Jianying**
   - Launch Jianying and open the generated project
   - You'll see separate tracks for each media type:
     - "视频占位符" track with red text
     - "图片占位符" track with orange text
     - "音频占位符" track with blue text
     - "文字" track with white text (regular content)

2. **Identify Placeholders by Track**
   - Find the "视频占位符" track → Contains all video placeholders
   - Find the "图片占位符" track → Contains all image placeholders
   - Find the "音频占位符" track → Contains all audio placeholders
   - Find the "文字" track → Contains regular text content (keep as-is)

3. **Replace Each Track**

   **Method 1: Replace entire track at once**
   - Select all elements on a placeholder track
   - Note all filenames and timings
   - Delete the entire track
   - Create new track of appropriate type (video/audio)
   - Add all media files at correct timings

   **Method 2: Replace one element at a time**
   For each placeholder element on a track:

   a. **Read the placeholder content**:
      - Example: `[VIDEO] intro.mp4 - 开场动画`
      - Extract filename: `intro.mp4`
      - Note the timing from the timeline
      - Note any animations applied

   b. **Delete the placeholder** text element

   c. **Add the real media**:
      - Import `intro.mp4` to Jianying
      - Drag to timeline at the same position
      - Ensure duration matches the placeholder's time_range

   d. **Reapply effects**:
      - Add the same intro/outro animations
      - Apply transitions if the placeholder had them

4. **Verify and Export**
   - Play through the entire timeline
   - Check all timings and transitions
   - Ensure all placeholders are replaced
   - Export when satisfied

### Quick Reference Table

| Track Name | Color | Media Type | Replace With |
|------------|-------|------------|--------------|
| 视频占位符 | 🔴 Red | Video | `.mp4`, `.mov` video files |
| 图片占位符 | 🟠 Orange | Image | `.png`, `.jpg` image files |
| 音频占位符 | 🔵 Blue | Audio | `.mp3`, `.wav` audio files |
| 文字 | ⚪ White | Regular Text | Keep as-is (no replacement) |

### Track Replacement Workflow Example

```
Original YAML structure:
├── "音频占位符" track → [AUDIO] bgm.mp3, [AUDIO] sfx.mp3
├── "视频占位符" track → [VIDEO] intro.mp4, [VIDEO] demo.mp4
├── "图片占位符" track → [IMAGE] screenshot.png
└── "文字" track → "标题", "字幕", "说明"

After replacement:
├── Audio track → bgm.mp3, sfx.mp3 (real audio files)
├── Video track → intro.mp4, demo.mp4 (real video files)
├── Video track → screenshot.png (real image file)
└── Text track → "标题", "字幕", "说明" (unchanged)
```

### Tips for Efficient Replacement

- **Track-by-track approach**: Replace one entire track before moving to the next
- **Keep a checklist**: Track which placeholders have been replaced
- **Organize media files**: Keep all assets in a folder with matching filenames
- **Preview frequently**: Check each replacement before moving to the next
- **Copy animations**: Note animation settings before deleting placeholders

## Notes

- Always preserve the original script structure in the YAML
- Use Chinese for animation names (as per specification)
- Default to common presets when not specified
- Provide helpful error messages for common mistakes
- The YAML file contains the complete video in one file
- Generate the YAML file first, then immediately convert to draft
- **⚠️ EVERY element MUST have `track_name` field - this is MANDATORY**
- **⚠️ Use `track_name` only - never use numeric `track` values**
- **⚠️ Elements on the same `track_name` must NOT overlap in time (except text)**
- **Placeholders use `type: text` with separate `track_name` values for each media type**
- **Separate tracks make it easy to identify and replace placeholders in Jianying**
- **Different tracks can overlap in time - use this to your advantage**
- **When replacing placeholders, match the exact timing and animations from the placeholder**

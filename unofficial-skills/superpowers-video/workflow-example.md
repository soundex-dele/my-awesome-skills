# Complete Video Production Workflow

End-to-end example of creating a video using the Superpowers Video skills and Jianying Converter Tools.

## Overview

This workflow demonstrates how to:
1. Brainstorm video concepts with `video-brainstorming` skill
2. Generate a detailed script with YAML segments using `video-script` skill
3. Convert the script to Jianying project format using `script-to-jianying` skill
4. Import and edit the project in JianyingPro/CapCut

## Prerequisites

- Python 3.10+ installed
- Agent system configured with Superpowers Video skills
- JianyingPro (China) or CapCut (International) installed
- Basic understanding of video editing concepts

## Step 1: Brainstorming - Video Concept Development

**Use the `video-brainstorming` skill** to develop your video concept.

**Example:**

```markdown
I want to create a tutorial video on "How to Build a REST API with Python".

Use the video-brainstorming skill to help me plan this video.
```

**The skill will guide you through:**

1. **Purpose Definition** - What is the video's goal?
   - Educational? Marketing? Entertainment?
   - What should viewers learn or do?

2. **Audience Analysis** - Who is this for?
   - Skill level (beginner, intermediate, advanced)
   - Age range, technical background
   - Platform expectations (YouTube, TikTok, etc.)

3. **Format Selection** - What type of video?
   - Tutorial with screen recording
   - Face-to-camera explanation
   - Mixed format (face + screen)
   - Animation or motion graphics

4. **Visual Direction** - What will it look like?
   - Color scheme and branding
   - Style (professional, casual, playful)
   - Graphics and overlays needed

**Output:** Approved video outline with visual direction

**Example Outline:**

```markdown
# Video Outline: Build a REST API with Python

## Purpose
Teach beginners how to create a simple REST API using Flask

## Audience
- Python beginners with basic programming knowledge
- Ages 18-35
- Platform: YouTube (16:9, 10-15 minutes)

## Format
- 30% face camera (intro/conclusion)
- 70% screen recording (coding demo)
- Voiceover narration

## Visual Direction
- Clean, professional look
- Blue and white color scheme
- Code syntax highlighting
- Cursor highlight and zoom effects
```

---

## Step 2: Generate Script with YAML Segments

**Use the `video-script` skill** to create a detailed script with embedded YAML segment mappings.

**Example:**

```markdown
I have an approved outline. Use the video-script skill with --export-jianying flag
to generate a production-ready script with YAML segment mappings.
```

**The skill will create:**

1. **Scene-by-scene breakdown** - Each visual/narration segment
2. **YAML segment blocks** - Structured data for each segment
3. **Timing specifications** - Exact duration for each segment
4. **Visual descriptions** - Camera angles, screen content, effects
5. **Narration text** - Exact spoken words

**Example Script with YAML Blocks:**

```markdown
# Scene 1: Introduction (0:00 - 0:30)

## Visual
Face camera, medium shot, professional background

## Narration
"Welcome to this tutorial on building REST APIs with Python. In this video,
you'll learn how to create a simple API using Flask."

## Segment Mapping
```yaml
segments:
  - id: scene1_intro
    type: video
    target_timerange:
      start: 0
      duration: 30000000  # 30 seconds
    content:
      source: "footage/intro_face.mp4"
      transform:
        position: [540, 960]  # Center of 1080x1920
        scale: 1.0

  - id: scene1_title
    type: text
    target_timerange:
      start: 2000000  # 2 seconds
      duration: 8000000  # 8 seconds
    content:
      text: "Building a REST API with Python"
      font:
        family: "Arial"
        size: 64
        color: "#FFFFFF"
      position:
        x: 540
        y: 300
      animation:
        type: "fadeIn"
        duration: 1000000  # 1 second
```

---

# Scene 2: What is a REST API? (0:30 - 1:30)

## Visual
Screen recording: PowerPoint slides with diagrams

## Narration
"Before we dive into coding, let's understand what a REST API is..."
[Continued...]
```

**Key Features:**

- **YAML blocks** embedded in each scene
- **Segment IDs** for tracking
- **Precise timing** in microseconds
- **Type-specific fields** (text content, video source, etc.)
- **Material references** (fonts, audio, video files)

**Output:** `video-script.md` with YAML segment mappings

---

## Step 3: Convert to Jianying Project Format

**Use the `script-to-jianying` skill** to parse the script and generate Jianying project files.

### 3.1 Parse and Validate

```python
from engine.agent.skills.superpowers_video.script_to_jianying.parsers.script_parser import ScriptParser
from engine.agent.skills.superpowers_video.script_to_jianying.parsers.segment_validator import SegmentValidator

# Parse script
parser = ScriptParser()
parsed_data = parser.parse_file('video-script.md')

# Validate all segments
validator = SegmentValidator()
validation_errors = []

for scene in parsed_data['scenes']:
    result = validator.validate_scene(scene)
    if not result.is_valid:
        validation_errors.extend(result.errors)

if validation_errors:
    print("❌ Validation failed:")
    for error in validation_errors:
        print(f"  - {error}")
else:
    print("✅ All segments validated successfully")
```

### 3.2 Generate Intermediate JSON

```python
import json
from pathlib import Path

# Build segment mapping
segment_mapping = {
    'project_name': Path('video-script.md').stem,
    'canvas': parsed_data['global_config'].get('canvas', {
        'width': 1080,
        'height': 1920,
        'ratio': '9:16',
        'fps': 30
    }),
    'tracks': parsed_data['scenes'],
    'materials': parsed_data['global_config'].get('materials', {}),
    'total_duration_us': parsed_data['total_duration_us']
}

# Write to file
with open('segment-mapping.json', 'w') as f:
    json.dump(segment_mapping, f, indent=2)
```

### 3.3 Convert to Jianying Files

```bash
python3 tools/video/jianying_converter.py \
    segment-mapping.json \
    -o jianying_project/ \
    --template-dir tools/video/jianying_templates \
    --strict
```

**Expected Output:**

```
✅ Conversion successful!
   Files: draft_info.json, draft_meta_info.json
   Segments: 45
   Duration: 612.50s
```

**Generated Files:**

```
jianying_project/
├── draft_info.json         # Main project file
└── draft_meta_info.json    # Project metadata
```

---

## Step 4: Import and Edit in JianyingPro

### 4.1 Locate Jianying Projects Directory

**macOS:**
```bash
~/Library/Application Support/JianyingPro/User Data/Projects/
```

**Windows:**
```bash
%USERPROFILE%\Documents\JianyingPro\
```

### 4.2 Copy Project Files

```bash
# Copy generated project to Jianying directory
cp -r jianying_project/ ~/Library/Application\ Support/JianyingPro/User\ Data/Projects/rest-api-tutorial/
```

### 4.3 Open in JianyingPro

1. Launch JianyingPro application
2. Click "Create New" or import existing project
3. Navigate to `rest-api-tutorial` folder
4. Open `draft_info.json`

### 4.4 Review and Adjust

**Check the following:**

- **Timeline Structure** - All segments present and correctly ordered
- **Text Content** - Font sizes, colors, positioning
- **Video/Audio Clips** - Correct sources, timing
- **Transitions** - Smooth scene changes
- **Effects** - Applied as specified

**Make manual adjustments if needed:**

- Add background music
- Adjust text positioning
- Fine-tune timing
- Add additional effects
- Insert B-roll footage

### 4.5 Export Final Video

1. Click "Export" button
2. Select platform preset (YouTube, TikTok, etc.)
3. Choose resolution and bitrate
4. Click "Export" to render final video

**Example Export Settings:**

- **Platform:** YouTube
- **Resolution:** 1080x1920 (9:16)
- **Frame Rate:** 30 fps
- **Bitrate:** 10 Mbps
- **Codec:** H.264

---

## Complete Workflow Summary

```
┌─────────────────────────────────────────────────────────────┐
│ Step 1: Brainstorming (video-brainstorming skill)           │
│ Input: Video idea                                           │
│ Output: Approved outline with visual direction              │
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│ Step 2: Generate Script (video-script skill)                │
│ Input: Approved outline                                     │
│ Output: video-script.md with YAML segment mappings          │
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│ Step 3: Convert to Jianying (script-to-jianying skill)      │
│ 3a. Parse script with ScriptParser                          │
│ 3b. Validate segments with SegmentValidator                 │
│ 3c. Generate segment-mapping.json                           │
│ 3d. Convert with jianying_converter.py                      │
│ Output: draft_info.json, draft_meta_info.json               │
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│ Step 4: Import and Edit (JianyingPro/CapCut)                │
│ 4a. Copy project files to Jianying directory                │
│ 4b. Open project in JianyingPro                             │
│ 4c. Review and adjust manually                              │
│ 4d. Export final video                                      │
│ Output: Final MP4 video file                                │
└─────────────────────────────────────────────────────────────┘
```

## Tips for Success

### Brainstorming Phase

- **Be specific** about your audience and platform
- **Approve the outline** before proceeding to scripting
- **Consider platform constraints** (TikTok: 9:16, YouTube: 16:9)

### Scripting Phase

- **Include all visual details** in YAML blocks
- **Use precise timing** (calculate durations carefully)
- **Reference materials** correctly (fonts, audio, video paths)

### Conversion Phase

- **Always validate** in strict mode first
- **Check the intermediate JSON** structure
- **Use absolute paths** for templates

### Editing Phase

- **Review timeline** for gaps or overlaps
- **Test playback** at full speed
- **Add polish** with music and effects
- **Export at appropriate quality** for your platform

## Troubleshooting

**Issue:** Validation fails during conversion

**Solution:**
```bash
# Check validation errors
python3 -c "
from engine.agent.skills.superpowers_video.script_to_jianying.parsers.segment_validator import SegmentValidator
validator = SegmentValidator()
# ... run validation
"

# Fix YAML syntax errors in script
# Ensure all required fields present
# Verify material references exist
```

**Issue:** Project doesn't import in JianyingPro

**Solution:**
```bash
# Verify draft_info.json structure
python3 -m json.tool jianying_project/draft_info.json

# Check file permissions
ls -la jianying_project/

# Ensure correct project directory location
```

**Issue:** Segments missing or incorrectly timed

**Solution:**
```bash
# Review segment-mapping.json
python3 -m json.tool segment-mapping.json | less

# Check timing calculations
# Verify no overlaps or gaps
# Re-run conversion with --no-strict for debugging
```

## Next Steps

Once comfortable with the basic workflow:

1. **Add Subtitles** - Use `video-subtitles` skill for multi-track subtitles
2. **Add Effects** - Use `video-effects` skill for transitions and polish
3. **Customize Templates** - Modify Jianying templates for your style
4. **Batch Processing** - Automate conversion for multiple videos

## Related Documentation

- **Jianying Converter README** - `tools/video/README.md`
- **video-script Skill** - `engine/agent/skills/superpowers-video/video-script/SKILL.md`
- **script-to-jianying Skill** - `engine/agent/skills/superpowers-video/script-to-jianying/SKILL.md`
- **Jianying Converter Plan** - `docs/superpowers/plans/2026-03-18-script-to-jianying-converter.md`

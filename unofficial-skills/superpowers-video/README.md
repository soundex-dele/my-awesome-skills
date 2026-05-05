# Jianying Converter Tools

Command-line utilities for converting video scripts with YAML segment mappings to Jianying (剪映/CapCut) project files.

## Overview

This toolkit provides a Python-based converter that transforms structured video scripts into Jianying project format. It parses scripts with embedded YAML segment blocks, validates the data, and generates `draft_info.json` files that can be imported directly into Jianying/CapCut for video editing.

## Quick Start

```bash
# Convert a script with segment mapping to Jianying project
python3 jianying_converter.py segment-mapping.json -o output_dir/

# With custom template directory
python3 jianying_converter.py segment-mapping.json \
  -o output_dir/ \
  --template-dir /path/to/templates
```

## File Structure

```
tools/video/
├── jianying_converter.py          # Main converter CLI
├── jianying_templates/            # Jianying project templates
│   ├── draft_info.json.template
│   ├── draft_meta_info.json.template
│   └── draft_settings.template
├── converters/                    # Data conversion modules
│   ├── track_converter.py        # Convert track data
│   ├── segment_converter.py      # Convert segment data
│   ├── material_converter.py     # Convert materials (fonts, audio)
│   └── keyframe_converter.py     # Convert keyframe data
├── validators/                    # Output validation
│   └── output_validator.py       # Validate generated project files
└── utils/                         # Utility functions
    ├── time_utils.py             # Time format conversions
    ├── id_generator.py           # Generate unique IDs
    └── path_resolver.py          # Resolve file paths
```

## Usage

### 1. Generate Script with YAML Segments

First, create a video script with YAML segment mappings using the `video-script` skill:

```bash
# Use the video-script skill with --export-jianying flag
# This generates a script with embedded YAML blocks
```

### 2. Parse and Validate with script-to-jianying Skill

Use the `script-to-jianying` skill to parse the script and generate intermediate JSON:

```python
from engine.agent.skills.superpowers_video.script_to_jianying.parsers.script_parser import ScriptParser

parser = ScriptParser()
parsed_data = parser.parse_file('video-script.md')

# Validate segments
from engine.agent.skills.superpowers_video.script_to_jianying.parsers.segment_validator import SegmentValidator

validator = SegmentValidator()
validation_result = validator.validate_scene(parsed_data['scenes'][0])
```

### 3. Convert to Jianying Project

Convert the intermediate JSON to Jianying project files:

```bash
python3 jianying_converter.py segment-mapping.json -o jianying_project/
```

## Input Format

The converter expects a JSON file with the following structure:

```json
{
  "project_name": "my-video",
  "canvas": {
    "width": 1080,
    "height": 1920,
    "ratio": "9:16",
    "fps": 30
  },
  "tracks": [
    {
      "scene_index": 1,
      "segments": [
        {
          "id": "seg_001",
          "type": "text",
          "target_timerange": {
            "start": 0,
            "duration": 3000000
          },
          "content": {
            "text": "Hello World",
            "font_size": 48
          }
        }
      ]
    }
  ],
  "materials": {
    "fonts": {},
    "audio": {}
  },
  "total_duration_us": 60000000
}
```

## Output

The converter generates the following files in the output directory:

- **draft_info.json** - Main Jianying project file containing tracks, segments, and materials
- **draft_meta_info.json** - Project metadata (name, duration, sync settings)

## Command-Line Options

```
usage: jianying_converter.py [-h] [-o OUTPUT] [--template-dir TEMPLATE_DIR]
                             [--strict] [--no-strict]
                             input

positional arguments:
  input                 Path to segment-mapping.json

optional arguments:
  -h, --help            Show help message and exit
  -o OUTPUT, --output OUTPUT
                        Output directory (default: .)
  --template-dir TEMPLATE_DIR
                        Template files directory
                        (default: tools/video/jianying_templates)
  --strict              Enable strict validation (default: True)
  --no-strict           Disable strict validation
```

## Validation

The converter performs strict validation by default:

- Required fields present (id, type, target_timerange)
- Valid segment types (text, audio, video, etc.)
- Type-specific fields (content for text/audio/video)
- Valid time ranges (start >= 0, duration > 0)
- No timing overlaps between segments
- No significant gaps (> 0.1s)
- Material references exist

Disable strict validation for debugging:

```bash
python3 jianying_converter.py segment-mapping.json --no-strict
```

## Integration with Video Skills

This tool integrates with the Superpowers Video skills framework:

1. **video-script** - Generates scripts with YAML segment mappings
2. **script-to-jianying** - Parses scripts and validates segments
3. **jianying_converter.py** - Converts to Jianying project format

## Supported Segment Types

- **text** - Text overlays with fonts, colors, animations
- **audio** - Audio clips with volume, fade in/out
- **video** - Video clips with transforms, effects
- **image** - Image overlays with positioning
- **sticker** - Sticker elements with animations

## Error Handling

The converter provides detailed error messages:

```bash
# Validation error example
❌ Conversion failed: Segment seg_001: Missing required field 'content'

# Template error example
❌ Conversion failed: Template not found: /invalid/path/draft_info.json.template
```

## Development

### Running Tests

```bash
cd tools/video
python -m pytest tests/
```

### Adding New Segment Types

1. Update schema in `tools/video/schemas/segment_schema.json`
2. Add conversion logic in `converters/segment_converter.py`
3. Add validation rules in `validators/output_validator.py`

## Troubleshooting

**Common Issues:**

1. **"Template not found"** - Check `--template-dir` path, use absolute path
2. **"Validation failed"** - Check segment-mapping.json structure, ensure all required fields present
3. **"Permission denied"** - Ensure output directory is writable
4. **"Invalid segment type"** - Check segment type is supported

**Debug Mode:**

```bash
# Disable strict validation to see partial output
python3 jianying_converter.py segment-mapping.json --no-strict

# Check intermediate JSON structure
python3 -m json.tool segment-mapping.json
```

## License

Part of the Superpowers Video skills framework.

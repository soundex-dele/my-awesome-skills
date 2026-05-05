"""Script to Jianying conversion skill."""

import json
from pathlib import Path
from typing import Dict, Any
from parsers.script_parser import ScriptParser
from parsers.segment_validator import SegmentValidator
from parsers.timing_calculator import TimingCalculator


def convert_script_to_mapping(script_path: str, output_dir: str) -> Dict[str, Any]:
    """Convert script to segment mapping JSON."""
    parser = ScriptParser()
    validator = SegmentValidator()
    calculator = TimingCalculator()

    # Parse script
    print("Parsing script...")
    parsed = parser.parse_file(script_path)
    print(f"✓ Found {parsed['total_scenes']} scenes with YAML blocks")

    # Build materials registry
    materials_registry = {}
    global_config = parsed.get('global_config', {})
    if 'materials' in global_config:
        for mat_type in global_config['materials']:
            for mat in global_config['materials'][mat_type]:
                if 'id' in mat:
                    materials_registry[mat['id']] = mat

    # Validate segments
    print("Validating segments...")
    all_errors = []
    for scene in parsed['scenes']:
        result = validator.validate_scene(scene, materials_registry)
        if not result.is_valid:
            all_errors.extend(result.errors)

    if all_errors:
        print("✗ Validation failed:")
        for error in all_errors:
            print(f"  {error}")
        raise ValueError("Segment validation failed")

    print(f"✓ All {sum(len(s['data'].get('segments', [])) for s in parsed['scenes'])} segments validated")

    # Calculate timing
    print("Calculating timeline...")
    timeline = calculator.calculate_timeline(parsed['scenes'])
    print(f"✓ Total duration: {timeline['total_duration_us'] / 1_000_000:.2f}s")

    # Generate output
    global_config = parsed.get('global_config', {})
    mapping = {
        'version': '1.0',
        'project_name': global_config.get('project_name', 'Untitled'),
        'canvas': global_config.get('canvas', {
            'width': 1080,
            'height': 1920,
            'ratio': '9:16',
            'fps': 30
        }),
        'total_duration_us': timeline['total_duration_us'],
        'tracks': _build_tracks(parsed['scenes'])
    }

    # Write output
    out_path = Path(output_dir) / 'segment-mapping.json'
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(mapping, indent=2, ensure_ascii=False))
    print(f"✓ Generated {out_path}")

    return mapping


def _build_tracks(scenes):
    """Build track structure from scenes."""
    # Aggregate segments by type into tracks
    tracks = {
        'main_track': [],
        'caption_track': [],
        'narration_track': []
    }

    for scene in scenes:
        segments = scene['data'].get('segments', [])
        for seg in segments:
            seg_type = seg.get('type')
            if seg_type == 'text':
                tracks['caption_track'].append(seg)
            elif seg_type == 'audio':
                tracks['narration_track'].append(seg)
            elif seg_type == 'video':
                tracks['main_track'].append(seg)

    return [
        {'id': 'main_track', 'type': 'video', 'segments': tracks['main_track']},
        {'id': 'caption_track', 'type': 'text', 'segments': tracks['caption_track']},
        {'id': 'narration_track', 'type': 'audio', 'segments': tracks['narration_track']}
    ]
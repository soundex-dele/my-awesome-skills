"""Validate segment data."""

from typing import List, Dict, Any


class ValidationResult:
    """Validation result."""
    def __init__(self, is_valid: bool, errors: List[str] = None):
        self.is_valid = is_valid
        self.errors = errors or []


class SegmentValidator:
    """Validate segment data in strict mode."""

    REQUIRED_FIELDS = ['id', 'type', 'target_timerange']
    VALID_TYPES = ['text', 'audio', 'video', 'image', 'sticker', 'effect', 'transition', 'handwrite', 'chroma']

    # Type-specific required fields
    TYPE_SPECIFIC_FIELDS = {
        'text': ['content'],
        'audio': ['content'],
        'video': ['content'],
        'image': ['content'],
        'sticker': ['content']
    }

    def validate_scene(self, scene: Dict[str, Any], materials_registry: Dict[str, Any] = None) -> ValidationResult:
        """Validate scene segments."""
        errors = []
        segments = scene.get('data', {}).get('segments', [])

        for i, seg in enumerate(segments):
            # Check required fields
            for field in self.REQUIRED_FIELDS:
                if field not in seg:
                    errors.append(f"Scene {scene['scene_index']}, Segment {i}: Missing required field '{field}'")

            # Check type
            seg_type = seg.get('type')
            if seg_type and seg_type not in self.VALID_TYPES:
                errors.append(f"Scene {scene['scene_index']}, Segment {i}: Invalid type '{seg_type}'")

            # Check type-specific fields
            if seg_type in self.TYPE_SPECIFIC_FIELDS:
                for field in self.TYPE_SPECIFIC_FIELDS[seg_type]:
                    if field not in seg:
                        errors.append(f"Scene {scene['scene_index']}, Segment {i}: Missing type-specific field '{field}' for type '{seg_type}'")

            # Check timerange
            if 'target_timerange' in seg:
                timerange = seg['target_timerange']
                if 'start' not in timerange or 'duration' not in timerange:
                    errors.append(f"Scene {scene['scene_index']}, Segment {i}: Incomplete timerange")
                elif timerange['start'] < 0 or timerange['duration'] <= 0:
                    errors.append(f"Scene {scene['scene_index']}, Segment {i}: Invalid timerange values")

            # Check material references
            if 'extra_material_refs' in seg:
                for ref_id in seg['extra_material_refs']:
                    if materials_registry and ref_id not in materials_registry:
                        errors.append(f"Scene {scene['scene_index']}, Segment {i}: Orphaned material reference '{ref_id}'")

        # Check for timing overlaps and gaps
        timing_errors = self._validate_timing(scene['scene_index'], segments)
        errors.extend(timing_errors)

        return ValidationResult(is_valid=len(errors) == 0, errors=errors)

    def _validate_timing(self, scene_index: int, segments: List[Dict]) -> List[str]:
        """Validate timing for overlaps and gaps."""
        errors = []

        # Sort segments by start time
        sorted_segments = sorted(segments, key=lambda s: s.get('target_timerange', {}).get('start', 0))

        for i in range(len(sorted_segments) - 1):
            current = sorted_segments[i]
            next_seg = sorted_segments[i + 1]

            current_range = current.get('target_timerange', {})
            next_range = next_seg.get('target_timerange', {})

            current_end = current_range.get('start', 0) + current_range.get('duration', 0)
            next_start = next_range.get('start', 0)

            # Check for overlap
            if current_end > next_start:
                overlap_us = current_end - next_start
                errors.append(f"Scene {scene_index}: Timing conflict - segments overlap by {overlap_us / 1_000_000:.2f}s")

            # Check for gaps (only if gap is significant, e.g., > 0.1s)
            gap = next_start - current_end
            if gap > 100000:  # 0.1 second in microseconds
                errors.append(f"Scene {scene_index}: Timing gap - {gap / 1_000_000:.2f}s between segments")

        return errors

"""Calculate and adjust segment timing."""

from typing import List, Dict, Any


class TimingCalculator:
    """Calculate timeline from scene data."""

    def calculate_timeline(self, scenes: List[Dict]) -> Dict[str, Any]:
        """Calculate absolute timing for all scenes."""
        timeline = {'scenes': [], 'total_duration_us': 0}
        current_time = 0

        for scene in scenes:
            scene_data = scene['data']
            duration_us = scene_data.get('duration_us', 0)

            # Adjust segment timing
            segments = scene_data.get('segments', [])
            for seg in segments:
                # Convert relative to absolute time
                if 'target_timerange' in seg:
                    seg['target_timerange']['start'] += current_time

            scene['absolute_start_us'] = current_time
            timeline['scenes'].append(scene)
            current_time += duration_us

        timeline['total_duration_us'] = current_time
        return timeline
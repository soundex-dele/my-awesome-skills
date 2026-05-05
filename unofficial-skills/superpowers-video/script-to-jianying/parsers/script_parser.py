"""Parse video scripts with embedded YAML blocks."""

import re
import yaml
from pathlib import Path
from typing import List, Dict, Any


class SceneBlock:
    """Scene with YAML block."""
    def __init__(self, index: int, start_line: int, yaml_content: str):
        self.index = index
        self.start_line = start_line
        self.yaml_content = yaml_content
        self.data = None


class ScriptParser:
    """Parse script files."""

    YAML_BLOCK_PATTERN = r'```yaml\n(.*?)\n```'

    def parse_file(self, script_path: str) -> Dict[str, Any]:
        """Parse script file."""
        path = Path(script_path)
        with open(path) as f:
            content = f.read()

        # Extract YAML blocks
        yaml_blocks = re.findall(self.YAML_BLOCK_PATTERN, content, re.DOTALL)

        # Parse global config
        global_config = self._extract_global_config(content)

        # Parse scene blocks
        scenes = []
        for i, block in enumerate(yaml_blocks, 1):
            try:
                data = yaml.safe_load(block)
                scenes.append({
                    'scene_index': i,
                    'data': data
                })
            except yaml.YAMLError as e:
                raise ValueError(f"Failed to parse YAML block {i}: {e}")

        return {
            'global_config': global_config,
            'scenes': scenes,
            'total_scenes': len(scenes)
        }

    def _extract_global_config(self, content: str) -> Dict[str, Any]:
        """Extract global config from end of script."""
        # Find "## Global Configuration" section
        match = re.search(r'## Global Configuration.*?```yaml\n(.*?)\n```', content, re.DOTALL)
        if match:
            try:
                return yaml.safe_load(match.group(1))
            except yaml.YAMLError:
                pass
        return {}

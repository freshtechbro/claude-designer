#!/usr/bin/env python3
"""
Fix Agent and Command Paths in Plugin Manifests

Converts directory paths to arrays of .md file paths.

Usage:
    ./fix_agent_command_paths.py
"""

import json
from pathlib import Path


def get_md_files(plugin_dir: Path, subdir: str) -> list[str]:
    """Get all .md files in a subdirectory"""
    md_dir = plugin_dir / subdir
    if not md_dir.exists():
        return []

    md_files = sorted(md_dir.glob("*.md"))
    return [f"./{subdir}/{f.name}" for f in md_files]


def fix_plugin_manifest(plugin_dir: Path):
    """Fix a single plugin manifest"""
    manifest_path = plugin_dir / ".claude-plugin" / "plugin.json"

    if not manifest_path.exists():
        return

    with open(manifest_path, 'r') as f:
        manifest = json.load(f)

    changed = False

    # Fix commands field
    if "commands" in manifest and isinstance(manifest["commands"], str):
        if manifest["commands"].endswith("/"):
            # It's a directory path, convert to array of .md files
            commands = get_md_files(plugin_dir, "commands")
            if commands:
                manifest["commands"] = commands
                changed = True

    # Fix agents field
    if "agents" in manifest and isinstance(manifest["agents"], str):
        if manifest["agents"].endswith("/"):
            # It's a directory path, convert to array of .md files
            agents = get_md_files(plugin_dir, "agents")
            if agents:
                manifest["agents"] = agents
                changed = True

    # Skills can remain as directory since it contains SKILL.md files
    # No need to change skills field

    if changed:
        with open(manifest_path, 'w') as f:
            json.dump(manifest, f, indent=2)
        print(f"✅ Fixed: {plugin_dir.name}")
    else:
        print(f"⏭️  Skipped: {plugin_dir.name} (no changes needed)")


def main():
    repo_root = Path(__file__).parent.parent.parent
    plugins_dir = repo_root / "plugins"

    print("🔧 Fixing agent and command paths...\n")

    # Fix individual plugins
    individual_dir = plugins_dir / "individual"
    if individual_dir.exists():
        for plugin_dir in sorted(individual_dir.iterdir()):
            if plugin_dir.is_dir():
                fix_plugin_manifest(plugin_dir)

    # Fix bundle plugins
    bundles_dir = plugins_dir / "bundles"
    if bundles_dir.exists():
        for plugin_dir in sorted(bundles_dir.iterdir()):
            if plugin_dir.is_dir():
                fix_plugin_manifest(plugin_dir)

    print("\n✅ All plugin manifests processed!")


if __name__ == "__main__":
    main()

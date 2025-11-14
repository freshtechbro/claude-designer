#!/usr/bin/env python3
"""
Fix Plugin Manifest Files

Fixes plugin.json schema validation errors across all plugins.

Usage:
    ./fix_plugin_manifests.py
"""

import json
from pathlib import Path


def fix_plugin_manifest(plugin_json_path: Path):
    """Fix a single plugin manifest"""
    with open(plugin_json_path, 'r') as f:
        manifest = json.load(f)

    # Fix author field: string -> object
    if "author" in manifest and isinstance(manifest["author"], str):
        manifest["author"] = {
            "name": manifest["author"],
            "email": "oladotun.olatunji@gmail.com"
        }

    # Fix repository field: object -> string
    if "repository" in manifest and isinstance(manifest["repository"], dict):
        manifest["repository"] = manifest["repository"]["url"]

    # Fix commands field: must start with ./ and be array of .md files
    if "commands" in manifest and isinstance(manifest["commands"], str):
        if not manifest["commands"].startswith("./"):
            manifest["commands"] = "./" + manifest["commands"]

    # Fix agents field: must start with ./
    if "agents" in manifest and isinstance(manifest["agents"], str):
        if not manifest["agents"].startswith("./"):
            manifest["agents"] = "./" + manifest["agents"]

    # Fix skills field: must start with ./
    if "skills" in manifest and isinstance(manifest["skills"], str):
        if not manifest["skills"].startswith("./"):
            manifest["skills"] = "./" + manifest["skills"]

    # Remove unrecognized fields
    for field in ["category", "bundle", "includes"]:
        if field in manifest:
            del manifest[field]

    # Write back
    with open(plugin_json_path, 'w') as f:
        json.dump(manifest, f, indent=2)

    print(f"✅ Fixed: {plugin_json_path.parent.parent.name}")


def main():
    repo_root = Path(__file__).parent.parent.parent
    plugins_dir = repo_root / ".claude" / "plugins"

    print("🔧 Fixing plugin manifests...\n")

    # Fix individual plugins
    individual_dir = plugins_dir / "individual"
    if individual_dir.exists():
        for plugin_dir in individual_dir.iterdir():
            if plugin_dir.is_dir():
                manifest_path = plugin_dir / ".claude-plugin" / "plugin.json"
                if manifest_path.exists():
                    fix_plugin_manifest(manifest_path)

    # Fix bundle plugins
    bundles_dir = plugins_dir / "bundles"
    if bundles_dir.exists():
        for plugin_dir in bundles_dir.iterdir():
            if plugin_dir.is_dir():
                manifest_path = plugin_dir / ".claude-plugin" / "plugin.json"
                if manifest_path.exists():
                    fix_plugin_manifest(manifest_path)

    print("\n✅ All plugin manifests fixed!")


if __name__ == "__main__":
    main()

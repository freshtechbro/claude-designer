#!/usr/bin/env python3
"""
Marketplace Manifest Generator for Claude Code

Generates the .claude-plugin/marketplace.json file that lists all available plugins.

Usage:
    ./generate_marketplace.py
"""

import json
import sys
from pathlib import Path
from typing import Dict, List


class MarketplaceGenerator:
    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        self.plugins_dir = repo_root / ".claude" / "plugins"
        self.marketplace_file = repo_root / ".claude-plugin" / "marketplace.json"

    def generate(self):
        """Generate marketplace.json"""
        print("\n🏪 Generating marketplace manifest...")

        # Collect all plugins
        individual_plugins = self._collect_individual_plugins()
        bundle_plugins = self._collect_bundle_plugins()

        all_plugins = individual_plugins + bundle_plugins

        # Create marketplace manifest
        marketplace = {
            "name": "claude-design-skillstack",
            "owner": {
                "name": "Claude Design Skillstack",
                "url": "https://github.com/freshtechbro/claudedesignskills"
            },
            "metadata": {
                "description": "Professional design agency skillstack for 3D/WebGL, animation, and modern web development. Comprehensive collection covering Three.js, GSAP, React Three Fiber, Framer Motion, Babylon.js, and more. Includes 22 individual plugins + 5 category bundles.",
                "version": "1.0.0",
                "pluginRoot": "./.claude/plugins",
                "homepage": "https://github.com/freshtechbro/claudedesignskills",
                "repository": "https://github.com/freshtechbro/claudedesignskills"
            },
            "plugins": all_plugins
        }

        # Write marketplace.json
        self.marketplace_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.marketplace_file, 'w') as f:
            json.dump(marketplace, f, indent=2)

        print(f"\n📄 Created: {self.marketplace_file}")
        print(f"   Individual plugins: {len(individual_plugins)}")
        print(f"   Bundle plugins: {len(bundle_plugins)}")
        print(f"   Total plugins: {len(all_plugins)}")
        print("\n✅ Marketplace manifest generated successfully!\n")

    def _collect_individual_plugins(self) -> List[Dict]:
        """Collect all individual plugins"""
        plugins = []
        individual_dir = self.plugins_dir / "individual"

        if not individual_dir.exists():
            return plugins

        for plugin_dir in sorted(individual_dir.iterdir()):
            if not plugin_dir.is_dir():
                continue

            manifest_file = plugin_dir / ".claude-plugin" / "plugin.json"
            if not manifest_file.exists():
                print(f"   ⚠️  Warning: No manifest found for {plugin_dir.name}")
                continue

            with open(manifest_file, 'r') as f:
                manifest = json.load(f)

            # Create plugin entry for marketplace
            plugin_entry = {
                "name": manifest["name"],
                "source": f"./individual/{plugin_dir.name}",
                "version": manifest.get("version", "1.0.0"),
                "description": manifest.get("description", ""),
                "category": manifest.get("category", "general"),
                "tags": manifest.get("keywords", []),
                "author": manifest.get("author", ""),
                "license": manifest.get("license", "Apache-2.0")
            }

            plugins.append(plugin_entry)
            print(f"   ✓ Added: {plugin_dir.name} (individual)")

        return plugins

    def _collect_bundle_plugins(self) -> List[Dict]:
        """Collect all bundle plugins"""
        plugins = []
        bundles_dir = self.plugins_dir / "bundles"

        if not bundles_dir.exists():
            return plugins

        for bundle_dir in sorted(bundles_dir.iterdir()):
            if not bundle_dir.is_dir():
                continue

            manifest_file = bundle_dir / ".claude-plugin" / "plugin.json"
            if not manifest_file.exists():
                print(f"   ⚠️  Warning: No manifest found for {bundle_dir.name}")
                continue

            with open(manifest_file, 'r') as f:
                manifest = json.load(f)

            # Create plugin entry for marketplace
            plugin_entry = {
                "name": manifest["name"],
                "source": f"./bundles/{bundle_dir.name}",
                "version": manifest.get("version", "1.0.0"),
                "description": manifest.get("description", ""),
                "category": manifest.get("category", "bundle"),
                "tags": manifest.get("keywords", []),
                "bundle": True,
                "includes": manifest.get("includes", []),
                "author": manifest.get("author", ""),
                "license": manifest.get("license", "Apache-2.0")
            }

            plugins.append(plugin_entry)
            print(f"   ✓ Added: {bundle_dir.name} (bundle)")

        return plugins


def main():
    """Main entry point"""
    # Find repository root
    repo_root = Path(__file__).parent.parent.parent

    generator = MarketplaceGenerator(repo_root)
    generator.generate()


if __name__ == "__main__":
    main()

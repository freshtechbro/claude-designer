#!/usr/bin/env python3
"""
Marketplace Validator for Claude Code

Validates all plugins and marketplace manifest structure.

Usage:
    ./validate_marketplace.py
"""

import json
import sys
from pathlib import Path
from typing import List, Tuple, Optional


class MarketplaceValidator:
    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        self.plugins_dir = repo_root / ".claude" / "plugins"
        self.marketplace_file = repo_root / ".claude-plugin" / "marketplace.json"
        self.errors = []
        self.warnings = []

    def validate(self) -> bool:
        """Validate all plugins and marketplace"""
        print("\n🔍 Validating marketplace and plugins...\n")

        # Validate marketplace.json
        self._validate_marketplace_json()

        # Validate individual plugins
        self._validate_individual_plugins()

        # Validate bundle plugins
        self._validate_bundle_plugins()

        # Print results
        self._print_results()

        return len(self.errors) == 0

    def _validate_marketplace_json(self):
        """Validate marketplace.json structure"""
        print("📄 Validating marketplace.json...")

        if not self.marketplace_file.exists():
            self.errors.append("marketplace.json not found")
            return

        try:
            with open(self.marketplace_file, 'r') as f:
                marketplace = json.load(f)

            # Check required fields
            required_fields = ["name", "owner", "metadata", "plugins"]
            for field in required_fields:
                if field not in marketplace:
                    self.errors.append(f"marketplace.json: Missing required field '{field}'")

            # Validate name
            if "name" in marketplace:
                if not isinstance(marketplace["name"], str):
                    self.errors.append("marketplace.json: 'name' must be a string")
                elif not marketplace["name"]:
                    self.errors.append("marketplace.json: 'name' cannot be empty")

            # Validate owner
            if "owner" in marketplace:
                if not isinstance(marketplace["owner"], dict):
                    self.errors.append("marketplace.json: 'owner' must be an object")
                else:
                    if "name" not in marketplace["owner"]:
                        self.errors.append("marketplace.json: owner.name is required")
                    if "url" not in marketplace["owner"]:
                        self.warnings.append("marketplace.json: owner.url is recommended")

            # Validate plugins array
            if "plugins" in marketplace:
                if not isinstance(marketplace["plugins"], list):
                    self.errors.append("marketplace.json: 'plugins' must be an array")
                else:
                    print(f"   ✓ {len(marketplace['plugins'])} plugins listed")

                    # Validate each plugin entry
                    for i, plugin in enumerate(marketplace["plugins"]):
                        self._validate_plugin_entry(plugin, i)

            print("   ✅ marketplace.json validated\n")

        except json.JSONDecodeError as e:
            self.errors.append(f"marketplace.json: Invalid JSON - {e}")

    def _validate_plugin_entry(self, plugin: dict, index: int):
        """Validate a plugin entry in marketplace.json"""
        required_fields = ["name", "source"]

        for field in required_fields:
            if field not in plugin:
                self.errors.append(f"marketplace.json plugins[{index}]: Missing '{field}'")

        # Validate source path
        if "source" in plugin:
            source = plugin["source"]
            if source.startswith("./"):
                # Relative path - verify it exists
                plugin_path = self.repo_root / ".claude" / "plugins" / source.lstrip("./")
                if not plugin_path.exists():
                    self.errors.append(f"Plugin '{plugin.get('name', 'unknown')}': Source path not found - {source}")

    def _validate_individual_plugins(self):
        """Validate all individual plugins"""
        print("📦 Validating individual plugins...")

        individual_dir = self.plugins_dir / "individual"
        if not individual_dir.exists():
            self.warnings.append("No individual plugins directory found")
            return

        plugin_dirs = [d for d in individual_dir.iterdir() if d.is_dir()]
        print(f"   Found {len(plugin_dirs)} individual plugins\n")

        for plugin_dir in sorted(plugin_dirs):
            self._validate_plugin(plugin_dir, "individual")

        print("   ✅ Individual plugins validated\n")

    def _validate_bundle_plugins(self):
        """Validate all bundle plugins"""
        print("📦 Validating bundle plugins...")

        bundles_dir = self.plugins_dir / "bundles"
        if not bundles_dir.exists():
            self.warnings.append("No bundles directory found")
            return

        bundle_dirs = [d for d in bundles_dir.iterdir() if d.is_dir()]
        print(f"   Found {len(bundle_dirs)} bundle plugins\n")

        for bundle_dir in sorted(bundle_dirs):
            self._validate_plugin(bundle_dir, "bundle")

        print("   ✅ Bundle plugins validated\n")

    def _validate_plugin(self, plugin_dir: Path, plugin_type: str):
        """Validate a single plugin"""
        plugin_name = plugin_dir.name
        print(f"   🔍 Validating {plugin_name}...")

        # Check required directories
        required_dirs = [".claude-plugin", "skills"]
        for dir_name in required_dirs:
            dir_path = plugin_dir / dir_name
            if not dir_path.exists():
                self.errors.append(f"{plugin_name}: Missing required directory '{dir_name}'")

        # Validate plugin.json
        manifest_file = plugin_dir / ".claude-plugin" / "plugin.json"
        if not manifest_file.exists():
            self.errors.append(f"{plugin_name}: plugin.json not found")
            return

        try:
            with open(manifest_file, 'r') as f:
                manifest = json.load(f)

            # Check required fields
            required_fields = ["name", "version", "description"]
            for field in required_fields:
                if field not in manifest:
                    self.errors.append(f"{plugin_name}: plugin.json missing '{field}'")

            # Validate name matches directory
            if manifest.get("name") != plugin_name:
                self.errors.append(f"{plugin_name}: plugin.json name '{manifest.get('name')}' doesn't match directory name")

            # Check for skills directory
            skills_dir = plugin_dir / "skills"
            if not skills_dir.exists():
                self.errors.append(f"{plugin_name}: skills/ directory not found")
            else:
                skill_count = len([d for d in skills_dir.iterdir() if d.is_dir()])
                if skill_count == 0:
                    self.errors.append(f"{plugin_name}: No skills found in skills/ directory")
                else:
                    print(f"      ✓ {skill_count} skill(s)")

            # Check for commands
            commands_dir = plugin_dir / "commands"
            if commands_dir.exists():
                command_count = len(list(commands_dir.glob("*.md")))
                print(f"      ✓ {command_count} command(s)")
            else:
                self.warnings.append(f"{plugin_name}: No commands directory found")

            # Check for agents
            agents_dir = plugin_dir / "agents"
            if agents_dir.exists():
                agent_count = len(list(agents_dir.glob("*.md")))
                print(f"      ✓ {agent_count} agent(s)")
            else:
                self.warnings.append(f"{plugin_name}: No agents directory found")

            print(f"      ✅ {plugin_name} valid")

        except json.JSONDecodeError as e:
            self.errors.append(f"{plugin_name}: Invalid JSON in plugin.json - {e}")

    def _print_results(self):
        """Print validation results"""
        print("\n" + "="*60)
        print("VALIDATION RESULTS")
        print("="*60 + "\n")

        if self.errors:
            print(f"❌ ERRORS ({len(self.errors)}):\n")
            for error in self.errors:
                print(f"   • {error}")
            print()

        if self.warnings:
            print(f"⚠️  WARNINGS ({len(self.warnings)}):\n")
            for warning in self.warnings:
                print(f"   • {warning}")
            print()

        if not self.errors and not self.warnings:
            print("✅ ALL VALIDATIONS PASSED!\n")
        elif not self.errors:
            print("✅ NO ERRORS (warnings present)\n")
        else:
            print("❌ VALIDATION FAILED\n")


def main():
    """Main entry point"""
    # Find repository root
    repo_root = Path(__file__).parent.parent.parent

    validator = MarketplaceValidator(repo_root)
    success = validator.validate()

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

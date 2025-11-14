#!/usr/bin/env python3
"""
Bundle Plugin Generator for Claude Code

Creates category bundle plugins that combine multiple related skills.

Usage:
    ./generate_bundle.py <bundle-name>
    ./generate_bundle.py core-3d-animation

    # Generate all bundles
    ./generate_bundle.py --all
"""

import os
import sys
import json
import shutil
from pathlib import Path
from typing import Dict, List

# Bundle definitions
BUNDLES = {
    "core-3d-animation": {
        "title": "Core 3D & Animation",
        "description": "Complete core 3D and animation stack with Three.js, GSAP, React Three Fiber, Framer Motion, and Babylon.js",
        "skills": ["threejs-webgl", "gsap-scrolltrigger", "react-three-fiber", "motion-framer", "babylonjs-engine"],
        "category": "bundle",
        "tags": ["bundle", "3d", "animation", "core", "complete-stack"]
    },
    "extended-3d-scroll": {
        "title": "Extended 3D & Scroll",
        "description": "Extended 3D graphics and smooth scroll stack with A-Frame, lightweight effects, PlayCanvas, PixiJS, Locomotive Scroll, and Barba.js",
        "skills": ["aframe-webxr", "lightweight-3d-effects", "playcanvas-engine", "pixijs-2d", "locomotive-scroll", "barba-js"],
        "category": "bundle",
        "tags": ["bundle", "3d", "scroll", "effects", "transitions"]
    },
    "animation-components": {
        "title": "Animation & Components",
        "description": "Comprehensive animation and component libraries with React Spring, Magic UI, React Bits, AOS, Anime.js, and Lottie",
        "skills": ["react-spring-physics", "animated-component-libraries", "scroll-reveal-libraries", "animejs", "lottie-animations"],
        "category": "bundle",
        "tags": ["bundle", "animation", "components", "ui", "motion"]
    },
    "authoring-motion": {
        "title": "3D Authoring & Motion",
        "description": "Professional 3D authoring and motion graphics pipeline with Blender, Spline, Rive, and Substance 3D",
        "skills": ["blender-web-pipeline", "spline-interactive", "rive-interactive", "substance-3d-texturing"],
        "category": "bundle",
        "tags": ["bundle", "authoring", "pipeline", "motion-graphics", "3d"]
    },
    "meta-skills": {
        "title": "Meta Skills",
        "description": "Integration patterns and modern web design guidelines for building cohesive 3D/animation experiences",
        "skills": ["web3d-integration-patterns", "modern-web-design"],
        "category": "bundle",
        "tags": ["bundle", "meta", "integration", "design", "patterns"]
    }
}


class BundleGenerator:
    def __init__(self, bundle_name: str, repo_root: Path):
        self.bundle_name = bundle_name
        self.repo_root = repo_root
        self.bundle_config = BUNDLES[bundle_name]
        self.bundle_dir = repo_root / ".claude" / "plugins" / "bundles" / bundle_name

    def generate(self):
        """Generate bundle plugin"""
        print(f"\n📦 Generating bundle: {self.bundle_name}")
        print(f"   Skills: {', '.join(self.bundle_config['skills'])}")
        print(f"   Target: {self.bundle_dir}")

        # Create bundle directory structure
        self._create_bundle_structure()

        # Generate bundle manifest
        self._generate_manifest()

        # Copy all skill content
        self._copy_skills()

        # Aggregate commands
        self._aggregate_commands()

        # Create bundle agents
        self._create_bundle_agents()

        print(f"✅ Bundle generated: {self.bundle_name}\n")

    def _create_bundle_structure(self):
        """Create bundle directory structure"""
        directories = [
            self.bundle_dir,
            self.bundle_dir / ".claude-plugin",
            self.bundle_dir / "skills",
            self.bundle_dir / "commands",
            self.bundle_dir / "agents",
        ]

        for dir_path in directories:
            dir_path.mkdir(parents=True, exist_ok=True)

    def _generate_manifest(self):
        """Generate bundle plugin.json"""
        manifest = {
            "name": self.bundle_name,
            "version": "1.0.0",
            "description": self.bundle_config["description"],
            "author": "Claude Design Skillstack",
            "license": "Apache-2.0",
            "homepage": "https://github.com/freshtechbro/claudedesignskills",
            "repository": {
                "type": "git",
                "url": "https://github.com/freshtechbro/claudedesignskills.git"
            },
            "keywords": self.bundle_config["tags"],
            "category": self.bundle_config["category"],
            "bundle": True,
            "includes": self.bundle_config["skills"],
            "skills": "skills/",
            "commands": "commands/",
            "agents": "agents/"
        }

        manifest_path = self.bundle_dir / ".claude-plugin" / "plugin.json"
        with open(manifest_path, 'w') as f:
            json.dump(manifest, f, indent=2)

        print(f"   📄 Created: plugin.json")

    def _copy_skills(self):
        """Copy all skills in bundle"""
        skills_dir = self.bundle_dir / "skills"

        for skill_name in self.bundle_config["skills"]:
            src = self.repo_root / ".claude" / "skills" / skill_name
            dst = skills_dir / skill_name

            if not src.exists():
                print(f"   ⚠️  Warning: Skill not found: {skill_name}")
                continue

            if dst.exists():
                shutil.rmtree(dst)

            shutil.copytree(src, dst, ignore=shutil.ignore_patterns('*.zip', '.DS_Store'))

            print(f"   📦 Copied: {skill_name}")

    def _aggregate_commands(self):
        """Aggregate commands from individual plugins"""
        commands_dir = self.bundle_dir / "commands"

        for skill_name in self.bundle_config["skills"]:
            # Check if individual plugin exists
            individual_plugin = self.repo_root / ".claude" / "plugins" / "individual" / skill_name
            individual_commands = individual_plugin / "commands"

            if not individual_commands.exists():
                continue

            # Copy commands from individual plugin
            for command_file in individual_commands.glob("*.md"):
                dst = commands_dir / f"{skill_name}-{command_file.name}"
                shutil.copy2(command_file, dst)

                print(f"   🔨 Aggregated: {skill_name}-{command_file.stem} command")

    def _create_bundle_agents(self):
        """Create bundle-specific integration agents"""
        agents_dir = self.bundle_dir / "agents"

        # Create integration agent
        self._create_integration_agent(agents_dir)

        # Copy individual agents
        for skill_name in self.bundle_config["skills"]:
            individual_plugin = self.repo_root / ".claude" / "plugins" / "individual" / skill_name
            individual_agents = individual_plugin / "agents"

            if not individual_agents.exists():
                continue

            for agent_file in individual_agents.glob("*.md"):
                dst = agents_dir / agent_file.name
                shutil.copy2(agent_file, dst)

                print(f"   🤖 Aggregated: {agent_file.stem} agent")

    def _create_integration_agent(self, agents_dir: Path):
        """Create bundle integration specialist agent"""
        agent_name = f"{self.bundle_name}-integration"

        content = f"""# {self.bundle_config['title']} Integration Specialist

## Role

Expert integration specialist for combining {self.bundle_config['title']} technologies into cohesive applications.

## Expertise

- Cross-library integration patterns
- Technology stack orchestration
- Performance optimization across libraries
- Unified architecture design
- Best practices for combined workflows

## Bundle Contents

This bundle includes:
{chr(10).join(f'- {skill}' for skill in self.bundle_config['skills'])}

## When to use

Activate this agent when working on:
- Projects using multiple libraries from this bundle
- Cross-library integration challenges
- Architecture decisions spanning multiple technologies
- Performance optimization across the stack
- Unified workflow design

## Approach

1. Understand project requirements across all technologies
2. Design cohesive architecture leveraging each library's strengths
3. Implement integration patterns proven for this stack
4. Optimize for overall system performance
5. Provide guidance on library coordination

## Tools

This agent has access to:
- All skills in the {self.bundle_config['title']} bundle
- Cross-library integration patterns
- Performance optimization techniques
- Architecture best practices
"""

        agent_file = agents_dir / f"{agent_name}.md"
        with open(agent_file, 'w') as f:
            f.write(content)

        print(f"   🤖 Created: {agent_name} agent")


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: ./generate_bundle.py <bundle-name>")
        print("   or: ./generate_bundle.py --all")
        print("\nAvailable bundles:")
        for bundle in BUNDLES.keys():
            print(f"  - {bundle}")
        sys.exit(1)

    # Find repository root
    repo_root = Path(__file__).parent.parent.parent

    if sys.argv[1] == "--all":
        # Generate all bundles
        print(f"\n🚀 Generating {len(BUNDLES)} bundles...\n")

        for bundle_name in BUNDLES.keys():
            try:
                generator = BundleGenerator(bundle_name, repo_root)
                generator.generate()
            except Exception as e:
                print(f"❌ Error generating {bundle_name}: {e}\n")
                continue

        print(f"\n✅ Generated {len(BUNDLES)} bundles successfully!\n")
    else:
        bundle_name = sys.argv[1]

        if bundle_name not in BUNDLES:
            print(f"❌ Unknown bundle: {bundle_name}")
            print("\nAvailable bundles:")
            for bundle in BUNDLES.keys():
                print(f"  - {bundle}")
            sys.exit(1)

        generator = BundleGenerator(bundle_name, repo_root)
        generator.generate()


if __name__ == "__main__":
    main()

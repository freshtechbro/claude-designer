# Claude Skills - Design Agency Toolstack

Claude Code skills for modern web development: 3D graphics, WebGL/WebGPU, animation, and interactive experiences.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Skills: 22](https://img.shields.io/badge/Skills-22-green.svg)](#available-skills)
[![Status: Production](https://img.shields.io/badge/Status-Production-brightgreen.svg)](#status)

## Overview

**22 complete, packaged skills** extending Claude Code with specialized knowledge for cutting-edge web technologies.

**Key Features**:
- ✅ 22 skills covering 3D, animation, and interactive web
- 🔧 50+ generator scripts for boilerplate and components
- 📚 Comprehensive patterns, examples, and integration guides
- 🚀 Auto-activates when Claude detects relevant tasks

## What are Claude Skills?

Modular packages that teach Claude specific technologies. Each contains:
- **SKILL.md** - Instructions and patterns
- **references/** - API docs and guides
- **scripts/** - Automation utilities
- **assets/** - Templates and examples

Progressive disclosure: Claude loads only what's needed per task.

## Available Skills

### Core 3D & Animation (5)
**threejs-webgl** • **gsap-scrolltrigger** • **react-three-fiber** • **motion-framer** • **babylonjs-engine**

### Extended 3D & Scroll (6)
**aframe-webxr** • **lightweight-3d-effects** • **playcanvas-engine** • **pixijs-2d** • **locomotive-scroll** • **barba-js**

### Animation & Components (5)
**react-spring-physics** • **animated-component-libraries** • **scroll-reveal-libraries** • **animejs** • **lottie-animations**

### 3D Authoring & Motion (4)
**blender-web-pipeline** • **spline-interactive** • **rive-interactive** • **substance-3d-texturing**

### Meta-Skills (2)
**web3d-integration-patterns** • **modern-web-design**

## Installation

**Prerequisites**: Claude Code CLI or [claude.com/code](https://claude.com/code), Python 3.7+

### Option 1: Use All Skills

```bash
git clone <repository-url>
cd claudeskills
```

Skills auto-activate when triggered. Example prompts:
- "Create a Three.js scene with PBR materials" → `threejs-webgl`
- "Add GSAP scroll animations" → `gsap-scrolltrigger`
- "Build React Three Fiber component with physics" → `react-three-fiber`

### Option 2: Individual Skills

Each skill packaged at `.claude/skills/<skill-name>/<skill-name>.zip`

```bash
cp claudeskills/.claude/skills/threejs-webgl/threejs-webgl.zip your-project/.claude/skills/
```

## Creating Skills

```bash
# Initialize new skill
.claude/skills/skill-creator/scripts/init_skill.py my-skill --path .claude/skills

# Validate
.claude/skills/skill-creator/scripts/quick_validate.py .claude/skills/my-skill

# Package (auto-validates)
.claude/skills/skill-creator/scripts/package_skill.py .claude/skills/my-skill
```

## Generator Scripts

Each skill includes automation utilities. Examples:

- **threejs-webgl**: `setup_scene.py` - Three.js boilerplate
- **react-three-fiber**: `component_generator.py` - 12 R3F component types
- **motion-framer**: `animation_generator.py` - 11 animation types
- **babylonjs-engine**: `scene_generator.py` - 8 scene types, `mesh_builder.py` - 13 shapes
- **gsap-scrolltrigger**: `generate_animation.py`, `timeline_builder.py`

50+ generators total across all skills.

## Repository Verification

```bash
# Count skills (should be 23)
ls -d .claude/skills/*/ | wc -l

# Count packages (should be 22)
find .claude/skills -name "*.zip" -type f | wc -l

# Validate all
for skill in .claude/skills/*/; do
  .claude/skills/skill-creator/scripts/quick_validate.py "$skill"
done
```

## Skill Relationships

**Foundation**: `threejs-webgl` (used by R3F, A-Frame, Vanta) • `gsap-scrolltrigger` (integrates with most) • `motion-framer` (used by component libs)

**Alternatives**: 3D (`threejs-webgl` vs `babylonjs-engine` vs `playcanvas-engine`) • Animation (`gsap` vs `motion` vs `react-spring`) • Scroll (`locomotive` vs `AOS`)

**Common Integrations**: Three.js + GSAP • R3F + Motion • Vanta + GSAP

## Contributing

1. Fork repo
2. Create/improve skill using `init_skill.py`
3. Follow [Claude Skills standards](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
4. Validate with `quick_validate.py`
5. Submit PR with packaged skill

**Guidelines**: Imperative form in SKILL.md • Runnable examples • Executable scripts (`chmod +x`) • Python 3 stdlib only • Proper YAML frontmatter

## Documentation

- **CLAUDE.md** - Repository guidance for Claude Code
- **Official Docs** - [Claude Skills guidelines](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
- **Individual Skills** - Each SKILL.md contains detailed instructions

## License

MIT License - see [LICENSE](LICENSE) file

## Status

✅ **Production Ready** - All 22 skills complete, validated, and packaged
📦 **22 Skills** - 3D graphics, animation, scroll effects, interactive web
🔧 **50+ Generators** - Automated boilerplate and components
📚 **Fully Documented** - Guides, patterns, examples

Built following [Anthropic's Claude Skills guidelines](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview).

**Star this repository** to stay updated!

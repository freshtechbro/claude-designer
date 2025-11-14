# Claude Design Skillstack

**Professional design agency skillstack for 3D/WebGL, animation, and modern web development**

Claude Code plugin marketplace providing comprehensive coverage of modern web technologies including Three.js, GSAP, React Three Fiber, Framer Motion, Babylon.js, and more.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Plugins: 27](https://img.shields.io/badge/Plugins-27-blue.svg)](#available-plugins)
[![Skills: 22](https://img.shields.io/badge/Skills-22-green.svg)](#available-skills)
[![Status: Production](https://img.shields.io/badge/Status-Production-brightgreen.svg)](#status)

## 🚀 Quick Start (Plugin Marketplace)

**New**: Install skills as plugins directly from this marketplace!

```bash
# Add marketplace to Claude Code
/plugin marketplace add freshtechbro/claudedesignskills

# Install individual plugins
/plugin install threejs-webgl
/plugin install gsap-scrolltrigger
/plugin install react-three-fiber

# Or install complete bundles
/plugin install core-3d-animation        # 5 skills: Three.js, GSAP, R3F, Motion, Babylon
/plugin install extended-3d-scroll       # 6 skills: A-Frame, Vanta, PlayCanvas, PixiJS, Locomotive, Barba
/plugin install animation-components     # 5 skills: React Spring, Magic UI, AOS, Anime.js, Lottie
/plugin install authoring-motion         # 4 skills: Blender, Spline, Rive, Substance 3D
/plugin install meta-skills             # 2 skills: Integration patterns, Modern design
```

**Each plugin includes**:
- ✅ Complete skill content with SKILL.md
- ✅ 1-3 slash commands for quick actions
- ✅ 1-2 specialized agents for domain expertise
- ✅ Scripts, references, and asset templates

📚 **[View complete marketplace documentation →](MARKETPLACE.md)**

## Overview

**27 plugins (22 individual + 5 bundles)** extending Claude Code with specialized knowledge for cutting-edge web technologies.

**Key Features**:
- 🏪 Plugin marketplace with 27 ready-to-install plugins
- ✅ 22 individual skills + 5 category bundles
- 🔧 50+ slash commands for instant boilerplate generation
- 🤖 27+ specialized agents for domain expertise
- 📚 Comprehensive patterns, examples, and integration guides
- 🚀 Auto-activates when Claude detects relevant tasks

## What are Claude Skills?

Modular packages that teach Claude specific technologies. Each contains:
- **SKILL.md** - Instructions and patterns
- **references/** - API docs and guides
- **scripts/** - Automation utilities
- **assets/** - Templates and examples

Progressive disclosure: Claude loads only what's needed per task.

## Available Plugins

### Individual Plugins (22)

All plugins include slash commands and specialized agents. [Full details →](MARKETPLACE.md)

### Category Bundles (5)

- **core-3d-animation** - Three.js, GSAP, R3F, Motion, Babylon.js (5 skills, 9 commands, 6 agents)
- **extended-3d-scroll** - A-Frame, Vanta, PlayCanvas, PixiJS, Locomotive, Barba (6 skills, 12 commands, 7 agents)
- **animation-components** - React Spring, Magic UI, AOS, Anime.js, Lottie (5 skills, 10 commands, 6 agents)
- **authoring-motion** - Blender, Spline, Rive, Substance 3D (4 skills, 10 commands, 5 agents)
- **meta-skills** - Integration patterns, Modern design (2 skills, 4 commands, 3 agents)

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

**Prerequisites**: Claude Code CLI or [claude.com/code](https://claude.com/code)

### Option 1: Plugin Marketplace (Recommended - New!)

Install directly from the marketplace:

```bash
# Add marketplace
/plugin marketplace add freshtechbro/claudedesignskills

# Browse and install plugins
/plugin install threejs-webgl
/plugin install core-3d-animation  # Bundle: 5 skills + commands + agents
```

**Benefits**:
- ✅ One-command installation
- ✅ Includes slash commands for quick actions
- ✅ Specialized agents for domain expertise
- ✅ Automatic updates when repo updates
- ✅ Individual plugins or category bundles

### Option 2: Upload to claude.ai

Upload individual skills directly to [claude.ai](https://claude.ai):

1. Go to **Settings > Features > Skills**
2. Click **Upload skill**
3. Select any `.zip` file from `.claude/skills/`
4. Skill activates automatically when Claude detects relevant tasks

**All skills are properly packaged** with:
- ✅ SKILL.md at root level with valid YAML frontmatter
- ✅ No nested zip files
- ✅ Correct directory structure for claude.ai

### Option 3: Clone Repository (Development)

Clone for skill development or local customization:

```bash
git clone https://github.com/freshtechbro/claudedesignskills.git
cd claudedesignskills
```

Skills auto-activate when triggered. Example prompts:
- "Create a Three.js scene with PBR materials" → `threejs-webgl`
- "Add GSAP scroll animations" → `gsap-scrolltrigger`
- "Build React Three Fiber component with physics" → `react-three-fiber`

### Option 4: Individual Skills (Local Projects)

Copy individual skills to your project:

```bash
# Extract skill contents (not the zip itself)
unzip .claude/skills/threejs-webgl.zip -d your-project/.claude/skills/threejs-webgl/
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

### Packaging Requirements

All skills in this repository meet claude.ai upload requirements:

**Required ZIP Structure**:
```
skill-name.zip
├── SKILL.md              ← Must be at root level!
├── references/
│   └── api_reference.md
├── scripts/
│   └── helper_script.py
└── assets/
    └── templates/
```

**Automatic Validation**:
- `package_skill.py` ensures correct structure
- Skips `.zip` files to prevent nesting
- Places SKILL.md at root level (not in subdirectory)
- Validates YAML frontmatter before packaging

**Common Errors** (all fixed in this repo):
- ❌ SKILL.md inside subdirectory (e.g., `skill-name/SKILL.md`)
- ❌ Nested .zip files inside archive
- ❌ Missing or invalid YAML frontmatter

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
🏪 **Plugin Marketplace** - 27 plugins (22 individual + 5 bundles) ready to install
📦 **22 Skills** - 3D graphics, animation, scroll effects, interactive web
🔧 **50+ Commands** - Slash commands for instant boilerplate
🤖 **27+ Agents** - Specialized domain experts
📚 **Fully Documented** - Guides, patterns, examples
🚀 **Upload Ready** - All skills meet claude.ai packaging requirements

### Recent Updates

**2025-11-13**: Launched Plugin Marketplace
- ✅ Created 27 plugins (22 individual + 5 category bundles)
- ✅ Added 50+ slash commands for quick actions
- ✅ Created 27+ specialized agents for domain expertise
- ✅ Published marketplace.json for easy installation
- ✅ Full marketplace documentation in MARKETPLACE.md

**2025-10-25**: Fixed packaging script for claude.ai compatibility
- ✅ Corrected ZIP structure (SKILL.md at root level)
- ✅ Removed nested .zip files
- ✅ All 22 skills re-packaged with correct structure
- ✅ Verified upload compatibility with claude.ai

Built following [Anthropic's Claude Skills guidelines](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview).

**Ready to use**: Upload any skill to [claude.ai](https://claude.ai) or clone the repository!

---

**Star this repository** to stay updated with new skills and features!

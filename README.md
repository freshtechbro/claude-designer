# Claude Skills - Design Agency Toolstack

A comprehensive collection of Claude Code skills for modern web development, specializing in 3D graphics, animation, and interactive web experiences.

## Overview

This repository contains 22 production-ready skills that extend Claude's capabilities with specialized knowledge for building cutting-edge web applications. Each skill acts as an "onboarding guide" providing Claude with deep expertise in specific technologies and workflows.

## What are Claude Skills?

Claude Skills are modular, self-contained packages that teach Claude how to work with specific technologies, frameworks, and workflows. Each skill includes:

- **SKILL.md**: Core instructions and patterns
- **References**: Detailed API documentation and guides
- **Scripts**: Automation utilities and generators
- **Assets**: Starter templates and examples

Skills use a progressive disclosure system - Claude loads only what's needed for each task, making interactions efficient and contextually relevant.

## Available Skills (22 Total)

### Phase 1: Core 3D & Animation (5 Skills) ✅

| Skill | Description | Status |
|-------|-------------|--------|
| **threejs-webgl** | Three.js WebGL/WebGPU 3D graphics development | ✅ Packaged |
| **gsap-scrolltrigger** | GSAP animation library with ScrollTrigger for scroll-driven experiences | ✅ Packaged |
| **react-three-fiber** | React renderer for Three.js with declarative 3D scenes | ✅ Packaged |
| **motion-framer** | Framer Motion animation library for React | ✅ Packaged |
| **babylonjs-engine** | Babylon.js game engine with built-in physics and PBR | ✅ Packaged |

### Phase 2: Extended 3D & Scroll (6 Skills) ✅

| Skill | Description | Status |
|-------|-------------|--------|
| **aframe-webxr** | Declarative VR/WebXR framework built on Three.js | ✅ Packaged |
| **lightweight-3d-effects** | Zdog, Vanta.js, and Vanilla-Tilt for decorative 3D effects | ✅ Packaged |
| **playcanvas-engine** | Lightweight WebGL game engine with visual editor | ✅ Packaged |
| **pixijs-2d** | High-performance 2D rendering engine using WebGL | ✅ Packaged |
| **locomotive-scroll** | Smooth scrolling library with parallax effects | ✅ Packaged |
| **barba-js** | Page transition library for fluid navigation | ✅ Packaged |

### Phase 3: Animation & Web Components (5 Skills) ✅

| Skill | Description | Status |
|-------|-------------|--------|
| **react-spring-physics** | Physics-based animation with React Spring and Popmotion | ✅ Packaged |
| **animated-component-libraries** | Magic UI and React Bits pre-built animated components | ✅ Packaged |
| **scroll-reveal-libraries** | AOS (Animate On Scroll) for simple scroll animations | ✅ Packaged |
| **animejs** | Lightweight animation library with stagger and timeline support | ✅ Packaged |
| **lottie-animations** | Lottie animations from After Effects | ✅ Packaged |

### Phase 4: 3D Authoring & Motion (4 Skills) ✅

| Skill | Description | Status |
|-------|-------------|--------|
| **blender-web-pipeline** | Blender to web workflow with glTF export optimization | ✅ Packaged |
| **spline-interactive** | Spline 3D design tool integration for React | ✅ Packaged |
| **rive-interactive** | Rive interactive animations with state machines | ✅ Packaged |
| **substance-3d-texturing** | Substance 3D Painter texturing workflow for web | ✅ Packaged |

### Phase 6: Meta-Skills (2 Skills) ✅

| Skill | Description | Status |
|-------|-------------|--------|
| **web3d-integration-patterns** | Integration patterns for combining multiple 3D/animation libraries | ✅ Packaged |
| **modern-web-design** | Modern web design principles and implementation patterns | ✅ Packaged |

### Pending Skills (6 Remaining)

- **model-viewer-component** - Web component for 3D model viewing with AR
- **figma-dev-mode** - Design-to-code workflow and Figma API integration
- **webflow-interactions** - Visual web development with GSAP animations
- **framer-sites** - React-based site building with Framer Motion
- **cesium-geospatial** - 3D globe and geospatial visualization
- **react-flow-graphs** - Node-based UI for workflow editors

## Repository Structure

```
claudeskills/
├── LICENSE                    # MIT License
├── README.md                  # This file
├── PROJECT_PLAN.md           # Detailed roadmap and progress tracking
├── CLAUDE.md                 # Repository guidance for Claude
└── .claude/
    └── skills/
        ├── skill-creator/         # Meta-skill for creating other skills
        │   ├── SKILL.md
        │   └── scripts/
        │       ├── init_skill.py      # Initialize new skill
        │       ├── package_skill.py   # Package skill for distribution
        │       └── quick_validate.py  # Validate skill structure
        │
        ├── threejs-webgl/
        │   ├── threejs-webgl.zip      # Packaged skill
        │   ├── SKILL.md              # Main instructions
        │   ├── references/           # API docs and guides
        │   ├── scripts/              # Automation utilities
        │   └── assets/               # Templates and examples
        │
        └── [... 21 more skills ...]
```

## Installation & Usage

### Prerequisites

- **Claude Code CLI** or access to [claude.com/code](https://claude.com/code)
- **Python 3.7+** (for skill creation and packaging scripts)

### Using Skills with Claude

1. **Clone this repository**:
   ```bash
   git clone <repository-url>
   cd claudeskills
   ```

2. **Skills are automatically available** to Claude when in this directory. Claude will load skills based on your requests.

3. **Trigger skills by mentioning technologies**:
   - "Help me create a Three.js scene" → Activates `threejs-webgl`
   - "Add GSAP scroll animations" → Activates `gsap-scrolltrigger`
   - "Build a React Three Fiber component" → Activates `react-three-fiber`

### Installing Individual Skills

Each skill is packaged as a `.zip` file in its directory:

```bash
# Skills are located at:
.claude/skills/<skill-name>/<skill-name>.zip

# For example:
.claude/skills/threejs-webgl/threejs-webgl.zip
.claude/skills/gsap-scrolltrigger/gsap-scrolltrigger.zip
```

To use a skill in another project:
1. Copy the `.zip` file to your project's `.claude/skills/` directory
2. Extract or use as-is (Claude can read from zip files)

## Creating New Skills

Use the `skill-creator` meta-skill to create new skills:

### Initialize a New Skill

```bash
.claude/skills/skill-creator/scripts/init_skill.py <skill-name> --path .claude/skills
```

Requirements:
- Skill name must be in hyphen-case (e.g., `my-new-skill`)
- Lowercase letters, digits, and hyphens only
- Maximum 40 characters

This creates the complete skill structure with:
- Proper YAML frontmatter in SKILL.md
- `scripts/`, `references/`, and `assets/` directories
- Example files to guide development

### Validate a Skill

```bash
.claude/skills/skill-creator/scripts/quick_validate.py .claude/skills/<skill-name>
```

Validates:
- YAML frontmatter format
- Required fields (name, description)
- Naming conventions
- File structure

### Package a Skill

```bash
.claude/skills/skill-creator/scripts/package_skill.py .claude/skills/<skill-name>
```

Automatically validates before packaging and creates a distributable `.zip` file.

## Skill Quality Standards

Each skill must include:

### SKILL.md Requirements
- ✅ YAML frontmatter with `name` and `description`
- ✅ Core concepts with code examples
- ✅ 3-7 common patterns (real-world use cases)
- ✅ Integration patterns with other skills
- ✅ Performance best practices
- ✅ Common pitfalls and solutions

### References Requirements
- ✅ Detailed API documentation
- ✅ Advanced patterns and techniques
- ✅ Troubleshooting guides

### Scripts Requirements
- ✅ Python/Bash automation utilities
- ✅ Boilerplate generators
- ✅ All scripts executable and documented
- ✅ Python 3 standard library only (no external dependencies)

### Assets Requirements
- ✅ Complete starter projects/templates
- ✅ Example implementations
- ✅ Configuration files

## Skill Relationships

Understanding how skills work together:

**Foundation Skills** (used by others):
- `threejs-webgl` → Used by `react-three-fiber`, `aframe-webxr`, `lightweight-3d-effects`
- `gsap-scrolltrigger` → Integrates with most animation and 3D skills
- `motion-framer` → Used by `animated-component-libraries`

**Alternative Skills** (similar use cases):
- 3D Engines: `threejs-webgl` vs `babylonjs-engine` vs `playcanvas-engine`
- Animation: `gsap-scrolltrigger` vs `motion-framer` vs `react-spring-physics`
- Scroll Libraries: `locomotive-scroll` vs `scroll-reveal-libraries`

**Integration Patterns**:
- Three.js + GSAP: Scroll-driven 3D animations
- React Three Fiber + Framer Motion: Interactive 3D UI components
- Vanta.js (uses Three.js) + GSAP: Animated backgrounds with scroll triggers

## Common Commands

### Validation
```bash
# Validate single skill
.claude/skills/skill-creator/scripts/quick_validate.py .claude/skills/my-skill

# Validate all skills
for skill in .claude/skills/*/; do
  echo "Validating $skill"
  .claude/skills/skill-creator/scripts/quick_validate.py "$skill"
done
```

### Packaging
```bash
# Package single skill
.claude/skills/skill-creator/scripts/package_skill.py .claude/skills/my-skill

# Package with custom output directory
.claude/skills/skill-creator/scripts/package_skill.py .claude/skills/my-skill ./dist
```

### Skill-Specific Generators

Each skill includes custom generator scripts. Examples:

**threejs-webgl**:
```bash
.claude/skills/threejs-webgl/scripts/setup_scene.py
```

**gsap-scrolltrigger**:
```bash
.claude/skills/gsap-scrolltrigger/scripts/generate_animation.py
.claude/skills/gsap-scrolltrigger/scripts/timeline_builder.py
```

**react-three-fiber**:
```bash
.claude/skills/react-three-fiber/scripts/component_generator.py
.claude/skills/react-three-fiber/scripts/scene_setup.py
```

See individual skill README files for complete documentation.

## Documentation

- **[PROJECT_PLAN.md](PROJECT_PLAN.md)**: Detailed roadmap with skill descriptions and progress tracking
- **[CLAUDE.md](CLAUDE.md)**: Repository guidance and conventions for Claude
- **Official Claude Docs**: [claude.com/docs/agents-and-tools/agent-skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)

## Progress

**Overall Progress**: 22/28 skills complete (78.6%)

- ✅ **Phase 1**: 5/5 skills (100%) - Core 3D & Animation
- ✅ **Phase 2**: 6/6 skills (100%) - Extended 3D & Scroll
- ✅ **Phase 3**: 5/5 skills (100%) - Animation & Web Components
- ✅ **Phase 4**: 4/4 skills (100%) - 3D Authoring & Motion
- ⏳ **Phase 5**: 0/3 skills (0%) - Design Platforms
- ✅ **Phase 6**: 2/2 skills (100%) - Meta-Skills
- ⏳ **Phase 7**: 0/2 skills (0%) - Specialized Use Cases

See [PROJECT_PLAN.md](PROJECT_PLAN.md) for detailed breakdown.

## Contributing

Contributions are welcome! To contribute a new skill:

1. **Fork this repository**
2. **Create a new skill** using `init_skill.py`
3. **Follow quality standards** (see CLAUDE.md)
4. **Validate your skill** with `quick_validate.py`
5. **Test with Claude** to ensure it activates correctly
6. **Submit a pull request** with your packaged skill

### Contribution Guidelines

- Follow the official Claude Skills standards
- Use imperative/infinitive form in SKILL.md (not second person)
- Include comprehensive examples and patterns
- Add integration patterns with existing skills
- Document common pitfalls and solutions
- Ensure all scripts are executable and well-documented
- Use only Python 3 standard library (no external dependencies)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built following [Anthropic's official Claude Skills guidelines](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
- Skills documentation sourced from official library documentation and community best practices
- Inspired by the need for comprehensive web development expertise in AI-assisted coding

## Support

For issues, questions, or suggestions:
1. Check [PROJECT_PLAN.md](PROJECT_PLAN.md) for roadmap and progress
2. Review [CLAUDE.md](CLAUDE.md) for development guidelines
3. Open an issue in this repository
4. Consult [Claude Code documentation](https://docs.claude.com/en/docs/claude-code)

---

**Note**: This is an active development project. Skills are continuously improved based on real-world usage and feedback. Star this repository to stay updated with new skills and improvements!

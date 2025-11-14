# Claude Design Skillstack - Plugin Marketplace

**Professional design agency skillstack for 3D/WebGL, animation, and modern web development**

This repository serves as both a development workspace for skills and a plugin marketplace for Claude Code, providing comprehensive coverage of modern web technologies including Three.js, GSAP, React Three Fiber, Framer Motion, Babylon.js, and more.

---

## 🚀 Quick Start

### Installing the Marketplace

Add this marketplace to your Claude Code:

```bash
/plugin marketplace add freshtechbro/claudedesignskills
```

### Installing Individual Plugins

```bash
# Install a specific skill
/plugin install threejs-webgl
/plugin install gsap-scrolltrigger
/plugin install react-three-fiber
```

### Installing Category Bundles

```bash
# Install complete 3D & animation stack
/plugin install core-3d-animation

# Install extended 3D & scroll effects
/plugin install extended-3d-scroll

# Install animation & component libraries
/plugin install animation-components

# Install 3D authoring pipeline
/plugin install authoring-motion

# Install meta-skills (integration patterns & design)
/plugin install meta-skills
```

---

## 📦 Available Plugins

### Individual Plugins (22)

All individual plugins include:
- ✅ Complete skill content with SKILL.md
- ✅ 1-3 slash commands for quick actions
- ✅ 1-2 specialized agents for domain expertise
- ✅ Scripts, references, and asset templates

#### Core 3D & Animation (5 plugins)

1. **threejs-webgl** - Three.js WebGL/WebGPU 3D Graphics
   - Commands: `/threejs-webgl-setup_scene`
   - Agent: Three.js Architect
   - Use for: 3D scenes, WebGL rendering, interactive visualizations

2. **gsap-scrolltrigger** - GSAP Animation & ScrollTrigger
   - Commands: `/gsap-scrolltrigger-generate_animation`, `/gsap-scrolltrigger-timeline_builder`
   - Agent: GSAP ScrollTrigger Animation Choreographer
   - Use for: Scroll-driven animations, complex timelines, performance-optimized motion

3. **react-three-fiber** - React Three Fiber (R3F)
   - Commands: `/react-three-fiber-component_generator`, `/react-three-fiber-scene_setup`
   - Agent: React Three Fiber Architect
   - Use for: React + Three.js integration, declarative 3D, component-based 3D

4. **motion-framer** - Framer Motion
   - Commands: `/motion-framer-animation_generator`, `/motion-framer-variant_builder`
   - Agent: Framer Motion Animation Choreographer
   - Use for: React animations, gesture-driven UI, layout animations

5. **babylonjs-engine** - Babylon.js Game Engine
   - Commands: `/babylonjs-engine-scene_generator`, `/babylonjs-engine-mesh_builder`
   - Agent: Babylon.js Architect
   - Use for: Game development, physics simulations, advanced 3D rendering

#### Extended 3D & Scroll (6 plugins)

6. **aframe-webxr** - A-Frame WebXR
   - Commands: `/aframe-webxr-scene_generator`, `/aframe-webxr-component_builder`
   - Agent: A-Frame WebXR Architect
   - Use for: VR/AR experiences, WebXR applications, 360° media

7. **lightweight-3d-effects** - Zdog, Vanta.js, Vanilla Tilt
   - Commands: `/lightweight-3d-effects-generate_zdog`, `/lightweight-3d-effects-setup_vanta`
   - Agent: Lightweight 3D Effects Architect
   - Use for: Decorative 3D, animated backgrounds, subtle depth effects

8. **playcanvas-engine** - PlayCanvas Game Engine
   - Commands: `/playcanvas-engine-project_generator`, `/playcanvas-engine-component_builder`
   - Agent: PlayCanvas Architect
   - Use for: Browser-based games, real-time 3D apps, editor-first workflows

9. **pixijs-2d** - PixiJS 2D Rendering
   - Commands: `/pixijs-2d-sprite_generator`, `/pixijs-2d-particle_builder`
   - Agent: PixiJS 2D Architect
   - Use for: 2D games, particle effects, high-performance canvas graphics

10. **locomotive-scroll** - Locomotive Scroll
    - Commands: `/locomotive-scroll-generate_config`, `/locomotive-scroll-integration_helper`
    - Agent: Locomotive Scroll Specialist
    - Use for: Smooth scrolling, parallax effects, scroll detection

11. **barba-js** - Barba.js Page Transitions
    - Commands: `/barba-js-project_setup`, `/barba-js-transition_generator`
    - Agent: Barba.js Specialist
    - Use for: Page transitions, SPA-like experiences, routing animations

#### Animation & Components (5 plugins)

12. **react-spring-physics** - React Spring Physics
    - Commands: `/react-spring-physics-spring_generator`, `/react-spring-physics-physics_calculator`
    - Agent: React Spring Animation Choreographer
    - Use for: Physics-based animations, spring dynamics, natural motion

13. **animated-component-libraries** - Magic UI & React Bits
    - Commands: `/animated-component-libraries-component_importer`, `/animated-component-libraries-props_generator`
    - Agent: Animated Component Libraries Specialist
    - Use for: Pre-built animated components, landing pages, marketing sites

14. **scroll-reveal-libraries** - AOS (Animate On Scroll)
    - Commands: `/scroll-reveal-libraries-aos_generator`, `/scroll-reveal-libraries-config_builder`
    - Agent: Scroll Reveal Libraries Specialist
    - Use for: Scroll-triggered reveals, simple scroll animations

15. **animejs** - Anime.js
    - Commands: `/animejs-animation_generator`, `/animejs-timeline_builder`
    - Agent: Anime.js Animation Choreographer
    - Use for: Timeline animations, SVG morphing, stagger effects

16. **lottie-animations** - Lottie
    - Commands: `/lottie-animations-generate_lottie_component`, `/lottie-animations-optimize_lottie`
    - Agent: Lottie Animation Choreographer
    - Use for: After Effects animations, JSON vector animations, micro-interactions

#### 3D Authoring & Motion (4 plugins)

17. **blender-web-pipeline** - Blender Web Export Pipeline
    - Commands: `/blender-web-pipeline-batch_export`, `/blender-web-pipeline-optimize_model`, `/blender-web-pipeline-generate_lods`
    - Agent: Blender Web Pipeline Specialist
    - Use for: Blender → glTF export, 3D asset optimization, batch processing

18. **spline-interactive** - Spline 3D Design Tool
    - Commands: `/spline-interactive-project_generator`, `/spline-interactive-component_builder`
    - Agent: Spline Pipeline Specialist
    - Use for: No-code 3D design, visual 3D editor, designer-friendly workflows

19. **rive-interactive** - Rive Interactive Animations
    - Commands: `/rive-interactive-component_generator`, `/rive-interactive-viewmodel_builder`
    - Agent: Rive Interactive Animation Choreographer
    - Use for: State machine animations, interactive vector graphics, runtime control

20. **substance-3d-texturing** - Substance 3D Painter
    - Commands: `/substance-3d-texturing-batch_export`, `/substance-3d-texturing-web_optimizer`, `/substance-3d-texturing-generate_export_preset`
    - Agent: Substance 3D Pipeline Specialist
    - Use for: PBR texturing, material creation, texture optimization for web

#### Meta-Skills (2 plugins)

21. **web3d-integration-patterns** - Web3D Integration Patterns
    - Commands: `/web3d-integration-patterns-setup`, `/web3d-integration-patterns-help`
    - Agent: Web3D Integration Patterns Specialist
    - Use for: Multi-library integration, architecture patterns, complex 3D apps

22. **modern-web-design** - Modern Web Design Trends
    - Commands: `/modern-web-design-pattern_generator`, `/modern-web-design-design_audit`
    - Agent: Modern Web Design Specialist
    - Use for: Design trends, UX best practices, accessibility compliance

---

### Bundle Plugins (5)

Bundles combine multiple related skills with integrated commands and cross-skill agents.

1. **core-3d-animation** (5 skills, 9 commands, 6 agents)
   - Includes: threejs-webgl, gsap-scrolltrigger, react-three-fiber, motion-framer, babylonjs-engine
   - Use for: Complete 3D & animation development stack
   - Agent: Core 3D & Animation Integration Specialist

2. **extended-3d-scroll** (6 skills, 12 commands, 7 agents)
   - Includes: aframe-webxr, lightweight-3d-effects, playcanvas-engine, pixijs-2d, locomotive-scroll, barba-js
   - Use for: Extended 3D graphics and smooth scroll experiences
   - Agent: Extended 3D & Scroll Integration Specialist

3. **animation-components** (5 skills, 10 commands, 6 agents)
   - Includes: react-spring-physics, animated-component-libraries, scroll-reveal-libraries, animejs, lottie-animations
   - Use for: Comprehensive animation and UI component development
   - Agent: Animation & Components Integration Specialist

4. **authoring-motion** (4 skills, 10 commands, 5 agents)
   - Includes: blender-web-pipeline, spline-interactive, rive-interactive, substance-3d-texturing
   - Use for: Professional 3D authoring and motion graphics pipeline
   - Agent: 3D Authoring & Motion Integration Specialist

5. **meta-skills** (2 skills, 4 commands, 3 agents)
   - Includes: web3d-integration-patterns, modern-web-design
   - Use for: Integration patterns and modern design guidelines
   - Agent: Meta Skills Integration Specialist

---

## 🎯 Use Cases

### For 3D Developers
- **Three.js Projects**: Install `threejs-webgl` or `core-3d-animation` bundle
- **React + 3D**: Install `react-three-fiber` + `threejs-webgl`
- **Game Development**: Install `babylonjs-engine` or `playcanvas-engine`
- **WebXR/VR**: Install `aframe-webxr`

### For Animation Designers
- **Scroll Animations**: Install `gsap-scrolltrigger` or `locomotive-scroll`
- **React Animations**: Install `motion-framer` or `react-spring-physics`
- **Timeline Animations**: Install `animejs` or `gsap-scrolltrigger`
- **After Effects Integration**: Install `lottie-animations`

### For Full-Stack Agencies
- **Complete Stack**: Install `core-3d-animation` + `animation-components` bundles
- **Landing Pages**: Install `animated-component-libraries` + `gsap-scrolltrigger`
- **Product Configurators**: Install `threejs-webgl` + `react-three-fiber`

### For 3D Artists/Pipeline TDs
- **Blender → Web**: Install `blender-web-pipeline`
- **Texturing Pipeline**: Install `substance-3d-texturing`
- **No-Code 3D**: Install `spline-interactive`
- **Interactive Graphics**: Install `rive-interactive`

---

## 📚 Documentation

### Command Usage

All slash commands follow this pattern:

```bash
# Basic usage
/<plugin-name>-<command-name>

# Examples
/threejs-webgl-setup_scene
/gsap-scrolltrigger-generate_animation
/react-three-fiber-component_generator
```

### Agent Activation

Agents activate automatically based on task context. Examples:

- **"Help me build a Three.js scene"** → Activates threejs-webgl-architect
- **"Create GSAP scroll animation"** → Activates gsap-scrolltrigger-choreographer
- **"Optimize Blender model for web"** → Activates blender-web-pipeline-pipeline

### Skill References

Each plugin includes comprehensive references:
- API documentation
- Pattern libraries
- Integration guides
- Optimization checklists
- Troubleshooting guides

---

## 🛠️ Development

### Repository Structure

```
claudeskills/
├── .claude/
│   ├── skills/              # Skill development workspace
│   └── plugins/             # Generated plugins
│       ├── individual/      # 22 individual plugins
│       └── bundles/         # 5 category bundles
├── .claude-plugin/
│   └── marketplace.json     # Marketplace manifest
└── scripts/
    └── marketplace/         # Plugin generation scripts
        ├── generate_plugin.py
        ├── generate_bundle.py
        ├── generate_marketplace.py
        └── validate_marketplace.py
```

### Updating Plugins

To regenerate plugins after skill updates:

```bash
# Regenerate all individual plugins
./scripts/marketplace/generate_plugin.py --all

# Regenerate all bundles
./scripts/marketplace/generate_bundle.py --all

# Regenerate marketplace manifest
./scripts/marketplace/generate_marketplace.py

# Validate everything
./scripts/marketplace/validate_marketplace.py
```

---

## 📄 License

All plugins are licensed under Apache License 2.0.

---

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create feature branches
3. Submit pull requests
4. Follow existing skill patterns

---

## 🔗 Links

- **Repository**: https://github.com/freshtechbro/claudedesignskills
- **Issues**: https://github.com/freshtechbro/claudedesignskills/issues
- **Claude Code Docs**: https://docs.claude.com/en/docs/claude-code/overview

---

## 📞 Support

For questions or issues:
- Open a GitHub issue
- Review the skill documentation in `.claude/skills/`
- Check the Claude Code documentation

---

**Built with ❤️ for the design and development community**

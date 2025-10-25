# Claude Skills Creation Plan - Design Agency Toolstack

## Project Overview

Creating comprehensive Claude skills for a design agency's web development toolstack. Each skill provides specialized knowledge, workflows, and bundled resources (scripts, references, assets) for building modern web experiences.

@https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview#why-use-skills


## Approach: Option B - Complete One Skill at a Time

For each skill:
1. ✅ Initialize skill structure (`init_skill.py`)
2. ✅ Fetch latest documentation (Context7 MCP)
3. ✅ Create comprehensive SKILL.md
4. ✅ Build references/ (detailed documentation)
5. ✅ Create scripts/ (automation utilities)
6. ✅ Add assets/ (templates, boilerplate)
7. ✅ Validate and package

## Phase 1: Core 3D & Animation (5 skills) - HIGHEST PRIORITY

### 1. threejs-webgl ✅ COMPLETED (100%)
**Status**: Fully complete and packaged

**Deliverables**:
- ✅ SKILL.md: Comprehensive Three.js guide
- ✅ References:
  - `api_reference.md`: Core API quick reference
  - `materials_guide.md`: Material comparison and optimization
  - `optimization_checklist.md`: Performance tips
- ✅ Scripts:
  - `setup_scene.py`: Boilerplate scene generator
- ✅ Assets:
  - `starter_scene/`: Complete HTML/JS project with demos

**Related Skills**: Used as foundation by react-three-fiber, aframe-webxr, lightweight-3d-effects (Vanta.js)

---

### 2. gsap-scrolltrigger ✅ COMPLETED (100%)
**Status**: Fully complete and packaged

**Deliverables**:
- ✅ SKILL.md: Comprehensive GSAP & ScrollTrigger guide
  - Core concepts (tweens, timelines, position parameter)
  - ScrollTrigger fundamentals (start/end, scrubbing, toggle actions)
  - Common patterns (fade-in, pinning, horizontal scroll, parallax, batching, stagger)
  - Integration with Three.js, React, Locomotive Scroll
  - Advanced techniques (image sequences, smooth scroll, media queries)
  - Performance best practices
  - Common pitfalls and solutions
  - Easing reference
- ✅ References:
  - `api_reference.md`: Complete GSAP & ScrollTrigger API (429 lines)
  - `easing_guide.md`: Visual easing reference with use cases (620+ lines)
  - `common_patterns.md`: Copy-paste patterns library (940+ lines)
- ✅ Scripts:
  - `generate_animation.py`: Boilerplate GSAP code generator (570+ lines)
  - `timeline_builder.py`: Interactive timeline sequence builder (520+ lines)
- ✅ Assets:
  - `easings/easing_visualizer.html`: Interactive easing tool (570+ lines)
  - `starter_scroll/`: Complete scroll-driven site template
    - index.html, style.css, main.js, README.md (1,700+ lines total)
  - `examples/`: Real-world ScrollTrigger demos documentation (380+ lines)

**Related Skills**: For Three.js-specific animations also reference threejs-webgl. Compare with react-spring-physics (physics-based alternative), scroll-reveal-libraries (simpler approach)

---

### 3. react-three-fiber ✅ COMPLETED (100%)
**Status**: Fully complete and packaged

**Deliverables**:
- ✅ SKILL.md: Comprehensive R3F guide (1,080 lines)
  - Core concepts (Canvas, hooks: useFrame, useThree, useLoader)
  - 7 common patterns (scene setup, interactivity, animations, GLTF, lighting, instancing, groups)
  - Drei integration (OrbitControls, Environment, Text, useGLTF, Bounds, Html, ScrollControls)
  - Library integration (GSAP, Framer Motion, Zustand, React Spring)
  - Performance optimization (on-demand rendering, instancing, LOD, adaptive performance)
  - 6 common pitfalls with solutions
- ✅ References:
  - `api_reference.md`: Complete R3F & Drei API (929 lines)
- ✅ Scripts:
  - `component_generator.py`: Generate R3F components (655 lines, 12 component types)
  - `scene_setup.py`: R3F scene setup with 6 presets (530+ lines, interactive CLI)
- ✅ Assets:
  - `starter_r3f/`: Complete R3F + Vite starter template
    - package.json, vite.config.js, index.html
    - src/main.jsx, App.jsx, Experience.jsx, components/
    - Interactive Box and animated Sphere components
    - README.md with full documentation
  - `examples/`: Real-world R3F patterns documentation (4,400+ lines)
    - GLTF loading, product viewer, scroll animations, particles, text 3D
    - Post-processing, physics, camera animations, LOD, performance monitoring

**Related Skills**: Built on threejs-webgl. For animations reference gsap-scrolltrigger and motion-framer. See cesium-geospatial for React integration patterns in specialized contexts.

---

### 4. motion-framer ✅ COMPLETED (100%)
**Status**: Fully complete and packaged

**Deliverables**:
- ✅ SKILL.md: Comprehensive Motion & Framer Motion guide (933 lines)
  - Core concepts (motion components, animate prop, variants, transitions)
  - 7 common patterns (hover, tap, drag, exit animations, layout, scroll, spring)
  - Gesture recognition (whileHover, whileTap, whileDrag, whileFocus, whileInView)
  - AnimatePresence for exit animations
  - Hooks (useAnimate, useMotionValue, useSpring, useInView, useScroll)
  - Integration with GSAP, R3F, forms
  - Performance optimization
  - 6 common pitfalls with solutions
- ✅ References:
  - `api_reference.md`: Complete Motion API reference (1,078 lines)
    - All motion component props, animation props, gesture props, layout props
    - Transition options (tween, spring, inertia)
    - Variants and orchestration
    - Complete hooks documentation
    - AnimatePresence modes and options
    - Utilities and TypeScript support
- ✅ Scripts:
  - `animation_generator.py`: Generate Motion component boilerplate (560+ lines, 11 animation types)
  - `variant_builder.py`: Interactive variant configuration tool (520+ lines, 7 presets)
- ✅ Assets:
  - `starter_motion/`: Complete Motion + Vite starter template
    - package.json, vite.config.js, index.html
    - src/main.jsx, App.jsx, App.css, components/
    - HoverCard, DraggableBox, StaggerList examples
    - README.md with full documentation
  - `examples/`: Real-world Motion component patterns (3,800+ lines)
    - Page transitions, route animations, complex gestures
    - Scroll-based animations, advanced layout animations
    - Shared element transitions, modals & dialogs
    - Form animations, loading states, list animations
    - Image galleries, navigation menus

**Related Skills**: Alternative to react-spring-physics (physics animations). Used by animated-component-libraries. Compare with gsap-scrolltrigger for scroll-driven animations.

---

### 5. babylonjs-engine ✅ COMPLETED (100%)
**Status**: Fully complete and packaged

**Deliverables**:
- ✅ SKILL.md: Comprehensive Babylon.js guide (933 lines)
  - Engine and scene initialization (basic, async, configuration)
  - Camera systems (FreeCamera, ArcRotateCamera, UniversalCamera, FollowCamera)
  - Lighting systems (Hemispheric, Directional, Point, Spot)
  - Mesh creation (all MeshBuilder shapes) and transformations
  - Materials (Standard, PBR, Multi-materials)
  - Model loading (GLTF/GLB, Asset Manager)
  - Physics engine (Havok integration, aggregates, shapes)
  - Animations (direct, Animation class, groups, skeletons)
  - 7 common patterns, 3 integration patterns
  - Performance optimization, 6 common pitfalls
- ✅ References:
  - `api_reference.md`: Complete Babylon.js API (1,700+ lines)
    - Engine, Scene, Cameras, Lights, Meshes
    - Materials, Textures, Physics, Animations
    - GUI, Post-processing, Constants
- ✅ Scripts:
  - `scene_generator.py`: Babylon scene boilerplate (560+ lines)
    - 8 scene types (basic, physics, pbr, model-viewer, vr, particles, gui, post-processing)
    - 4 camera types, interactive CLI mode
  - `mesh_builder.py`: Mesh creation tool (520+ lines)
    - 13 mesh shapes with full parameter customization
    - Material presets, batch creation, interactive mode
- ✅ Assets:
  - `starter_babylon/`: Complete Babylon + Vite starter template
    - package.json, vite.config.js, index.html
    - src/main.js with physics, PBR materials, shadows
    - Interactive picking, dynamic mesh spawning
    - FPS counter, Inspector integration
    - src/style.css, README.md with full documentation
  - `examples/`: Real-world Babylon.js patterns (3,800+ lines)
    - Model loading & optimization (progress, LOD, simplification, batch)
    - Advanced materials (PBR all maps, glass, water, node materials)
    - Physics simulations (ragdoll, cloth, vehicle)
    - Particle systems (fire, smoke, GPU particles)
    - Post-processing (bloom+DOF, outline/glow, custom shaders)
    - GUI & HUD, WebXR & VR, performance optimization

**Related Skills**: Alternative to threejs-webgl for complex 3D applications requiring built-in physics and PBR.

---

## Phase 2: Extended 3D & Scroll (6 skills) - MEDIUM PRIORITY

### 6. aframe-webxr ✅ COMPLETED (100%)
**Description**: Declarative VR/WebXR framework built on Three.js. HTML-like entity-component architecture, visual inspector, cross-platform VR support.

**Deliverables**:
- ✅ SKILL.md: Comprehensive A-Frame guide (933 lines)
  - Entity-component-system architecture (ECS)
  - Scene setup, camera systems, lighting, materials, animations
  - 7 common patterns (VR controllers, AR hit testing, 360° gallery, interactions, dynamic scenes, environment, GLTF models)
  - Integration with Three.js, GSAP, React
  - Performance best practices, 6 common pitfalls
- ✅ References:
  - `api_reference.md`: Complete A-Frame API (1,950+ lines)
    - Scene, Entity, Core components (camera, geometry, material, light, animation, sound)
    - All primitives, controls, VR/XR components, systems
    - Component API, JavaScript API, complete examples
  - `webxr_guide.md`: WebXR integration patterns (1,300+ lines)
    - VR mode configuration, AR mode setup, hit testing
    - Controller systems, hand tracking, platform support
    - Performance optimization, testing and debugging
  - `components_library.md`: Community components catalog (1,200+ lines)
    - Environment & effects, physics, locomotion, models, UI
    - Particles, audio/video, input, networking, utilities
- ✅ Scripts:
  - `scene_generator.py`: A-Frame scene boilerplate (690+ lines)
    - 7 scene types (basic, VR, AR, 360°, networked, physics, environment)
    - Interactive and CLI modes
  - `component_builder.py`: Custom component generator (620+ lines)
    - 7 component types (basic, interactive, animation, physics, controller, networked, loader)
    - Full lifecycle methods, interactive mode
- ✅ Assets:
  - `starter_aframe/`: Complete VR scene template
    - index.html with interactive objects and animations
    - style.css with responsive info panel
    - main.js with event handlers and VR mode detection
    - README.md with full documentation (300+ lines)
  - `examples/`: Real-world A-Frame patterns (1,500+ lines)
    - VR interaction patterns (two-handed grab, inventory system)
    - AR object placement (rotation controls, measurement tool)
    - 360° experiences (hotspots, photo tours)
    - Advanced controllers (gesture recognition)
    - Multi-user networking (NAF setup, voice chat)
    - Physics simulations (ragdoll, constraints)
    - Performance optimization (LOD, object pooling)

**Related Skills**: Built on threejs-webgl. For advanced 3D scenes reference threejs-webgl directly.

---

### 7. lightweight-3d-effects ✅ COMPLETED (100%)
**Status**: Fully complete and packaged

**Deliverables**:
- ✅ SKILL.md: Comprehensive guide covering all three libraries (800+ lines)
  - Zdog (setup, shapes, groups, animation, drag rotation)
  - Vanta.js (setup, 14+ effects, methods, React integration, performance)
  - Vanilla-Tilt (setup, options, methods, events, React integration)
  - 4 common patterns (hero with Vanta, icon grids, tilt galleries, combined effects)
  - Performance best practices for each library
  - 5 common pitfalls with solutions (Vanta instances, memory leaks, mobile tilt, color formats)
- ✅ References:
  - `zdog_api.md`: Complete Zdog API reference (950+ lines)
    - Core classes (Illustration, Anchor, Shape), all shape types (Ellipse, Rect, Polygon, Box, Hemisphere, Cylinder, Cone)
    - Properties, methods, animation patterns, advanced techniques (paths, bezier, arcs, models, instancing)
  - `vantajs_effects.md`: Vanta.js effects catalog (700+ lines)
    - All 14 effects (WAVES, CLOUDS, BIRDS, NET, CELLS, FOG, GLOBE, RINGS, HALO, TRUNK, TOPOLOGY, DOTS, CLOUDS2, RIPPLE)
    - Common options, methods (destroy, setOptions, resize)
    - Framework integration (React, Vue, Angular, Svelte), performance optimization
  - `tilt_patterns.md`: Vanilla-Tilt patterns reference (850+ lines)
    - Complete configuration options (25+ parameters), methods, events
    - Common patterns (card gallery, parallax layers, hover reveal, 3D buttons, product showcase)
    - Advanced techniques (dynamic values, conditional tilt, sync elements, scroll integration)
    - Framework integration (React, Vue, Angular, Svelte)
- ✅ Scripts:
  - `generate_zdog.py`: Zdog illustration generator (620+ lines)
    - 6 illustration types (shapes, cube, robot, icons, particles, spiral)
    - Interactive and CLI modes, HTML template generation
  - `setup_vanta.py`: Vanta.js background setup (640+ lines)
    - 11 effects (WAVES, CLOUDS, BIRDS, NET, CELLS, FOG, GLOBE, RINGS, DOTS, TOPOLOGY, TRUNK)
    - Interactive and CLI modes, control buttons for each effect
- ✅ Assets:
  - `starter_lightweight/`: Complete combined template
    - index.html with Vanta background, Zdog icons, tilt cards
    - style.css with responsive design, tilt layers, glare effects
    - main.js with 5 Zdog illustrations, tilt init, demo controls
    - README.md with full documentation (600+ lines)
  - `examples/`: Real-world production patterns (1,500+ lines)
    - Hero sections (split hero, full-screen with scroll indicator)
    - Product cards (pricing cards, product gallery)
    - Portfolio layouts (project grid with Vanta backgrounds)
    - Interactive dashboards (stats with Zdog charts)
    - Marketing pages (feature showcase with staggered animations)
    - E-commerce (product detail with 360° view)
    - SaaS landing pages (feature comparison table)
    - Performance patterns (lazy loading, conditional loading, idle callback, debounced resize)

**Related Skills**: Vanta.js uses threejs-webgl under the hood. For animation timing reference gsap-scrolltrigger.

---

### 8. playcanvas-engine ✅ COMPLETED (100%)
**Status**: Fully complete and packaged

**Deliverables**:
- ✅ SKILL.md: Comprehensive PlayCanvas guide (933 lines)
  - Core concepts (Application, Entity, Components: Model, Camera, Light, Rigidbody, Collision, Script, Animation, Sound)
  - 7 common patterns (basic scene, GLTF loading, materials, physics, scripts, input, animations)
  - Integration patterns (React, Editor workflow, Engine-only approach)
  - Performance optimization
  - 6 common pitfalls with solutions
- ✅ References:
  - `api_reference.md`: Complete PlayCanvas API (1,100+ lines)
    - Application, Entity, Components, Assets, Graphics, Input, Physics, Audio, Utilities
  - `editor_workflow.md`: PlayCanvas Editor integration guide (860+ lines)
    - Editor vs Engine-only comparison, project setup, asset pipeline, scene management
    - Script workflow, publishing & deployment, editor-code integration
  - `optimization_guide.md`: Performance optimization strategies (900+ lines)
    - Profiling, rendering optimization, asset optimization, memory management
    - Script optimization, mobile optimization, network & loading
- ✅ Scripts:
  - `project_generator.py`: PlayCanvas project boilerplate (620+ lines)
    - 5 project types (basic, physics, viewer, fps, particles)
    - Interactive and CLI modes
  - `component_builder.py`: Script component generator (800+ lines)
    - 7 component types (basic, interactive, animation, physics, character, camera, ui)
    - Full lifecycle methods, attribute definitions, interactive mode
- ✅ Assets:
  - `starter_playcanvas/`: Complete PlayCanvas starter template
    - index.html with UI overlay and controls
    - style.css with responsive design
    - scripts/app.js with scene setup and demo objects
    - scripts/camera-controller.js with orbit camera
    - scripts/input-manager.js with centralized input handling
    - README.md with full documentation (400+ lines)
  - `examples/`: Real-world PlayCanvas patterns (4,500+ lines)
    - Basic examples (hello cube, multiple objects, model loading)
    - 3D graphics (materials, lighting, camera effects)
    - Physics & interaction (raycasting, character controller)
    - Animation (tweens, skeletal, particles)
    - User Interface (2D UI, health bar)
    - Audio (background music, 3D positional)
    - Performance (object pooling, LOD)
    - Integration patterns (React, Three.js migration, WebXR)

**Related Skills**: Alternative to threejs-webgl for projects requiring visual editor workflow. Compare babylonjs-engine for feature comparison.

---

### 9. pixijs-2d ✅ COMPLETED (100%)
**Status**: Fully complete and packaged

**Deliverables**:
- ✅ SKILL.md: Comprehensive PixiJS v8+ guide (933+ lines)
  - Core concepts (Application, Sprite, Texture, Graphics, Container, ParticleContainer, Filters, Text)
  - 7 common patterns (interactive sprite, graphics drawing, particle systems, filters, custom shaders, sprite animations, object pooling)
  - Integration patterns (React, Three.js overlay, vanilla JS)
  - Performance optimization (100,000+ sprites at 60 FPS)
  - 6 common pitfalls with solutions
- ✅ References:
  - `api_reference.md`: Complete PixiJS v8 API (1,700+ lines)
    - Application, Sprite, Texture, Graphics, Container, ParticleContainer
    - Built-in Filters (Blur, ColorMatrix, Displacement, Alpha, Noise, FXAA)
    - Custom Filters with GLSL shaders, Text & BitmapText, Assets system
    - DisplayObject, Events, complete API with examples
  - `performance_guide.md`: Optimization strategies (1,000+ lines)
    - Rendering optimization (ParticleContainer 10x faster, culling, cacheAsBitmap)
    - Texture management (destroy, atlases, lazy loading)
    - Memory management, mobile optimization, spatial hashing O(n) collisions
    - Performance profiling and monitoring
  - `filters_effects.md`: Visual effects guide (900+ lines)
    - All built-in filters with full API and examples
    - Custom filter creation with GLSL shaders
    - Example filters (Pixelate, Chromatic Aberration, Vignette, CRT, Outline)
    - Effect combinations (glow, film grain, color grading)
- ✅ Scripts:
  - `sprite_generator.py`: PixiJS sprite application generator (600+ lines)
    - 6 sprite types (basic, interactive, animated, tiled, atlas, masked)
    - Interactive and CLI modes, HTML/JS template generation
  - `particle_builder.py`: Particle system generator (650+ lines)
    - 5 particle systems (fountain, fire, snow, explosion, stars)
    - ParticleContainer optimization, interactive/CLI modes
- ✅ Assets:
  - `starter_pixijs/`: Complete interactive template
    - index.html with UI overlay (info panel, stats, controls)
    - style.css with glassmorphism effects and responsive design
    - main.js with bouncing sprites, physics, performance monitoring
    - README.md with full documentation (800+ lines)
  - `examples/`: Real-world PixiJS patterns (12,000+ lines)
    - Basic applications (minimal app, responsive canvas, asset loading, multi-scene)
    - Interactive elements (draggable, hover effects, buttons, click detection)
    - Particle systems (emitter, fire effect, trail effect, explosions)
    - Filters & effects (glow, chromatic aberration, CRT, displacement map)
    - Custom shaders (wave distortion, pixelate, color grading, outline)
    - Animation patterns (sprite sheets, GSAP integration, custom easing, path following)
    - Performance optimization (object pooling, viewport culling, texture atlases, spatial hashing)
    - Game development (platformer physics, top-down movement, health bars, state machine)
    - UI components (progress bar, modal dialog, slider)
    - Framework integration (React with @pixi/react, Vue 3)
    - Mobile optimization (touch joystick, device detection)
    - Advanced techniques (render textures, multi-pass shaders, WebWorker integration)

**Related Skills**: Complements threejs-webgl for 2D UI overlays on 3D scenes. For animation timing reference gsap-scrolltrigger.

---

### 10. locomotive-scroll ⏳ PENDING (0%)
**Description**: Smooth scroll implementation with parallax patterns and performance considerations.

**Related Skills**: Integrates with gsap-scrolltrigger. See scroll-reveal-libraries for simpler alternatives.

---

### 11. barba-js ✅ COMPLETED (100%)
**Status**: Fully complete and packaged

**Deliverables**:
- ✅ SKILL.md: Comprehensive Barba.js guide (870+ lines)
  - Core concepts (wrapper, container, namespace, lifecycle)
  - Transition lifecycle (async and sync modes)
  - All 11 hooks with execution order
  - Views for page-specific logic
  - 7 common patterns (basic setup, fade, crossfade, slide, transition rules, router plugin, loading indicator)
  - Integration patterns (GSAP, analytics, third-party scripts)
  - Performance optimization
  - 6 common pitfalls with solutions
- ✅ References:
  - `api_reference.md`: Complete Barba.js API (1,100+ lines)
    - Core API (init, go, hooks, history, url, use)
    - Transitions (structure, rules, sync vs async)
    - Views (namespace-based logic)
    - All 11 hooks with data object reference
    - Router plugin (@barba/router)
    - Prefetch plugin (@barba/prefetch)
    - CSS plugin (@barba/css)
    - Head plugin (@barba/head)
  - `hooks_guide.md`: Complete hooks documentation (950+ lines)
    - Hook execution order (initial load and navigation)
    - Hook types (global, transition, view)
    - Async patterns (promises, async/await, manual async)
    - Individual hook reference with examples
    - Common hook patterns (loading, scroll, analytics, third-party, views)
    - Best practices
  - `gsap_integration.md`: GSAP animation patterns (800+ lines)
    - Basic integration (fade, slide, scale)
    - Timeline-based transitions
    - Advanced patterns (conditional, direction-based, curtain, morphing, split text, parallax)
    - Performance tips
    - Common issues and solutions
    - Easing reference
  - `transition_patterns.md`: Copy-paste transition library (900+ lines)
    - Fade transitions (simple, crossfade, fade-scale)
    - Slide transitions (horizontal, vertical, direction-based)
    - Scale transitions (zoom, rotate-zoom)
    - Creative transitions (curtain, wipe, stagger)
    - Conditional transitions
    - Production examples (e-commerce, portfolio, blog, agency, SaaS)
- ✅ Scripts:
  - `transition_generator.py`: Generate transition boilerplate (350+ lines)
    - 8 transition types (fade, crossfade, slide, slide-vertical, scale, stagger, curtain, custom)
    - Interactive and CLI modes
    - Customizable name, sync mode, duration, easing
    - Output to file or stdout
  - `project_setup.py`: Initialize Barba.js project (700+ lines)
    - Complete project scaffolding with Vite
    - 5 transition presets
    - Multi-page setup (index, about, contact)
    - Automatic npm install
    - Interactive and CLI modes
    - Minimal mode option
- ✅ Assets:
  - `README.md`: Complete asset documentation
    - Starter template usage guide
    - Generated project structure
    - Available transition types
    - Development workflow
    - Manual setup instructions

**Related Skills**: Works with gsap-scrolltrigger for transition animations.

---

## Phase 3: Animation & Web Components (6 skills) - MEDIUM PRIORITY

### 12. react-spring-physics ✅ COMPLETED (100%)
**Status**: Fully complete and packaged

**Deliverables**:
- ✅ SKILL.md: Comprehensive React Spring & Popmotion guide (465 lines)
  - Core concepts (useSpring, useSprings, useTrail, useTransition, useChain, useInView)
  - Spring physics fundamentals (mass, tension, friction, damping)
  - 7 common patterns (click animation, scroll-driven, trail animation, transition list, in-view reveal, chained animations, gesture-driven drag)
  - Integration patterns (Three.js, GSAP, gesture library)
  - Performance optimization
  - 6 common pitfalls with solutions
- ✅ References:
  - `react_spring_api.md`: Complete React Spring hooks and API (1,100+ lines)
  - `popmotion_api.md`: Popmotion functions and reactive streams (850+ lines)
  - `physics_guide.md`: Spring configuration, damping, stiffness tuning (900+ lines)
- ✅ Scripts:
  - `spring_generator.py`: React Spring animation boilerplate (560+ lines, 7 animation types)
  - `physics_calculator.py`: Spring physics parameter calculator (480+ lines)
- ✅ Assets:
  - `README.md`: Complete starter guide with examples, React + Vite template documentation (330+ lines)

**Related Skills**: Alternative physics approach to motion-framer. Compare with gsap-scrolltrigger for timeline-based animations. Used by react-flow-graphs for node animations.

---

### 13. animated-component-libraries ✅ COMPLETED (100%)
**Status**: Fully complete and packaged

**Deliverables**:
- ✅ SKILL.md: Comprehensive guide (933+ lines)
  - Magic UI and React Bits overview
  - Component architecture and installation methods
  - 7 common patterns (background patterns, text reveals, buttons, dock navigation, statistics, marquees, WebGL effects)
  - Integration patterns (shadcn/ui, Framer Motion, React Router, combining libraries)
  - Performance optimization (lazy loading, reduced motion, conditional rendering)
  - 6 common pitfalls with solutions
- ✅ References:
  - `magic_ui_components.md`: Complete Magic UI component catalog (800+ lines)
  - `react_bits_components.md`: React Bits component library reference (900+ lines)
  - `customization_guide.md`: Prop-based customization patterns (1,000+ lines)
- ✅ Scripts:
  - `component_importer.py`: Import and customize components (350+ lines)
  - `props_generator.py`: Generate component prop configurations (400+ lines)
- ✅ Assets:
  - `README.md`: Complete setup guides, examples, integration patterns (400+ lines)

**Related Skills**: Components built with motion-framer. Alternative to hand-crafting animations with gsap-scrolltrigger.

---

### 14. scroll-reveal-libraries ✅ COMPLETED (100%)
**Status**: Fully complete and packaged

**Deliverables**:
- ✅ SKILL.md: Comprehensive AOS guide (820+ lines)
  - Core concepts (installation, configuration, data attributes)
  - 7 common patterns (hero sections, feature cards, alternating content, testimonials, anchor triggers, animation chains, image galleries)
  - Integration patterns (React, Vue, Next.js, component wrappers)
  - Performance optimization (mobile disable, once-only animations, throttle/debounce)
  - 6 common pitfalls with solutions
  - Built-in animations catalog (50+ animations)
  - Custom animation creation
  - AOS vs GSAP ScrollTrigger comparison
- ✅ References:
  - `aos_api.md`: AOS API reference
  - `animation_catalog.md`: Built-in animations catalog
- ✅ Scripts:
  - `aos_generator.py`: AOS HTML boilerplate generator
  - `config_builder.py`: AOS configuration builder
- ✅ Assets:
  - `README.md`: Complete examples and integration patterns

**Related Skills**: Simpler alternative to gsap-scrolltrigger for basic fade/slide effects. Works with locomotive-scroll for smooth scrolling.

---

### 15. animejs ✅ COMPLETED (100%)
**Status**: Fully complete and packaged

**Deliverables**:
- ✅ SKILL.md: Comprehensive Anime.js guide (526 lines)
  - Core concepts (targets, properties, timeline, stagger)
  - 7 common patterns (stagger animation, grid stagger, SVG line drawing, SVG morphing, timeline sequence, keyframe, scroll-triggered)
  - Integration patterns (React, Vue, path following)
  - Advanced techniques (spring easing, steps, custom bezier)
  - Performance optimization
  - 6 common pitfalls with solutions
- ✅ References:
  - `api_reference.md`: Complete Anime.js API (622 lines)
  - `stagger_guide.md`: Comprehensive stagger utilities guide (522 lines)
  - `timeline_guide.md`: Timeline sequencing deep dive (663 lines)
- ✅ Scripts:
  - `animation_generator.py`: Generate Anime.js animation boilerplate (260+ lines, 8 animation types)
  - `timeline_builder.py`: Build complex timeline sequences (280+ lines, 7 presets)
- ✅ Assets:
  - `README.md`: Complete starter guide with Vite template, examples, framework integration (340+ lines)

**Related Skills**: Alternative to gsap-scrolltrigger for SVG-heavy animations. Compare animation approaches with motion-framer.

---

### 16. lottie-animations ✅ COMPLETED (100%)
**Status**: Fully complete and packaged

**Deliverables**:
- ✅ SKILL.md: Comprehensive Lottie guide
  - Core concepts (Lottie JSON, dotLottie format, library options)
  - 7 common patterns (basic, interactive, events, scroll-driven, hover, multi-animation, web worker)
  - Integration with GSAP ScrollTrigger, Framer Motion, Vue, Svelte
  - Performance optimization
  - Common pitfalls and solutions
- ✅ References:
  - `api_reference.md`: Complete API for lottie-web, lottie-react, dotlottie-web
  - `after_effects_export.md`: Guide for exporting from After Effects with Bodymovin
  - `performance_guide.md`: Detailed performance optimization strategies
- ✅ Scripts:
  - `generate_lottie_component.py`: Generate React/Vue/Svelte component boilerplate
  - `optimize_lottie.py`: Optimize Lottie JSON file size
- ✅ Assets:
  - `starter_lottie/`: Complete React + Vite starter template with Lottie examples

**Related Skills**: Complements motion-framer and gsap-scrolltrigger for designer-created animations.

---

### 17. model-viewer-component ⏳ PENDING (0%)
**Description**: Web component for 3D model viewing with AR support, product customization, and accessibility features.

**Related Skills**: Alternative to threejs-webgl and react-three-fiber for simple 3D product viewers.

---

## Phase 4: 3D Authoring & Motion (4 skills) - LOW PRIORITY

### 18. blender-web-pipeline ✅ COMPLETED (100%)
**Status**: Fully complete and packaged

**Deliverables**:
- ✅ SKILL.md: Comprehensive Blender to web pipeline guide
  - Core concepts (glTF 2.0 format, Blender Python API, web optimization)
  - 7 common patterns (manual export, batch export, optimization, texture baking, LOD generation, compression, CLI automation)
  - Integration with Three.js, React Three Fiber, Babylon.js
  - Optimization techniques (geometry, textures, materials)
  - Common pitfalls and best practices
- ✅ References:
  - `gltf_export_guide.md`: Complete glTF export settings reference
  - `bpy_api_reference.md`: Blender Python API quick reference
  - `optimization_strategies.md`: Detailed 3D model optimization techniques
- ✅ Scripts:
  - `batch_export.py`: Batch export .blend files to glTF
  - `optimize_model.py`: Optimize geometry and textures for web
  - `generate_lods.py`: Generate LOD copies automatically
- ✅ Assets:
  - `README.md`: Template and shader library documentation

**Related Skills**: Exports models for threejs-webgl, react-three-fiber, babylonjs-engine.

---

### 19. spline-interactive ✅ COMPLETED (100%)
**Status**: Fully complete and packaged

**Deliverables**:
- ✅ SKILL.md: Comprehensive Spline guide (757 lines)
  - Core concepts (scene structure, components, state-based animation, interactivity, export options)
  - 7 common patterns (basic React integration, event handling, object control, triggering animations, Next.js SSR, lazy loading, responsive scenes)
  - Integration patterns (Three.js, GSAP, Framer Motion)
  - Performance optimization
  - 6 common pitfalls with solutions
- ✅ References:
  - `api_reference.md`: Complete Spline React API (530+ lines)
- ✅ Scripts:
  - `project_generator.py`: Generate Spline + React projects (300+ lines)
  - `component_builder.py`: Build Spline component wrappers (200+ lines)
- ✅ Assets:
  - `README.md`: Complete usage guide with examples (230+ lines)

**Related Skills**: Alternative to threejs-webgl for designers who prefer visual tools over code. Exports to web formats compatible with react-three-fiber.

---

### 20. rive-interactive ✅ COMPLETED (100%)
**Status**: Fully complete and packaged

**Deliverables**:
- ✅ SKILL.md: Comprehensive Rive guide (587 lines)
  - Core concepts (state machines, inputs, ViewModels, events)
  - 7 common patterns (basic animation, state machine control, ViewModel data binding, event handling, preloading, controlled refs, multi-property updates)
  - Integration patterns (Framer Motion, GSAP ScrollTrigger)
  - Performance optimization
  - 3 common pitfalls with solutions
- ✅ References:
  - `api_reference.md`: Complete Rive React API (334 lines)
- ✅ Scripts:
  - `component_generator.py`: Generate Rive component boilerplate
  - `viewmodel_builder.py`: Build ViewModel property bindings
- ✅ Assets:
  - `README.md`: Quick start guide with examples

**Related Skills**: Similar to lottie-animations but with state machines for interactive animations. Alternative to Spline for 2D vector animations with state logic.

---

### 21. substance-3d-texturing ✅ COMPLETED (100%)
**Status**: Fully complete and packaged

**Deliverables**:
- ✅ SKILL.md: Comprehensive Substance 3D Painter texturing guide (507 lines)
  - Core concepts (PBR workflow, export presets, texture resolution guidelines)
  - 7 common patterns (basic web export, batch export with Python API, resolution override, custom presets, mobile optimization, glTF integration, event-driven export)
  - Integration patterns (Three.js, React Three Fiber, Babylon.js, glTF pipeline)
  - Performance optimization (texture size budgets, compression strategies, channel packing, mipmaps)
  - 6 common pitfalls with solutions (color space, normal maps, channel order, padding artifacts, oversized textures, missing AO)
- ✅ References:
  - `python_api_reference.md`: Complete Substance Painter Python API documentation (500+ lines)
  - `export_presets.md`: Built-in and custom export preset catalog (500+ lines)
  - `pbr_channel_guide.md`: Deep dive into PBR texture channels (600+ lines)
- ✅ Scripts:
  - `batch_export.py`: Batch export all texture sets with web optimization (270+ lines)
  - `web_optimizer.py`: Post-process textures for web (resize, compress, LOD generation) (400+ lines)
  - `generate_export_preset.py`: Create custom export preset JSON (interactive and CLI) (500+ lines)
- ✅ Assets:
  - `export_templates/`: Pre-configured export presets
    - gltf_standard.json, threejs_optimized.json, babylonjs_pbr.json, web_orm_packed.json, mobile_webgl.json
  - `README.md`: Complete asset documentation with usage examples (300+ lines)

**Related Skills**: Creates optimized textures for threejs-webgl, react-three-fiber, babylonjs-engine materials. Integrates with blender-web-pipeline for complete 3D asset workflow.

---

## Phase 5: Design Platforms (3 skills) - LOW PRIORITY

### 22. figma-dev-mode ⏳ PENDING (0%)
**Description**: Design-to-code workflow, component extraction, Figma API integration for design tokens.

**Related Skills**: Integrates with animated-component-libraries and motion-framer for implementing designs.

---

### 23. webflow-interactions ⏳ PENDING (0%)
**Description**: Visual web development, GSAP-powered animations, CMS integration patterns.

**Related Skills**: Uses gsap-scrolltrigger concepts. Compare with locomotive-scroll for smooth scrolling.

---

### 24. framer-sites ⏳ PENDING (0%)
**Description**: React-based site building platform, component library, motion integration (uses Framer Motion).

**Related Skills**: Built on motion-framer. Alternative visual development to webflow-interactions.

---

## Phase 6: Meta-Skills (2 skills) - LOW PRIORITY

### 25. web3d-integration-patterns ✅ COMPLETED (100%)
**Status**: Fully complete and packaged

**Deliverables**:
- ✅ SKILL.md: Comprehensive meta-skill for integrating multiple 3D/animation libraries (850+ lines)
  - 4 architecture patterns (Layered Separation, Unified React, Hybrid, Physics-Based)
  - Common integration patterns (scroll-driven cameras, gesture-driven 3D, state synchronization)
  - State management strategies (Zustand, Context, React Query)
  - Performance optimization (render loop coordination, on-demand rendering, memory management)
  - 3 common pitfalls with solutions (animation conflicts, state sync, memory leaks)
  - Decision matrix for choosing library combinations
  - Migration strategies between approaches

**Related Skills**: Synthesizes threejs-webgl, gsap-scrolltrigger, react-three-fiber, motion-framer, react-spring-physics.

---

### 26. modern-web-design ✅ COMPLETED (100%)
**Status**: Fully complete and packaged

**Deliverables**:
- ✅ SKILL.md: Comprehensive modern web design guide (933+ lines)
  - 7 core design principles (Performance-First, Bold Minimalism, Micro-Interactions, Scrollytelling, Cursor UX, Glassmorphism & Depth, AI-Enhanced Personalization)
  - 7 common design patterns (Immersive Hero, Horizontal Scroll Gallery, 3D Product Viewer, Animated Data Visualization, Page Transitions, Interactive Cursor Effects, Staggered Content Reveals)
  - Integration with animation skills (GSAP, Framer Motion, React Spring, Anime.js, Lottie)
  - Integration with 3D skills (Three.js, R3F, Babylon.js, Lightweight 3D)
  - Accessibility best practices (motion, color contrast, keyboard nav, screen readers, touch targets)
  - Performance optimization (animation, loading, images, fonts, JS/CSS, 3D)
  - 6 common pitfalls with solutions
  - Design system architecture (tokens, component patterns)
- ✅ References:
  - `design_trends_2024.md`: Current web design trends catalog (500+ lines, 24 trends)
  - `interaction_patterns.md`: Comprehensive micro-interaction catalog (600+ lines, 10 categories, 50+ patterns)
  - `accessibility_guide.md`: WCAG AAA compliance guide (800+ lines, complete implementation examples)
  - `performance_checklist.md`: Optimization strategies & Core Web Vitals (700+ lines, actionable checklists)
- ✅ Scripts:
  - `pattern_generator.py`: Generate design pattern boilerplate (400+ lines, 4 pattern types: hero, card, navigation, form)
  - `design_audit.py`: Audit existing designs for compliance (400+ lines, audits accessibility, performance, SEO, responsive, modern practices)
- ✅ Assets:
  - `README.md`: Design system templates documentation (500+ lines, complete asset catalog)

**Related Skills**: References all animation and interaction skills (gsap-scrolltrigger, motion-framer, react-spring-physics, animejs, lottie-animations) and 3D skills (threejs-webgl, react-three-fiber, babylonjs-engine, lightweight-3d-effects) for implementing modern trends.

---

## Phase 7: Specialized Use Cases (2 skills) - LOW PRIORITY

### 27. cesium-geospatial ⏳ PENDING (0%)
**Description**: 3D globe and 2D map visualization library. Terrain, imagery layers, vector overlays, dynamic data visualization. Integrates with React/Vue/Angular for geospatial applications and digital twins.

**Planned Deliverables**:
- SKILL.md: Cesium fundamentals, globe setup, data layers, terrain rendering
- References:
  - `api_reference.md`: Cesium core API (viewer, entities, data sources)
  - `geospatial_guide.md`: Coordinate systems, projections, GeoJSON
  - `performance_guide.md`: Tile optimization, LOD, streaming
- Scripts:
  - `globe_setup.py`: Cesium globe boilerplate generator
  - `data_loader.py`: Load GeoJSON, KML, CZML data
- Assets:
  - `starter_cesium/`: Complete Cesium + React template
  - `examples/`: Flight tracking, weather visualization, digital twins, 3D buildings

**Related Skills**: For React integration patterns reference react-three-fiber. Different domain from threejs-webgl but similar performance considerations.

---

### 28. react-flow-graphs ⏳ PENDING (0%)
**Description**: Node-based UI library for creating workflow editors, chatbot designers, data flow diagrams, and no-code tools. Drag, zoom, pan, connect nodes with custom React components.

**Planned Deliverables**:
- SKILL.md: React Flow fundamentals, node/edge customization, layout algorithms, interactivity
- References:
  - `api_reference.md`: React Flow components, hooks, utilities
  - `layout_guide.md`: Auto-layout algorithms (dagre, elk)
  - `interaction_patterns.md`: Node selection, multi-select, grouping
- Scripts:
  - `flow_generator.py`: Generate React Flow boilerplate
  - `node_builder.py`: Custom node component generator
- Assets:
  - `starter_flow/`: React Flow + Vite template with examples
  - `examples/`: Workflow builder, state machine editor, API flow visualizer

**Related Skills**: Use motion-framer for node animations. Consider react-spring-physics for physics-based node movements. Reference animated-component-libraries for custom node UI.

---

## Quality Standards

Each skill must include:

### SKILL.md Requirements
- Clear description with trigger scenarios (when to use)
- Core concepts with examples
- Common patterns (3-7 real-world examples)
- Integration patterns (with other skills)
- Performance best practices
- Common pitfalls and solutions
- Resource references

### References Requirements
- Detailed API documentation
- Advanced patterns and techniques
- Migration guides (if applicable)
- Troubleshooting guides

### Scripts Requirements
- Python/Bash automation utilities
- Boilerplate generators
- Validation/optimization tools
- All scripts must be executable and documented

### Assets Requirements
- Complete starter projects/templates
- Example implementations
- Configuration files
- Design system tokens (where applicable)

---

## Documentation Sources

Always use the latest documentation via:
- **Context7 MCP Server**: `/mcp__context7__resolve-library-id` → `/mcp__context7__get-library-docs`
- **Official Documentation**: WebFetch for official docs
- **Anthropic Agent Skills Guidelines**: Follow skill structure best practices

---

## Progress Tracking

**Overall Progress**: 21/28 skills (75%)
- ✅ Completed: 21 skills (threejs-webgl, gsap-scrolltrigger, react-three-fiber, motion-framer, babylonjs-engine, aframe-webxr, lightweight-3d-effects, playcanvas-engine, pixijs-2d, barba-js, react-spring-physics, animated-component-libraries, scroll-reveal-libraries, animejs, lottie-animations, blender-web-pipeline, spline-interactive, rive-interactive, substance-3d-texturing, web3d-integration-patterns, modern-web-design)
- 🔄 In Progress: 0 skills
- ⏳ Pending: 8 skills

**Phase 1 Progress**: 5/5 skills (100%) ✅ COMPLETE
- ✅ Completed: threejs-webgl, gsap-scrolltrigger, react-three-fiber, motion-framer, babylonjs-engine

**Phase 2 Progress**: 5/6 skills (83.3%)
- ✅ Completed: aframe-webxr, lightweight-3d-effects, playcanvas-engine, pixijs-2d, barba-js
- Next: locomotive-scroll
- Priority: locomotive-scroll

**Phase 3 Progress**: 5/6 skills (83.3%)
- ✅ Completed: react-spring-physics, animated-component-libraries, scroll-reveal-libraries, animejs, lottie-animations
- Next: model-viewer-component
- Priority: model-viewer-component

**Phase 4 Progress**: 4/4 skills (100%) ✅ COMPLETE
- ✅ Completed: blender-web-pipeline, spline-interactive, rive-interactive, substance-3d-texturing

**Phase 5 Progress**: 0/3 skills (0%)
- ⏳ Pending: figma-dev-mode, webflow-interactions, framer-sites

**Phase 6 Progress**: 2/2 skills (100%) ✅ COMPLETE
- ✅ Completed: web3d-integration-patterns, modern-web-design

**Phase 7 Progress**: 0/2 skills (0%)
- ⏳ Pending: cesium-geospatial, react-flow-graphs

---

## Success Criteria

Each skill is complete when:
1. ✅ SKILL.md is comprehensive and follows guidelines
2. ✅ All references are detailed and accurate
3. ✅ Scripts are functional and documented
4. ✅ Assets are production-ready
5. ✅ Skill passes validation (`scripts/package_skill.py`)
6. ✅ Skill is packaged as `.zip` for distribution

---

## Timeline Estimate

- **Phase 1** (5 skills): Core foundation - Complete first
- **Phase 2** (6 skills): Extended 3D/VR and scroll libraries
- **Phase 3** (6 skills): Animation variety and component libraries
- **Phases 4-7**: Expand based on agency needs and feedback

**Current Focus**: Complete motion-framer (scripts and assets pending)

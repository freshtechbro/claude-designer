# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Instructions

Be concise and to the point. Sacrifice grammar and punctuation for clarity and conciseness.

## Repository Overview

This is a **dual-purpose repository**:
1. **Development Workspace** - Create and manage Claude skills in `.claude/skills/`
2. **Plugin Marketplace** - Distribute skills as plugins via `.claude/plugins/` and `.claude-plugin/marketplace.json`

Skills are modular, self-contained packages that extend Claude's capabilities by providing specialized knowledge, workflows, and tools. Each skill acts as an "onboarding guide" for specific domains or tasks.

The repository focuses on creating comprehensive skills for a design agency's web development toolstack, particularly 3D/WebGL and animation technologies, then packaging them as plugins with slash commands and specialized agents.

## Official Documentation Reference

**IMPORTANT**: All skills in this repository MUST follow Claude's official skill standards.

📚 **Official Claude Skill Documentation**: https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview

Key resources:
- Skill Overview: https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview
- Creating Skills: https://docs.claude.com/en/docs/agents-and-tools/agent-skills/creating-skills
- Skill Structure: https://docs.claude.com/en/docs/agents-and-tools/agent-skills/skill-structure

When creating or modifying skills, **always consult the official documentation** to ensure compliance with the latest standards.

## Quick Reference

**Skill Development Workflows**:

```bash
# Create a new skill
.claude/skills/skill-creator/scripts/init_skill.py my-new-skill --path .claude/skills

# Validate a skill
.claude/skills/skill-creator/scripts/quick_validate.py .claude/skills/my-new-skill

# Package a skill (automatically validates first)
.claude/skills/skill-creator/scripts/package_skill.py .claude/skills/my-new-skill

# Validate all skills
for skill in .claude/skills/*/; do
  .claude/skills/skill-creator/scripts/quick_validate.py "$skill"
done

# Make a script executable (required after creating new scripts)
chmod +x .claude/skills/my-skill/scripts/my_script.py
```

**Plugin Marketplace Workflows**:

```bash
# Generate individual plugin from skill
./scripts/marketplace/generate_plugin.py threejs-webgl

# Generate all individual plugins
./scripts/marketplace/generate_plugin.py --all

# Generate category bundle plugin
./scripts/marketplace/generate_bundle.py core-3d-animation

# Generate all bundles
./scripts/marketplace/generate_bundle.py --all

# Generate marketplace.json manifest
./scripts/marketplace/generate_marketplace.py

# Validate marketplace and all plugins
./scripts/marketplace/validate_marketplace.py
```

**User Installation Workflows**:

```bash
# Add marketplace to Claude Code
/plugin marketplace add freshtechbro/claudedesignskills

# Install individual plugin
/plugin install threejs-webgl

# Install bundle plugin
/plugin install core-3d-animation
```

**Skill Activation**:
- Skills auto-activate when Claude detects trigger keywords from the description
- Mention specific technologies: "Three.js", "GSAP", "React Three Fiber"
- Describe tasks: "create 3D scene", "scroll-driven animations", "physics-based motion"

## Repository Structure

```
claudeskills/
├── CLAUDE.md                      # This file - repository guidance
├── MARKETPLACE.md                 # Plugin marketplace documentation
├── README.md                      # Public-facing documentation
│
├── .claude/
│   ├── skills/                    # Skill development workspace
│   │   ├── skill-creator/         # Meta-skill for creating skills
│   │   ├── threejs-webgl/         # ✅ Complete (22 total)
│   │   ├── gsap-scrolltrigger/
│   │   └── ...                    # (20 more skills)
│   │
│   └── plugins/                   # Generated plugins for distribution
│       ├── individual/            # 22 individual skill plugins
│       │   ├── threejs-webgl/     # Each includes skills/, commands/, agents/
│       │   ├── gsap-scrolltrigger/
│       │   └── ...
│       │
│       └── bundles/               # 5 category bundle plugins
│           ├── core-3d-animation/
│           ├── extended-3d-scroll/
│           ├── animation-components/
│           ├── authoring-motion/
│           └── meta-skills/
│
├── .claude-plugin/
│   └── marketplace.json           # Marketplace manifest (27 plugins)
│
└── scripts/
    ├── skill-creator/             # (existing skill scripts)
    └── marketplace/               # Marketplace automation
        ├── generate_plugin.py     # Convert skill → plugin
        ├── generate_bundle.py     # Create category bundles
        ├── generate_marketplace.py # Build marketplace.json
        └── validate_marketplace.py # Validate all plugins
```

**Each skill directory contains**:
- `SKILL.md` - Main instructions
- `scripts/` - Automation utilities
- `references/` - Documentation
- `assets/` - Templates and starter projects

**Each plugin directory contains**:
- `.claude-plugin/plugin.json` - Plugin manifest
- `skills/<skill-name>/` - Skill content (copied from `.claude/skills/`)
- `commands/` - Slash commands (1-3 per plugin)
- `agents/` - Specialized agents (1-2 per plugin)

## Current Repository State

**Skills**: 22/22 complete (100%) - All skills packaged and ready for distribution

**Plugins**: 27/27 complete (100%) - 22 individual + 5 bundles with commands and agents

**Marketplace**: ✅ Active - marketplace.json published

**All Skills Complete**:
- **Core 3D & Animation (5)**: threejs-webgl, gsap-scrolltrigger, react-three-fiber, motion-framer, babylonjs-engine
- **Extended 3D & Scroll (6)**: aframe-webxr, lightweight-3d-effects, playcanvas-engine, pixijs-2d, locomotive-scroll, barba-js
- **Animation & Components (5)**: react-spring-physics, animated-component-libraries, scroll-reveal-libraries, animejs, lottie-animations
- **3D Authoring & Motion (4)**: blender-web-pipeline, spline-interactive, rive-interactive, substance-3d-texturing
- **Meta-Skills (2)**: web3d-integration-patterns, modern-web-design

**All Plugins Complete**:
- **Individual (22)**: Each with 1-3 slash commands + 1-2 specialized agents
- **Bundles (5)**: core-3d-animation, extended-3d-scroll, animation-components, authoring-motion, meta-skills

Each skill directory contains SKILL.md, references/, scripts/, assets/, and a packaged .zip file.
Each plugin directory contains plugin.json manifest, skills/, commands/, and agents/.

## Common Commands

### Initialize a New Skill

```bash
.claude/skills/skill-creator/scripts/init_skill.py <skill-name> --path .claude/skills
```

Requirements:
- Skill name must be in hyphen-case (e.g., `my-new-skill`)
- Lowercase letters, digits, and hyphens only
- Maximum 40 characters
- Must match directory name exactly

This creates:
- `SKILL.md` with proper YAML frontmatter and TODO placeholders
- `scripts/` directory with example Python script
- `references/` directory with example reference documentation
- `assets/` directory with example asset placeholder

### Validate a Skill

```bash
.claude/skills/skill-creator/scripts/quick_validate.py <path/to/skill>
```

Checks:
- SKILL.md exists
- Valid YAML frontmatter format
- Required fields present (name, description)
- Naming conventions followed
- No angle brackets in description

### Package a Skill

```bash
.claude/skills/skill-creator/scripts/package_skill.py <path/to/skill> [output-directory]
```

Automatically validates before packaging. Creates a distributable zip file named `<skill-name>.zip`.

#### ZIP Structure Requirements

**CRITICAL**: Claude.ai requires a specific ZIP structure for skill uploads:

**Required Structure** (correct):
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

**Common Errors** (will be rejected):
- ❌ SKILL.md inside subdirectory (e.g., `skill-name/SKILL.md`)
- ❌ Nested .zip files inside the archive
- ❌ Missing YAML frontmatter in SKILL.md

**How package_skill.py Ensures Correct Structure**:
1. **Root-level files**: Uses `relative_to(skill_path)` to place SKILL.md at root
2. **No nested zips**: Automatically skips .zip files during packaging
3. **Safe output location**: Outputs to parent directory by default to avoid nesting
4. **Validation first**: Runs validation before creating the zip file

**Upload Requirements** (from claude.ai):
- ZIP file must include exactly one SKILL.md file at the root level
- SKILL.md must contain valid YAML frontmatter with `name` and `description`
- No nested zip files are allowed in the archive

### Python Script Requirements

**CRITICAL**: All Python scripts in skills MUST meet these standards:

#### 1. Shebang Line (MANDATORY)
Every Python script MUST start with:
```python
#!/usr/bin/env python3
```

**Why**: Allows scripts to be executed directly with `./script.py`

#### 2. Executable Permissions (MANDATORY)
All scripts MUST have executable permissions:
```bash
chmod +x script.py
```

**Verification**: Check with `ls -l script.py` - should show `-rwxr-xr-x`

**Common Error**: Forgetting to set executable permissions after creating scripts. Scripts will have `-rw-r--r--` permissions by default.

#### 3. Documentation (MANDATORY)
Every script MUST include:
- Module-level docstring describing purpose
- Usage examples in docstring or comments
- Argument descriptions if script accepts parameters

**Example**:
```python
#!/usr/bin/env python3
"""
Three.js Scene Setup Generator

Generates boilerplate Three.js scene code with customizable options.

Usage:
    ./setup_scene.py                    # Interactive mode
    ./setup_scene.py --renderer webgl   # CLI mode
"""
```

#### 4. Dependencies (REQUIRED)
- Use ONLY Python 3 standard library
- No external dependencies (no pip packages)
- Script must be self-contained and portable

#### 5. Execution Methods
Scripts should support both:
```bash
./script.py              # Direct execution (requires executable permissions)
python3 script.py        # Explicit Python invocation
```

#### 6. Quality Standards
- Single responsibility - one clear purpose per script
- Error handling with helpful messages
- Input validation
- Exit codes (0 for success, non-zero for errors)

### Common Script Execution Patterns

**Interactive Mode** (most scripts support this):
```bash
.claude/skills/skill-creator/scripts/init_skill.py
# Script will prompt for required information
```

**CLI Mode** (with arguments):
```bash
.claude/skills/skill-creator/scripts/init_skill.py my-skill --path .claude/skills
```

**Validation Before Packaging**:
```bash
# Validate first (optional, but recommended during development)
.claude/skills/skill-creator/scripts/quick_validate.py .claude/skills/my-skill

# Package (automatically validates)
.claude/skills/skill-creator/scripts/package_skill.py .claude/skills/my-skill
```

### Available Skill-Specific Generators

Each completed skill includes custom generator scripts:

**threejs-webgl**:
- `setup_scene.py` - Generate Three.js scene boilerplate

**gsap-scrolltrigger**:
- `generate_animation.py` - Generate GSAP animation code
- `timeline_builder.py` - Build animation timeline sequences

**react-three-fiber**:
- `component_generator.py` - Generate R3F components (12 types)
- `scene_setup.py` - R3F scene setup with presets

**motion-framer**:
- `animation_generator.py` - Generate Motion component boilerplate (11 animation types)
- `variant_builder.py` - Build variant configurations (7 presets)

**babylonjs-engine**:
- `scene_generator.py` - Babylon scene boilerplate (8 scene types)
- `mesh_builder.py` - Mesh creation tool (13 shapes)

**aframe-webxr**:
- `scene_generator.py` - A-Frame scene boilerplate (7 scene types)
- `component_builder.py` - Custom component generator (7 component types)

**lightweight-3d-effects**:
- `generate_zdog.py` - Zdog illustration generator (6 illustration types)
- `setup_vanta.py` - Vanta.js background setup (11 effects)

These scripts can be referenced when creating similar generators for new skills.

## Official Claude Skill Standards

### Critical Requirements

**EVERY skill MUST comply with these standards** (per Claude's official documentation):

#### 1. YAML Frontmatter (MANDATORY)

Every `SKILL.md` file **MUST start** with YAML frontmatter:

```yaml
---
name: skill-name
description: What the skill does and when to use it
---
```

**Frontmatter Requirements**:
- Must be at the **very beginning** of SKILL.md (line 1)
- Must start with `---` and end with `---`
- Must contain exactly two required fields: `name` and `description`
- No optional fields are currently supported

#### 2. Name Field Requirements

The `name` field MUST:
- Match the directory name **exactly** (case-sensitive)
- Use hyphen-case (lowercase with hyphens): `my-skill-name`
- Contain only: lowercase letters (a-z), digits (0-9), and hyphens (-)
- Be between 1-40 characters
- Not contain spaces, underscores, or special characters
- Not start or end with a hyphen

**Examples**:
- ✅ Correct: `threejs-webgl`, `gsap-scrolltrigger`, `react-three-fiber`
- ❌ Wrong: `ThreeJS-WebGL` (uppercase), `three_js_webgl` (underscores), `three.js.webgl` (periods)

#### 3. Description Field Requirements

The `description` field MUST:
- Be **non-empty** (minimum 10 characters recommended)
- Be **maximum 1024 characters**
- **Not contain angle brackets** (`<` or `>`) - these cause validation errors
- Explain **WHAT the skill does** and **WHEN Claude should use it**
- Use **third person** language (e.g., "This skill should be used when...")
- Include **clear trigger scenarios** so Claude knows when to activate the skill

**Description Best Practices**:

1. **Start with what it does**:
   ```yaml
   description: Comprehensive skill for Three.js WebGL/WebGPU development...
   ```

2. **Include trigger scenarios**:
   ```yaml
   description: Use this skill when building 3D scenes, creating WebGL applications, implementing 3D visualizations...
   ```

3. **List specific keywords/technologies**:
   ```yaml
   description: Triggers on tasks involving Three.js, scene graphs, meshes, materials, lighting, animations, or WebGL rendering...
   ```

4. **Mention alternatives/comparisons**:
   ```yaml
   description: Alternative to Babylon.js with lighter footprint and more flexible architecture...
   ```

**Complete Example**:
```yaml
---
name: threejs-webgl
description: Comprehensive skill for Three.js WebGL/WebGPU 3D graphics development. Use this skill when building 3D scenes, creating interactive visualizations, implementing game graphics, or developing immersive web experiences. Triggers on tasks involving Three.js, scene graphs, geometries, meshes, materials, textures, lighting, cameras, animations, shaders, or WebGL/WebGPU rendering. Alternative to Babylon.js and PlayCanvas with more flexibility.
---
```

#### 4. Validation Requirements

**Before considering a skill complete**, it MUST:
- Pass `quick_validate.py` script without errors
- Have valid YAML frontmatter structure
- Have name matching directory name
- Have non-empty description
- Have no angle brackets in description
- Contain actual content after frontmatter

**How to Validate**:
```bash
.claude/skills/skill-creator/scripts/quick_validate.py .claude/skills/my-skill
```

**Expected output**: `Skill is valid!`

#### 5. Common Validation Errors and Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| "SKILL.md not found" | File missing or wrong name | Create `SKILL.md` (exact name, case-sensitive) |
| "No YAML frontmatter found" | Missing `---` delimiters | Add YAML block at beginning of file |
| "Missing required field: name" | No `name:` field | Add `name: skill-name` to frontmatter |
| "Missing required field: description" | No `description:` field | Add `description: ...` to frontmatter |
| "Name mismatch" | `name` doesn't match directory | Change name to match directory exactly |
| "Invalid name format" | Contains invalid characters | Use only lowercase, digits, hyphens |
| "Angle brackets in description" | Description contains `<` or `>` | Remove or replace angle brackets |
| "Empty description" | Description field is blank | Add meaningful description with triggers |

### Recent Validation Audit Results

**Audit Date**: 2025 (Latest)

**Findings**: 4 out of 9 skills (44%) were **non-compliant** and missing YAML frontmatter entirely.

**Fixed Skills**:
- `babylonjs-engine` - Added proper YAML frontmatter ✅
- `aframe-webxr` - Added proper YAML frontmatter ✅
- `lightweight-3d-effects` - Added proper YAML frontmatter ✅
- `playcanvas-engine` - Added proper YAML frontmatter ✅

**Current Status**: 9/9 skills (100%) now compliant ✅

**Key Lesson**: The most common error is completely omitting YAML frontmatter. Skills with `## Description` markdown sections instead of YAML frontmatter will **not work** with Claude's skill system.

## Skill Architecture

### Required Components

Every skill MUST have:
- **SKILL.md** - Main skill file with:
  - **YAML frontmatter** containing `name` and `description` (see "Official Claude Skill Standards" above)
  - Markdown instructions in imperative/infinitive form (verb-first, not second person)

### Optional Components

Skills may include any combination of:

1. **scripts/** - Executable code (Python/Bash) for deterministic operations
   - Token efficient
   - May be executed without loading into context
   - Use when code is repeatedly rewritten or reliability is critical

2. **references/** - Documentation loaded into context as needed
   - API documentation, schemas, policies, detailed workflow guides
   - Loaded only when Claude determines it's needed
   - For large files (>10k words), include grep search patterns in SKILL.md

3. **assets/** - Files used in output, not loaded into context
   - Templates, images, fonts, boilerplate code
   - Copied or modified in final output

### Progressive Disclosure System

Skills use three-level loading:
1. **Metadata** (name + description) - Always in context (~100 words)
2. **SKILL.md body** - When skill triggers (<5k words)
3. **Bundled resources** - As needed by Claude (unlimited for scripts)

## Skill Creation Workflow

When creating or editing skills, follow this process:

1. **Review Official Standards** - Read the "Official Claude Skill Standards" section above and consult https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview

2. **Understand with Concrete Examples** - Gather real usage examples from official documentation

3. **Plan Reusable Contents** - Identify needed scripts/references/assets

4. **Fetch Documentation** - Use Context7 MCP to get latest library docs:
   - `mcp__context7__resolve-library-id` to find the library ID
   - `mcp__context7__get-library-docs` to retrieve documentation
   - If library not found, use `WebFetch` on official documentation

5. **Initialize** - Run `init_skill.py` for new skills (automatically creates proper YAML frontmatter)

6. **Write Description** - Craft description with:
   - What the skill does
   - When to use it (trigger scenarios)
   - Key technologies/keywords
   - Alternatives/comparisons
   - No angle brackets (`<` or `>`)
   - Max 1024 characters

7. **Edit Content** - Customize SKILL.md body and resources:
   - Use imperative/infinitive form (not second person)
   - Include core concepts, patterns, integrations, pitfalls
   - Delete unused example content
   - Keep SKILL.md focused, move details to references/

8. **Validate Early and Often** - Run validation after major changes:
   ```bash
   .claude/skills/skill-creator/scripts/quick_validate.py .claude/skills/my-skill
   ```

9. **Package** - Run `package_skill.py` to validate and create distributable zip:
   ```bash
   .claude/skills/skill-creator/scripts/package_skill.py .claude/skills/my-skill
   ```

10. **Iterate** - Test skill activation, improve based on real usage, re-validate

### Documentation Sources

When creating skills, always use the most current documentation:
- **Context7 MCP Server** - Primary source for library documentation (see commands above)
- **WebFetch** - For official documentation websites when Context7 doesn't have the library
- **Skill Creator** - Follow the guidance in `.claude/skills/skill-creator/SKILL.md`

## Key Conventions

### Naming
- Skills: hyphen-case, lowercase only (e.g., `skill-creator`)
- Skill titles: Title Case in SKILL.md (e.g., "Skill Creator")
- Directory name must match YAML `name` field exactly

### Writing Style
- Use imperative/infinitive form throughout SKILL.md
- Write "To accomplish X, do Y" not "You should do X"
- Maintain objective, instructional language for AI consumption
- Avoid second person ("you") - Claude is the consumer, not the end user

### YAML Frontmatter
- `name`: Must match directory name exactly (hyphen-case)
- `description`: Should explain WHAT the skill does and WHEN to use it
- Use third person (e.g., "This skill should be used when...")
- No angle brackets allowed (`<` or `>`)
- See "Official Claude Skill Standards" section for complete requirements

### Avoid Duplication
- Information should live in either SKILL.md or references files, not both
- Prefer references files for detailed information
- Keep SKILL.md lean with only essential procedural instructions

## Skill Creation Best Practices

### 1. Writing Effective Descriptions

**Goal**: Help Claude understand when to activate the skill.

**Formula**:
```
[What it does] + [When to use it] + [Trigger keywords] + [Alternatives/comparisons]
```

**Example**:
```yaml
description: Comprehensive skill for Three.js WebGL/WebGPU 3D graphics development. Use this skill when building 3D scenes, creating interactive visualizations, implementing game graphics, or developing immersive web experiences. Triggers on tasks involving Three.js, scene graphs, geometries, meshes, materials, textures, lighting, cameras, animations, shaders, or WebGL/WebGPU rendering. Alternative to Babylon.js and PlayCanvas with more flexibility.
```

### 2. Structuring SKILL.md Content

**Recommended sections** (in order):

1. **Overview** - Brief introduction (2-3 paragraphs)
2. **Core Concepts** - Fundamental concepts with code examples
3. **Common Patterns** - 5-7 real-world patterns with full implementations
4. **Integration Patterns** - How to use with other libraries/frameworks
5. **Performance Optimization** - Best practices and anti-patterns
6. **Common Pitfalls** - Issues developers face and solutions
7. **Resources** - Links to official docs, examples, communities
8. **Related Skills** - Cross-references to other skills in repository

### 3. Code Examples

**All code examples must**:
- Be complete and runnable
- Include imports/dependencies
- Show realistic use cases
- Include comments explaining key concepts
- Follow language/framework conventions

### 4. Validation Workflow

**Validate continuously during development**:

```bash
# After creating skill
.claude/skills/skill-creator/scripts/init_skill.py my-skill

# After writing description
.claude/skills/skill-creator/scripts/quick_validate.py .claude/skills/my-skill

# After adding content
.claude/skills/skill-creator/scripts/quick_validate.py .claude/skills/my-skill

# Before marking complete
.claude/skills/skill-creator/scripts/package_skill.py .claude/skills/my-skill
```

### 5. Testing Skill Activation

**How to verify Claude uses your skill**:

1. **Trigger words**: Include specific keywords from description in prompts
2. **Use cases**: Request tasks described in "when to use it" scenarios
3. **Technology names**: Mention the library/framework by name
4. **Check activation**: Claude should reference the skill when responding

**Example**: For `threejs-webgl` skill:
- ✅ Trigger: "Help me create a Three.js scene with a rotating cube"
- ✅ Trigger: "I need to implement WebGL rendering for 3D visualization"
- ❌ Won't trigger: "Help me with 3D" (too vague, no specific keywords)

### 6. Maintaining Skills

**When updating skills**:

1. Update description if trigger scenarios change
2. Re-validate after any changes to frontmatter
3. Keep examples current with latest library versions
4. Add new patterns as they emerge
5. Document breaking changes in references/
6. Update related skills cross-references

### 7. Common Mistakes to Avoid

❌ **Don't**:
- Omit YAML frontmatter
- Write descriptions without trigger keywords
- Use second person ("you") in skill content
- Include angle brackets in descriptions
- Copy-paste content from other skills without customization
- Skip validation
- Create skills without consulting official Claude docs
- **Forget to make scripts executable** (`chmod +x`)
- **Leave template files** (example.py, example_asset.txt) in production skills
- Create scripts with external dependencies

✅ **Do**:
- Always include proper YAML frontmatter
- Write comprehensive descriptions with clear triggers
- Use imperative/infinitive form
- Test skill activation with real prompts
- Validate early and often
- Follow official Claude standards
- Cross-reference related skills
- **Set executable permissions on all scripts** immediately after creation
- **Remove template/example files** before marking skill complete
- Use only Python 3 standard library in scripts

## Skill Quality Standards

Each completed skill must include:

### SKILL.md Requirements
- Clear description with trigger scenarios (when to use)
- Core concepts with examples
- Common patterns (3-7 real-world examples)
- Integration patterns (with other skills/libraries)
- Performance best practices
- Common pitfalls and solutions
- Resource references (scripts/references/assets)

### References Requirements
- Detailed API documentation
- Advanced patterns and techniques
- Migration guides (if applicable)
- Troubleshooting guides

### Scripts Requirements
- Python/Bash automation utilities
- Boilerplate generators
- Validation/optimization tools
- All scripts executable and documented

### Assets Requirements
- Complete starter projects/templates
- Example implementations
- Configuration files
- Design system tokens (where applicable)

## Skill Relationships and Dependencies

Understanding skill relationships helps when creating integration patterns:

**Foundation Skills** (used by others):
- `threejs-webgl` → Used by react-three-fiber, aframe-webxr, lightweight-3d-effects (Vanta.js)
- `gsap-scrolltrigger` → Integrates with most animation and 3D skills
- `motion-framer` → Used by animated-component-libraries, integrates with R3F

**Alternative Skills** (similar use cases):
- 3D engines: `threejs-webgl` vs `babylonjs-engine` vs `playcanvas-engine`
- Animation: `gsap-scrolltrigger` vs `motion-framer` vs `react-spring-physics`
- Smooth scroll: `locomotive-scroll` vs `scroll-reveal-libraries`

**Integration Patterns**:
- Three.js + GSAP: Scroll-driven 3D animations
- React Three Fiber + Framer Motion: Interactive 3D UI components
- Vanta.js (uses Three.js) + GSAP: Animated backgrounds with scroll triggers

When creating a new skill, reference related skills in existing skill directories for integration examples.

## Development Workflow

When working on skills in this repository:

1. **Complete one skill at a time** - Finish all components (SKILL.md, references, scripts, assets) before moving to the next
2. **Validate frequently** - Run `quick_validate.py` after significant changes
3. **Package when complete** - Use `package_skill.py` to create distributable zip

## Repository Verification

To verify the integrity of the entire repository:

```bash
# Count total skills (should be 23 including skill-creator)
ls -d .claude/skills/*/ | wc -l

# Verify all skills have SKILL.md
find .claude/skills -name "SKILL.md" -type f | wc -l

# Verify all skills are packaged (should be 22, excluding skill-creator)
find .claude/skills -name "*.zip" -type f | wc -l

# Validate all skills at once
for skill in .claude/skills/*/; do
  skill_name=$(basename "$skill")
  echo "Validating $skill_name..."
  .claude/skills/skill-creator/scripts/quick_validate.py "$skill" 2>&1 | grep -q "valid" && echo "✅ $skill_name" || echo "❌ $skill_name"
done

# Verify script permissions (all should be executable)
find .claude/skills -name "*.py" -type f ! -perm -111 -print
# (No output means all scripts are executable)
```

## Troubleshooting

### Script Permission Issues

If a script is not executable:
```bash
chmod +x .claude/skills/skill-creator/scripts/init_skill.py
```

### Validation Errors

**See "Official Claude Skill Standards" section above for comprehensive validation error reference.**

Quick fixes for common issues:

1. **Missing YAML frontmatter** (MOST COMMON):
   - **Problem**: SKILL.md doesn't start with `---`
   - **Fix**: Add YAML frontmatter at the very beginning (line 1)
   - **Example**:
     ```yaml
     ---
     name: my-skill
     description: What the skill does and when to use it
     ---
     ```

2. **Name mismatch**:
   - **Problem**: `name:` field doesn't match directory name
   - **Fix**: Make name match directory exactly (hyphen-case, lowercase)

3. **Angle brackets in description**:
   - **Problem**: Description contains `<` or `>`
   - **Fix**: Remove or replace with words (e.g., `less than` instead of `<`)

4. **Empty description**:
   - **Problem**: Description field is blank or too short
   - **Fix**: Write comprehensive description with trigger scenarios (see standards above)

5. **Invalid name format**:
   - **Problem**: Name contains uppercase, underscores, periods, or spaces
   - **Fix**: Use only lowercase letters, digits, and hyphens

### Running Validation

**Always validate before considering a skill complete**:

```bash
# Validate single skill
.claude/skills/skill-creator/scripts/quick_validate.py .claude/skills/my-skill

# Validate all skills
for skill in .claude/skills/*/; do
  echo "Validating $skill"
  .claude/skills/skill-creator/scripts/quick_validate.py "$skill"
done
```

**Expected output**: `Skill is valid!`

### Context7 MCP Documentation Fetching

When creating skills for libraries:
1. First resolve the library ID: `mcp__context7__resolve-library-id` with library name
2. Then fetch documentation: `mcp__context7__get-library-docs` with the resolved ID
3. If library not found in Context7, use `WebFetch` on official documentation

### Skill Quality Checklist

Before marking a skill complete, ensure:

**Critical (Must Pass)**:
- [ ] ✅ **YAML frontmatter present** with `name` and `description` fields
- [ ] ✅ **Name matches directory name** exactly (hyphen-case)
- [ ] ✅ **Description is complete** with trigger scenarios (10-1024 chars)
- [ ] ✅ **No angle brackets** in description
- [ ] ✅ **All scripts are executable**: Run `ls -l scripts/*.py` - all should show `-rwxr-xr-x`
- [ ] ✅ **All scripts have shebang**: First line is `#!/usr/bin/env python3`
- [ ] ✅ **No template files remain**: No `example.py` or `example_asset.txt` files
- [ ] ✅ **Passes validation script**: `quick_validate.py` returns "Skill is valid!"
- [ ] ✅ **Packages successfully**: `package_skill.py` completes without errors

**Content Quality (Recommended)**:
- [ ] SKILL.md includes all required sections (overview, core concepts, common patterns, integration patterns, performance, pitfalls)
- [ ] All scripts include comprehensive documentation (docstrings with usage examples)
- [ ] Scripts handle errors gracefully with helpful messages
- [ ] References directory contains detailed API documentation
- [ ] Assets directory includes complete starter templates
- [ ] Documentation is current and accurate
- [ ] Examples are tested and working

**Repository Hygiene**:
- [ ] Related skills are cross-referenced
- [ ] Integration patterns documented

### Historical Issues

**2025 YAML Frontmatter Audit**:
- 44% of skills (4 out of 9) were missing YAML frontmatter entirely
- Skills had `## Description` markdown sections instead of YAML
- This caused skills to not be recognized by Claude's system
- All skills have been fixed and now validate successfully

**2025 Script Executability Audit**:
- 100% of custom scripts (13 out of 13) were missing executable permissions
- Scripts had `-rw-r--r--` instead of `-rwxr-xr-x` permissions
- Users had to use `python3 script.py` instead of `./script.py`
- Template files (example.py, example_asset.txt) remained in 2 skills
- All issues fixed: scripts now executable, template files removed

**2025 Full Repository Completion**:
- All 22 skills now complete with SKILL.md, references/, scripts/, and assets/
- All skills validated and packaged as distributable .zip files
- Repository ready for production use

**Key Takeaways**:
1. YAML frontmatter is **not optional** - skills without it won't work
2. Scripts **must be executable** - set permissions immediately after creation
3. **Remove template files** before marking skills complete
4. **Verify all directories** (scripts, references, assets) have actual content

## License

All skills in this repository are licensed under Apache License 2.0.

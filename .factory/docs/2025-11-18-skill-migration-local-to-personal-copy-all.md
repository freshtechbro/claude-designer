## Skill Migration Spec: Local → Personal (Copy Strategy)

**Objective**: Copy all skills from `<repo>/.factory/skills/` to `~/.factory/skills/` while keeping originals in repo for team access.

### Execution Steps

1. **Create personal skills directory** (if missing)
   - `mkdir -p ~/.factory/skills/`

2. **Copy all skills from repo to personal**
   - `cp -r <repo>/.factory/skills/* ~/.factory/skills/`
   - This preserves all skill directories, `SKILL.md` files, and supporting content (references/, scripts/, assets/)

3. **Verify migration**
   - Count skills: `ls ~/.factory/skills/ | wc -l` should match `ls <repo>/.factory/skills/ | wc -l`
   - Check directory structure: `tree ~/.factory/skills/` or `find ~/.factory/skills -type f | head -20`

4. **Restart Droid**
   - Exit current session
   - Restart `droid` to rescan skill locations
   - Run `/skills` to confirm all skills appear in personal scope

5. **Confirm functionality**
   - Test skill activation by mentioning trigger keywords
   - Verify personal skills are discovered alongside workspace skills

### Outcome

- ✅ All skills available in `~/.factory/skills/` (personal, machine-wide)
- ✅ Original skills remain in `<repo>/.factory/skills/` (team-accessible)
- ✅ Personal copies take precedence if names match (Factory discovery order)
- ✅ Skills follow you across all projects on your machine

### No changes to git or repo configuration needed
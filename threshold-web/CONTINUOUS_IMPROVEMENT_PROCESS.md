# Continuous Improvement Process

**Every fix, every lesson, every improvement gets recorded. No exceptions.**

---

## The Process (5 Steps)

### Step 1: Log the Learning
**File**: `.learnings/YYYY-MM-DD-description.md`

**Content**:
```markdown
# Fix: [Title of Problem]

## Problem
[What was broken? What error occurred?]

## Root Cause
[Why did it happen? What was missing?]

## Solution
[How did you fix it? Code, config, etc.]

## Prevention
[How do we prevent this happening again?]

## Lesson
[What should we remember for future projects?]

## Template Created
[If applicable, what template/checklist was created?]

## Related Files
[What other files were updated?]
```

**Example**:
```markdown
# Fix: Missing tailwind.config.js Causes Webpack Error

## Problem
Vercel build failed with:
Error: Generated code for /app/globals.css
Import trace for requested module: ./app/globals.css
> Build failed because of webpack errors

## Root Cause
globals.css uses @tailwind directives
but tailwind.config.js was missing

## Solution
Created tailwind.config.js with:
- Content paths (app/**, pages/**, components/**)
- Theme extend section
- Plugins array

## Prevention
- Add "Create tailwind.config.js" to project setup checklist
- Verify npm run build works locally before GitHub push
- Check webpack output for CSS loader errors

## Lesson
When using @tailwind CSS directives, ALWAYS create tailwind.config.js
or webpack CSS loader will fail during build

## Template Created
- BUILD_CHECKLIST.md (added "Create tailwind.config.js" step)
- NEXT_CONFIG_TEMPLATE.md (included tailwind.config.js)

## Related Files
- threshold-web/tailwind.config.js (created)
- MEMORY.md (updated with fix)
```

### Step 2: Update MEMORY.md
**Location**: `/home/clawdbot/.openclaw/workspace/MEMORY.md`

**Add to relevant section** (or create new):
```markdown
### [Fix Title] (Date)
**Problem**: [Brief description]
**Root Cause**: [Why it happened]
**Solution**: [How it was fixed]
**Prevention**: [How to avoid next time]
**See**: `.learnings/YYYY-MM-DD-description.md` for full details
```

### Step 3: Create/Update Templates
**Goal**: Make the problem impossible to repeat

**Examples**:
1. **BUILD_CHECKLIST.md** - Pre-deployment verification
   - Add step: "Create tailwind.config.js"
   - Add: "Verify npm run build locally"
   - Add: "Check webpack output for errors"

2. **NEXT_CONFIG_TEMPLATE.md** - Standard setup
   - Include tailwind.config.js example
   - Include postcss.config.js example
   - Include next.config.js example

3. **[TOPIC]_BEST_PRACTICES.md** - General lessons
   - Always X when Y
   - Never Z without A
   - Check B before deploying

### Step 4: Commit to Git

**Command**:
```bash
git add MEMORY.md .learnings/[file] [templates]
git commit -m "Fix: [what] because [why]

Root cause: [root cause]
Solution: [solution]
Prevention: [how to prevent]

See .learnings/[filename] for full details"
```

**Example**:
```bash
git add MEMORY.md .learnings/2026-03-11-missing-tailwind-config.md BUILD_CHECKLIST.md NEXT_CONFIG_TEMPLATE.md
git commit -m "Fix: Missing tailwind.config.js causes webpack error

Root cause: @tailwind CSS directives require tailwind.config.js
Solution: Create tailwind.config.js with content paths and theme
Prevention: Added to BUILD_CHECKLIST and NEXT_CONFIG_TEMPLATE

See .learnings/2026-03-11-missing-tailwind-config.md for details"
```

### Step 5: Update Behavior (If Pattern)
**When to do this**: If this is a recurring issue or changes how you work

**Update**:
- `SOUL.md` - If it's about who you are
- `AGENTS.md` - If it's about how you work
- `TOOLS.md` - If it's about tool configuration

**Example**:
```markdown
## Continuous Improvement

Every fix gets:
1. Logged to .learnings/YYYY-MM-DD-description.md
2. Added to MEMORY.md
3. Captured in a template/checklist
4. Committed to git
5. Used in next project

This prevents problems from recurring.
```

---

## The Improvement Cycle

```
WORK ON PROJECT
  ↓
ENCOUNTER PROBLEM
  ↓
FIX IT
  ↓
DOCUMENT SOLUTION (.learnings/)
  ↓
UPDATE MEMORY.MD
  ↓
CREATE/UPDATE TEMPLATE
  ↓
COMMIT TO GIT
  ↓
NEXT PROJECT HAS TEMPLATE
  ↓
PROBLEM PREVENTED ✓
```

---

## Examples of What Gets Logged

### 1. Build Errors
**Learn from**: Webpack errors, TypeScript errors, missing configs
**Template Created**: BUILD_CHECKLIST.md, [FRAMEWORK]_CONFIG_TEMPLATE.md

### 2. Configuration Issues
**Learn from**: Missing config files, wrong settings, environment variables
**Template Created**: [TOOL]_CONFIG.md, PROJECT_SETUP_CHECKLIST.md

### 3. Integration Issues
**Learn from**: API errors, authentication failures, permission issues
**Template Created**: [SERVICE]_SETUP_GUIDE.md, INTEGRATION_CHECKLIST.md

### 4. Performance Issues
**Learn from**: Slow builds, large bundle sizes, poor metrics
**Template Created**: PERFORMANCE_CHECKLIST.md, OPTIMIZATION_GUIDE.md

### 5. Deployment Issues
**Learn from**: Vercel errors, DNS issues, CORS problems
**Template Created**: DEPLOYMENT_CHECKLIST.md, [PLATFORM]_TROUBLESHOOTING.md

### 6. Data/Process Issues
**Learn from**: Tracking problems, workflow gaps, missing steps
**Template Created**: WORKFLOW_CHECKLIST.md, DATA_STRUCTURE.md

---

## Checklist: Did You Improve?

After every fix, ask yourself:

- [ ] Did I log the learning to `.learnings/`?
- [ ] Did I update `MEMORY.md`?
- [ ] Did I create/update a template or checklist?
- [ ] Did I commit to git?
- [ ] Did I update behavior files (SOUL.md, AGENTS.md)?
- [ ] Would this prevent the problem next time?
- [ ] Is this documented so future me can find it?

**If any are NO, finish them now before moving on.**

---

## Remember

**The goal is not to fix problems. The goal is to prevent them from happening again.**

Every lesson learned → Template created → Problem prevented.

That's how you scale a system. That's how you build something that works.

---

## Search for Learnings

To find what's been learned:

```bash
# List all learnings
ls -la .learnings/

# Search MEMORY.md for a topic
grep -i "tailwind\|webpack\|build" MEMORY.md

# Find learnings from a date
ls .learnings/ | grep "2026-03"

# Read a specific learning
cat .learnings/2026-03-11-missing-tailwind-config.md
```

---

## Never Forget

```
FIX → LOG → TEMPLATE → COMMIT → PREVENT

Every single time. No exceptions.
```

This is how you build from experience instead of repeating mistakes.

# Improvement System

**Build from experience, not luck. Learn once, prevent forever.**

---

## Core Principle

Every time something is fixed, improved, or learned:
1. **Document it** (so you remember)
2. **Create a template** (so it never breaks again)
3. **Commit it** (so it persists across sessions)
4. **Use it next time** (breaking the cycle of repeated mistakes)

---

## The System (Simple Version)

### When You Fix Something

1. **Create file**: `.learnings/YYYY-MM-DD-description.md`
   - What broke
   - Why it broke
   - How you fixed it
   - How to prevent it

2. **Update file**: `MEMORY.md`
   - Add the fix to long-term memory
   - Link to the learning file

3. **Create template**: `[TOPIC]_CHECKLIST.md` or `[TOPIC]_TEMPLATE.md`
   - Prevent this from happening again
   - Make it easy for next project

4. **Commit**: `git add ... && git commit -m "Fix: ..."`
   - Push to GitHub
   - Persist the improvement

### Next Time You Do Similar Work

- [ ] Check `.learnings/` for relevant experiences
- [ ] Check `MEMORY.md` for lessons
- [ ] Use the template (BUILD_CHECKLIST.md, etc.)
- [ ] Prevent the problem before it happens

---

## Structure

### `.learnings/` Directory
**Purpose**: Raw session learnings (what was fixed, why, how)

**Files**:
- `.learnings/2026-03-11-missing-tailwind-config.md`
- `.learnings/2026-03-12-stripe-api-integration.md`
- `.learnings/2026-03-13-vercel-deployment-timeouts.md`

**Size**: Keep under 1000 lines (one learning per file)

### `MEMORY.md`
**Purpose**: Curated long-term memory (important lessons, patterns, insights)

**Content**: 
- Critical fixes (organized by category)
- Key learnings
- Links to `.learnings/` files for details

**Size**: Growing over time (becomes the playbook)

### Checklists & Templates
**Purpose**: Prevent problems before they happen

**Examples**:
- `BUILD_CHECKLIST.md` - Before deployment
- `NEXT_CONFIG_TEMPLATE.md` - Project setup
- `API_INTEGRATION_CHECKLIST.md` - Before building integrations
- `GOOGLE_SHEETS_TEMPLATES.md` - Copy-paste structure

---

## Example: The Tailwind Webpack Error

### Session 1 (Problem Occurs)
```
You: "Vercel build failed with webpack error"
Me: "Found it - missing tailwind.config.js"
Me: Fixed it
```

### Step 1: Log the Learning
```
Created: .learnings/2026-03-11-missing-tailwind-config.md
Content: Problem, root cause, solution, prevention
```

### Step 2: Update MEMORY.md
```
Added: 
"### Build System Fix (Missing tailwind.config.js)
When using @tailwind in globals.css, must create tailwind.config.js
Solution: [details]
See .learnings/2026-03-11-missing-tailwind-config.md"
```

### Step 3: Create Template
```
Updated: BUILD_CHECKLIST.md
Added: "□ Create tailwind.config.js (if using Tailwind)"
Added: "□ Run npm run build locally before pushing"
```

### Step 4: Commit
```bash
git commit -m "Fix: Missing tailwind.config.js causes webpack error

Root cause: @tailwind CSS needs tailwind.config.js
Prevention: Added to BUILD_CHECKLIST
See .learnings/2026-03-11-missing-tailwind-config.md"
```

### Session 2 (Same Project Type)
```
You: "Creating new Next.js + Tailwind project"
Me: Check MEMORY.md → Finds tailwind lesson
Me: Check BUILD_CHECKLIST.md → Has step for tailwind.config.js
Result: ✅ Tailwind configured correctly from the start
        ✅ No webpack error
        ✅ Problem prevented
```

---

## Why This Works

### Without System
```
Project 1: Webpack error (tailwind config)
  → Fix it manually
  → Move on, forget
Project 2: Webpack error (same issue)
  → Fix it manually again
  → Move on, forget
Project 3: Same error again
  → Frustration!
```

### With System
```
Project 1: Webpack error (tailwind config)
  → Fix it
  → Log it (.learnings/)
  → Create template (BUILD_CHECKLIST.md)
  → Commit to git
Project 2: Check template first
  → Have tailwind.config.js from start
  → Zero webpack errors
  → ✅ Problem prevented
Project 3+: Always use template
  → Never see this error again
```

---

## How to Use This System

### Daily/During Work
1. Encounter a problem
2. Fix it
3. **Before moving on**: Log it (5 min)
4. **Create template** (5 min)
5. **Commit** (1 min)
6. **Total**: 11 minutes to prevent future problems

### At Start of New Session
1. Read `MEMORY.md` - What have I learned?
2. Check `.learnings/` - Details on past fixes
3. Review relevant templates - Use them!
4. Prevent problems before they happen

### At End of Project
1. Review all `.learnings/` from this session
2. Update `MEMORY.md` with key insights
3. Consolidate templates
4. Commit everything
5. Knowledge persists for next project

---

## Files to Know

### Entry Points
- **MEMORY.md** - Start here (summary of all learning)
- **CONTINUOUS_IMPROVEMENT_PROCESS.md** - How to log learning
- **IMPROVEMENT_SYSTEM.md** - This file (overview)

### References
- **BUILD_CHECKLIST.md** - Before any deployment
- **[TOPIC]_BEST_PRACTICES.md** - General wisdom
- **[TOPIC]_TEMPLATE.md** - Copy-paste examples
- **[TOPIC]_TROUBLESHOOTING.md** - Common issues

### Raw Learning
- **.learnings/** - Dated session logs
- **SOUL.md** - Core behavior principles
- **AGENTS.md** - How system works

---

## Golden Rules

### Rule 1: Log Everything
Don't think "I'll remember this." You won't.
→ Create `.learnings/` file (5 minutes)

### Rule 2: Create Templates
Don't think "I'll fix it manually next time." You won't.
→ Create checklist/template (5 minutes)

### Rule 3: Commit to Git
Don't think "I'll do it later." You won't.
→ Push to GitHub immediately (1 minute)

### Rule 4: Update MEMORY.md
Don't let learnings stay scattered in `.learnings/`.
→ Curate important ones to MEMORY.md (weekly)

### Rule 5: Use Templates
Don't ignore checklists next time.
→ Read them before starting new projects

---

## Metrics

### Success = Prevention
- Session 1: Fix problem (cost: time + effort)
- Session 2+: Prevent problem (cost: zero)
- **ROI**: Invest 15 min → Save hours in future

### Track These
- **Problems fixed**: Count by category
- **Templates created**: How many prevent future issues?
- **Time saved**: How much faster are new projects?
- **Repeated mistakes**: Zero is the goal

---

## Tools You Use

### For Logging
- `.learnings/YYYY-MM-DD-description.md` - Raw learning

### For Curation
- `MEMORY.md` - Important patterns
- `SOUL.md` - Core principles
- `AGENTS.md` - System behavior

### For Prevention
- `BUILD_CHECKLIST.md` - Pre-deployment
- `[TOPIC]_BEST_PRACTICES.md` - General wisdom
- `[TOPIC]_TEMPLATE.md` - Copy-paste

### For Persistence
- `git commit` - Push to GitHub
- `GitHub` - Permanent record

---

## Remember

**You are building institutional memory.**

Every fix you document becomes a lesson.
Every template you create prevents a future problem.
Every commit you make persists across sessions.

That's how you scale from reactive (fixing) to proactive (preventing).

---

## Start Now

When you fix your next thing:

1. **Log it** (5 min) → `.learnings/YYYY-MM-DD-description.md`
2. **Update** (2 min) → `MEMORY.md`
3. **Template** (5 min) → `[TOPIC]_CHECKLIST.md`
4. **Commit** (1 min) → `git commit`

**Total time: 13 minutes to prevent future problems forever.**

---

See `CONTINUOUS_IMPROVEMENT_PROCESS.md` for detailed steps.

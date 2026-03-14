# Claude Web Development Skill - Build Websites with AI

**Goal**: Create an OpenClaw skill that leverages Claude (21st dev/Claude Code) to build professional websites using AI-assisted development.

**Status**: Ready for implementation

---

## Skill Overview

### Name
`claude-webdev`

### Description
Build professional websites using Claude AI with Next.js 14, TypeScript, Tailwind CSS, and Framer Motion. Integrate design references from Instagram reels. Deploy to Vercel automatically.

### Use Cases
1. **Website Builder**: Generate full websites from descriptions
2. **Design Integration**: Use DESIGN_REFERENCES.md patterns automatically
3. **Code Generation**: AI-powered component creation
4. **Quality Assurance**: Automated Lighthouse scoring (95+ target)
5. **Deployment**: One-command deploy to Vercel
6. **Batch Building**: Build multiple websites in parallel

---

## Technical Architecture

### Core Dependencies
```
anthropic>=0.25.0          # Claude AI API
playwright>=1.40.0         # Browser automation
next-js-client>=0.0.0      # Next.js integration (simulated)
vercel-cli>=33.0.0         # Deployment
requests>=2.31.0           # HTTP requests
python-dotenv>=1.0.0       # Config
```

### Recommended Tech Stack
- **Language**: Python (for skill) + TypeScript (for generated code)
- **Framework**: Next.js 14 (App Router, Server Components)
- **Styling**: Tailwind CSS (utility-first)
- **Animations**: Framer Motion (professional UI)
- **Database**: (Optional) Firebase/Supabase
- **Deployment**: Vercel (auto-deploy from GitHub)
- **Design Input**: DESIGN_REFERENCES.md (Instagram patterns)

---

## Skill Commands

### 1. `generate_website`
**Purpose**: Generate a complete website from a brief description

**Input**:
```python
{
  "business_name": "Summer Street Hair Studio",
  "business_type": "Salon",
  "description": "Professional hair salon in downtown Boston",
  "design_style": "modern",
  "include_design_patterns": True,  # Use DESIGN_REFERENCES.md
  "pages": ["home", "services", "gallery", "booking", "about"],
  "color_scheme": "amber",  # Or custom
  "features": ["booking", "gallery", "reviews"],
  "github_username": "AEnldlya",
  "auto_deploy": True
}
```

**Output**:
```json
{
  "success": true,
  "website_id": "summer-street-hair-2026",
  "project_path": "/workspace/summer-street-hair/",
  "github_url": "https://github.com/AEnldlya/summer-street-hair",
  "vercel_url": "https://summer-street-hair.vercel.app",
  "pages_generated": 5,
  "components_created": 23,
  "build_time_seconds": 180,
  "lighthouse_score": 96,
  "wcag_compliance": "AA",
  "status": "DEPLOYED"
}
```

---

### 2. `generate_from_design_references`
**Purpose**: Build website using patterns from DESIGN_REFERENCES.md

**Input**:
```python
{
  "business_name": "Modern Coffee Shop",
  "business_type": "Cafe",
  "design_references_tags": ["fade-in", "glassmorphism", "micro-interactions"],
  "use_instagram_patterns": True,
  "custom_description": "Trendy coffee shop with modern design"
}
```

**Output**:
```json
{
  "success": true,
  "patterns_used": [
    "fade-in animation",
    "glassmorphism cards",
    "micro-interactions"
  ],
  "components_enhanced": [
    "hero section with fade-in",
    "glass effect cards",
    "button micro-interactions"
  ]
}
```

---

### 3. `generate_pages`
**Purpose**: Generate specific pages for a website

**Input**:
```python
{
  "website_id": "summer-street-hair-2026",
  "pages": ["services", "gallery", "testimonials"],
  "template": "salon",  # Or custom
  "include_cms": True  # Headless CMS integration
}
```

**Output**:
```json
{
  "success": true,
  "pages_created": [
    { "name": "services", "path": "app/pages/services.tsx", "status": "ready" },
    { "name": "gallery", "path": "app/pages/gallery.tsx", "status": "ready" },
    { "name": "testimonials", "path": "app/pages/testimonials.tsx", "status": "ready" }
  ]
}
```

---

### 4. `add_features`
**Purpose**: Add specific features to existing website

**Input**:
```python
{
  "website_id": "summer-street-hair-2026",
  "features": [
    "appointment_booking",
    "testimonial_section",
    "instagram_feed",
    "payment_integration"
  ]
}
```

**Output**:
```json
{
  "success": true,
  "features_added": 4,
  "new_components": 12,
  "integration_status": {
    "appointment_booking": "stripe + calendar",
    "testimonial_section": "dynamic comments",
    "instagram_feed": "API feed",
    "payment_integration": "stripe connected"
  }
}
```

---

### 5. `optimize_lighthouse`
**Purpose**: Optimize website for Lighthouse score 95+

**Input**:
```python
{
  "website_id": "summer-street-hair-2026",
  "target_score": 95,
  "focus_areas": ["performance", "accessibility", "seo"]
}
```

**Output**:
```json
{
  "success": true,
  "lighthouse_score_before": 87,
  "lighthouse_score_after": 96,
  "optimizations_applied": [
    "Image optimization (WebP/AVIF)",
    "Code splitting",
    "Lazy loading components",
    "WCAG AA compliance fixes",
    "SEO structured data"
  ],
  "core_web_vitals": {
    "LCP": "1.8s",
    "FID": "45ms",
    "CLS": "0.08"
  }
}
```

---

### 6. `deploy_website`
**Purpose**: Deploy website to Vercel

**Input**:
```python
{
  "website_id": "summer-street-hair-2026",
  "domain": "summer-street-hair.com",  # Or Vercel domain
  "environment": "production",
  "auto_deploy_future": True  # Auto-deploy on GitHub push
}
```

**Output**:
```json
{
  "success": true,
  "deployment_time": 45,
  "url": "https://summer-street-hair.vercel.app",
  "custom_domain": "summer-street-hair.com",
  "ssl_certificate": "active",
  "ci_cd": "configured"
}
```

---

### 7. `batch_build_websites`
**Purpose**: Build multiple websites in parallel

**Input**:
```python
{
  "websites": [
    {
      "business_name": "Hair Salon A",
      "business_type": "Salon"
    },
    {
      "business_name": "Restaurant B",
      "business_type": "Restaurant"
    },
    {
      "business_name": "Plumbing C",
      "business_type": "Services"
    }
  ],
  "max_parallel": 3,
  "auto_deploy_all": True
}
```

**Output**:
```json
{
  "success": true,
  "total_websites": 3,
  "completed": 3,
  "failed": 0,
  "total_time_seconds": 420,
  "websites_deployed": 3,
  "urls": [
    "https://hair-salon-a.vercel.app",
    "https://restaurant-b.vercel.app",
    "https://plumbing-c.vercel.app"
  ]
}
```

---

## Implementation Strategy

### Phase 1: Core Website Generation
1. **Claude Prompt Engineering**
   - Create comprehensive prompts for each page type
   - Include design system specifications
   - Reference DESIGN_REFERENCES.md patterns
   - Specify Next.js 14 + TypeScript conventions

2. **Project Scaffolding**
   - Create Next.js 14 project structure
   - Setup Tailwind CSS + Framer Motion
   - Configure TypeScript
   - Create component library

3. **Code Generation**
   - Use Claude to generate page components
   - Generate layout components
   - Generate utility functions
   - Generate API routes if needed

### Phase 2: Design Integration
1. **DESIGN_REFERENCES Parser**
   - Read DESIGN_REFERENCES.md
   - Extract patterns (animations, colors, techniques)
   - Map to generated components

2. **Auto-Enhancement**
   - Add fade-in animations from references
   - Apply color schemes
   - Include micro-interactions
   - Enhance UI elements

### Phase 3: Quality Assurance
1. **Lighthouse Scoring**
   - Build and test locally
   - Run Lighthouse audit
   - Auto-optimize if below 95
   - Generate performance report

2. **Accessibility (WCAG AA)**
   - Check semantic HTML
   - Verify color contrast
   - Test keyboard navigation
   - Validate ARIA labels

### Phase 4: Deployment
1. **GitHub Integration**
   - Create GitHub repo
   - Push code automatically
   - Configure CI/CD

2. **Vercel Deployment**
   - Deploy to Vercel
   - Setup auto-deploys
   - Configure custom domain
   - Enable SSL

---

## File Structure

```
~/.openclaw/workspace/skills/claude-webdev/
├── SKILL.md                          # Skill metadata
├── README.md                         # User guide
├── claude_webdev.py                  # Main CLI
├── src/
│   ├── __init__.py
│   ├── claude_prompts.py             # Claude prompt templates
│   ├── project_scaffolder.py         # Create Next.js structure
│   ├── code_generator.py             # Generate components
│   ├── design_integrator.py          # Apply design patterns
│   ├── lighthouse_optimizer.py       # Optimize for 95+ score
│   ├── github_manager.py             # GitHub integration
│   ├── vercel_deployer.py            # Deploy to Vercel
│   ├── batch_builder.py              # Parallel website building
│   └── quality_checker.py            # QA and validation
├── templates/
│   ├── nextjs_14_template/           # Next.js 14 base
│   ├── salon_template.py             # Salon industry template
│   ├── restaurant_template.py        # Restaurant template
│   ├── services_template.py          # Service business template
│   └── ecommerce_template.py         # E-commerce template
├── references/
│   ├── claude-api-guide.md           # Claude API usage
│   ├── nextjs-14-guide.md            # Next.js 14 best practices
│   ├── tailwind-design-system.md     # Design system
│   ├── lighthouse-optimization.md    # Performance tips
│   └── vercel-deployment.md          # Vercel guide
├── examples/
│   ├── example_generate_website.py   # Single website example
│   ├── example_batch_build.py        # Batch build example
│   └── example_with_design_refs.py   # Using design references
├── test_claude_webdev.py             # 30+ unit tests
├── requirements.txt
└── .env.example
```

---

## Core Modules

### claude_prompts.py (15 KB)
Comprehensive prompt templates for:
- Hero section generation
- Services page layout
- Gallery components
- Booking system
- Contact forms
- About page
- Testimonials section
- Navigation/header
- Footer
- Custom pages

**Key Features**:
- Parameterized prompts
- Design pattern injection
- WCAG compliance requirements
- Lighthouse optimization tips
- Mobile-first approach
- Framer Motion animation directives

### project_scaffolder.py (12 KB)
Create Next.js 14 project structure:
- Initialize npm/yarn project
- Setup Tailwind CSS
- Configure TypeScript
- Create folder structure
- Generate package.json
- Setup environment variables
- Create GitHub repo structure

### code_generator.py (16 KB)
Use Claude to generate code:
- Call Claude API with prompts
- Parse generated code
- Validate TypeScript
- Create component files
- Generate page files
- Create layout components
- Add proper exports

### design_integrator.py (12 KB)
Integrate DESIGN_REFERENCES patterns:
- Parse DESIGN_REFERENCES.md
- Extract animation patterns
- Extract color schemes
- Extract UI element styles
- Map to generated components
- Auto-apply enhancements
- Validate integration

### lighthouse_optimizer.py (14 KB)
Optimize for 95+ Lighthouse score:
- Build project
- Run Lighthouse audit
- Identify bottlenecks
- Auto-optimize images (WebP/AVIF)
- Implement code splitting
- Add lazy loading
- Optimize fonts
- Improve Core Web Vitals

### github_manager.py (10 KB)
GitHub integration:
- Create repository
- Initialize git
- Create commit history
- Push to GitHub
- Configure branch protection
- Setup GitHub Actions

### vercel_deployer.py (11 KB)
Deploy to Vercel:
- Create Vercel project
- Connect GitHub repo
- Deploy production build
- Setup custom domain
- Configure environment variables
- Enable auto-deploy
- Monitor deployment

### batch_builder.py (13 KB)
Build multiple websites in parallel:
- Queue management
- Concurrent building (max 3-5)
- Progress tracking
- Error handling
- Batch reporting
- Aggregate statistics

---

## Prompt Templates (Examples)

### Hero Section Prompt
```
Create a professional hero section for a ${BUSINESS_TYPE} website.
Business: ${BUSINESS_NAME}
Description: ${BUSINESS_DESCRIPTION}

Requirements:
- Next.js 14 + TypeScript
- Tailwind CSS styling
- Framer Motion animations: ${ANIMATION_PATTERNS}
- Colors: ${COLOR_SCHEME}
- Responsive (mobile-first)
- WCAG AA accessibility
- Lighthouse optimized

Component structure:
- Hero wrapper with gradient background
- Headline text (bold, large)
- Subheading text (secondary color)
- CTA button with hover effects
- Optional: hero image or video background

Design patterns to use:
${DESIGN_REFERENCES_PATTERNS}

Output: Generate complete TSX component with all styles.
```

### Services Page Prompt
```
Create a services listing page for a ${BUSINESS_TYPE} website.
Services: ${SERVICES_LIST}

Requirements:
- Card-based layout
- 2-3 columns responsive grid
- Glassmorphism effects (from DESIGN_REFERENCES)
- Hover interactions
- Price/details display
- CTA buttons

Output: Complete TSX component ready to use.
```

---

## Usage Examples

### Python API
```python
from claude_webdev import ClaudeWebdevSkill

skill = ClaudeWebdevSkill()

# Generate a website
result = await skill.generate_website(
    business_name="Summer Street Hair Studio",
    business_type="Salon",
    pages=["home", "services", "gallery", "booking"],
    include_design_patterns=True,
    auto_deploy=True
)

print(f"Website deployed to: {result['vercel_url']}")
```

### CLI Commands
```bash
# Generate single website
python claude_webdev.py generate-website \
  --name "Summer Street Hair" \
  --type "Salon" \
  --pages home,services,gallery \
  --deploy

# Batch build 3 websites
python claude_webdev.py batch-build \
  --config websites.json \
  --parallel 3 \
  --deploy-all

# Optimize lighthouse score
python claude_webdev.py optimize-lighthouse \
  --website-id summer-street-hair \
  --target 95
```

---

## Integration with OpenClaw

### With Stock Watcher
- Build website when stock pick hits target
- Celebrate wins with new website launch
- Automate customer acquisition

### With Instagram Reels Skill
- Auto-import design patterns
- Build with trendy techniques
- Keep designs fresh

### With CPA Agent
- Log website creation cost ($0, auto-generated)
- Track revenue ($2,500 per site)
- Calculate profit metrics

### With JEwed Prospect Finder
- Auto-build website for prospects
- Deploy immediately
- Increase closure rate

---

## Quality Standards

✅ **Code Quality**:
- TypeScript strict mode
- Full type hints
- Proper error handling
- Logging throughout
- 30+ unit tests

✅ **Design Quality**:
- Lighthouse 95+ target
- WCAG AA compliance
- Mobile-first responsive
- Core Web Vitals optimized
- SEO best practices

✅ **User Experience**:
- Fast load times (<2.5s LCP)
- Smooth animations
- Clear CTAs
- Professional design
- Accessibility first

✅ **Development**:
- GitHub version control
- CI/CD auto-deploy
- Environment management
- Database-ready (optional)
- Scalable architecture

---

## Success Criteria

✅ Can generate complete website from description
✅ Can build website with 5+ pages
✅ Integrates design patterns from DESIGN_REFERENCES.md
✅ Achieves Lighthouse 95+ score automatically
✅ Meets WCAG AA accessibility standards
✅ Deploys to Vercel with auto-deploy enabled
✅ Creates GitHub repository automatically
✅ Batch builds multiple websites in parallel
✅ Includes responsive mobile design
✅ Includes professional animations (Framer Motion)
✅ Production-ready code quality
✅ Full documentation and examples

---

## Technology Stack

**Backend**:
- Python 3.8+
- Claude API (anthropic)
- Playwright (automation)
- Requests (HTTP)

**Generated Code**:
- Node.js 18+
- Next.js 14
- TypeScript
- Tailwind CSS
- Framer Motion
- React 18

**Deployment**:
- GitHub (version control)
- Vercel (hosting)
- GitHub Actions (CI/CD)

---

## Next Steps for Implementation

1. **Phase 1**: Build prompt engineering system (claude_prompts.py)
2. **Phase 2**: Create project scaffolding (project_scaffolder.py)
3. **Phase 3**: Implement code generation (code_generator.py)
4. **Phase 4**: Add design integration (design_integrator.py)
5. **Phase 5**: Build QA system (lighthouse_optimizer.py)
6. **Phase 6**: Deploy automation (vercel_deployer.py)
7. **Phase 7**: Batch processing (batch_builder.py)
8. **Phase 8**: Testing & documentation

---

## Timeline

- **MVP (Phase 1-3)**: 2-3 weeks
  - Generate basic websites
  - Deploy to Vercel
  - Functional but simple

- **Production (Phase 1-6)**: 4-6 weeks
  - Full feature set
  - Design integration
  - Lighthouse optimization
  - Batch building

- **Enterprise (Phase 1-8)**: 6-8 weeks
  - Complete testing
  - Advanced features
  - Documentation
  - Performance tuning

---

**Ready for implementation!** This skill will enable building professional websites at scale using Claude AI. 🚀

Follow this prompt to create the `claude-webdev` skill and integrate it with your existing agents.

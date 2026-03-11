# Long-Term Memory - Website Agency System

## Mission (Set Feb 2026)
Build and sell professional websites to local businesses without web presence.
- **Revenue model**: $500 per site (3-day build) + $40/month maintenance
- **Target**: 3-5 closed deals/month = $1.5K-$2.5K monthly + $120-200 recurring
- **Year 1 goal**: 20-30 sites built ($10K-$15K) + 10-20 maintenance customers ($400-800/month)

## Core Strategy
1. **Trust-building sales model**: Deploy to temp Netlify URL first → customer reviews → pays $500 → deploy to permanent domain. Avoids hosting costs if customer doesn't pay.
2. **Personalized outreach**: Real Boston businesses (not templates) with Google review references, no phone numbers in email body
3. **Automation-first ops**: Email scheduling, deployment scripting, tracking spreadsheets eliminate manual work
4. **Pure HTML/CSS/JS tech stack**: No frameworks (faster to build, deploy to free Netlify, requires less infrastructure)

## What Doesn't Work
- Generic email templates (low response rate; need personal business context)
- Phone-first outreach (email-only until trust established, avoids filter flags)
- Manual deployments (use API automation for temp/permanent/delete)
- Manual email pacing (5-minute delays between sends to avoid Gmail spam filtering)

## Critical Lessons Learned
- **Web search > Selenium**: Gemini web_search provides verified business data without rendering. Successfully found 30+ Boston businesses with real contact emails.
- **Netlify API automation**: Temp deployments with Site IDs enable instant website launch + instant deletion if payment fails (zero hosting cost risk)
- **Airtable CRM over spreadsheets**: 17 custom fields, 5 views, daily workflow automation better than CSV tracking
- **PayPal payment links**: Simple customer checkout, no credit card storage headaches
- **5-minute email delays**: Completely avoids Gmail spam detection (72 seconds was too aggressive; 5 min looks like real person)

## Key Files & Locations
- **Automation**: `schedule_daily_sends.py`, `send_outreach.py`, `deploy_website.py`
- **Data**: `boston_businesses_final.json` (30 verified businesses), `deployments_log.json`, outreach_tracker.csv
- **Documentation**: 11+ playbooks (SALES_PLAYBOOK.md, BUILD_CHECKLIST.md, DEPLOY_THEN_PAY_WORKFLOW.md, etc.)
- **Credentials**: `.gmail_credentials.json`, `.netlify_token` (stored securely in workspace root)

## Contact & Payment
- **Andy Zhang**: 603-306-7508, Andy.li.zhang2010@gmail.com
- **PayPal**: $500 website link + $40/month maintenance link (ready for sharing with customers)

## Current Phase (March 8, 2026)
✅ **HapLink website**: Multi-page redesign COMPLETE (8 pages, real images, professional design, animations)
✅ **Boston Campaign v1 (Email)**: System fully automated, 167 verified prospects loaded, duplicate prevention active, city rotation configured, daily 7 AM reports active. **CSV parsing bug FIXED**. Awaiting user approval of email template example before first 50-email batch.
✅ **Boston Campaign v2 (Selenium Forms)**: Contact form automation working, 20+ restaurants submitted so far, 0 replies yet. Continuing systematic waves toward 100+ target.
🆕 **AI Translation App Project**: Planning phase started (split-screen phone app for real-time speech translation, two-person conversation model)

## Lessons for Scaling
- One email per prospect (never duplicate sends)
- Build templates for emails/websites by industry type (plumber, salon, restaurant, electrician, HVAC, etc.) to speed up personalization
- Track response rate by industry (plumbers/trades = 30-40% conversion; salons/restaurants = 20-30%)
- Implement daily email sends (50 emails/day, 5-min delays) once initial campaign validates market
- Hire VA to handle website photo collection + initial customer calls at $2K/month (frees Andy for sales/strategy)

## New Project: AI Translation App (March 2026)
**Goal**: Design and build a phone-based real-time speech translation app
**Unique Feature**: Split-screen interface where two people hold phone horizontally; each person sees their language normally, other language appears upside-down
**Status**: Planning/design phase only (website work deferred for later)
**Next Steps**: MVP planning, tech architecture, UI/UX design for split-screen, real-time sync strategy, implementation roadmap
**Use Case**: Two-person conversation with phone between them; speech recognized on each side, translated, and displayed in split screen

---

## 🔄 MAJOR BUSINESS MODEL PIVOT (March 10, 2026)

**Old Model** (Feb 2026): $500 per 3-day build, email campaigns, Netlify hosting, HTML/CSS/JS
**New Model** (March 2026): $2,500 per 10-day build, phone outreach, Vercel deployment, professional Next.js stack

### Why the Pivot?
- Email campaigns had low response rates (automating didn't increase quality)
- $500 pricing attracted price-conscious buyers, not serious businesses
- Need for professional positioning & sustainable margins
- Opportunity to leverage higher-value service model with quality differentiation

### New Revenue Model
- **Base price**: $2,500 per website (5x higher)
- **Build timeline**: 10 days (vs 3 days) → allows professional quality
- **Add-ons**: E-commerce (+$1,500-2,000), admin dashboard (+$500)
- **Monthly maintenance**: $100/month recurring (instead of $40)
- **Year 1 target**: $74K+ annual (20 initial builds × $2,500 + 10-20 maintenance clients @ $100/mo)
- **Per-client LTV**: $2,500 + ($100 × 36 months) = $6,100

### New Technology Stack
- **Framework**: Next.js 14 (App Router, Server Components)
- **Language**: TypeScript (strict mode for reliability)
- **Styling**: Tailwind CSS (utility-first, responsive)
- **Animations**: Framer Motion (professional UI/UX)
- **Deployment**: Vercel (git-based, auto-deploy, serverless)
- **Version control**: GitHub (AEnldlya account, source of truth)
- **Analytics target**: Lighthouse 95+, WCAG AA, Core Web Vitals <2.5s LCP

### Example Website: Summer Street Hair Studio
- **Status**: Production-ready (Next.js 14, TypeScript, Tailwind, Framer Motion)
- **Location**: `/home/clawdbot/.openclaw/workspace/example-salon/`
- **GitHub**: https://github.com/AEnldlya/summer-street-salon
- **Deployment**: Vercel (pending live confirmation)
- **Recent enhancements**: Professional color scheme (amber/cream), fade animations, booking page, gallery page
- **Config format**: CommonJS (module.exports) for Next.js 14 compatibility
- **Verification**: Local build tested (132 kB First Load JS, routes generated)

### 6-Point Business Verification System
**Purpose**: Identify ONLY businesses with NO existing websites (high-relevance targeting)
**Rules** (in VERIFICATION_RULES.md):
1. Google Search: `"[Business Name] [City] website"` → must NOT find website
2. Google Business Profile: Check GBP → must NOT have website link
3. Facebook Page: Check About → must NOT have website link
4. Instagram Profile: Check bio → must NOT have link
5. Direct domain check: Try .com, .net, [name]boston.com, [name][city].com → must NOT load
6. Yelp: Search Yelp → must NOT have website link

**Critical**: REJECT if ANY check finds a website. One email per prospect maximum.

### Daily Workflow (7 AM Start)
1. **Morning verification**: Find 20-30 Boston businesses (any service type)
2. **Run checklist**: Verify each against 6-point system
3. **Send to user**: Only NO-website businesses (max 15/day)
4. **User's task**: Make 15 phone calls/day with sales script from CONVERSION_PSYCHOLOGY_GUIDE.md
5. **Expected pipeline**: 10-15 interested → 4-6 closed deals/week → $2K-3K/week when full

### 10-Day Build Timeline (When First YES Comes)
- **Days 1-2**: Discovery call + Figma mockup (client approval required before proceeding)
- **Days 3-5**: Development (Next.js components, Tailwind styling, Framer Motion animations, image optimization)
- **Days 6-7**: Refinement (Lighthouse 95+, WCAG AA accessibility audit, SEO review)
- **Days 8-9**: Staging deployment + client review + revisions
- **Day 10**: Final QA + production launch + Google Business integration

### Learning Sprint Completed (57K+ Words)
✅ Mastered professional web development through intensive learning:
- **PROFESSIONAL_WEBDEV_LEARNING.md** (13.5K): Next.js 14, TypeScript, Tailwind CSS fundamentals
- **ADVANCED_WEBDEV_MASTERY.md** (16.6K): Performance optimization, animations, accessibility, Core Web Vitals
- **INDUSTRY_SPECIFIC_TEMPLATES.md** (14.3K): Salon, restaurant, plumbing industry templates
- **CONVERSION_PSYCHOLOGY_GUIDE.md** (13.3K): Sales psychology, CTAs, persuasion techniques, phone scripts

### Key Strategic Insights
- **Quality over automation**: Professional positioning justifies premium pricing
- **Human touch matters**: User phone calls (15/day) more effective than automated email
- **Verification prevents waste**: 6-point checklist = high-relevance prospect targeting
- **Template approach scales**: Salon template customizable for all industries
- **Recurring revenue**: $100/month maintenance provides stable cash base
- **GitHub source of truth**: Version control + client collaboration on single platform

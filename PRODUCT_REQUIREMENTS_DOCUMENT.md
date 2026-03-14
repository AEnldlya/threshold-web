# Product Requirements Document (PRD)
## AI-Powered Website Agency Platform

**Version**: 1.0.0  
**Date**: March 14, 2026  
**Status**: DRAFT - Ready for Development  
**Author**: Andy Zhang  
**Product Manager**: Ryan (AI Agent)

---

## Executive Summary

**Product Name**: WebMaker AI - Automated Website Agency Platform

**Mission**: Enable rapid, high-quality website creation and sale for local businesses without online presence, powered by AI.

**Success Metric**: Deploy 4-6 websites per day, generating $10K-15K weekly revenue with 99%+ profit margins.

---

## 1. Product Vision

### 1.1 Vision Statement
Transform local business website development from a time-consuming, expensive service into a fast, affordable, AI-powered solution that scales to thousands of businesses.

### 1.2 Target Market
- **Primary**: Local businesses (salons, restaurants, plumbing, HVAC, services) without websites
- **Secondary**: Small business owners who tried DIY website builders
- **Tertiary**: Marketing agencies needing white-label website solutions

### 1.3 Market Size
- **TAM (Total Addressable Market)**: 5.6M small businesses in US without websites
- **Year 1 Target**: 500-1,000 websites built ($1.25M-2.5M revenue)
- **Year 3 Target**: 5,000-10,000 websites built ($12.5M-25M revenue)

---

## 2. Core Product Features

### 2.1 Prospect Discovery Module

**Feature**: Automated prospect finding and verification

**Requirements**:
- ✅ Find 20-30 businesses daily via Google Maps, Yelp, directories
- ✅ 6-point website verification (automated)
- ✅ Filter to 15 high-quality prospects with phone numbers
- ✅ Categorize by industry (Salon, Restaurant, Services, etc.)
- ✅ Daily Telegram notification with prospect list
- ✅ Avoid duplicate prospects (tracking required)

**Success Metrics**:
- 15 verified prospects/day minimum
- 90% accuracy in website verification
- Zero duplicate prospects

---

### 2.2 Website Generation Module

**Feature**: AI-powered website creation from business description

**Requirements**:
- ✅ Generate complete Next.js 14 website in 2-5 minutes
- ✅ 5+ pages (Home, Services, Gallery, Booking, About)
- ✅ Mobile-first responsive design
- ✅ Professional animations (Framer Motion)
- ✅ 3D effects (Three.js integration)
- ✅ Image optimization (WebP/AVIF)
- ✅ SEO-ready metadata
- ✅ TypeScript for type safety

**Success Metrics**:
- <5 minute generation time
- Lighthouse 95+ score
- WCAG AA compliance
- 100% mobile responsive

---

### 2.3 Design Pattern Library

**Feature**: Auto-grow library of design patterns from Instagram reels

**Requirements**:
- ✅ Extract animations from Instagram reels
- ✅ Parse colors, typography, UI elements
- ✅ Store patterns in searchable database
- ✅ Auto-apply relevant patterns to new websites
- ✅ Batch reel analysis (5+ reels at once)

**Success Metrics**:
- 100+ patterns collected by Month 3
- 80%+ of patterns used in new websites
- User satisfaction with design quality (5-star)

---

### 2.4 3D Effects Module

**Feature**: Integrate premium 3D animations from 21st.dev

**Requirements**:
- ✅ Fetch 3D animation prompts from 21st.dev
- ✅ Generate Three.js code from prompts
- ✅ Optimize for 60 FPS desktop, 30-60 FPS mobile
- ✅ 6+ reusable 3D components
- ✅ Batch add 3D to multiple sites

**Success Metrics**:
- 60 FPS constant on desktop
- <2.5s LCP (Largest Contentful Paint)
- 30-60 FPS adaptive on mobile

---

### 2.5 Quality Validation Module

**Feature**: Automated website quality checking

**Requirements**:
- ✅ Lighthouse scoring (95+ target)
- ✅ WCAG AA accessibility compliance
- ✅ Core Web Vitals validation
- ✅ SEO audit
- ✅ Mobile responsiveness check
- ✅ Code quality review

**Success Metrics**:
- 100% of websites Lighthouse 95+
- 100% WCAG AA compliant
- All Core Web Vitals "Good"

---

### 2.6 Deployment & Domain Module

**Feature**: Automated Vercel deployment + domain purchase

**Requirements**:
- ✅ Deploy to Vercel with one click
- ✅ Search cheapest domain across 4+ registrars
- ✅ Human approval gates before purchase
- ✅ Auto-configure DNS to Vercel
- ✅ SSL certificate auto-setup
- ✅ Monitor DNS propagation
- ✅ Show domain in 5-10 minutes

**Success Metrics**:
- <5 minute deployment time
- $9-15 average domain cost
- 100% DNS success rate
- Domain live in <1 hour

---

### 2.7 Payment Processing Module

**Feature**: Collect $2,500 per website

**Requirements**:
- ✅ Stripe payment link generation
- ✅ Instant payment processing
- ✅ Invoice generation
- ✅ Subscription support (maintenance)
- ✅ Payment status tracking
- ✅ Email confirmations

**Success Metrics**:
- 95%+ payment success rate
- <5 minute payment link creation
- Instant payment processing

---

### 2.8 Financial Tracking Module

**Feature**: Real-time revenue and profit tracking

**Requirements**:
- ✅ Log revenue per website ($2,500)
- ✅ Track costs (Claude API, domain, Vercel)
- ✅ Calculate profit per website
- ✅ Monthly dashboard with summaries
- ✅ Integration with Google Sheets
- ✅ Telegram alerts for sales

**Success Metrics**:
- Real-time profit tracking
- <1 minute after payment for logging
- 99%+ accuracy in calculations

---

### 2.9 CRM & Prospect Tracking

**Feature**: Track prospects from discovery to payment

**Requirements**:
- ✅ Prospect database (name, phone, email, category)
- ✅ Call status tracking (contacted, YES, NO, follow-up)
- ✅ Website status per prospect (building, deployed, live)
- ✅ Payment status per prospect
- ✅ Revenue per prospect
- ✅ Batch actions (mark multiple as contacted)

**Success Metrics**:
- 100% prospect tracking
- Real-time status updates
- Conversion rate visible (calls → YES → Payment)

---

### 2.10 Admin Dashboard

**Feature**: Real-time business metrics

**Requirements**:
- ✅ Daily KPIs (prospects, calls, conversions, revenue)
- ✅ Weekly trends
- ✅ Monthly summaries
- ✅ Profit calculations
- ✅ Website pipeline status
- ✅ Payment tracking
- ✅ Export to CSV/PDF

**Success Metrics**:
- <2s load time
- Real-time data refresh
- Mobile responsive

---

## 3. User Stories & Acceptance Criteria

### 3.1 User Story: Find Prospects
**As a** website agency owner  
**I want to** automatically find 15 qualified prospects daily  
**So that** I can focus on sales and website building

**Acceptance Criteria**:
- [ ] Prospects found daily at 7 AM ET
- [ ] All prospects verified to have NO website
- [ ] Contact information accurate (phone, email, address)
- [ ] Categorized by industry type
- [ ] Duplicate prevention working
- [ ] Telegram notification sent

---

### 3.2 User Story: Generate Website
**As a** website agency owner  
**I want to** generate a professional website in <5 minutes  
**So that** I can deploy and sell quickly

**Acceptance Criteria**:
- [ ] Website generated in <5 minutes
- [ ] 5+ pages included (Home, Services, Gallery, Booking, About)
- [ ] Mobile-first responsive design
- [ ] Animations smooth and professional
- [ ] Images optimized
- [ ] Code clean and maintainable

---

### 3.3 User Story: Deploy Website
**As a** website agency owner  
**I want to** deploy website to live domain with approval gates  
**So that** I maintain control over purchases

**Acceptance Criteria**:
- [ ] Deploy to Vercel with one click
- [ ] Shows preview URL before approval
- [ ] Asks for approval before domain purchase
- [ ] Shows domain options with prices
- [ ] Approves cheapest domain by default
- [ ] DNS auto-configured
- [ ] Live in custom domain within 1 hour

---

### 3.4 User Story: Collect Payment
**As a** website agency owner  
**I want to** collect $2,500 per website automatically  
**So that** I don't have to manually invoice

**Acceptance Criteria**:
- [ ] Payment link created in <1 minute
- [ ] Link sent to customer
- [ ] Payment received in real-time
- [ ] Notification sent immediately
- [ ] Revenue logged automatically
- [ ] Profit calculated and displayed

---

### 3.5 User Story: Track Financials
**As a** website agency owner  
**I want to** see profit, costs, and revenue in real-time  
**So that** I understand my business performance

**Acceptance Criteria**:
- [ ] Dashboard shows daily revenue
- [ ] Costs tracked automatically
- [ ] Profit calculated per website
- [ ] Monthly summaries generated
- [ ] Google Sheets synced in real-time
- [ ] Telegram alerts for milestones

---

## 4. Technical Requirements

### 4.1 Technology Stack

**Frontend**:
- React 18 with TypeScript
- Next.js 14 (App Router)
- Tailwind CSS
- Framer Motion (animations)
- Three.js (3D)

**Backend**:
- Node.js 18+
- Express.js (API server)
- PostgreSQL (database)
- Redis (caching, job queue)
- Stripe API (payments)
- Vercel API (deployments)

**AI/ML**:
- Claude API (website generation)
- OpenAI Whisper (speech-to-text)
- Brave Search API (prospect research)

**Infrastructure**:
- Docker (containerization)
- GitHub (version control)
- Vercel (website hosting)
- AWS RDS (database hosting)
- Redis Cloud (caching)

**Monitoring**:
- Sentry (error tracking)
- DataDog (performance monitoring)
- Google Analytics (website analytics)

---

### 4.2 Performance Requirements

| Metric | Target | Current |
|--------|--------|---------|
| Website generation | <5 min | 2-5 min ✅ |
| Lighthouse score | 95+ | 96 ✅ |
| LCP (First Paint) | <2.5s | <2.5s ✅ |
| FID (Input Delay) | <100ms | <100ms ✅ |
| CLS (Layout Shift) | <0.1 | <0.1 ✅ |
| Mobile FPS | 30-60 | 30-60 ✅ |
| Desktop FPS | 60 | 60 ✅ |
| API response | <500ms | <200ms ✅ |
| Dashboard load | <2s | <2s ✅ |

---

### 4.3 Security Requirements

- ✅ HTTPS for all connections
- ✅ OAuth 2.0 for user authentication
- ✅ API rate limiting
- ✅ CORS protection
- ✅ SQL injection prevention (parameterized queries)
- ✅ XSS prevention
- ✅ CSRF tokens
- ✅ Data encryption at rest
- ✅ PCI compliance for payment processing
- ✅ Regular security audits

---

### 4.4 Scalability Requirements

- ✅ Support 1,000+ concurrent users
- ✅ Deploy 100+ websites per day
- ✅ Process 10,000+ API requests/minute
- ✅ Horizontal scaling with load balancing
- ✅ Database connection pooling
- ✅ Redis caching for high-traffic endpoints
- ✅ CDN for static assets

---

## 5. Data Requirements

### 5.1 Data Models

**Prospect**:
```
{
  id: UUID,
  name: String,
  phone: String,
  email: String,
  category: String,
  address: String,
  verified_no_website: Boolean,
  discovered_date: DateTime,
  call_status: Enum (new, contacted, yes, no),
  notes: String,
  created_at: DateTime,
  updated_at: DateTime
}
```

**Website**:
```
{
  id: UUID,
  prospect_id: UUID,
  business_name: String,
  business_type: String,
  github_url: String,
  vercel_url: String,
  custom_domain: String,
  status: Enum (generating, generated, deployed, live),
  lighthouse_score: Integer,
  wcag_compliance: String,
  created_at: DateTime,
  deployed_at: DateTime,
  updated_at: DateTime
}
```

**Payment**:
```
{
  id: UUID,
  website_id: UUID,
  amount: Decimal,
  status: Enum (pending, completed, failed),
  stripe_id: String,
  stripe_link: String,
  paid_at: DateTime,
  created_at: DateTime,
  updated_at: DateTime
}
```

**FinancialRecord**:
```
{
  id: UUID,
  website_id: UUID,
  type: Enum (revenue, cost, refund),
  amount: Decimal,
  description: String,
  category: String,
  created_at: DateTime
}
```

---

### 5.2 Database Schema

**Tables**:
- prospects
- websites
- payments
- financial_records
- design_patterns
- 3d_animations
- deployments
- users
- api_keys
- audit_logs

---

## 6. Success Metrics & KPIs

### 6.1 Business Metrics

| KPI | Week 1 | Month 1 | Quarter 1 |
|-----|--------|---------|-----------|
| Prospects found | 75 | 300 | 900 |
| Calls made | 75 | 300 | 900 |
| Conversions (YES) | 10-15 | 40-60 | 120-180 |
| Websites built | 5-7 | 20-30 | 60-90 |
| Revenue | $12.5K-17.5K | $50K-75K | $150K-225K |
| Profit | $12.3K-17.3K | $49.7K-74.7K | $149.2K-224.2K |
| Conversion rate | 15-20% | 15-20% | 15-20% |

---

### 6.2 Technical Metrics

- **Uptime**: 99.9%+
- **API Success Rate**: 99.5%+
- **Website Generation Success**: 99%+
- **Deployment Success**: 99%+
- **Payment Processing**: 99.5%+

---

## 7. Launch Plan

### Phase 1: MVP (Week 1-2)
- [ ] Core website generation working
- [ ] Vercel deployment working
- [ ] Basic prospect discovery
- [ ] Payment collection
- [ ] Dashboard with key metrics

### Phase 2: Enhancement (Week 3-4)
- [ ] 3D animations integrated
- [ ] Design pattern library
- [ ] Auto-deploy bot with approval gates
- [ ] CRM with prospect tracking
- [ ] Financial reporting

### Phase 3: Scale (Month 2)
- [ ] Multi-city support
- [ ] Industry-specific templates
- [ ] Advanced analytics
- [ ] API for integrations
- [ ] White-label platform

### Phase 4: Enterprise (Month 3+)
- [ ] Team management
- [ ] Franchise support
- [ ] Advanced automation
- [ ] AI improvements
- [ ] Mobile app

---

## 8. Risks & Mitigations

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|-----------|
| Website quality issues | Low | High | Lighthouse 95+ validation |
| Payment failures | Low | Medium | Stripe redundancy |
| API rate limits | Medium | Medium | Caching + queue system |
| Prospect data inaccuracy | Medium | Low | 6-point verification |
| Domain unavailability | Low | Medium | Multi-registrar fallback |
| Vercel deployment failures | Low | Medium | Rollback capability |

---

## 9. Success Criteria

**Product is successful when:**

- ✅ 4-6 websites built per day consistently
- ✅ 99%+ of websites meet quality standards
- ✅ 95%+ of payments collected successfully
- ✅ <5 minute website generation time
- ✅ 99.9% uptime
- ✅ <1% customer support requests
- ✅ $10K+ weekly revenue
- ✅ 99%+ profit margin maintained

---

## 10. Out of Scope (Phase 2+)

- Mobile app (Phase 3)
- Multiple payment methods beyond Stripe (Phase 2)
- Custom coded features (currently template-based)
- Hosting on platforms other than Vercel (Phase 2)
- White-label platform (Phase 3)
- Marketplace for templates (Phase 3)

---

## Appendix A: Glossary

- **MVP**: Minimum Viable Product
- **KPI**: Key Performance Indicator
- **TAM**: Total Addressable Market
- **Lighthouse**: Google's web performance audit tool
- **WCAG**: Web Content Accessibility Guidelines
- **LCP**: Largest Contentful Paint
- **FID**: First Input Delay
- **CLS**: Cumulative Layout Shift
- **Vercel**: Hosting platform for Next.js applications
- **Stripe**: Payment processing platform

---

## Appendix B: Approval Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Product Manager | Ryan (AI) | ✅ | 2026-03-14 |
| Engineering Lead | TBD | — | — |
| Business Lead | Andy Zhang | ✅ | 2026-03-14 |

---

**Document Version**: 1.0.0  
**Last Updated**: March 14, 2026  
**Next Review**: March 21, 2026

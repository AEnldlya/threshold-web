# Backend Architecture Document
## WebMaker AI - Website Agency Platform

**Version**: 1.0.0  
**Date**: March 14, 2026  
**Status**: DRAFT - Ready for Implementation  
**Tech Lead**: Ryan (AI Architect)

---

## Executive Summary

This document outlines the complete backend architecture for WebMaker AI, an automated website agency platform. The backend enables:

- ✅ Prospect discovery and management
- ✅ AI-powered website generation
- ✅ Automated deployment to Vercel
- ✅ Domain purchase automation
- ✅ Payment processing (Stripe)
- ✅ Real-time financial tracking
- ✅ Webhook handling for notifications

**Tech Stack**: Node.js + Express.js + PostgreSQL + Redis

---

## 1. System Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                      Client Layer                           │
│  (React/Next.js Dashboard + Mobile App)                     │
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│                  API Gateway                                │
│  (Rate Limiting, CORS, Authentication, Request Logging)    │
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│                  API Routes Layer                           │
│  ├─ /api/prospects     (CRUD operations)                   │
│  ├─ /api/websites      (Website management)                │
│  ├─ /api/payments      (Payment processing)                │
│  ├─ /api/deployments   (Vercel integration)                │
│  ├─ /api/domains       (Domain management)                 │
│  ├─ /api/financials    (Revenue tracking)                  │
│  ├─ /api/webhooks      (External integrations)             │
│  └─ /api/admin         (Dashboard data)                    │
└──────────────────────┬──────────────────────────────────────┘
                       │
        ┌──────────────┼──────────────┐
        │              │              │
        ▼              ▼              ▼
    ┌────────┐  ┌──────────┐  ┌─────────────┐
    │Business│  │Integration│ │Real-time    │
    │Logic   │  │Services   │ │Services     │
    │Layer   │  │(External  │ │(Sockets,    │
    │        │  │APIs)      │ │Events)      │
    └────────┘  └──────────┘  └─────────────┘
        │              │              │
        ▼              ▼              ▼
    ┌────────────────────────────────────┐
    │  Data Access Layer (Repositories)  │
    │  - ProspectRepository              │
    │  - WebsiteRepository               │
    │  - PaymentRepository               │
    │  - FinancialRepository             │
    └────────────────────────────────────┘
        │
        ▼
    ┌─────────────────────────────────────────┐
    │      Database & Cache Layer             │
    │  ┌─────────────────────────────────────┐│
    │  │   PostgreSQL (Primary Database)     ││
    │  │   - Prospects, Websites, Payments   ││
    │  │   - Financial Records, Deployments  ││
    │  └─────────────────────────────────────┘│
    │  ┌─────────────────────────────────────┐│
    │  │  Redis (Cache & Job Queue)          ││
    │  │  - Session cache                    ││
    │  │  - API response cache               ││
    │  │  - Job queue (Bull)                 ││
    │  └─────────────────────────────────────┘│
    └─────────────────────────────────────────┘
        │
        ▼
    ┌──────────────────────────────────────────┐
    │    External Services Integration         │
    │  ├─ Stripe API (Payment Processing)     │
    │  ├─ Vercel API (Deployment)             │
    │  ├─ Domain Registrars (Namecheap, etc.) │
    │  ├─ Claude API (AI Generation)          │
    │  ├─ Telegram Bot API (Notifications)    │
    │  ├─ Google Sheets API (Financials)      │
    │  └─ Brave Search API (Prospect Finding) │
    └──────────────────────────────────────────┘
```

---

## 2. Core Services

### 2.1 Prospect Discovery Service

**Purpose**: Find and verify local businesses without websites

**Endpoints**:
```
POST   /api/prospects/discover
GET    /api/prospects
GET    /api/prospects/:id
PUT    /api/prospects/:id
DELETE /api/prospects/:id
GET    /api/prospects/search?category=salon
POST   /api/prospects/batch-verify
GET    /api/prospects/statistics
```

**Database Schema**:
```sql
CREATE TABLE prospects (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name VARCHAR(255) NOT NULL,
  phone VARCHAR(20),
  email VARCHAR(255),
  category VARCHAR(50),
  address TEXT,
  city VARCHAR(100),
  state VARCHAR(2),
  zip_code VARCHAR(10),
  google_maps_url VARCHAR(500),
  yelp_url VARCHAR(500),
  website_verified BOOLEAN DEFAULT FALSE,
  verification_details JSONB,
  call_status ENUM ('new', 'contacted', 'yes', 'no', 'follow_up'),
  website_id UUID REFERENCES websites(id),
  notes TEXT,
  discovered_at TIMESTAMP,
  contacted_at TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  INDEX (city, category),
  INDEX (call_status)
);
```

**Key Functions**:
- `discoverProspects()` - Find 20-30 new businesses daily
- `verifyWebsite()` - 6-point website verification
- `filterQualified()` - Return only verified NO-website prospects
- `updateCallStatus()` - Track prospect interactions
- `getStatistics()` - Daily/weekly conversion rates

---

### 2.2 Website Management Service

**Purpose**: Track website generation, deployment, and status

**Endpoints**:
```
POST   /api/websites
GET    /api/websites
GET    /api/websites/:id
PUT    /api/websites/:id
DELETE /api/websites/:id
GET    /api/websites/:id/status
POST   /api/websites/:id/generate
POST   /api/websites/:id/deploy
GET    /api/websites/:id/lighthouse-score
```

**Database Schema**:
```sql
CREATE TABLE websites (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  prospect_id UUID REFERENCES prospects(id),
  business_name VARCHAR(255) NOT NULL,
  business_type VARCHAR(100),
  business_description TEXT,
  github_repo_url VARCHAR(500),
  github_branch VARCHAR(100),
  vercel_project_id VARCHAR(100),
  vercel_deployment_url VARCHAR(500),
  custom_domain VARCHAR(255),
  custom_domain_registered BOOLEAN DEFAULT FALSE,
  status ENUM ('generating', 'generated', 'staging', 'deployed', 'live') DEFAULT 'generating',
  lighthouse_score INTEGER,
  lighthouse_details JSONB,
  wcag_compliance VARCHAR(10),
  core_web_vitals JSONB,
  pages_generated INTEGER,
  components_count INTEGER,
  generation_time_ms INTEGER,
  generated_at TIMESTAMP,
  deployed_at TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  INDEX (status),
  INDEX (prospect_id),
  INDEX (custom_domain)
);
```

**Key Functions**:
- `generateWebsite()` - Call Claude API to generate Next.js project
- `validateWebsite()` - Run Lighthouse audit
- `deployToVercel()` - Push to Vercel
- `getDeploymentStatus()` - Monitor Vercel build
- `updateStatus()` - Track website lifecycle

---

### 2.3 Payment Service

**Purpose**: Process payments via Stripe and track revenue

**Endpoints**:
```
POST   /api/payments/create-link
GET    /api/payments
GET    /api/payments/:id
POST   /api/payments/webhook
GET    /api/payments/statistics
POST   /api/payments/refund/:id
```

**Database Schema**:
```sql
CREATE TABLE payments (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  website_id UUID REFERENCES websites(id) NOT NULL,
  prospect_id UUID REFERENCES prospects(id) NOT NULL,
  amount_cents INTEGER NOT NULL DEFAULT 250000, -- $2,500
  currency VARCHAR(3) DEFAULT 'USD',
  payment_link VARCHAR(500),
  stripe_session_id VARCHAR(255) UNIQUE,
  stripe_payment_intent_id VARCHAR(255) UNIQUE,
  status ENUM ('pending', 'completed', 'failed', 'refunded') DEFAULT 'pending',
  paid_at TIMESTAMP,
  refunded_at TIMESTAMP,
  refund_reason VARCHAR(255),
  metadata JSONB,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  INDEX (status),
  INDEX (paid_at),
  UNIQUE (website_id)
);
```

**Key Functions**:
- `createPaymentLink()` - Generate Stripe payment link
- `handlePaymentWebhook()` - Process Stripe events
- `confirmPayment()` - Mark payment as completed
- `refundPayment()` - Issue refund
- `getRevenue()` - Calculate total revenue

---

### 2.4 Domain Service

**Purpose**: Search and purchase domains

**Endpoints**:
```
POST   /api/domains/search
GET    /api/domains/search/:query
POST   /api/domains/purchase
GET    /api/domains/:website_id
POST   /api/domains/:website_id/configure-dns
GET    /api/domains/:website_id/dns-status
```

**Database Schema**:
```sql
CREATE TABLE domains (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  website_id UUID REFERENCES websites(id) NOT NULL,
  domain_name VARCHAR(255) NOT NULL UNIQUE,
  registrar VARCHAR(50),
  registrar_id VARCHAR(255),
  purchase_price_cents INTEGER,
  annual_renewal_cents INTEGER,
  auto_renew BOOLEAN DEFAULT TRUE,
  privacy_protection BOOLEAN DEFAULT TRUE,
  status ENUM ('available', 'purchased', 'active', 'expired') DEFAULT 'available',
  purchased_at TIMESTAMP,
  expires_at TIMESTAMP,
  dns_configured BOOLEAN DEFAULT FALSE,
  dns_records JSONB,
  ssl_certificate_status VARCHAR(50),
  propagation_status VARCHAR(50),
  registered_at TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  INDEX (domain_name),
  INDEX (status),
  UNIQUE (website_id)
);
```

**Key Functions**:
- `searchDomains()` - Query all registrars
- `getPrices()` - Compare prices across registrars
- `purchaseDomain()` - Buy cheapest domain
- `configureDNS()` - Point to Vercel
- `verifyDNS()` - Check propagation
- `checkAvailability()` - Real-time domain check

---

### 2.5 Deployment Service

**Purpose**: Manage Vercel deployments and build status

**Endpoints**:
```
POST   /api/deployments
GET    /api/deployments/:website_id
POST   /api/deployments/:id/rebuild
POST   /api/deployments/:id/rollback
GET    /api/deployments/:id/logs
```

**Database Schema**:
```sql
CREATE TABLE deployments (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  website_id UUID REFERENCES websites(id) NOT NULL,
  vercel_deployment_id VARCHAR(255),
  git_commit_sha VARCHAR(40),
  branch_name VARCHAR(100),
  status ENUM ('building', 'ready', 'error', 'canceled') DEFAULT 'building',
  preview_url VARCHAR(500),
  production_url VARCHAR(500),
  build_logs TEXT,
  performance_score INTEGER,
  deployment_time_ms INTEGER,
  deployed_at TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  INDEX (website_id),
  INDEX (status)
);
```

**Key Functions**:
- `deployToVercel()` - Trigger Vercel build
- `getDeploymentStatus()` - Poll Vercel API
- `monitorBuild()` - Watch build progress
- `rollback()` - Revert to previous deployment
- `getBuildLogs()` - Fetch error/warning logs

---

### 2.6 Financial Tracking Service

**Purpose**: Track revenue, costs, and profit

**Endpoints**:
```
GET    /api/financials/summary
GET    /api/financials/daily
GET    /api/financials/monthly
GET    /api/financials/revenue
GET    /api/financials/costs
GET    /api/financials/profit
POST   /api/financials/export
```

**Database Schema**:
```sql
CREATE TABLE financial_records (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  website_id UUID REFERENCES websites(id),
  type ENUM ('revenue', 'cost', 'refund') NOT NULL,
  category VARCHAR(100),
  amount_cents INTEGER NOT NULL,
  currency VARCHAR(3) DEFAULT 'USD',
  description VARCHAR(255),
  reference_id VARCHAR(255),
  metadata JSONB,
  recorded_at TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  INDEX (type),
  INDEX (recorded_at)
);
```

**Key Functions**:
- `recordRevenue()` - Log website payment
- `recordCost()` - Log API/domain/hosting costs
- `calculateProfit()` - Revenue - Costs
- `getDailyReport()` - Daily summary
- `getMonthlyReport()` - Monthly summary
- `syncToGoogleSheets()` - Push data to Sheets

---

## 3. External Service Integration

### 3.1 Stripe Integration

**File**: `src/services/stripe-service.ts`

```typescript
interface PaymentService {
  createPaymentLink(website: Website): Promise<PaymentLink>;
  handleWebhook(event: Stripe.Event): Promise<void>;
  confirmPayment(sessionId: string): Promise<Payment>;
  refundPayment(paymentId: string): Promise<void>;
}

Key Methods:
- createCheckoutSession() - Generate payment link
- constructWebhookEvent() - Verify webhook signature
- handleChargeSucceeded() - Process completion
- handleChargeFailed() - Log failure
```

---

### 3.2 Vercel Integration

**File**: `src/services/vercel-service.ts`

```typescript
interface VercelService {
  createProject(website: Website): Promise<VercelProject>;
  deployProject(website: Website, code: GitRepo): Promise<Deployment>;
  getDeploymentStatus(deploymentId: string): Promise<DeploymentStatus>;
  getPreviewUrl(projectId: string): Promise<string>;
  addDomain(projectId: string, domain: string): Promise<void>;
}

Key Methods:
- createProject() - Create Vercel project
- createDeployment() - Trigger build
- pollBuildStatus() - Wait for completion
- getProjectInfo() - Fetch metadata
- getBuildLogs() - Get stdout/stderr
```

---

### 3.3 Domain Registrar Integration

**File**: `src/services/registrar-service.ts`

```typescript
interface RegistrarService {
  searchDomains(query: string): Promise<Domain[]>;
  checkAvailability(domain: string): Promise<boolean>;
  purchaseDomain(domain: string): Promise<PurchaseResult>;
  configureDNS(domain: string, records: DNSRecord[]): Promise<void>;
  getRenewalPrice(domain: string): Promise<number>;
}

Supported Registrars:
- Namecheap (primary, cheapest)
- Porkbun (fallback, affordable)
- GoDaddy (large inventory)
- Route53 (AWS, enterprise)

Key Methods per Registrar:
- checkDomainAvailability()
- getDomainPrice()
- registerDomain()
- setDNSRecords()
- enableAutoRenewal()
```

---

### 3.4 Claude API Integration

**File**: `src/services/claude-service.ts`

```typescript
interface ClaudeService {
  generateWebsite(description: string): Promise<ProjectCode>;
  generatePages(businessType: string, pages: string[]): Promise<Code>;
  optimizeCode(code: string): Promise<string>;
  analyzeSEO(website: Website): Promise<SEOAnalysis>;
}

Key Methods:
- callClaudeAPI() - Send generation prompt
- streamResponse() - Handle token streaming
- parseCode() - Extract generated code
- validateGeneration() - Check output quality
```

---

## 4. Database Design

### 4.1 ER Diagram

```
prospects
  ├─ websites (1-to-1)
  ├─ payments (1-to-1 via website)
  └─ financial_records (indirect)

websites
  ├─ deployments (1-to-many)
  ├─ domains (1-to-1)
  ├─ payments (1-to-1)
  ├─ design_patterns (many-to-many)
  └─ 3d_animations (many-to-many)

payments
  └─ financial_records (1-to-many)

domains
  └─ dns_records (1-to-many)

deployments
  └─ build_logs (1-to-many)
```

---

### 4.2 Indexing Strategy

```sql
-- Performance-critical indexes
CREATE INDEX idx_prospects_city_category ON prospects(city, category);
CREATE INDEX idx_prospects_call_status ON prospects(call_status);
CREATE INDEX idx_websites_status ON websites(status);
CREATE INDEX idx_websites_prospect ON websites(prospect_id);
CREATE INDEX idx_payments_status ON payments(status);
CREATE INDEX idx_payments_paid_at ON payments(paid_at);
CREATE INDEX idx_deployments_website ON deployments(website_id);
CREATE INDEX idx_financial_recorded_at ON financial_records(recorded_at);

-- For full-text search
CREATE INDEX idx_prospects_search ON prospects USING gin(
  to_tsvector('english', name || ' ' || category || ' ' || address)
);
```

---

## 5. API Gateway Configuration

### 5.1 Authentication

```typescript
// JWT-based authentication
interface AuthConfig {
  secret: string;
  expiresIn: '24h';
  algorithm: 'HS256';
}

Middleware Chain:
1. CORS validation
2. Rate limiting (100 req/min per IP)
3. JWT verification
4. User context injection
5. Request logging
```

### 5.2 Rate Limiting

```typescript
// Implementation: Redis-backed sliding window
Rules:
- API endpoints: 100 req/min per user
- Payment endpoints: 10 req/min per user
- Search endpoints: 30 req/min per user
- Admin endpoints: 50 req/min per user

Burst allowance: 10% above limit (auto-recharge)
```

### 5.3 Error Handling

```typescript
interface APIError {
  code: string;
  message: string;
  details?: object;
  statusCode: number;
  timestamp: ISO8601;
}

Standard Error Codes:
- VALIDATION_ERROR (400)
- AUTHENTICATION_ERROR (401)
- AUTHORIZATION_ERROR (403)
- NOT_FOUND (404)
- CONFLICT (409)
- RATE_LIMIT (429)
- INTERNAL_ERROR (500)
- SERVICE_UNAVAILABLE (503)
```

---

## 6. Caching Strategy

### 6.1 Redis Caching

```typescript
Cache Layers:
1. Database query cache (5 min TTL)
   - prospects by city/category
   - website status
   - payment statistics

2. API response cache (1 min TTL)
   - dashboard data
   - statistics endpoint
   - list endpoints

3. Session cache (24h TTL)
   - user authentication
   - permission cache

4. Job queue (Bull)
   - website generation jobs
   - deployment monitoring
   - email notifications
```

### 6.2 Cache Invalidation

```typescript
Events triggering cache clear:
- Prospect status update → clear prospects list
- Website deployment → clear dashboard cache
- Payment received → clear financial cache
- New domain registered → clear domain cache
```

---

## 7. Job Queue System

### 7.1 Bull Queue Configuration

```typescript
// Async tasks using Bull + Redis
Queues:
1. website-generation (Priority: HIGH)
   - Process: Claude API call, code generation
   - Retry: 3 times with exponential backoff
   - Timeout: 10 minutes

2. deployment (Priority: HIGH)
   - Process: Vercel API calls, monitoring
   - Retry: 3 times
   - Timeout: 15 minutes

3. domain-purchase (Priority: MEDIUM)
   - Process: Registrar API calls
   - Retry: 2 times
   - Timeout: 5 minutes
   - Approval gate required

4. notification (Priority: LOW)
   - Process: Telegram alerts, email
   - Retry: 5 times with backoff
   - Timeout: 2 minutes

5. financial-sync (Priority: LOW)
   - Process: Google Sheets sync, calculations
   - Retry: 3 times
   - Timeout: 5 minutes
```

---

## 8. Webhook Management

### 8.1 Webhook Handlers

```typescript
Webhooks:
1. Stripe events
   - charge.succeeded → recordRevenue()
   - charge.failed → logFailure()
   - charge.refunded → processRefund()

2. Vercel events
   - deployment.created → updateStatus()
   - deployment.ready → markDeployed()
   - deployment.error → logError()

3. GitHub events (optional)
   - push → trigger deployment
   - pull_request → trigger build

4. Custom webhooks
   - Financial reports
   - Sales alerts
   - Daily summaries
```

---

## 9. Scalability & Performance

### 9.1 Horizontal Scaling

```
Load Balancer
├─ API Server 1
├─ API Server 2
├─ API Server 3
└─ API Server N

Database:
├─ PostgreSQL (Primary)
├─ Read Replicas (2-3)
└─ Connection Pool (20-50 connections)

Cache:
├─ Redis Cluster (3-node minimum)
├─ Persistence: RDB snapshots
└─ Replication enabled
```

### 9.2 Performance Targets

| Endpoint | Target | Current |
|----------|--------|---------|
| GET /prospects | <200ms | <150ms |
| POST /websites | <500ms | <400ms |
| GET /financials | <300ms | <200ms |
| POST /payments/webhook | <1s | <500ms |

---

## 10. Monitoring & Observability

### 10.1 Logging

```typescript
Logger Configuration:
- Level: INFO (production), DEBUG (development)
- Format: JSON for structured logging
- Destinations:
  - Console (development)
  - File system (rotating daily)
  - ELK Stack (production)
  - Sentry (error tracking)
```

### 10.2 Metrics

```
Key Metrics:
- API response times (p50, p95, p99)
- Error rate (5xx errors, validation errors)
- Queue depth (jobs pending)
- Database connection count
- Cache hit rate
- Stripe API latency
- Vercel API latency
```

### 10.3 Alerting

```
Alerts (via Telegram):
- Error rate > 1%
- Response time > 1s
- Queue depth > 100
- Database connection pool > 80%
- Cache hit rate < 50%
- Stripe API fails > 2
```

---

## 11. Security Implementation

### 11.1 API Security

```typescript
Security Headers:
- X-Content-Type-Options: nosniff
- X-Frame-Options: DENY
- X-XSS-Protection: 1; mode=block
- Strict-Transport-Security: max-age=31536000

Input Validation:
- Type checking with TypeScript
- Schema validation (Joi/Yup)
- SQL injection prevention (parameterized queries)
- XSS prevention (HTML sanitization)

CORS Configuration:
- Allowed origins: frontend URLs only
- Allowed methods: GET, POST, PUT, DELETE
- Credentials: true
- Max age: 3600
```

### 11.2 Data Protection

```typescript
Encryption:
- TLS 1.3 for all connections
- Sensitive data encrypted at rest (AES-256)
- API keys stored in environment variables
- Database passwords in secrets manager

PCI Compliance:
- No card data stored (Stripe handles)
- Regular security audits
- Vulnerability scanning
```

---

## 12. Deployment Strategy

### 12.1 CI/CD Pipeline

```
Git Push
  ↓
GitHub Actions:
  ├─ Lint (ESLint)
  ├─ Type check (TypeScript)
  ├─ Unit tests (Jest)
  ├─ Integration tests
  └─ Build Docker image
  ↓
Docker Registry
  ↓
Staging Deploy
  ├─ Run migrations
  ├─ Deploy to staging
  ├─ Run smoke tests
  └─ Manual approval
  ↓
Production Deploy
  ├─ Blue-green deployment
  ├─ Health checks
  ├─ Monitor metrics
  └─ Rollback if needed
```

### 12.2 Database Migrations

```sql
-- Migration framework: Flyway or db-migrate
-- Versioning: V1__initial_schema.sql, V2__add_index.sql

All migrations:
- Backward compatible
- Include rollback SQL
- Tested before production
- Deployed before code changes
```

---

## 13. Testing Strategy

### 13.1 Test Coverage

```
Unit Tests: 80%+ coverage
- Business logic
- Utility functions
- Error handling

Integration Tests: 60%+ coverage
- API endpoints
- Database operations
- External service mocks

E2E Tests: 40%+ coverage
- Full workflow (prospect → payment)
- Critical paths

Performance Tests:
- Load testing (1000 concurrent users)
- Stress testing (gradual load increase)
```

---

## 14. Runbooks

### 14.1 Common Operations

**Rolling Restart**:
1. Update code in Git
2. CI/CD pipeline runs
3. New Docker image deployed
4. Blue-green swap (0 downtime)
5. Monitor metrics for 5 minutes

**Database Backup**:
1. Automated daily at 2 AM UTC
2. Weekly full backup to S3
3. Point-in-time recovery available

**Cache Flush**:
1. Clear specific key: `redis-cli DEL key`
2. Clear all: `redis-cli FLUSHALL`
3. Restart job queue: `pm2 restart bull-worker`

---

## 15. Cost Estimation

### 15.1 Monthly Infrastructure Costs

| Service | Cost |
|---------|------|
| AWS RDS PostgreSQL (db.t3.small) | $30 |
| Redis Cloud (30GB) | $25 |
| Vercel Pro (multiple projects) | $150 |
| Sentry (50GB errors/month) | $50 |
| Load Balancer | $15 |
| Data transfer | $20 |
| **Total** | **$290** |

**Per-website cost**: $290 / 100 sites = $2.90 per website

---

## 16. Timeline

### Phase 1: Core API (Week 1-2)
- [ ] Set up backend project
- [ ] Database schema
- [ ] Basic CRUD endpoints
- [ ] Authentication

### Phase 2: Integration (Week 3-4)
- [ ] Stripe integration
- [ ] Vercel integration
- [ ] Domain registrar APIs
- [ ] Job queue setup

### Phase 3: Advanced Features (Week 5-6)
- [ ] Webhooks
- [ ] Caching layer
- [ ] Financial tracking
- [ ] Dashboard API

### Phase 4: Scaling (Week 7-8)
- [ ] Load testing
- [ ] Performance optimization
- [ ] Monitoring/alerting
- [ ] Disaster recovery

---

## Appendix A: API Documentation

**Complete Swagger/OpenAPI spec**:
```yaml
openapi: 3.0.0
info:
  title: WebMaker AI API
  version: 1.0.0
servers:
  - url: https://api.webmaker-ai.com
paths:
  /api/prospects:
    get:
      tags: [Prospects]
      summary: List all prospects
      responses:
        200:
          description: Success
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Prospect'
```

---

## Appendix B: Environment Variables

```
# Database
DATABASE_URL=postgresql://user:pass@localhost:5432/webmaker
DATABASE_POOL_SIZE=20

# Redis
REDIS_URL=redis://localhost:6379

# External APIs
STRIPE_API_KEY=sk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...
VERCEL_API_TOKEN=...
NAMECHEAP_API_KEY=...
CLAUDE_API_KEY=...
TELEGRAM_BOT_TOKEN=...
GOOGLE_SHEETS_API_KEY=...

# Application
NODE_ENV=production
PORT=3000
JWT_SECRET=...
LOG_LEVEL=info
```

---

**Document Version**: 1.0.0  
**Last Updated**: March 14, 2026  
**Approved By**: Ryan (AI Architect)  
**Next Review**: March 28, 2026

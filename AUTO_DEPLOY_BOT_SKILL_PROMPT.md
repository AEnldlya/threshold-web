# Auto-Deploy Bot Skill - Vercel + Domain Automation with Permission Gates

**Goal**: Create an OpenClaw skill that automatically deploys websites to Vercel and purchases the cheapest available domain, with human approval at each step.

**Status**: Ready for implementation

---

## Skill Overview

### Name
`auto-deploy-bot`

### Description
Automated deployment and domain purchase bot with permission gates. Deploys to Vercel, searches for affordable domains, and buys the cheapest fit - but asks for approval before each major action.

### Use Cases
1. **One-Command Website Launch**: Deploy + domain in one request
2. **Cost Optimization**: Find cheapest domain automatically
3. **Safety Gates**: Human approval before purchases
4. **Batch Deployment**: Deploy multiple sites with approval workflow
5. **Domain Strategy**: Suggest best domain options before buying

---

## Technical Architecture

### Core Dependencies
```
anthropic>=0.25.0          # Claude for domain suggestions
vercel-cli>=33.0.0         # Vercel deployment
requests>=2.31.0           # HTTP requests
namecheap-api>=1.0.0       # Domain registrar API
pydantic>=2.0.0            # Data validation
python-dotenv>=1.0.0       # Configuration
```

### Domain Registrar APIs Supported
- **Namecheap** (cheapest, recommended)
- **Porkbun** (affordable, good support)
- **GoDaddy** (large inventory)
- **Route53** (AWS - for enterprise)

---

## Skill Commands

### 1. `deploy_with_approval()`
**Purpose**: Deploy to Vercel with human permission gates

**Input**:
```python
{
  "website_id": "summer-street-hair-2026",
  "project_path": "/workspace/summer-street-hair/",
  "vercel_project_name": "summer-street-hair",
  "custom_domain": "optional-domain.com",  # Optional
  "require_approval": True,  # Ask before deploy
  "deployment_timeout": 300  # 5 minutes
}
```

**Output**:
```json
{
  "success": true,
  "status": "awaiting_approval",
  "action": "deploy_to_vercel",
  "project": "summer-street-hair",
  "message": "Ready to deploy to Vercel. Approve? (yes/no)",
  "estimated_time": 120,
  "vercel_preview_url": "https://summer-street-hair-draft.vercel.app"
}
```

---

### 2. `search_cheapest_domain()`
**Purpose**: Find cheapest domain that fits the website

**Input**:
```python
{
  "website_id": "summer-street-hair-2026",
  "business_name": "Summer Street Hair",
  "business_type": "Salon",
  "preferred_tld": [".com", ".io", ".co"],  # Priority order
  "max_price": 50,  # USD per year
  "registrars": ["namecheap", "porkbun"],
  "suggest_alternatives": True,  # Suggest 5 options
  "require_approval": True  # Ask before showing results
}
```

**Output**:
```json
{
  "success": true,
  "status": "awaiting_approval",
  "action": "domain_search_complete",
  "options": [
    {
      "domain": "summerstassalon.com",
      "price": 8.99,
      "registrar": "namecheap",
      "availability": true,
      "rank": 1
    },
    {
      "domain": "summerstreethouse.com",
      "price": 12.99,
      "registrar": "namecheap",
      "availability": true,
      "rank": 2
    },
    {
      "domain": "summerhaircuts.io",
      "price": 19.99,
      "registrar": "porkbun",
      "availability": true,
      "rank": 3
    }
  ],
  "cheapest": "summerstassalon.com",
  "cheapest_price": 8.99,
  "message": "Found 3 domains. Buy summerstassalon.com for $8.99/year? (yes/no)"
}
```

---

### 3. `buy_domain_with_approval()`
**Purpose**: Purchase domain from registrar (with approval)

**Input**:
```python
{
  "domain": "summerstassalon.com",
  "registrar": "namecheap",
  "auto_renew": True,
  "privacy_protection": True,
  "years": 1,
  "require_approval": True
}
```

**Output**:
```json
{
  "success": true,
  "status": "awaiting_approval",
  "action": "purchase_domain",
  "domain": "summerstassalon.com",
  "price": 8.99,
  "registrar": "namecheap",
  "auto_renew": true,
  "privacy": true,
  "total_cost": 8.99,
  "message": "About to purchase summerstassalon.com for $8.99. Approve? (yes/no)"
}
```

---

### 4. `configure_domain_dns()`
**Purpose**: Point domain to Vercel deployment

**Input**:
```python
{
  "domain": "summerstassalon.com",
  "registrar": "namecheap",
  "vercel_project": "summer-street-hair",
  "auto_configure": True,
  "require_approval": True
}
```

**Output**:
```json
{
  "success": true,
  "status": "awaiting_approval",
  "action": "configure_dns",
  "domain": "summerstassalon.com",
  "dns_records": [
    {
      "type": "CNAME",
      "name": "www",
      "value": "cname.vercel-dns.com"
    },
    {
      "type": "A",
      "name": "@",
      "value": "76.76.19.165"
    }
  ],
  "message": "Configure DNS for summerstassalon.com pointing to Vercel? (yes/no)"
}
```

---

### 5. `deploy_and_buy_complete()`
**Purpose**: Full workflow - deploy + find domain + buy + configure

**Input**:
```python
{
  "website_id": "summer-street-hair-2026",
  "project_path": "/workspace/summer-street-hair/",
  "business_name": "Summer Street Hair",
  "business_type": "Salon",
  "max_domain_price": 50,
  "auto_renew_domain": True,
  "require_approval_at_each_step": True  # Key parameter
}
```

**Output - Step 1**:
```json
{
  "step": 1,
  "action": "deploy_to_vercel",
  "message": "Deploy summer-street-hair to Vercel? (yes/no)",
  "preview_url": "https://summer-street-hair-draft.vercel.app"
}
```

**Output - Step 2** (after approval):
```json
{
  "step": 2,
  "action": "search_domain",
  "message": "Found 3 domains. Best: summerstassalon.com ($8.99/yr). Buy it? (yes/no)",
  "cheapest_option": "summerstassalon.com",
  "price": 8.99
}
```

**Output - Step 3** (after approval):
```json
{
  "step": 3,
  "action": "purchase_domain",
  "message": "Purchased summerstassalon.com for $8.99",
  "domain": "summerstassalon.com",
  "registrar": "namecheap"
}
```

**Output - Step 4** (automatic):
```json
{
  "step": 4,
  "action": "configure_dns",
  "message": "DNS configured. Website live in 30-60 minutes at summerstassalon.com"
}
```

---

### 6. `batch_deploy_with_domains()`
**Purpose**: Deploy multiple websites with domain purchases

**Input**:
```python
{
  "websites": [
    {
      "website_id": "salon-1",
      "business_name": "Sunshine Hair Studio",
      "business_type": "Salon"
    },
    {
      "website_id": "salon-2",
      "business_name": "Elite Haircuts",
      "business_type": "Salon"
    }
  ],
  "require_approval": True,
  "batch_approval": True  # Approve all at once or each individually
}
```

**Output**:
```json
{
  "batch_id": "batch_20260314_001",
  "websites_to_deploy": 2,
  "message": "Deploy 2 websites + buy domains? (yes/no)",
  "estimated_cost": 17.98,
  "estimated_time": 600
}
```

---

### 7. `deployment_status()`
**Purpose**: Check status of ongoing deployments

**Input**:
```python
{
  "website_id": "summer-street-hair-2026",
  "include_domain_status": True
}
```

**Output**:
```json
{
  "website_id": "summer-street-hair-2026",
  "deployment": {
    "status": "deployed",
    "vercel_url": "https://summer-street-hair.vercel.app",
    "deployment_time": 120,
    "lighthouse_score": 96
  },
  "domain": {
    "status": "active",
    "domain": "summerstassalon.com",
    "registrar": "namecheap",
    "dns_configured": true,
    "live_since": "2026-03-14T18:45:00Z"
  },
  "total_cost": 8.99
}
```

---

## Permission Gate Architecture

### Human Approval Flow

```
User Request: "Deploy website X"
    ↓
[GATE 1] Deploy to Vercel?
    ├─ YES → Deploy
    ├─ NO → Cancel
    └─ Show preview URL for review
    ↓
[GATE 2] Search for domains?
    ├─ YES → Find domains
    ├─ NO → Skip domain search
    └─ Show top 5 options with prices
    ↓
[GATE 3] Buy cheapest domain?
    ├─ YES → Purchase
    ├─ NO → Pick different domain
    └─ Show domain details + cost
    ↓
[GATE 4] Configure DNS?
    ├─ YES → Auto-configure
    ├─ NO → Manual DNS setup
    └─ Show DNS records
    ↓
✅ COMPLETE - Live website with domain
```

### Optional: Auto-Approve Thresholds

```python
{
  "auto_approve_rules": {
    "deploy_vercel": False,  # Always ask
    "search_domain": False,  # Always ask
    "buy_domain_under": 15,  # Auto-buy if <$15/year
    "configure_dns": True    # Auto-configure after purchase
  }
}
```

---

## Implementation Strategy

### Phase 1: Permission Framework
1. **Approval Handler**
   - Accept yes/no responses
   - Store approval history
   - Prevent double-spending
   - Log all approvals

2. **State Management**
   - Track deployment step
   - Save intermediate results
   - Resume on interruption
   - Rollback capability

### Phase 2: Vercel Integration
1. **Deploy Manager**
   - Create project if needed
   - Deploy code from GitHub
   - Show preview URL
   - Monitor build status

2. **Build Monitoring**
   - Track build progress
   - Show estimated time
   - Alert on failures
   - Provide rollback option

### Phase 3: Domain Intelligence
1. **Smart Domain Search**
   - Generate domain suggestions from business name
   - Check availability across registrars
   - Compare prices
   - Rank by fit + affordability

2. **Price Optimization**
   - Check multiple registrars
   - Find cheapest option
   - Include renewal cost
   - Show privacy protection cost

### Phase 4: Domain Purchase
1. **Registrar Integration**
   - Namecheap API
   - Porkbun API
   - GoDaddy API
   - Payment handling (using stored credentials)

2. **DNS Configuration**
   - Generate correct DNS records
   - Point to Vercel
   - Verify propagation
   - Monitor resolution

---

## File Structure

```
~/.openclaw/workspace/skills/auto-deploy-bot/
├── SKILL.md                          # Skill metadata
├── README.md                         # User guide
├── auto_deploy_bot.py                # Main CLI
├── src/
│   ├── __init__.py
│   ├── vercel_manager.py             # Vercel deployment
│   ├── domain_searcher.py            # Domain search engine
│   ├── registrar_manager.py          # Registrar API integration
│   ├── permission_gates.py           # Approval workflow
│   ├── state_manager.py              # Deployment state tracking
│   ├── dns_configurator.py           # DNS setup
│   ├── price_optimizer.py            # Find cheapest domains
│   └── batch_processor.py            # Multiple websites
├── registrars/
│   ├── namecheap_api.py              # Namecheap integration
│   ├── porkbun_api.py                # Porkbun integration
│   ├── godaddy_api.py                # GoDaddy integration
│   └── route53_api.py                # AWS integration
├── examples/
│   ├── example_deploy_with_approval.py
│   ├── example_search_domain.py
│   ├── example_auto_deploy_complete.py
│   └── example_batch_deploy.py
├── test_auto_deploy_bot.py           # 50+ unit tests
├── requirements.txt
└── .env.example
```

---

## Core Modules

### vercel_manager.py (15 KB)
- Create Vercel projects
- Deploy from GitHub
- Get preview URLs
- Monitor build status
- Handle failures

### domain_searcher.py (14 KB)
- Generate domain suggestions
- Check availability
- Query multiple registrars
- Compare prices
- Rank by fit

### permission_gates.py (12 KB)
- Request approvals
- Parse yes/no responses
- Log approval history
- Prevent double-spending
- Track state between approvals

### registrar_manager.py (16 KB)
- Namecheap API
- Porkbun API
- GoDaddy API
- Route53 API
- Purchase domains
- Auto-renew setup

### dns_configurator.py (10 KB)
- Generate DNS records
- Configure at registrar
- Verify propagation
- Monitor resolution
- Rollback if needed

### state_manager.py (10 KB)
- Track deployment steps
- Save intermediate data
- Resume interrupted deployments
- Provide rollback
- Audit trail

---

## Usage Examples

### Simple Deploy + Domain

```bash
auto-deploy-bot deploy_and_buy_complete \
  --website-id "summer-street-hair" \
  --business-name "Summer Street Hair" \
  --business-type "Salon" \
  --max-domain-price 50 \
  --require-approval
```

**Workflow**:
```
Step 1: Deploy to Vercel? [YES/NO]
  > YES
  ✓ Deployed to https://summer-street-hair.vercel.app

Step 2: Search domains? [YES/NO]
  > YES
  ✓ Found summerstassalon.com for $8.99/year

Step 3: Buy summerstassalon.com? [YES/NO]
  > YES
  ✓ Purchased!

Step 4: Configure DNS? [YES/NO]
  > YES
  ✓ DNS configured
  
✅ Complete! Live at summerstassalon.com in 30-60 minutes
```

---

## Security & Safety Features

✅ **Permission Gates**
- Human approval before every purchase
- No auto-buy without explicit permission
- Log all approvals with timestamps

✅ **Cost Controls**
- Set maximum domain price
- Show prices before buying
- Review total cost before commit

✅ **Rollback Capability**
- Save state at each step
- Revert failed deployments
- Cancel domain purchases if needed

✅ **Audit Trail**
- Log all decisions
- Track approval flow
- Document all purchases

✅ **Rate Limiting**
- Prevent accidental double-purchase
- Confirm expensive operations
- Cool-off period for large batches

---

## Success Criteria

✅ Can deploy to Vercel with approval
✅ Can search for cheapest domains
✅ Can purchase domains from registrars
✅ Can configure DNS automatically
✅ Has human permission gates at each step
✅ Supports batch deployment
✅ Tracks deployment state
✅ Provides rollback capability
✅ Maintains audit trail
✅ Integrates with multiple registrars
✅ Full documentation and examples
✅ 50+ unit tests

---

## Integration with Your System

### With Claude WebDev
- Deploy generated websites automatically
- Ask for approval before buying domain
- Fully automated except for permission gates

### With Stripe
- Calculate domain cost
- Add to customer invoice
- Include in total website cost

### With CPA Agent
- Log domain purchase cost
- Track renewal costs
- Include in profit calculations

---

## Timeline

- **MVP (Phase 1-2)**: 1-2 weeks
  - Deploy to Vercel
  - Search for domains
  - Permission gates

- **Production (Phase 1-3)**: 2-3 weeks
  - Full registrar integration
  - DNS configuration
  - Batch processing

- **Enterprise (Phase 1-4)**: 3-4 weeks
  - Complete testing
  - Advanced features
  - Production monitoring

---

**Ready for implementation!** This skill automates deployment and domain purchases while keeping humans in control with permission gates at every step. 🚀

Follow this prompt to create the complete `auto-deploy-bot` skill.

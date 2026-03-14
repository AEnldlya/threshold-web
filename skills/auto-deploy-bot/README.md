# Auto-Deploy Bot Skill

**Automated deployment and domain purchase bot with permission gates. Deploys to Vercel, searches for affordable domains, and buys the cheapest fit - but asks for approval before each major action.**

## Table of Contents

1. [Quick Start](#quick-start)
2. [Features](#features)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Usage](#usage)
6. [Commands](#commands)
7. [Permission Gates](#permission-gates)
8. [Registrar Support](#registrar-support)
9. [Examples](#examples)
10. [Testing](#testing)
11. [Troubleshooting](#troubleshooting)
12. [Security](#security)
13. [Cost Control](#cost-control)
14. [Advanced Usage](#advanced-usage)

## Quick Start

### Deploy a website and buy a domain in one command:

```bash
auto-deploy-bot deploy_and_buy_complete \
  --website-id "my-salon" \
  --project-path "/workspace/my-salon/" \
  --business-name "My Hair Salon" \
  --business-type "Salon" \
  --max-domain-price 50

# Follow the prompts:
# Deploy to Vercel? [YES/NO] → YES
# Search for domains? [YES/NO] → YES
# Buy cheapest domain? [YES/NO] → YES
# Configure DNS? [YES/NO] → YES
# ✅ Complete! Live at yourdomain.com
```

### Just deploy to Vercel:

```bash
auto-deploy-bot deploy_with_approval \
  --website-id "my-salon" \
  --project-path "/workspace/my-salon/" \
  --vercel-project-name "my-salon"
```

### Search for domains:

```bash
auto-deploy-bot search_cheapest_domain \
  --website-id "my-salon" \
  --business-name "My Hair Salon" \
  --business-type "Salon" \
  --max-price 50
```

### Buy a specific domain:

```bash
auto-deploy-bot buy_domain_with_approval \
  --domain "mysalon.com" \
  --registrar "namecheap" \
  --years 1
```

## Features

### ✅ Permission Gates at Every Step

Every critical action requires human approval:

- **Deploy to Vercel?** [YES/NO]
  - Shows preview URL before asking
  - Can review before committing

- **Search for domains?** [YES/NO]
  - Shows search criteria
  - Can customize registrars

- **Buy domain?** [YES/NO]
  - Shows domain name and price
  - Shows total cost including privacy
  - Prevents accidental purchases

- **Configure DNS?** [YES/NO]
  - Shows DNS records
  - Can review settings before applying

### ✅ Cost Control

- Set maximum domain price (`--max-domain-price`)
- Show all prices before purchase
- Track spending across registrars
- Batch cost estimation
- Automatic selection of cheapest option

### ✅ Multiple Registrars

Search and compare prices across:
- **Namecheap** (recommended - lowest prices)
- **Porkbun** (affordable, good support)
- **GoDaddy** (largest inventory)
- **Route53** (AWS integration)

### ✅ Smart Domain Search

- Generate suggestions from business name
- Check availability across registrars
- Compare prices automatically
- Rank by affordability and fit
- Show top 5 options

### ✅ State Management

- Track deployment steps
- Resume interrupted workflows
- Rollback capability
- Audit trail of all decisions
- Cost tracking

## Installation

### Prerequisites

- Python 3.8+
- Vercel CLI installed (`npm install -g vercel`)
- Vercel account
- Domain registrar account(s)

### Step 1: Install the skill

```bash
cd ~/.openclaw/workspace/skills/
git clone https://github.com/yourusername/auto-deploy-bot.git
cd auto-deploy-bot
pip install -r requirements.txt
```

### Step 2: Set up environment variables

Create a `.env` file:

```bash
cp .env.example .env
```

Edit `.env` with your credentials:

```bash
# Vercel
VERCEL_TOKEN=your_vercel_token

# Namecheap
NAMECHEAP_API_KEY=your_namecheap_key
NAMECHEAP_API_USER=your_namecheap_user

# Porkbun
PORKBUN_API_KEY=your_porkbun_key
PORKBUN_SECRET_API_KEY=your_porkbun_secret

# GoDaddy
GODADDY_API_KEY=your_godaddy_key
GODADDY_API_SECRET=your_godaddy_secret

# AWS (Route53)
AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_aws_secret
```

### Step 3: Verify installation

```bash
python auto_deploy_bot.py --help
```

## Configuration

### Environment Setup

See `Installation` section above.

### Configuration File (Optional)

Create `.deployment_config.json` for default settings:

```json
{
  "default_registrar": "namecheap",
  "preferred_tlds": [".com", ".io", ".co"],
  "max_domain_price": 50.0,
  "auto_renew": true,
  "privacy_protection": true,
  "vercel_deployment_timeout": 300,
  "dns_check_timeout": 600
}
```

### Auto-Approval Thresholds (Optional)

Create `.auto_approval.json` to auto-approve low-cost operations:

```json
{
  "auto_approve_rules": {
    "deploy_vercel": false,
    "search_domain": false,
    "buy_domain_under": 15.0,
    "configure_dns": true,
    "batch_deploy_under": 100.0
  }
}
```

## Usage

### Basic Commands

#### 1. Deploy to Vercel with approval

```bash
auto-deploy-bot deploy_with_approval \
  --website-id "my-project" \
  --project-path "/path/to/project" \
  --vercel-project-name "my-project"
```

**Input**: Project location
**Output**: Deployment URL and status
**Approval**: Required before deployment

#### 2. Search for domains

```bash
auto-deploy-bot search_cheapest_domain \
  --website-id "my-project" \
  --business-name "My Business" \
  --business-type "Salon" \
  --max-price 50 \
  --registrars namecheap porkbun
```

**Input**: Business info, budget, registrars
**Output**: Top 5 domain options with prices
**Approval**: Required before showing results

#### 3. Buy domain

```bash
auto-deploy-bot buy_domain_with_approval \
  --domain "mybusiness.com" \
  --registrar "namecheap" \
  --years 1 \
  --privacy-protection \
  --auto-renew
```

**Input**: Domain details
**Output**: Confirmation ID and receipt
**Approval**: Required - shows price first

#### 4. Configure DNS

```bash
auto-deploy-bot configure_domain_dns \
  --domain "mybusiness.com" \
  --registrar "namecheap" \
  --vercel-project "my-project"
```

**Input**: Domain and Vercel project
**Output**: DNS records applied
**Approval**: Can auto-approve after purchase

#### 5. Full workflow

```bash
auto-deploy-bot deploy_and_buy_complete \
  --website-id "my-salon" \
  --project-path "/workspace/my-salon/" \
  --business-name "Summer Street Hair Salon" \
  --business-type "Salon" \
  --max-domain-price 50 \
  --require-approval-at-each-step
```

**Output**: Complete deployment with domain
- Step 1: Deploy to Vercel
- Step 2: Search domains
- Step 3: Buy cheapest domain
- Step 4: Configure DNS
- Final: Website live at domain

#### 6. Batch deployment

```bash
auto-deploy-bot batch_deploy_with_domains \
  --websites-json websites.json \
  --require-approval \
  --batch-approval
```

**websites.json**:
```json
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
  ]
}
```

#### 7. Check deployment status

```bash
auto-deploy-bot deployment_status \
  --website-id "my-project"
```

**Output**: Current status of all steps

## Commands

### deploy_with_approval

Deploy website to Vercel with human approval gate.

**Options**:
- `--website-id` (required): Unique identifier for website
- `--project-path` (required): Path to local project
- `--vercel-project-name` (required): Name in Vercel
- `--deployment-timeout` (default: 300): Timeout in seconds
- `--require-approval` (default: True): Require human approval

**Example**:
```bash
auto-deploy-bot deploy_with_approval \
  --website-id summer-hair-2026 \
  --project-path ~/projects/summer-hair \
  --vercel-project-name summer-hair
```

### search_cheapest_domain

Find affordable domains across registrars.

**Options**:
- `--website-id` (required): Identifier
- `--business-name` (required): Business name
- `--business-type` (required): Type (Salon, Restaurant, etc.)
- `--max-price` (default: 50): Max price per year
- `--preferred-tld` (default: .com, .io): TLD preferences
- `--registrars` (default: namecheap, porkbun): Registrars to search
- `--require-approval` (default: True): Require approval

**Example**:
```bash
auto-deploy-bot search_cheapest_domain \
  --website-id summer-hair \
  --business-name "Summer Street Hair" \
  --business-type Salon \
  --max-price 50 \
  --preferred-tld .com .io \
  --registrars namecheap porkbun
```

### buy_domain_with_approval

Purchase domain from registrar.

**Options**:
- `--domain` (required): Domain to buy
- `--registrar` (default: namecheap): Which registrar
- `--years` (default: 1): Years to register
- `--auto-renew` (default: True): Auto-renew enabled
- `--privacy-protection` (default: True): Privacy enabled
- `--require-approval` (default: True): Require approval

**Example**:
```bash
auto-deploy-bot buy_domain_with_approval \
  --domain summerstassalon.com \
  --registrar namecheap \
  --years 1 \
  --privacy-protection \
  --auto-renew
```

### configure_domain_dns

Point domain to Vercel deployment.

**Options**:
- `--domain` (required): Domain to configure
- `--registrar` (default: namecheap): Registrar
- `--vercel-project` (required): Vercel project name
- `--require-approval` (default: True): Require approval

### deploy_and_buy_complete

Full automated workflow.

**Options**:
- `--website-id` (required): Website ID
- `--project-path` (required): Project path
- `--business-name` (required): Business name
- `--business-type` (required): Business type
- `--max-domain-price` (default: 50): Budget
- `--auto-renew-domain` (default: True): Auto-renew
- `--require-approval-at-each-step` (default: True): Gates

### batch_deploy_with_domains

Deploy multiple websites.

**Options**:
- `--websites-json` (required): JSON file with websites
- `--require-approval` (default: True): Require approval
- `--batch-approval` (default: False): Batch or individual gates

### deployment_status

Check deployment status.

**Options**:
- `--website-id` (required): Website ID to check

## Permission Gates

### How Permission Gates Work

Every critical operation asks for human approval. The workflow:

```
Action Requested
    ↓
Show all details (cost, domain, timeline)
    ↓
Ask for approval: "Approve? (yes/no)"
    ↓
User responds
    ↓
Log decision to approval history
    ↓
Execute if approved
    ↓
Check for double-spend protection
```

### Approval Gate Flow

```
APPROVAL REQUIRED
=================================================
Action: deploy_to_vercel
Details:
  project: summer-hair
  path: /workspace/summer-hair
  timeout: 300
  
Approve this action? (yes/no)
> yes
✅ Approved

[Execute action]

✅ Deployment complete!
```

### Purchase Gate Example

```
APPROVAL REQUIRED
=================================================
Action: purchase_domain
Details:
  domain: summerstassalon.com
  registrar: namecheap
  price: 8.99
  total: 8.99
  privacy: Enabled (+$2.99/year)
  
Approve this action? (yes/no)
> yes
✅ Approved

[Processing purchase...]

✅ Purchased: summerstassalon.com
```

### Double-Spend Protection

The system checks if you already purchased this domain recently:

- Prevents accidental duplicate purchases
- Checks registrar account for existing domains
- Logs all approval decisions with timestamps
- Can cancel at any time

### Approval History

All approvals are logged to `.approval_log.json`:

```json
[
  {
    "timestamp": "2026-03-14T18:45:00.123456",
    "action": "deploy_to_vercel",
    "details": { "project": "summer-hair" },
    "approved": true
  },
  {
    "timestamp": "2026-03-14T18:50:00.123456",
    "action": "purchase_domain",
    "details": {
      "domain": "summerstassalon.com",
      "price": 8.99
    },
    "approved": true
  }
]
```

## Registrar Support

### Namecheap (Recommended)

**Pros**:
- Cheapest domains
- Good API documentation
- Reliable service
- Included privacy protection

**Pricing** (sample):
- .com: $8.88/year
- .io: $48.88/year
- .co: $19.88/year

**Setup**:
```bash
export NAMECHEAP_API_KEY=your_key
export NAMECHEAP_API_USER=your_user
```

### Porkbun

**Pros**:
- Affordable prices
- Great customer support
- Simple API

**Pricing** (sample):
- .com: $8.74/year
- .io: $45.00/year
- .co: $19.00/year

**Setup**:
```bash
export PORKBUN_API_KEY=your_key
export PORKBUN_SECRET_API_KEY=your_secret
```

### GoDaddy

**Pros**:
- Largest inventory
- Popular interface
- Many TLDs

**Pricing** (sample - higher):
- .com: $12.99/year
- .io: $59.99/year
- .co: $24.99/year

**Setup**:
```bash
export GODADDY_API_KEY=your_key
export GODADDY_API_SECRET=your_secret
```

### Route53 (AWS)

**Pros**:
- AWS integration
- Unified DNS management
- Enterprise-grade

**Pricing**: Varies by TLD
- .com: $12.00/year
- .io: $50.00/year

**Setup**:
```bash
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
```

## Examples

See `examples/` directory for complete working examples:

1. **example_deploy_with_approval.py** - Basic deployment
2. **example_search_domain.py** - Domain search
3. **example_auto_deploy_complete.py** - Full workflow
4. **example_batch_deploy.py** - Batch deployment

## Testing

### Run all tests

```bash
python -m pytest test_auto_deploy_bot.py -v
```

### Run specific test class

```bash
python -m pytest test_auto_deploy_bot.py::TestPermissionGates -v
```

### Run with coverage

```bash
python -m pytest test_auto_deploy_bot.py --cov=src --cov=registrars
```

### Run specific test

```bash
python -m pytest test_auto_deploy_bot.py::TestPermissionGates::test_approval_logging -v
```

## Troubleshooting

### Issue: "VERCEL_TOKEN not set"

**Solution**: Set your Vercel token in `.env`:
```bash
VERCEL_TOKEN=your_vercel_token_here
```

### Issue: Domain not found on registrar

**Solution**: The domain may already be registered:
1. Check domain at registrar website
2. Try different TLD (`.io` instead of `.com`)
3. Use `--preferred-tld .io .co` to try alternatives

### Issue: DNS not propagating

**Solution**: DNS can take 30-60 minutes:
1. Check DNS records are correct at registrar
2. Wait longer (don't re-configure yet)
3. Use `verify_propagation` command to check status

### Issue: Permission denied for Vercel deploy

**Solution**:
1. Check Vercel token has correct permissions
2. Verify project exists in Vercel
3. Check project path is correct

### Issue: Deployment timeout

**Solution**: Increase timeout:
```bash
auto-deploy-bot deploy_with_approval \
  --website-id my-project \
  --project-path /path \
  --vercel-project-name my-project \
  --deployment-timeout 600  # 10 minutes
```

### Issue: No domains found

**Solution**:
1. Check business name is valid
2. Try broader search (higher `--max-price`)
3. Check registrar API credentials
4. Check internet connection

## Security

### API Credentials

- Store credentials in `.env` file (in `.gitignore`)
- Never commit `.env` to version control
- Use environment variables for CI/CD
- Rotate API keys regularly

### Permission Gates

- Always require approval for purchases
- Log all approvals with timestamps
- Review approval history regularly
- Check for unusual activities

### Payment Security

- Registrar handles payment processing
- No credit card stored by this tool
- Enable registrar account security
- Use strong passwords

## Cost Control

### Budget Setting

Set maximum domain price:

```bash
--max-domain-price 50
```

The tool will only show domains under this price.

### Cost Comparison

The tool automatically shows prices from all registrars:

```
✅ Found 3 domains:

1. summerstassalon.com
   Price: $8.99/year
   Registrar: namecheap

2. summerhaircuts.io
   Price: $19.99/year
   Registrar: porkbun

3. summerstreethouse.com
   Price: $12.99/year
   Registrar: namecheap
```

### Batch Cost Estimation

Check total cost before approving batch:

```json
{
  "batch_id": "batch_20260314_001",
  "estimated_cost": 17.98,
  "websites": 2,
  "cost_per_website": 8.99
}
```

### Cost Tracking

Check costs in approval log:

```bash
grep "purchase_domain" .approval_log.json | jq '.[] | .details.total'
```

## Advanced Usage

### Custom Domain Suggestions

The tool generates suggestions from business name:

- Business: "Summer Street Hair"
- Suggestions:
  - summerstassalon.com
  - summerstassalon.io
  - summerstassalon.co
  - summerstreethouse.com
  - hairstudio.com

### Resumable Workflows

If a deployment is interrupted, resume it:

```bash
# Check status
auto-deploy-bot deployment_status --website-id my-project

# The tool will show what steps completed
# Run the command again to continue
```

### DNS Verification

Check if domain is live:

```bash
# Manual check
dig summerstassalon.com

# Or wait for automatic propagation:
auto-deploy-bot configure_domain_dns \
  --domain summerstassalon.com \
  --registrar namecheap \
  --vercel-project my-project
  # Tool will wait and verify
```

### Custom Registrar Pricing

Edit `src/price_optimizer.py` to customize pricing:

```python
self.base_prices = {
    "namecheap": {
        ".com": 8.88,  # Customize here
        ...
    }
}
```

### State Management

View all saved state:

```bash
cat .deployment_state/my-project.json
```

See [State Manager](src/state_manager.py) for details.

## Integration Examples

### With Claude WebDev

Deploy generated websites automatically:

```python
from auto_deploy_bot import deploy_and_buy_complete

result = deploy_and_buy_complete(
    website_id="generated-site-2026",
    project_path="/tmp/generated/",
    business_name="Local Business",
    business_type="Service",
    max_domain_price=50
)

# Get live domain
domain = result["domain"]
vercel_url = result["vercel_url"]
```

### With Stripe

Calculate domain costs and add to invoice:

```python
from src.price_optimizer import PriceOptimizer

optimizer = PriceOptimizer()
cost = optimizer.calculate_total_cost(
    domain="mybusiness.com",
    registrar="namecheap",
    years=1,
    privacy=True
)

# Add cost["total"] to customer invoice
stripe.Invoice.create(
    amount=int(cost["total"] * 100),  # cents
    description="Domain registration"
)
```

## License

This skill is provided as-is for OpenClaw users.

## Support

For issues, questions, or feature requests:
1. Check this README and troubleshooting section
2. Check approval log for recent operations
3. Run tests to verify setup: `pytest test_auto_deploy_bot.py`
4. Review state files in `.deployment_state/`

## Contributing

To improve this skill:
1. Add new registrar integrations in `registrars/`
2. Add tests in `test_auto_deploy_bot.py`
3. Update documentation
4. Submit improvements

---

**Created by Auto-Deploy Bot Skill Team**
**Version**: 1.0.0
**Last Updated**: 2026-03-14

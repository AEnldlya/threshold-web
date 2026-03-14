# Auto-Deploy Bot Skill

**Automated deployment and domain purchase bot with permission gates. Deploys to Vercel, searches for affordable domains, and buys the cheapest fit - but asks for approval before each major action.**

## Quick Start

```bash
# Deploy website and buy domain (with approval at each step)
auto-deploy-bot deploy_and_buy_complete \
  --website-id "my-salon" \
  --business-name "My Hair Salon" \
  --business-type "Salon" \
  --max-domain-price 50

# Just deploy to Vercel
auto-deploy-bot deploy_with_approval \
  --website-id "my-salon" \
  --project-path "/workspace/my-salon/"

# Search for cheapest domains
auto-deploy-bot search_cheapest_domain \
  --website-id "my-salon" \
  --business-name "My Hair Salon" \
  --business-type "Salon"

# Buy a specific domain
auto-deploy-bot buy_domain_with_approval \
  --domain "mysalon.com" \
  --registrar "namecheap"
```

## Commands

1. **deploy_with_approval** - Deploy to Vercel with permission gate
2. **search_cheapest_domain** - Find affordable domains across registrars
3. **buy_domain_with_approval** - Purchase domain with approval
4. **configure_domain_dns** - Point domain to Vercel deployment
5. **deploy_and_buy_complete** - Full workflow: deploy → search → buy → configure
6. **batch_deploy_with_domains** - Deploy multiple websites
7. **deployment_status** - Check status of deployments

## Features

✅ **Permission Gates at Every Step**
- Deploy to Vercel? [YES/NO]
- Search for domains? [YES/NO]
- Buy domain? [YES/NO] (shows price first)
- Configure DNS? [YES/NO]

✅ **Cost Control**
- Set max domain price
- Show prices before buying
- Prevent accidental purchases

✅ **Multiple Registrars**
- Namecheap (recommended)
- Porkbun
- GoDaddy
- Route53 (AWS)

✅ **Smart Domain Search**
- Generate suggestions from business name
- Check availability across registrars
- Compare prices
- Rank by fit + affordability

✅ **State Management**
- Track deployment steps
- Resume interrupted flows
- Rollback capability
- Audit trail of all decisions

## Environment Setup

```bash
# .env file (required)
VERCEL_TOKEN=your_vercel_token
NAMECHEAP_API_KEY=your_namecheap_key
NAMECHEAP_API_USER=your_namecheap_user
PORKBUN_API_KEY=your_porkbun_key
PORKBUN_SECRET_API_KEY=your_porkbun_secret
GODADDY_API_KEY=your_godaddy_key
GODADDY_API_SECRET=your_godaddy_secret
AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_aws_secret
```

## Installation

```bash
pip install -r requirements.txt
```

## Testing

```bash
# Run all 50+ unit tests
python -m pytest test_auto_deploy_bot.py -v

# Run specific test
python -m pytest test_auto_deploy_bot.py::TestPermissionGates -v

# Run with coverage
python -m pytest test_auto_deploy_bot.py --cov=src --cov=registrars
```

## Usage Examples

See `examples/` directory for complete examples:
- `example_deploy_with_approval.py` - Basic deployment
- `example_search_domain.py` - Domain search
- `example_auto_deploy_complete.py` - Full workflow
- `example_batch_deploy.py` - Batch deployment

## Documentation

Full documentation available in `README.md`.

## Safety Notes

⚠️ **This skill requires human approval before purchases**
- No domains will be bought without explicit approval
- All costs shown before confirmation
- Approval history logged with timestamps
- Rollback available for failed deployments

## Support

For issues, questions, or feature requests, see the README troubleshooting section.

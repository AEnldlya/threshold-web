# Installation Guide - Auto-Deploy Bot

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- Vercel CLI: `npm install -g vercel`
- Vercel account: https://vercel.com
- Domain registrar account (at least one of):
  - Namecheap (recommended)
  - Porkbun
  - GoDaddy
  - AWS (Route53)

## Step 1: Copy the Skill

The skill should be located at:
```
~/.openclaw/workspace/skills/auto-deploy-bot/
```

If not, copy it:
```bash
mkdir -p ~/.openclaw/workspace/skills/
cp -r auto-deploy-bot ~/.openclaw/workspace/skills/
cd ~/.openclaw/workspace/skills/auto-deploy-bot
```

## Step 2: Create Virtual Environment (Optional but Recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- anthropic (Claude API)
- vercel (Vercel CLI wrapper)
- requests (HTTP library)
- pydantic (Data validation)
- python-dotenv (Environment variables)
- dnspython (DNS resolution)
- boto3 (AWS integration)
- pytest (Testing framework)

## Step 4: Get API Credentials

### Vercel Token

1. Go to https://vercel.com/account/tokens
2. Create a new token
3. Copy the token

### Namecheap (Recommended)

1. Go to https://www.namecheap.com/support/api/
2. Enable API access
3. Generate API key
4. Copy API key and username

### Porkbun

1. Go to https://porkbun.com/account/api
2. Create API key and secret
3. Copy both

### GoDaddy

1. Go to https://developer.godaddy.com
2. Create API keys
3. Copy API key and secret

### AWS (Route53)

1. Go to https://aws.amazon.com/iam/
2. Create IAM user with Route53 permissions
3. Create access keys
4. Copy access key and secret key

## Step 5: Configure Environment Variables

Create `.env` file:

```bash
cp .env.example .env
```

Edit `.env` with your credentials:

```bash
nano .env  # or use your favorite editor
```

**Minimum required**:
```
VERCEL_TOKEN=your_vercel_token
NAMECHEAP_API_KEY=your_key
NAMECHEAP_API_USER=your_user
```

**All options**:
```
# Vercel
VERCEL_TOKEN=your_vercel_token

# Namecheap
NAMECHEAP_API_KEY=your_key
NAMECHEAP_API_USER=your_user

# Porkbun
PORKBUN_API_KEY=your_key
PORKBUN_SECRET_API_KEY=your_secret

# GoDaddy
GODADDY_API_KEY=your_key
GODADDY_API_SECRET=your_secret

# AWS
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
```

## Step 6: Verify Installation

Test that everything is working:

```bash
# Test CLI help
python auto_deploy_bot.py --help

# Run tests
python -m pytest test_auto_deploy_bot.py -v

# Run a specific test
python -m pytest test_auto_deploy_bot.py::TestPermissionGates -v
```

## Step 7: Test with Example

Run one of the included examples:

```bash
# Test deployment example
python examples/example_deploy_with_approval.py

# Test domain search example
python examples/example_search_domain.py

# Test complete workflow
python examples/example_auto_deploy_complete.py

# Test batch deployment
python examples/example_batch_deploy.py
```

## Step 8: First Deployment

Try deploying your first website:

```bash
auto-deploy-bot deploy_and_buy_complete \
  --website-id "my-test-site" \
  --project-path "/path/to/your/project" \
  --business-name "My Business" \
  --business-type "Salon" \
  --max-domain-price 50
```

## Troubleshooting

### Issue: Command not found

**Solution**: The script isn't in your PATH. Use full path:
```bash
python auto_deploy_bot.py deploy_with_approval ...
```

Or create a symlink:
```bash
ln -s $(pwd)/auto_deploy_bot.py /usr/local/bin/auto-deploy-bot
chmod +x /usr/local/bin/auto-deploy-bot
```

### Issue: "No module named 'src'"

**Solution**: Run from the skill directory:
```bash
cd ~/.openclaw/workspace/skills/auto-deploy-bot
python auto_deploy_bot.py ...
```

### Issue: "VERCEL_TOKEN not set"

**Solution**: Set your token:
```bash
export VERCEL_TOKEN=your_token
# Or add to .env file
```

### Issue: Tests fail

**Solution**: Check dependencies:
```bash
pip install -r requirements.txt --upgrade
pytest test_auto_deploy_bot.py -v --tb=short
```

### Issue: Domain registration fails

**Solution**: Check:
1. API credentials are correct
2. Domain is available (try different TLD)
3. Registrar account has sufficient balance
4. API is enabled in registrar account

## Configuration

### Default Settings

Create `.deployment_config.json`:

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

### Auto-Approval Rules

Create `.auto_approval.json` for automatic approvals:

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

## Security

### Protect Your Credentials

1. **Never commit .env file**
```bash
echo ".env" >> .gitignore
```

2. **Use environment variables for CI/CD**
```bash
export VERCEL_TOKEN=your_token
export NAMECHEAP_API_KEY=your_key
```

3. **Rotate API keys regularly**
- Change Vercel tokens
- Regenerate registrar API keys
- Update AWS access keys

4. **Restrict API key permissions**
- Namecheap: Only API access
- GoDaddy: Only Domain operations
- AWS: Only Route53 permissions

## Next Steps

1. Read the [README.md](README.md) for full documentation
2. Check [BUILD_SUMMARY.md](BUILD_SUMMARY.md) for feature details
3. Review examples in `examples/` directory
4. Deploy your first website!

## Getting Help

1. Check README.md troubleshooting section
2. Review test files for usage examples
3. Check approval log: `cat .approval_log.json`
4. Review state files: `cat .deployment_state/*.json`

## Upgrading

To update to latest version:

```bash
cd ~/.openclaw/workspace/skills/auto-deploy-bot
git pull  # If using git
pip install -r requirements.txt --upgrade
```

## Uninstalling

```bash
rm -rf ~/.openclaw/workspace/skills/auto-deploy-bot
```

---

**Installation Complete!** 🎉

You're ready to deploy websites and buy domains.

Start with: `python auto_deploy_bot.py --help`

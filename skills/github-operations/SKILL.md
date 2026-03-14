# GitHub Operations

**Manage your website repo, pull requests, issues, and CI/CD pipeline**

## What It Does

Use GitHub CLI to:
- Create issues for new website projects
- Manage pull requests and code reviews
- Check CI/CD status (Vercel deployments)
- Push commits automatically
- Manage branches for different clients
- Track project progress

## How to Use

### Check Vercel Deployment Status
```bash
gh run list --repo AEnldlya/summer-street-salon --limit 5
```

### Create Issue for New Website
```bash
gh issue create --repo AEnldlya/summer-street-salon \
  --title "Website: Sarah Chen Salon" \
  --body "Client: Sarah Chen, Service: Hair Salon, Budget: $2,500"
```

### Create Pull Request
```bash
gh pr create --repo AEnldlya/summer-street-salon \
  --title "Website: Sarah Chen Salon" \
  --body "Completed website for Sarah Chen's salon"
```

### View Recent Commits
```bash
gh repo view AEnldlya/summer-street-salon --web
```

### Check Deployment Status
```bash
gh run list --repo AEnldlya/summer-street-salon --workflow=Deploy --limit 1
```

## Setup

1. Have GitHub CLI installed: `gh --version`
2. Authenticate: `gh auth login`
3. Store your repo URL as env variable:
   ```bash
   export GITHUB_REPO="AEnldlya/summer-street-salon"
   ```

## Integration Points

- **With Airtable**: Create issue when prospect says YES
- **With Stripe**: Add payment link to issue description
- **With Telegram**: Notify when PR is merged (site deployed!)

## Commands in OpenClaw

```
/gh issue create "Website: [Client Name]"
/gh pr create "Website: [Client Name] - Completed"
/gh run check  # Check Vercel deployment status
```

## Useful Links

- GitHub CLI Docs: https://cli.github.com/
- Your Repo: https://github.com/AEnldlya/summer-street-salon
- Vercel Dashboard: https://vercel.com/dashboard

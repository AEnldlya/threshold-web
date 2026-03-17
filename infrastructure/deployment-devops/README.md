# Deployment & DevOps

## Next.js Project Template

```bash
# scripts/create-client-project.sh
#!/bin/bash

CLIENT_NAME=$1
DEST_DIR="./$CLIENT_NAME"

# Clone template
git clone git@github.com:yourorg/website-template.git "$DEST_DIR"
cd "$DEST_DIR"

# Update project name
sed -i "s/website-template/$CLIENT_NAME/g" package.json

# Create environment files
cp .env.example .env.local
cat > .env.production << EOF
NEXT_PUBLIC_SITE_URL=https://$CLIENT_NAME.com
NEXT_PUBLIC_GA_ID=G_XXXXXXXXXXXXXX
EOF

# Install dependencies
npm install

# Initialize git for client repo
git remote remove origin
git remote add origin "git@github.com:yourorg/$CLIENT_NAME.git"
git branch -M main
git push -u origin main

echo "✓ Project created for $CLIENT_NAME"
```

## Vercel Configuration

```json
// vercel.json
{
  "buildCommand": "npm run build",
  "outputDirectory": ".next",
  "env": {
    "NEXT_PUBLIC_SITE_URL": "@next_public_site_url",
    "NEXT_PUBLIC_GA_ID": "@next_public_ga_id"
  },
  "functions": {
    "api/**": {
      "maxDuration": 30
    }
  },
  "rewrites": [
    {
      "source": "/sitemap.xml",
      "destination": "/api/sitemap"
    },
    {
      "source": "/robots.txt",
      "destination": "/api/robots"
    }
  ],
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        {
          "key": "X-Content-Type-Options",
          "value": "nosniff"
        },
        {
          "key": "X-Frame-Options",
          "value": "SAMEORIGIN"
        },
        {
          "key": "X-XSS-Protection",
          "value": "1; mode=block"
        },
        {
          "key": "Referrer-Policy",
          "value": "strict-origin-when-cross-origin"
        },
        {
          "key": "Permissions-Policy",
          "value": "geolocation=(), microphone=(), camera=()"
        }
      ]
    },
    {
      "source": "/fonts/(.*)",
      "headers": [
        {
          "key": "Cache-Control",
          "value": "public, max-age=31536000, immutable"
        }
      ]
    },
    {
      "source": "/images/(.*)",
      "headers": [
        {
          "key": "Cache-Control",
          "value": "public, max-age=31536000, immutable"
        }
      ]
    },
    {
      "source": "/_next/static/(.*)",
      "headers": [
        {
          "key": "Cache-Control",
          "value": "public, max-age=31536000, immutable"
        }
      ]
    }
  ]
}
```

## Environment Variables

```bash
# .env.local (development)
NEXT_PUBLIC_SITE_URL=http://localhost:3000
NEXT_PUBLIC_GA_ID=G_DEV_XXXXXX

# .env.production (deployed)
NEXT_PUBLIC_SITE_URL=https://clientname.com
NEXT_PUBLIC_GA_ID=G_PROD_XXXXXX
SENDGRID_API_KEY=sg_xxxxx
STRIPE_PUBLIC_KEY=pk_live_xxxxx
```

## GitHub Actions CI/CD

```yaml
# .github/workflows/deploy.yml
name: Deploy to Vercel

on:
  push:
    branches:
      - main

env:
  VERCEL_ORG_ID: ${{ secrets.VERCEL_ORG_ID }}
  VERCEL_PROJECT_ID: ${{ secrets.VERCEL_PROJECT_ID }}

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Install dependencies
        run: npm install

      - name: Run linting
        run: npm run lint

      - name: Run tests
        run: npm run test

      - name: Build
        run: npm run build

      - name: Run quality checks
        run: npm run quality-check

      - name: Install Vercel CLI
        run: npm i -g vercel

      - name: Pull Vercel environment information
        run: vercel pull --yes --environment=production --token=${{ secrets.VERCEL_TOKEN }}

      - name: Build project artifacts
        run: vercel build --prod --token=${{ secrets.VERCEL_TOKEN }}

      - name: Deploy project artifacts to Vercel
        run: vercel deploy --prebuilt --prod --token=${{ secrets.VERCEL_TOKEN }}

      - name: Lighthouse CI
        uses: treosh/lighthouse-ci-action@v9
        with:
          configPath: './lighthouserc.json'
          temporaryPublicStorage: true
```

## Lighthouse Configuration

```json
// lighthouserc.json
{
  "ci": {
    "collect": {
      "url": [
        "https://staging.clientname.com"
      ],
      "numberOfRuns": 1,
      "settings": {
        "chromeFlags": "--no-sandbox"
      }
    },
    "upload": {
      "target": "temporary-public-storage"
    },
    "assert": {
      "preset": "lighthouse:recommended",
      "assertions": {
        "cumulative-layout-shift": ["error", {"maxNumericValue": 0.1}],
        "first-contentful-paint": ["error", {"maxNumericValue": 2500}],
        "largest-contentful-paint": ["error", {"maxNumericValue": 2500}],
        "categories:performance": ["error", {"minScore": 0.9}],
        "categories:accessibility": ["error", {"minScore": 0.95}],
        "categories:seo": ["error", {"minScore": 0.95}]
      }
    }
  }
}
```

## Domain Configuration

```markdown
# DNS Setup Instructions

## Vercel Default Domain
- No setup needed, automatically deployed

## Custom Domain (Cloudflare)
1. Add domain to Vercel project
2. Go to Cloudflare DNS settings
3. Create CNAME record:
   - Name: @ (root)
   - Value: cname.vercel-dns.com
   - TTL: Auto

## SSL Certificate
- Automatically provisioned by Vercel (Let's Encrypt)
- Force HTTPS in vercel.json

## Redirect Setup
- Add www to non-www in Cloudflare Rules
```

## Monitoring & Alerts

```tsx
// monitoring/alerts.ts
export async function monitorSite(domain: string) {
  const checks = {
    uptime: await checkUptime(domain),
    performance: await checkPerformance(domain),
    ssl: await checkSSL(domain),
    dns: await checkDNS(domain)
  };

  const alerts = [];
  
  if (checks.uptime < 99.9) {
    alerts.push({
      level: 'warning',
      message: `Uptime below 99.9% (${checks.uptime}%)`
    });
  }

  if (checks.performance.lcp > 2500) {
    alerts.push({
      level: 'warning',
      message: `LCP above 2.5s (${checks.performance.lcp}ms)`
    });
  }

  if (!checks.ssl.valid) {
    alerts.push({
      level: 'critical',
      message: 'SSL certificate invalid or expired'
    });
  }

  return { checks, alerts };
}
```

## Backup Strategy

```bash
# scripts/backup.sh
#!/bin/bash

DOMAIN=$1
BACKUP_DIR="./backups/$DOMAIN"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

mkdir -p "$BACKUP_DIR"

# Backup DNS records
vercel domains inspect "$DOMAIN" > "$BACKUP_DIR/dns_$TIMESTAMP.json"

# Backup environment variables
vercel env pull --production > "$BACKUP_DIR/env_$TIMESTAMP.env"

# Backup current git state
git bundle create "$BACKUP_DIR/git_$TIMESTAMP.bundle" HEAD

echo "✓ Backup created: $BACKUP_DIR"
```

## Rollback Procedure

```markdown
# Rollback Checklist

## Immediate (< 5 min)
- [ ] Notify client
- [ ] Identify last known good commit
- [ ] Check Vercel deployment history

## Execution (5-15 min)
1. In Vercel dashboard, promote previous deployment
2. Wait for DNS propagation (usually instant for Vercel)
3. Test critical paths (homepage, forms, animations)
4. Verify no data loss

## Post-Rollback (15-60 min)
1. Identify root cause
2. Document issue
3. Fix in development
4. Deploy to staging
5. Full QA before re-deploying to production

## If emergency data restore needed:
1. Contact Vercel support for backup access
2. Restore from latest backup
3. Re-deploy with restored data
```

## Implementation Checklist

- [ ] Vercel project configured
- [ ] Environment variables set
- [ ] GitHub Actions workflow created
- [ ] Lighthouse CI configured
- [ ] Domain DNS configured
- [ ] SSL certificate verified
- [ ] Monitoring alerts set up
- [ ] Backup strategy documented
- [ ] Rollback procedures tested
- [ ] Staging environment ready
- [ ] Analytics configured
- [ ] Error tracking (Sentry/similar)

# Browser Verification

**Verify businesses don't have websites using 6-point automated check**

## What It Does

Automate the business verification process:
- Check if business has website via Google search
- Verify Google Business Profile
- Check Facebook page
- Check Instagram bio
- Test direct domain
- Verify Yelp listing

## Setup

```bash
# Install browser automation tools
npm install -g puppeteer playwright

# Store API keys if needed
export GOOGLE_API_KEY="your_key"
```

## Verification Checks

### Check 1: Google Search
```bash
# Search: "[Business Name] [City] website"
# Pass: No website link in first 5 results
# Fail: Website found
```

### Check 2: Google Business Profile
```bash
# Search: business on Google Maps
# Pass: GBP exists but NO website link
# Fail: Website link in GBP
```

### Check 3: Facebook
```bash
# Find Facebook page
# Check "About" section
# Pass: No website URL listed
# Fail: Website URL in About
```

### Check 4: Instagram
```bash
# Find Instagram profile
# Check bio
# Pass: No website link in bio
# Fail: Website link in bio
```

### Check 5: Direct Domain
```bash
# Try .com domain
# Try .net domain
# Try [name]boston.com
# Try [name][city].com
# Pass: Domain doesn't load or is parked
# Fail: Website loads (business has site)
```

### Check 6: Yelp
```bash
# Search Yelp for business
# Check business listing
# Pass: No website link
# Fail: Website link in Yelp
```

## Automation Script

Create file: `verify-business.js`

```javascript
const puppeteer = require('puppeteer');

async function verifyBusiness(name, city) {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  
  const checks = {
    google: false,
    gbp: false,
    facebook: false,
    instagram: false,
    domain: false,
    yelp: false
  };
  
  // Check 1: Google Search
  try {
    await page.goto(`https://google.com/search?q="${name}+${city}+website"`);
    const hasWebsite = await page.$('[href*="website"]') !== null;
    checks.google = !hasWebsite; // PASS if NO website
  } catch (e) {
    checks.google = null; // Error
  }
  
  // Check 2: Direct Domain
  try {
    const domain = `${name.toLowerCase().replace(/\s/g, '')}.com`;
    const response = await page.goto(`https://${domain}`, { timeout: 5000 });
    checks.domain = response.status === 404; // PASS if 404
  } catch (e) {
    checks.domain = true; // Domain doesn't exist = pass
  }
  
  await browser.close();
  
  // Return results
  const passed = Object.values(checks).filter(v => v === true).length;
  const result = {
    business: name,
    city: city,
    checks: checks,
    passed: passed,
    verified: passed >= 5, // Need 5+ checks to pass
    timestamp: new Date()
  };
  
  return result;
}

module.exports = { verifyBusiness };
```

## Commands in OpenClaw

```
/verify "Sarah Chen Salon" "Boston"     # Run 6-point check
/verify-batch "restaurants.csv"         # Verify 100 businesses
/verify-report today                    # Show today's verifications
```

## Integration Points

- **With Airtable**: Save results to "Verified" table
- **With Telegram**: Alert when verification complete
- **With GitHub**: Create issue if business already has website (skip them)

## Sample Output

```json
{
  "business": "Sarah Chen Salon",
  "city": "Boston",
  "checks": {
    "google": true,
    "gbp": true,
    "facebook": true,
    "instagram": true,
    "domain": true,
    "yelp": true
  },
  "passed": 6,
  "verified": true,
  "timestamp": "2026-03-11T12:00:00Z"
}
```

## Daily Verification Workflow

1. Get list of 30 new businesses from Google Maps
2. Run automated 6-point check
3. Save results to Airtable "Verified" table
4. Filter to "Ready to Call" status
5. Send list to user: "Here are today's 15 verified businesses"

## Best Practices

✅ **Do:**
- Verify each business before calling
- Log results (Airtable timestamp)
- Re-verify monthly (some businesses add sites)
- Check multiple sources (don't trust one check)

❌ **Don't:**
- Call businesses with existing websites (waste of time)
- Assume no website if one check fails (verify all 6)
- Skip verification (low-quality prospects)

## Useful Tools

- Google Chrome DevTools: Inspect websites
- Playwright/Puppeteer: Automate verification
- Yelp API: Get business listings
- Google Maps API: Get business info

# Form-Filling Outreach Strategy

## Phase 1: Find Websites
- Search Google for each of the 30 Boston businesses
- Extract their website URLs
- Store in `business_websites.json`

## Phase 2: Scout Contact Forms
- Visit each website
- Identify contact form locations (usually /contact, footer, or built into page)
- Document form fields needed

## Phase 3: Auto-Fill Forms
- Use browser automation to visit each website
- Fill out contact form with pitch:
  - Name: "Website Design Studio"
  - Message: "Hi [Business Name], we're a local Boston web design team. We specialize in building professional websites for local businesses. Would you be interested in a website redesign for your business? We typically build and deploy in 3-5 days for $500. Let's chat!"
  - Email: andy@websiteagency.com (or your email)
  
## Phase 4: Track Responses
- Log which forms we submitted to
- Monitor email for responses
- Measure conversion rate by industry

## Tech
- Use Playwright / Puppeteer for form automation
- 5-minute delays between submissions (avoid spam detection)
- Log all submissions with timestamps

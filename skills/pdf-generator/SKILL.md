# PDF Generator

**Create professional proposals, invoices, and portfolio PDFs**

## What It Does

Generate PDFs for:
- Website proposals (send before payment)
- Invoices with Stripe payment link
- Portfolio case studies
- Website specifications
- Monthly maintenance reports

## Setup

```bash
npm install html-pdf puppeteer pdfkit
```

## Proposal PDF Template

Create file: `generate-proposal.js`

```javascript
const PDFDocument = require('pdfkit');
const fs = require('fs');

function generateProposal(client) {
  const doc = new PDFDocument({ size: 'A4' });
  const filename = `${client.name}_Proposal_$${client.price}.pdf`;
  
  doc.pipe(fs.createWriteStream(filename));
  
  // Header
  doc.fontSize(24).text('Website Proposal', { align: 'center' });
  doc.fontSize(12).text(`For: ${client.name}`, { align: 'center' });
  doc.moveDown();
  
  // Details
  doc.fontSize(12).text(`Business: ${client.business}`);
  doc.text(`Category: ${client.category}`);
  doc.text(`Date: ${new Date().toLocaleDateString()}`);
  doc.moveDown();
  
  // What's Included
  doc.fontSize(14).text('What\'s Included:', { underline: true });
  doc.fontSize(11).list([
    'Professional custom website design',
    'Mobile-responsive (phone/tablet/desktop)',
    'Contact form and lead capture',
    'Lighthouse 95+ performance',
    'WCAG AA accessibility',
    'Google Business Profile setup',
    'SSL security (HTTPS)',
    '1 month free maintenance'
  ]);
  doc.moveDown();
  
  // Timeline
  doc.fontSize(14).text('Timeline:', { underline: true });
  doc.fontSize(11).list([
    'Days 1-2: Discovery call + Figma design',
    'Days 3-5: Development & coding',
    'Days 6-7: Performance & accessibility audit',
    'Days 8-9: Client review & revisions',
    'Day 10: Deploy live + training'
  ]);
  doc.moveDown();
  
  // Pricing
  doc.fontSize(14).text('Investment:', { underline: true });
  doc.fontSize(12).text(`Website Build: $${client.price}`, { color: 'darkgreen' });
  if (client.maintenance) {
    doc.fontSize(11).text(`Monthly Maintenance: $${client.maintenance} (optional)`);
  }
  doc.moveDown(2);
  
  // Call to Action
  doc.fontSize(12).text('Next Steps:', { underline: true });
  doc.fontSize(11).text([
    '1. Review this proposal',
    '2. Click the payment link to secure your spot',
    '3. Schedule kickoff call',
    '4. We build your website'
  ].join('\n'));
  doc.moveDown(2);
  
  // Payment Link
  doc.fontSize(10).text('Payment Link:', { underline: true });
  doc.fontSize(10)
    .fillColor('blue')
    .text(client.paymentLink, { link: client.paymentLink })
    .fillColor('black');
  doc.moveDown();
  
  // Footer
  doc.fontSize(9).text('Questions? Call or email anytime.', { align: 'center' });
  doc.text('Andy Zhang | 603-306-7508 | Andy.li.zhang2010@gmail.com', { align: 'center' });
  
  doc.end();
  return filename;
}

module.exports = { generateProposal };
```

## Invoice PDF Template

```javascript
function generateInvoice(client, amount) {
  const doc = new PDFDocument({ size: 'A4' });
  const filename = `Invoice_${client.name}_${amount}.pdf`;
  
  doc.pipe(fs.createWriteStream(filename));
  
  // Header
  doc.fontSize(20).text('INVOICE', { align: 'center' });
  doc.moveDown();
  
  // Invoice Details
  doc.fontSize(10)
    .text(`Invoice #: INV-${Date.now()}`, 50, 150)
    .text(`Date: ${new Date().toLocaleDateString()}`, 50, 165)
    .text(`Due: ${new Date(Date.now() + 30*24*60*60*1000).toLocaleDateString()}`, 50, 180);
  
  doc.moveDown(2);
  
  // Bill To
  doc.fontSize(12).text('Bill To:', { underline: true });
  doc.fontSize(10)
    .text(client.name)
    .text(client.address || '')
    .text(client.email)
    .text(client.phone);
  
  doc.moveDown();
  
  // Line Items Table
  doc.fontSize(10)
    .text('Description', 50, 300)
    .text('Amount', 500, 300)
    .text('---');
  
  doc.text(`Professional Website Design & Development`, 50, 320);
  doc.text(`$${amount}`, 500, 320);
  
  doc.moveDown();
  
  // Total
  doc.fontSize(12).text(`Total Due: $${amount}`, { color: 'darkgreen' });
  doc.moveDown();
  
  // Payment Link
  doc.fontSize(10).text('Pay Online:', { underline: true });
  doc.fontSize(9)
    .fillColor('blue')
    .text(client.paymentLink, { link: client.paymentLink })
    .fillColor('black');
  
  doc.end();
  return filename;
}
```

## Portfolio Case Study

```javascript
function generateCaseStudy(website) {
  const doc = new PDFDocument();
  const filename = `CaseStudy_${website.clientName}.pdf`;
  
  doc.pipe(fs.createWriteStream(filename));
  
  doc.fontSize(16).text(`Case Study: ${website.clientName}`, { align: 'center' });
  doc.moveDown();
  
  doc.fontSize(12).text('The Challenge:');
  doc.fontSize(10).text(website.challenge);
  doc.moveDown();
  
  doc.fontSize(12).text('The Solution:');
  doc.fontSize(10).text(website.solution);
  doc.moveDown();
  
  doc.fontSize(12).text('Results:');
  doc.fontSize(10).list([
    `${website.monthlyVisitors} monthly visitors`,
    `${website.conversions}% conversion rate`,
    `${website.calls} calls from website`,
    `Lighthouse score: ${website.lighthouse}`,
  ]);
  
  doc.moveDown();
  doc.fontSize(10).text(`Website: ${website.url}`);
  
  doc.end();
  return filename;
}
```

## Commands in OpenClaw

```
/pdf proposal [client-name] $2500        # Generate proposal
/pdf invoice [client-name] $2500         # Generate invoice
/pdf case-study [website-slug]           # Generate case study
/pdf portfolio                           # Generate all case studies (for pitching)
```

## Integration Points

- **With Email**: Attach PDF to email
- **With Stripe**: Include payment link in invoice
- **With GitHub**: Save PDFs to client project folder

## Files to Generate

1. **Proposal PDF** → Send before payment (builds trust)
2. **Invoice PDF** → Send after completion (formality)
3. **Case Study PDF** → Portfolio for next prospect
4. **Portfolio PDF** → All case studies combined (pitching tool)

## Output Examples

```
Sarah Chen Proposal.pdf         → Send via email Day 1
Sarah Chen Invoice.pdf          → Send after site ready
CaseStudy_SarahChen.pdf        → Add to portfolio
PortfolioFull_2026-03.pdf      → Show prospects "here's our work"
```

## Useful Libraries

- **pdfkit**: Simple, flexible PDF generation
- **puppeteer**: Screenshot + PDF from HTML
- **html-pdf**: Convert HTML to PDF
- **jsPDF**: Client-side PDF generation

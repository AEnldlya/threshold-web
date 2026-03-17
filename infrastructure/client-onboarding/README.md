# Client Onboarding System

## Asset Collection Template

```markdown
# [Client Name] - Asset Collection

## Folder Structure
```
[Client Name]/
├── Brand/
│   ├── logo.png (transparent, 1000x1000px min)
│   ├── logo-variations/
│   │   ├── wordmark.png
│   │   ├── icon-only.png
│   │   └── lockup.png
│   ├── brand-guidelines.pdf
│   └── color-specs.txt (hex codes)
├── Photography/
│   ├── hero-images/
│   ├── product-shots/
│   ├── team/
│   └── process/
├── Content/
│   ├── homepage.txt
│   ├── services.txt
│   ├── about.txt
│   ├── testimonials.txt
│   └── contact-info.txt
└── References/
    ├── competitor-analysis.pdf
    ├── brand-inspiration-links.txt
    └── preferred-styles.txt
```

## Color Extraction Workflow

```tsx
// workflow/ColorExtraction.tsx
export function ColorExtractionWorkflow() {
  const [logo, setLogo] = useState(null);
  const [colors, setColors] = useState([]);

  return (
    <div className="color-workflow">
      <h2>Step 1: Upload Logo</h2>
      <input 
        type="file" 
        accept="image/*"
        onChange={(e) => {
          const file = e.target.files[0];
          // Extract colors using color-thief
          extractColors(file).then(setColors);
        }}
      />

      <h2>Step 2: Select Primary & Accent</h2>
      <div className="color-grid">
        {colors.map((color, i) => (
          <div 
            key={i}
            className="color-option"
            style={{ backgroundColor: color }}
            onClick={() => selectColors({ primary: color })}
          >
            {color}
          </div>
        ))}
      </div>

      <h2>Step 3: Generate Palette</h2>
      {/* Show generated CSS, Tailwind config, etc. */}
    </div>
  );
}
```

## Content Organization Checklist

```markdown
# Content Checklist

## Homepage
- [ ] Hero headline (120 characters max)
- [ ] Hero subheading (200 characters max)
- [ ] Primary CTA text
- [ ] 3-5 main value propositions
- [ ] 1-2 hero images or videos
- [ ] Social proof (testimonials, stats)

## Services/Products
- [ ] Service name
- [ ] Description (100-150 words)
- [ ] Key benefits (3-5 bullet points)
- [ ] Images per service
- [ ] Pricing (if applicable)

## About
- [ ] Company story (200-300 words)
- [ ] Mission statement
- [ ] Key team members with bios
- [ ] Company photos/video
- [ ] Contact information

## Contact
- [ ] Email address
- [ ] Phone number
- [ ] Physical address (if applicable)
- [ ] Social media links
- [ ] Business hours

## Photography Requirements
- [ ] Hero image: 1920x1080px minimum
- [ ] Product shots: 1200x800px minimum
- [ ] Team photos: 600x600px minimum
- [ ] All in high quality (not compressed)
- [ ] All properly licensed/owned
```

## Discovery Call Questions

```tsx
// forms/DiscoveryForm.tsx
export function DiscoveryCallForm() {
  return (
    <form className="discovery-form">
      <fieldset>
        <legend>Business Basics</legend>
        <label>
          Business Name
          <input type="text" required />
        </label>
        <label>
          Industry/Category
          <select required>
            <option>SaaS</option>
            <option>Luxury</option>
            <option>Food</option>
            {/* ... etc */}
          </select>
        </label>
        <label>
          Primary Service/Product
          <textarea required />
        </label>
        <label>
          Target Audience
          <textarea required />
        </label>
      </fieldset>

      <fieldset>
        <legend>Current State</legend>
        <label>
          <input type="checkbox" />
          We have no website
        </label>
        <label>
          <input type="checkbox" />
          We have a website but need redesign
        </label>
        <label>
          Do you have existing brand guidelines?
          <select required>
            <option>No</option>
            <option>Yes, we have a PDF</option>
            <option>Yes, we have a brand designer</option>
          </select>
        </label>
      </fieldset>

      <fieldset>
        <legend>Goals & Timeline</legend>
        <label>
          Primary goal for this website
          <textarea required />
        </label>
        <label>
          Desired launch date
          <input type="date" required />
        </label>
        <label>
          Budget range
          <select required>
            <option>$2,500 - $5,000</option>
            <option>$5,000 - $10,000</option>
            <option>$10,000+</option>
          </select>
        </label>
      </fieldset>

      <fieldset>
        <legend>Brand Preferences</legend>
        <label>
          Preferred design style
          <textarea placeholder="e.g., minimal, bold, luxury, playful" />
        </label>
        <label>
          Competitor websites you like
          <textarea placeholder="URLs of sites you admire" />
        </label>
        <label>
          Colors/fonts you love
          <textarea placeholder="Specific color codes, font names, etc." />
        </label>
      </fieldset>

      <button type="submit">Submit</button>
    </form>
  );
}
```

## Asset Verification Checklist

```tsx
// components/AssetVerification.tsx
export function AssetVerification({ client }) {
  const [verification, setVerification] = useState({
    logo: { uploaded: false, size: false, quality: false },
    photos: { count: 0, minimum: 5, passed: false },
    content: { complete: false, wordCount: 0 },
    colorSpecs: { provided: false, format: null }
  });

  return (
    <div className="verification">
      <h2>Asset Verification for {client.name}</h2>

      <section>
        <h3>Logo</h3>
        <label>
          <input type="checkbox" disabled={!verification.logo.uploaded} />
          Uploaded
        </label>
        <label>
          <input type="checkbox" disabled={!verification.logo.size} />
          1000x1000px minimum
        </label>
        <label>
          <input type="checkbox" disabled={!verification.logo.quality} />
          High quality (not compressed)
        </label>
      </section>

      <section>
        <h3>Photography ({verification.photos.count}/{verification.photos.minimum})</h3>
        <progress value={verification.photos.count} max={verification.photos.minimum} />
      </section>

      <section>
        <h3>Content</h3>
        <label>
          <input type="checkbox" disabled={!verification.content.complete} />
          All pages complete
        </label>
        <p>Word count: {verification.content.wordCount}</p>
      </section>

      <section>
        <h3>Brand Colors</h3>
        <label>
          <input type="checkbox" disabled={!verification.colorSpecs.provided} />
          Color specs provided ({verification.colorSpecs.format})
        </label>
      </section>

      <button 
        className={verification.allPassed ? 'ready' : 'incomplete'}
        disabled={!verification.allPassed}
      >
        {verification.allPassed ? 'Ready to Start Design' : 'Complete All Assets'}
      </button>
    </div>
  );
}
```

## Onboarding Timeline

```markdown
# Typical Onboarding Timeline

## Week 0 (Discovery)
- [ ] Discovery call (30-45 min)
- [ ] Send asset collection template
- [ ] Send brand guidelines questionnaire
- [ ] Schedule design kickoff

## Week 1 (Asset Collection)
- [ ] Client gathers assets
- [ ] Logo uploaded and verified
- [ ] Photos collected and organized
- [ ] Content outline created
- [ ] Color specs extracted

## Week 2 (Design Direction)
- [ ] Initial color palette shown
- [ ] Layout concepts presented
- [ ] Animation style proposals
- [ ] 3D element options
- [ ] Client feedback incorporated

## Week 3 (Development)
- [ ] Foundation built (starter kit customized)
- [ ] Assets optimized and integrated
- [ ] Animations implemented
- [ ] Content placed
- [ ] Staging URL ready

## Week 4 (Review)
- [ ] Client review and feedback
- [ ] Revisions made
- [ ] Final polish and optimization
- [ ] Accessibility audit
- [ ] Performance optimization

## Week 5 (Launch)
- [ ] Deploy to production
- [ ] DNS and SSL configured
- [ ] Analytics and tracking set up
- [ ] Client training (if needed)
- [ ] Support and monitoring
```

## Implementation Checklist

- [ ] Asset collection template created
- [ ] Logo color extraction tool built
- [ ] Content checklist documented
- [ ] Discovery form created
- [ ] Asset verification system
- [ ] Timeline template ready
- [ ] Onboarding email sequence
- [ ] Asset storage organized
- [ ] Client portal setup (optional)
- [ ] Regular check-in schedule

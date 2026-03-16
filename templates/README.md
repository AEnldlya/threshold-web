# Website Templates

A collection of website templates for local businesses.

---

## Template 1: Local Service Business (Barber/Salon)
**Based on:** Twisted Scissors - Hanover, NH

### Overview
A clean, straightforward website for a local service business. No fluff, no cringe - just the info customers need.

### Key Features
- Simple hero with business name and tagline
- Services with clear pricing
- Real customer reviews
- Hours and location prominently displayed
- Online booking CTA

### Content Structure

#### Hero Section
- Business location tagline (e.g., "Barber Shop in Hanover, NH")
- Main headline: "[What you do]. [Value prop]."
  - Example: "Good haircuts. Done right."
- Brief description of experience/qualifications
- Two CTAs: Primary (Book Now) + Secondary (See Services)

#### Services Section
- Grid of 3-4 main services
- Each service card:
  - Service name
  - Brief description (1 line)
  - Duration
  - Price
- "All Services" button

#### About Section
- Years of experience
- Location
- What makes you different (keep it simple)
- Key stats (years, rating, etc.)

#### Reviews Section
- Real customer testimonials
- Name, rating, date
- Keep it authentic - no fake reviews

#### Hours & Location
- Clear hours table
- Full address
- Phone number
- Simple map or address link

#### Footer
- Logo + brief tagline
- Hours
- Contact info
- Booking link

### Tone & Style
- **Tone:** Conversational, straightforward, no BS
- **Language:** Simple words, short sentences
- **Avoid:** Superlatives ("best," "finest"), all-caps, flowery language
- **Colors:** Neutral with one accent color (gold in this case)
- **Fonts:** Clean sans-serif, one display font for headlines

### Technical Stack
- Next.js + React
- Tailwind CSS
- Framer Motion (subtle animations only)
- Static export for easy hosting

---

## Template 2: Outdoor/Recreation Business
**Based on:** Outlook Farm - Norwich, VT

### Overview
A warm, inviting website for an outdoor business (farm, ranch, stables, etc.). Focus on the experience and the land.

### Key Features
- Full-screen hero image of the property
- Clear service offerings with pricing
- Photos of facilities and activities
- Information about the land/property
- Contact/booking CTAs

### Content Structure

#### Hero Section
- Location tagline
- Business name as main headline
- Brief description of what you offer
- Two CTAs: "Book a visit" + "See services"

#### Introduction Section
- Years in business
- Brief origin story (2-3 sentences)
- Link to full about page
- Photo of the property/activity

#### Services Section
- 3 main services with:
  - Photo
  - Service name
  - Brief description
  - Starting price
- Link to full services page

#### Feature Image Section
- Wide panoramic image of facilities
- Brief caption about what's shown

#### Land/Property Section
- Description of the property
- Key stats (acres, facilities, etc.)
- Photo of the land

#### Contact CTA
- Simple invitation to visit
- Contact button

### Tone & Style
- **Tone:** Warm, welcoming, down-to-earth
- **Language:** Simple, descriptive, no fancy words
- **Avoid:** "Excellence," "premier," "luxury," flowery descriptions
- **Colors:** Earth tones (greens, creams, browns)
- **Fonts:** Light weights for headlines, readable body text

### Technical Stack
- Next.js + React
- Tailwind CSS
- Framer Motion (scroll animations)
- Static export
- Regular `<img>` tags (not Next.js Image) for static hosting

---

## General Best Practices

### Do:
- Use real photos of your business
- Include real customer reviews
- Show clear pricing
- Make contact info easy to find
- Keep copy short and scannable
- Use white space

### Don't:
- Use stock photos
- Write long paragraphs
- Use all-caps text
- Add excessive animations
- Use words like "excellence," "finest," "premier"
- Make customers hunt for basic info (hours, location, pricing)

### Common Sections to Include:
1. Hero (who you are, what you do)
2. Services/Products
3. About (brief)
4. Reviews/Testimonials
5. Hours & Location
6. Contact/Booking CTA

### Colors That Work:
- **Service businesses:** Black, white, grey + one accent (gold, blue, etc.)
- **Outdoor businesses:** Earth tones (green, cream, brown, tan)
- **Food businesses:** Warm tones (red, orange, brown)
- **Professional services:** Navy, grey, white + accent

### Fonts That Work:
- **Headlines:** Clean sans-serif (Inter, Helvetica, etc.) or light weights
- **Body:** Readable sans-serif (Inter, system fonts)
- **Avoid:** Script fonts, decorative fonts, more than 2 fonts

---

## Repository Structure
```
/templates
  /barber-service       # Twisted Scissors template
  /outdoor-recreation   # Outlook Farm template
  README.md             # This file
```

## How to Use These Templates

1. Copy the relevant template folder
2. Replace all content with your own
3. Use your own photos
4. Update colors in tailwind.config.ts
5. Build and deploy

## Live Examples
- Barber/Service: https://twisted-scissors.example.com
- Outdoor/Recreation: https://outlook-farm.example.com

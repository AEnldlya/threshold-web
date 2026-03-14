# Industry-Specific Website Templates & Implementation Guide

## Quick Reference: Build Time & Features by Industry

### RESTAURANTS (3-5 days)
**Must-Have Features:**
- Menu display (PDF or interactive)
- Hours & location
- Photo gallery
- Online ordering (optional)
- Reservation system (optional)
- Reviews/testimonials

**Tech Stack:**
- Next.js + Tailwind
- Optional: Stripe for ordering
- Google Maps embed
- Image optimizations (food photos)

**Design Focus:**
- Large, appetizing food photos
- Clear CTA: "Reserve Table" or "Order Now"
- Mobile-optimized (customers check on phone)
- Google Business integration

**Pricing: $1,500-$3,000**

### SALONS & BARBER SHOPS (2-4 days)
**Must-Have Features:**
- Service menu with prices
- Staff profiles with photos
- Booking calendar
- Photo gallery of work
- Testimonials
- Hours & location

**Tech Stack:**
- Next.js + Tailwind
- Calendly or Acuity Scheduling integration
- Image gallery (before/after photos)

**Design Focus:**
- Showcase quality of work visually
- Easy appointment booking
- Mobile-friendly (high mobile traffic)
- Social proof (reviews, ratings)

**Pricing: $1,500-$2,500**

### PLUMBING & ELECTRICAL (2-3 days)
**Must-Have Features:**
- Service list
- Pricing estimates
- Emergency contact
- Testimonials & certifications
- Before/after photos
- Service area map

**Tech Stack:**
- Next.js + Tailwind
- Google Maps for service area
- Contact form → email notification
- Simple, fast loading (older demographic)

**Design Focus:**
- Professional, trustworthy appearance
- Certifications/licenses prominently displayed
- Clear emergency number
- Customer testimonials (social proof)
- Simple navigation (easy for older users)

**Pricing: $1,000-$2,000**

### PET GROOMING (2-3 days)
**Must-Have Features:**
- Service menu with prices
- Photo gallery (happy pets!)
- Booking system
- Staff profiles
- Testimonials
- FAQ
- Health/safety info

**Tech Stack:**
- Next.js + Tailwind
- Booking integration
- Image gallery optimized
- Mobile-first (pet owners use phones)

**Design Focus:**
- Cute, friendly design
- High-quality pet photos
- Easy booking
- Safety certifications
- Customer testimonials

**Pricing: $1,500-$2,500**

### DRY CLEANING & LAUNDRY (2-3 days)
**Must-Have Features:**
- Services offered
- Pricing
- Location & hours
- Online ordering (optional)
- Pickup/delivery info
- FAQ

**Tech Stack:**
- Next.js + Tailwind
- Contact form
- Simple, clean design
- Mobile responsive (busy customers)

**Design Focus:**
- Fast loading (busy demographic)
- Clear pricing
- Convenient ordering process
- Multiple locations support (if applicable)

**Pricing: $800-$1,500**

---

## TECHNICAL IMPLEMENTATION PATTERNS

### E-Commerce Pattern (Restaurant Ordering)

```typescript
// app/menu/page.tsx
import { getMenuItems } from '@/lib/db'
import { MenuItem } from '@/components/MenuItem'
import { CartSummary } from '@/components/CartSummary'

export const revalidate = 3600 // Revalidate hourly

export default async function MenuPage() {
  const items = await getMenuItems()
  
  return (
    <div className="flex gap-8">
      <div className="flex-1">
        <h1>Our Menu</h1>
        <div className="grid grid-cols-2 gap-4">
          {items.map(item => (
            <MenuItem key={item.id} item={item} />
          ))}
        </div>
      </div>
      <aside className="w-80">
        <CartSummary />
      </aside>
    </div>
  )
}

// components/MenuItem.tsx
'use client'

import { useCartStore } from '@/store/cart'

export function MenuItem({ item }) {
  const addItem = useCartStore(state => state.addItem)
  
  return (
    <div className="border rounded-lg p-4">
      <img src={item.image} alt={item.name} className="w-full h-40 object-cover" />
      <h3>{item.name}</h3>
      <p className="text-gray-600 text-sm">{item.description}</p>
      <div className="flex justify-between items-center mt-4">
        <span className="text-xl font-bold">${item.price}</span>
        <button
          onClick={() => addItem(item)}
          className="bg-blue-500 text-white px-4 py-2 rounded"
        >
          Add
        </button>
      </div>
    </div>
  )
}

// store/cart.ts
import { create } from 'zustand'

export const useCartStore = create((set) => ({
  items: [],
  
  addItem: (item) => set((state) => ({
    items: [...state.items, item],
  })),
  
  removeItem: (id) => set((state) => ({
    items: state.items.filter(i => i.id !== id),
  })),
  
  checkout: async (email) => {
    const state = useCartStore.getState()
    const response = await fetch('/api/orders', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        email,
        items: state.items,
        total: state.items.reduce((sum, i) => sum + i.price, 0),
      }),
    })
    
    if (response.ok) {
      set({ items: [] })
    }
  },
}))

// app/api/orders/route.ts
import { Stripe } from 'stripe'

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!)

export async function POST(req: Request) {
  const { email, items, total } = await req.json()
  
  // Create Stripe Checkout Session
  const session = await stripe.checkout.sessions.create({
    payment_method_types: ['card'],
    line_items: items.map(item => ({
      price_data: {
        currency: 'usd',
        product_data: {
          name: item.name,
          description: item.description,
        },
        unit_amount: Math.round(item.price * 100),
      },
      quantity: 1,
    })),
    mode: 'payment',
    customer_email: email,
    success_url: `${process.env.NEXT_PUBLIC_URL}/success?session_id={CHECKOUT_SESSION_ID}`,
    cancel_url: `${process.env.NEXT_PUBLIC_URL}/menu`,
  })
  
  return new Response(JSON.stringify({ sessionId: session.id }), {
    status: 200,
    headers: { 'Content-Type': 'application/json' },
  })
}
```

### Booking Calendar Pattern (Salon)

```typescript
// app/book/page.tsx
'use client'

import { useState } from 'react'
import { useQuery } from '@tanstack/react-query'
import { Calendar } from '@/components/Calendar'
import { TimeSlots } from '@/components/TimeSlots'

export default function BookingPage() {
  const [selectedDate, setSelectedDate] = useState<Date | null>(null)
  const [selectedTime, setSelectedTime] = useState<string | null>(null)
  const [selectedService, setSelectedService] = useState<string>('haircut')
  
  // Fetch available times for selected date
  const { data: availableTimes } = useQuery({
    queryKey: ['availableTimes', selectedDate, selectedService],
    queryFn: () =>
      fetch(`/api/availability?date=${selectedDate}&service=${selectedService}`)
        .then(r => r.json()),
    enabled: !!selectedDate,
  })
  
  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault()
    
    const formData = new FormData(e.currentTarget)
    const response = await fetch('/api/bookings', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        name: formData.get('name'),
        email: formData.get('email'),
        phone: formData.get('phone'),
        service: selectedService,
        date: selectedDate,
        time: selectedTime,
      }),
    })
    
    if (response.ok) {
      window.location.href = '/booking-confirmed'
    }
  }
  
  return (
    <div className="max-w-2xl mx-auto py-8">
      <h1 className="text-3xl font-bold mb-8">Book Appointment</h1>
      
      <form onSubmit={handleSubmit} className="space-y-6">
        {/* Service Selection */}
        <div>
          <label className="block text-sm font-medium mb-2">Service</label>
          <select
            value={selectedService}
            onChange={(e) => setSelectedService(e.target.value)}
            className="w-full border rounded-lg p-2"
          >
            <option value="haircut">Haircut ($25)</option>
            <option value="color">Hair Color ($60)</option>
            <option value="perm">Perm ($80)</option>
          </select>
        </div>
        
        {/* Date Selection */}
        <div>
          <label className="block text-sm font-medium mb-2">Date</label>
          <Calendar onSelect={setSelectedDate} />
        </div>
        
        {/* Time Selection */}
        {selectedDate && (
          <div>
            <label className="block text-sm font-medium mb-2">Time</label>
            <TimeSlots
              times={availableTimes || []}
              selected={selectedTime}
              onSelect={setSelectedTime}
            />
          </div>
        )}
        
        {/* Personal Info */}
        <div className="space-y-4">
          <input
            type="text"
            name="name"
            placeholder="Full Name"
            required
            className="w-full border rounded-lg p-2"
          />
          <input
            type="email"
            name="email"
            placeholder="Email"
            required
            className="w-full border rounded-lg p-2"
          />
          <input
            type="tel"
            name="phone"
            placeholder="Phone"
            required
            className="w-full border rounded-lg p-2"
          />
        </div>
        
        <button
          type="submit"
          disabled={!selectedTime}
          className="w-full bg-blue-500 text-white py-2 rounded-lg disabled:opacity-50"
        >
          Confirm Booking
        </button>
      </form>
    </div>
  )
}

// app/api/bookings/route.ts
import { db } from '@/lib/db'
import { sendEmail } from '@/lib/email'

export async function POST(req: Request) {
  const body = await req.json()
  
  // Save to database
  const booking = await db.booking.create({
    data: {
      name: body.name,
      email: body.email,
      phone: body.phone,
      service: body.service,
      date: new Date(body.date),
      time: body.time,
    },
  })
  
  // Send confirmation email
  await sendEmail({
    to: body.email,
    subject: 'Booking Confirmed',
    html: `
      <h1>Your appointment is confirmed!</h1>
      <p>Date: ${body.date}</p>
      <p>Time: ${body.time}</p>
      <p>Service: ${body.service}</p>
      <p>We look forward to seeing you!</p>
    `,
  })
  
  // Send notification to business
  await sendEmail({
    to: 'business@example.com',
    subject: 'New Booking',
    html: `<p>New booking from ${body.name}: ${body.service} at ${body.time}</p>`,
  })
  
  return new Response(JSON.stringify({ success: true }), {
    status: 201,
    headers: { 'Content-Type': 'application/json' },
  })
}
```

### Gallery Pattern (Before/After Photos)

```typescript
// app/gallery/page.tsx
'use client'

import { useState } from 'react'
import Image from 'next/image'
import { Lightbox } from '@/components/Lightbox'

const gallery = [
  {
    before: '/gallery/haircut-1-before.jpg',
    after: '/gallery/haircut-1-after.jpg',
    title: 'Color Transformation',
  },
  // ... more items
]

export default function GalleryPage() {
  const [selectedIndex, setSelectedIndex] = useState<number | null>(null)
  
  return (
    <div className="max-w-5xl mx-auto py-8">
      <h1 className="text-4xl font-bold mb-12 text-center">Our Work</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {gallery.map((item, idx) => (
          <div key={idx} className="cursor-pointer" onClick={() => setSelectedIndex(idx)}>
            <div className="relative h-96 bg-gray-200 rounded-lg overflow-hidden hover:opacity-90">
              {/* Before/After Slider */}
              <div className="relative w-full h-full">
                <Image
                  src={item.before}
                  alt={`${item.title} before`}
                  fill
                  className="object-cover"
                  sizes="(max-width: 768px) 100vw, 50vw"
                />
                <div className="absolute inset-0 left-1/2 overflow-hidden">
                  <Image
                    src={item.after}
                    alt={`${item.title} after`}
                    fill
                    className="object-cover"
                    sizes="(max-width: 768px) 50vw, 25vw"
                  />
                </div>
              </div>
              
              <div className="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black to-transparent p-4">
                <p className="text-white text-lg font-semibold">{item.title}</p>
              </div>
            </div>
          </div>
        ))}
      </div>
      
      {selectedIndex !== null && (
        <Lightbox
          items={gallery}
          index={selectedIndex}
          onClose={() => setSelectedIndex(null)}
        />
      )}
    </div>
  )
}
```

---

## CONVERSION OPTIMIZATION

### Key Elements for Each Industry

**Restaurants:**
- Hero image: Signature dish
- CTA: "Reserve Table Now" / "Order Online"
- Social proof: Latest reviews
- Menu PDF download

**Salons:**
- Hero image: Beautiful transformation
- CTA: "Book Appointment"
- Staff profiles with photos
- Before/after gallery

**Plumbing/Electric:**
- Hero text: "Emergency Service Available 24/7"
- CTA: "Call for Estimate"
- Certifications/licenses
- Customer testimonials
- Service area map

**Pet Grooming:**
- Hero image: Happy pets
- CTA: "Book Grooming"
- Photo gallery of happy customers
- Health certifications
- Staff profiles

---

## DEPLOYMENT STEPS

1. **Build locally** → Test on device
2. **Push to GitHub**
3. **Deploy to Vercel** → Free tier handles traffic
4. **Set up domain** → Point to Vercel
5. **Google Search Console** → Submit sitemap
6. **Google Business Profile** → Link website
7. **Enable analytics** → Vercel Analytics
8. **Backup setup** → Database backups if applicable

---

## PRICING BY INDUSTRY

| Industry | Basic | Custom | E-Commerce |
|----------|-------|--------|-----------|
| Restaurant | $1,500 | $2,500 | $4,000+ |
| Salon | $1,500 | $2,000 | $2,500 |
| Plumbing | $1,000 | $1,500 | - |
| Pet Grooming | $1,500 | $2,000 | $2,500 |
| Cleaning | $800 | $1,200 | $1,500 |

**Add for each feature:**
- Booking system: +$500
- E-commerce: +$1,000-2,000
- Admin dashboard: +$500
- Custom integrations: +$500-1,000

---

*Use these templates to cut build time by 50% and increase your profit margin.*

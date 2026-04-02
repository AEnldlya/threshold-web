'use client'

import Header from '@/components/Header'
import HeroAceternity from '@/components/HeroAceternity'
import Footer from '@/components/Footer'

export default function Home() {
  return (
    <main className="min-h-screen bg-navy">
      <Header />
      <HeroAceternity />
      <Footer />
    </main>
  )
}

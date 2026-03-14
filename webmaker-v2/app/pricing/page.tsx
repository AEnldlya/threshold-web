'use client';

import { useState } from 'react';
import { motion } from 'framer-motion';
import Link from 'next/link';
import { ArrowRight, Sparkles, Check, X } from 'lucide-react';
import ScrollProgress from '@/components/animations/ScrollProgress';
import MagneticButton from '@/components/animations/MagneticButton';
import TiltCard from '@/components/animations/TiltCard';

const plans = [
  {
    name: 'Starter',
    description: 'Perfect for small businesses just getting started',
    monthlyPrice: 2500,
    yearlyPrice: 2200,
    features: [
      { text: '5-page website', included: true },
      { text: 'Mobile responsive', included: true },
      { text: 'Basic SEO setup', included: true },
      { text: 'Contact form', included: true },
      { text: '2 revision rounds', included: true },
      { text: 'E-commerce functionality', included: false },
      { text: 'Custom animations', included: false },
      { text: 'CMS integration', included: false },
    ],
    popular: false,
  },
  {
    name: 'Professional',
    description: 'Best for growing businesses with specific needs',
    monthlyPrice: 3500,
    yearlyPrice: 3200,
    features: [
      { text: '10-page website', included: true },
      { text: 'Mobile responsive', included: true },
      { text: 'Advanced SEO', included: true },
      { text: 'Contact form + Map', included: true },
      { text: '3 revision rounds', included: true },
      { text: 'E-commerce (up to 50 products)', included: true },
      { text: 'Custom animations', included: true },
      { text: 'CMS integration', included: false },
    ],
    popular: true,
  },
  {
    name: 'Enterprise',
    description: 'For businesses needing comprehensive solutions',
    monthlyPrice: 5500,
    yearlyPrice: 5000,
    features: [
      { text: 'Unlimited pages', included: true },
      { text: 'Mobile responsive', included: true },
      { text: 'Enterprise SEO', included: true },
      { text: 'Advanced forms', included: true },
      { text: 'Unlimited revisions', included: true },
      { text: 'Full e-commerce', included: true },
      { text: 'Premium animations', included: true },
      { text: 'Custom CMS', included: true },
    ],
    popular: false,
  },
];

export default function PricingPage() {
  const [isYearly, setIsYearly] = useState(false);

  return (
    <div className="min-h-screen bg-background">
      <ScrollProgress />
      
      {/* Navigation */}
      <motion.nav className="fixed top-0 left-0 right-0 z-40 glass">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-20 items-center">
            <Link href="/" className="flex items-center space-x-2">
              <div className="w-10 h-10 rounded-xl bg-primary flex items-center justify-center">
                <Sparkles className="h-5 w-5 text-white" />
              </div>
              <span className="text-xl font-bold text-white">WebMaker AI</span>
            </Link>
            <div className="hidden md:flex items-center space-x-8">
              <Link href="/services" className="text-slate-300 hover:text-primary-light transition-colors">Services</Link>
              <Link href="/portfolio" className="text-slate-300 hover:text-primary-light transition-colors">Portfolio</Link>
              <Link href="/process" className="text-slate-300 hover:text-primary-light transition-colors">Process</Link>
              <Link href="/pricing" className="text-primary-light">Pricing</Link>
              <Link href="/about" className="text-slate-300 hover:text-primary-light transition-colors">About</Link>
              <MagneticButton>
                <Link href="/contact" className="bg-primary text-white px-6 py-3 rounded-lg font-semibold hover:bg-primary-dark transition-colors">
                  Get Started
                </Link>
              </MagneticButton>
            </div>
          </div>
        </div>
      </motion.nav>

      {/* Hero Section */}
      <section className="relative pt-32 pb-24 overflow-hidden">
        <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-primary-dark/20 via-background to-background"></div>
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="text-center max-w-3xl mx-auto"
          >
            <span className="text-primary font-semibold tracking-wider uppercase text-sm">Pricing</span>
            <h1 className="text-5xl md:text-6xl font-bold text-white mt-4 mb-6">
              Simple, Transparent Pricing
            </h1>
            <p className="text-xl text-slate-400">
              Choose the plan that fits your business. All plans include our 10-day delivery guarantee.
            </p>
          </motion.div>
        </div>
      </section>

      {/* Toggle */}
      <section className="pb-12">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-center items-center space-x-4">
            <span className={`text-sm font-medium ${!isYearly ? 'text-white' : 'text-slate-400'}`}>One-time</span>
            <button
              onClick={() => setIsYearly(!isYearly)}
              className="relative w-14 h-7 bg-surface rounded-full p-1 transition-colors"
            >
              <motion.div
                className="w-5 h-5 bg-primary rounded-full"
                animate={{ x: isYearly ? 28 : 0 }}
                transition={{ type: 'spring', stiffness: 500, damping: 30 }}
              />
            </button>
            <span className={`text-sm font-medium ${isYearly ? 'text-white' : 'text-slate-400'}`}>
              With maintenance <span className="text-primary">(Save 10%)</span>
            </span>
          </div>
        </div>
      </section>

      {/* Pricing Cards */}
      <section className="py-12 bg-surface">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid md:grid-cols-3 gap-8">
            {plans.map((plan, i) => (
              <motion.div
                key={i}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: i * 0.1 }}
              >
                <TiltCard tiltAmount={plan.popular ? 5 : 3}>
                  <div className={`relative bg-background border rounded-2xl p-8 h-full ${plan.popular ? 'border-primary' : 'border-slate-700'}`}>
                    {plan.popular && (
                      <div className="absolute -top-4 left-1/2 -translate-x-1/2 bg-primary text-white text-sm font-semibold px-4 py-1 rounded-full">
                        Most Popular
                      </div>
                    )}
                    <h3 className="text-2xl font-bold text-white mb-2">{plan.name}</h3>
                    <p className="text-slate-400 text-sm mb-6">{plan.description}</p>
                    <div className="mb-6">
                      <span className="text-4xl font-bold text-white">
                        ${isYearly ? plan.yearlyPrice : plan.monthlyPrice}
                      </span>
                      <span className="text-slate-400">{isYearly ? '/year' : ''}</span>
                    </div>
                    <ul className="space-y-3 mb-8">
                      {plan.features.map((feature, j) => (
                        <li key={j} className="flex items-center space-x-3">
                          {feature.included ? (
                            <Check className="h-5 w-5 text-primary flex-shrink-0" />
                          ) : (
                            <X className="h-5 w-5 text-slate-600 flex-shrink-0" />
                          )}
                          <span className={feature.included ? 'text-slate-300' : 'text-slate-500'}>
                            {feature.text}
                          </span>
                        </li>
                      ))}
                    </ul>
                    <MagneticButton>
                      <Link 
                        href="/contact" 
                        className={`block text-center w-full py-3 rounded-lg font-semibold transition-colors ${
                          plan.popular 
                            ? 'bg-primary text-white hover:bg-primary-dark' 
                            : 'border border-slate-600 text-white hover:border-primary hover:text-primary'
                        }`}
                      >
                        Get Started
                      </Link>
                    </MagneticButton>
                  </div>
                </TiltCard>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* FAQ */}
      <section className="py-24 bg-background">
        <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
          <motion.div 
            className="text-center mb-12"
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
          >
            <h2 className="text-3xl font-bold text-white">Frequently Asked Questions</h2>
          </motion.div>
          <div className="space-y-4">
            {[
              { q: 'What is included in the price?', a: 'Everything needed to get your site live: design, development, content upload, SEO setup, and deployment. Hosting is separate.' },
              { q: 'How long does it take?', a: 'Most websites are delivered in 10 business days from when we receive all necessary content and approvals.' },
              { q: 'Can I make changes after launch?', a: 'Yes. We provide training on how to update your site, or you can purchase our maintenance plan for ongoing support.' },
              { q: 'Do you offer refunds?', a: 'We offer a satisfaction guarantee. If you are not happy with the initial design, we will revise it or refund your deposit.' },
            ].map((faq, i) => (
              <motion.div
                key={i}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: i * 0.1 }}
                className="bg-surface border border-slate-700 rounded-xl p-6"
              >
                <h3 className="font-semibold text-white mb-2">{faq.q}</h3>
                <p className="text-slate-400">{faq.a}</p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-surface border-t border-slate-800 py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex flex-col md:flex-row justify-between items-center">
            <div className="flex items-center space-x-2 mb-4 md:mb-0">
              <div className="w-10 h-10 rounded-xl bg-primary flex items-center justify-center">
                <Sparkles className="h-5 w-5 text-white" />
              </div>
              <span className="text-xl font-bold text-white">WebMaker AI</span>
            </div>
            <p className="text-slate-500 text-sm">2024 WebMaker AI. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  );
}

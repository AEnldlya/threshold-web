'use client';

import { motion } from 'framer-motion';
import Link from 'next/link';
import { ArrowRight, Sparkles, Search, Palette, Code, Rocket, CheckCircle } from 'lucide-react';
import ScrollProgress from '@/components/animations/ScrollProgress';
import MagneticButton from '@/components/animations/MagneticButton';
import Counter from '@/components/animations/Counter';

const steps = [
  {
    icon: Search,
    title: 'Discovery',
    description: 'We start by understanding your business, goals, and target audience. This includes competitor analysis and keyword research.',
    duration: 'Day 1',
    details: ['Business analysis', 'Competitor research', 'Goal setting', 'Timeline planning']
  },
  {
    icon: Palette,
    title: 'Design',
    description: 'Our designers create mockups and prototypes. You will review and provide feedback before we move to development.',
    duration: 'Days 2-3',
    details: ['Wireframing', 'Visual design', 'Prototype review', 'Revision rounds']
  },
  {
    icon: Code,
    title: 'Development',
    description: 'We build your site with clean, modern code. Every site is responsive, fast, and SEO-optimized.',
    duration: 'Days 4-8',
    details: ['Frontend development', 'Responsive coding', 'Performance optimization', 'SEO setup']
  },
  {
    icon: Rocket,
    title: 'Launch',
    description: 'After final testing and your approval, we deploy your site and provide training on how to manage it.',
    duration: 'Days 9-10',
    details: ['Quality testing', 'Content upload', 'Domain setup', 'Go live']
  },
];

export default function ProcessPage() {
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
              <Link href="/process" className="text-primary-light">Process</Link>
              <Link href="/pricing" className="text-slate-300 hover:text-primary-light transition-colors">Pricing</Link>
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
            <span className="text-primary font-semibold tracking-wider uppercase text-sm">Our Process</span>
            <h1 className="text-5xl md:text-6xl font-bold text-white mt-4 mb-6">
              How We Work
            </h1>
            <p className="text-xl text-slate-400">
              A streamlined 10-day process from concept to launch. Transparent, efficient, and results-driven.
            </p>
          </motion.div>
        </div>
      </section>

      {/* Timeline */}
      <section className="py-24 bg-surface">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="relative">
            {/* Timeline Line */}
            <div className="absolute left-8 md:left-1/2 top-0 bottom-0 w-px bg-slate-700 md:-translate-x-px"></div>
            
            {steps.map((step, i) => (
              <motion.div
                key={i}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: i * 0.1 }}
                className={`relative flex items-start mb-16 ${i % 2 === 0 ? 'md:flex-row' : 'md:flex-row-reverse'}`}
              >
                {/* Icon */}
                <div className="absolute left-8 md:left-1/2 w-16 h-16 -translate-x-1/2 rounded-full bg-primary flex items-center justify-center z-10">
                  <step.icon className="h-8 w-8 text-white" />
                </div>
                
                {/* Content */}
                <div className={`ml-24 md:ml-0 md:w-1/2 ${i % 2 === 0 ? 'md:pr-16 md:text-right' : 'md:pl-16'}`}>
                  <span className="text-primary font-bold text-sm">{step.duration}</span>
                  <h3 className="text-2xl font-bold text-white mt-2 mb-4">{step.title}</h3>
                  <p className="text-slate-400 mb-4">{step.description}</p>
                  <ul className={`space-y-2 ${i % 2 === 0 ? 'md:ml-auto' : ''}`}>
                    {step.details.map((detail, j) => (
                      <li key={j} className={`flex items-center space-x-2 text-slate-300 ${i % 2 === 0 ? 'md:justify-end' : ''}`}>
                        {i % 2 !== 0 && <CheckCircle className="h-4 w-4 text-primary flex-shrink-0" />}
                        <span>{detail}</span>
                        {i % 2 === 0 && <CheckCircle className="h-4 w-4 text-primary flex-shrink-0" />}
                      </li>
                    ))}
                  </ul>
                </div>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Stats */}
      <section className="py-24 bg-background">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <motion.div 
            className="grid grid-cols-2 md:grid-cols-4 gap-8"
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
          >
            {[
              { value: 10, suffix: '', label: 'Days Average' },
              { value: 3, suffix: '', label: 'Revisions Included' },
              { value: 100, suffix: '%', label: 'Satisfaction Rate' },
              { value: 24, suffix: '/7', label: 'Support' },
            ].map((stat, i) => (
              <div key={i} className="text-center">
                <div className="text-4xl font-bold text-gradient mb-2">
                  <Counter end={stat.value} suffix={stat.suffix} />
                </div>
                <p className="text-slate-400">{stat.label}</p>
              </div>
            ))}
          </motion.div>
        </div>
      </section>

      {/* CTA */}
      <section className="py-24 bg-surface">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
          >
            <h2 className="text-4xl font-bold text-white mb-6">Ready to Start?</h2>
            <p className="text-xl text-slate-400 mb-10">Your new website could be live in just 10 days.</p>
            <MagneticButton>
              <Link href="/contact" className="bg-primary text-white text-lg px-10 py-4 rounded-lg font-semibold hover:bg-primary-dark transition-all inline-flex items-center space-x-2 group">
                <span>Get Started</span>
                <ArrowRight className="h-5 w-5 group-hover:translate-x-1 transition-transform" />
              </Link>
            </MagneticButton>
          </motion.div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-background border-t border-slate-800 py-16">
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

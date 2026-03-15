'use client';

import { motion } from 'framer-motion';
import Link from 'next/link';
import { ArrowRight, ExternalLink } from 'lucide-react';
import ScrollProgress from '@/components/animations/ScrollProgress';
import MagneticButton from '@/components/animations/MagneticButton';
import SpotlightCard from '@/components/animations/SpotlightCard';
import TiltCard from '@/components/animations/TiltCard';
import Logo from '@/components/Logo';

const projects = [
  { 
    title: 'Summer Street Hair Studio',
    category: 'Salon',
    description: 'Elegant website for an upscale Boston hair salon with online booking.',
    tags: ['Next.js', 'Tailwind', 'Framer Motion'],
    color: 'from-rose-500 to-pink-600'
  },
  { 
    title: 'Bella Vista Bistro',
    category: 'Restaurant',
    description: 'Warm, inviting website with menu display and reservation system.',
    tags: ['React', 'GSAP', 'Three.js'],
    color: 'from-amber-500 to-orange-600'
  },
  { 
    title: 'Quick Fix Plumbing',
    category: 'Services',
    description: 'Professional website emphasizing reliability and emergency services.',
    tags: ['Next.js', 'TypeScript', 'Vercel'],
    color: 'from-blue-500 to-cyan-600'
  },
  { 
    title: 'CareFirst Clinic',
    category: 'Medical',
    description: 'Clean, calming design for healthcare with appointment booking.',
    tags: ['React', 'Accessibility', 'HIPAA'],
    color: 'from-emerald-500 to-teal-600'
  },
  { 
    title: 'Urban Boutique',
    category: 'Retail',
    description: 'Stylish e-commerce ready website for a fashion boutique.',
    tags: ['Next.js', 'Stripe', 'CMS'],
    color: 'from-violet-500 to-purple-600'
  },
  { 
    title: 'Morning Brew Coffee',
    category: 'Cafe',
    description: 'Cozy, artisanal design for a local coffee shop.',
    tags: ['React', 'Animations', 'SEO'],
    color: 'from-amber-600 to-yellow-500'
  },
];

export default function PortfolioPage() {
  return (
    <div className="min-h-screen bg-background">
      <ScrollProgress />
      
      {/* Navigation */}
      <motion.nav className="fixed top-0 left-0 right-0 z-40 glass">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-20 items-center">
            <Link href="/">
              <Logo />
            </Link>
            <div className="hidden md:flex items-center space-x-8">
              <Link href="/services" className="text-slate-300 hover:text-primary-light transition-colors">Services</Link>
              <Link href="/portfolio" className="text-primary-light">Portfolio</Link>
              <Link href="/process" className="text-slate-300 hover:text-primary-light transition-colors">Process</Link>
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
            <span className="text-primary font-semibold tracking-wider uppercase text-sm">Portfolio</span>
            <h1 className="text-5xl md:text-6xl font-bold text-white mt-4 mb-6">
              Our Work
            </h1>
            <p className="text-xl text-slate-400">
              Explore websites we have built for local businesses across various industries.
            </p>
          </motion.div>
        </div>
      </section>

      {/* Projects Grid */}
      <section className="py-24 bg-surface">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            {projects.map((project, i) => (
              <motion.div
                key={i}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: i * 0.1 }}
              >
                <TiltCard tiltAmount={8}>
                  <SpotlightCard className="h-full">
                    <div className="bg-background border border-slate-700 rounded-2xl overflow-hidden h-full hover:border-primary/50 transition-colors group">
                      <div className={`aspect-video bg-gradient-to-br ${project.color} flex items-center justify-center`}>
                        <div className="w-20 h-20 rounded-2xl bg-white/20 backdrop-blur flex items-center justify-center">
                          <span className="text-3xl font-bold text-white">{project.title[0]}</span>
                        </div>
                      </div>
                      <div className="p-6">
                        <span className="text-primary text-sm font-medium">{project.category}</span>
                        <h3 className="text-xl font-semibold text-white mt-2 mb-3">{project.title}</h3>
                        <p className="text-slate-400 text-sm mb-4">{project.description}</p>
                        <div className="flex flex-wrap gap-2 mb-4">
                          {project.tags.map((tag, j) => (
                            <span key={j} className="text-xs bg-slate-700 text-slate-300 px-2 py-1 rounded">
                              {tag}
                            </span>
                          ))}
                        </div>
                        <button className="text-primary flex items-center space-x-2 group-hover:underline">
                          <span>View Project</span>
                          <ExternalLink className="h-4 w-4" />
                        </button>
                      </div>
                    </div>
                  </SpotlightCard>
                </TiltCard>
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
              { value: '47', label: 'Websites Built' },
              { value: '12', label: 'Industries Served' },
              { value: '94%', label: 'Client Satisfaction' },
              { value: '3', label: 'Years Experience' },
            ].map((stat, i) => (
              <div key={i} className="text-center">
                <div className="text-4xl font-bold text-gradient mb-2">{stat.value}</div>
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
            <h2 className="text-4xl font-bold text-white mb-6">Want a Website Like These?</h2>
            <p className="text-xl text-slate-400 mb-10">We can build one for your business in just 10 days.</p>
            <MagneticButton>
              <Link href="/contact" className="bg-primary text-white text-lg px-10 py-4 rounded-lg font-semibold hover:bg-primary-dark transition-all inline-flex items-center space-x-2 group">
                <span>Start Your Project</span>
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
            <Logo className="mb-4 md:mb-0" />
            <p className="text-slate-500 text-sm">2024 WebMaker AI. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  );
}

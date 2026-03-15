'use client';

import { motion } from 'framer-motion';
import Link from 'next/link';
import { ArrowRight, Globe, Zap, Shield, Code, Palette, Rocket, CheckCircle } from 'lucide-react';
import ScrollProgress from '@/components/animations/ScrollProgress';
import MagneticButton from '@/components/animations/MagneticButton';
import SpotlightCard from '@/components/animations/SpotlightCard';
import TiltCard from '@/components/animations/TiltCard';
import Logo from '@/components/Logo';

const fadeInUp = {
  initial: { opacity: 0, y: 20 },
  animate: { opacity: 1, y: 0 },
  transition: { duration: 0.5 }
};

export default function ServicesPage() {
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
              <Link href="/services" className="text-primary-light">Services</Link>
              <Link href="/portfolio" className="text-slate-300 hover:text-primary-light transition-colors">Portfolio</Link>
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
            <span className="text-primary font-semibold tracking-wider uppercase text-sm">Services</span>
            <h1 className="text-5xl md:text-6xl font-bold text-white mt-4 mb-6">
              What We Offer
            </h1>
            <p className="text-xl text-slate-400">
              End-to-end website solutions for local businesses. From discovery to deployment, we handle it all.
            </p>
          </motion.div>
        </div>
      </section>

      {/* Main Services */}
      <section className="py-24 bg-surface">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid md:grid-cols-2 gap-8">
            {[
              { 
                icon: Globe, 
                title: 'Website Development', 
                desc: 'Custom-built websites using Next.js, React, and modern technologies. Fast, responsive, and SEO-optimized.',
                features: ['Next.js 14', 'React Components', 'TypeScript', 'Tailwind CSS']
              },
              { 
                icon: Palette, 
                title: 'UI/UX Design', 
                desc: 'Beautiful, intuitive designs that convert visitors into customers. Mobile-first approach with accessibility in mind.',
                features: ['Figma Prototypes', 'Responsive Design', 'Accessibility', 'Brand Identity']
              },
              { 
                icon: Code, 
                title: 'AI Integration', 
                desc: 'Leverage artificial intelligence to automate content generation, image creation, and optimization.',
                features: ['AI Content', 'Image Generation', 'SEO Optimization', 'Analytics']
              },
              { 
                icon: Rocket, 
                title: 'Deployment & Hosting', 
                desc: 'One-click deployment to Vercel with custom domains, SSL certificates, and global CDN.',
                features: ['Vercel Hosting', 'Custom Domains', 'SSL/HTTPS', 'Global CDN']
              },
            ].map((service, i) => (
              <motion.div
                key={i}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: i * 0.1 }}
              >
                <TiltCard>
                  <SpotlightCard className="h-full">
                    <div className="bg-background border border-slate-700 rounded-2xl p-8 h-full hover:border-primary/50 transition-colors">
                      <div className="w-14 h-14 rounded-xl bg-primary/10 flex items-center justify-center mb-6">
                        <service.icon className="h-7 w-7 text-primary" />
                      </div>
                      <h3 className="text-2xl font-semibold text-white mb-4">{service.title}</h3>
                      <p className="text-slate-400 mb-6 leading-relaxed">{service.desc}</p>
                      <div className="flex flex-wrap gap-2">
                        {service.features.map((feature, j) => (
                          <span key={j} className="text-xs bg-primary/10 text-primary px-3 py-1 rounded-full">
                            {feature}
                          </span>
                        ))}
                      </div>
                    </div>
                  </SpotlightCard>
                </TiltCard>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Process Steps */}
      <section className="py-24 bg-background">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <motion.div 
            className="text-center mb-16"
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
          >
            <span className="text-primary font-semibold tracking-wider uppercase text-sm">How It Works</span>
            <h2 className="text-4xl font-bold text-white mt-4">Our Process</h2>
          </motion.div>

          <div className="grid md:grid-cols-4 gap-8">
            {[
              { step: '01', title: 'Discovery', desc: 'We learn about your business and goals' },
              { step: '02', title: 'Design', desc: 'Create mockups and get your approval' },
              { step: '03', title: 'Development', desc: 'Build your site with clean code' },
              { step: '04', title: 'Launch', desc: 'Deploy and hand over the keys' },
            ].map((item, i) => (
              <motion.div
                key={i}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: i * 0.1 }}
                className="text-center"
              >
                <div className="text-6xl font-bold text-primary/20 mb-4">{item.step}</div>
                <h3 className="text-xl font-semibold text-white mb-2">{item.title}</h3>
                <p className="text-slate-400">{item.desc}</p>
              </motion.div>
            ))}
          </div>
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
            <h2 className="text-4xl font-bold text-white mb-6">Ready to Get Started?</h2>
            <p className="text-xl text-slate-400 mb-10">Let us build your perfect website.</p>
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

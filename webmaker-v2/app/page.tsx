'use client';

import { motion } from 'framer-motion';
import Link from 'next/link';
import { ArrowRight, Globe, Zap, Shield, ChevronDown } from 'lucide-react';
import ScrollProgress from '@/components/animations/ScrollProgress';
import MagneticButton from '@/components/animations/MagneticButton';
import SpotlightCard from '@/components/animations/SpotlightCard';
import Counter from '@/components/animations/Counter';
import TiltCard from '@/components/animations/TiltCard';
import Logo from '@/components/Logo';

const fadeInUp = {
  initial: { opacity: 0, y: 20 },
  animate: { opacity: 1, y: 0 },
  transition: { duration: 0.5 }
};

const staggerContainer = {
  animate: {
    transition: {
      staggerChildren: 0.1
    }
  }
};

export default function HomePage() {
  return (
    <div className="min-h-screen bg-background">
      <ScrollProgress />
      
      {/* Navigation */}
      <motion.nav 
        className="fixed top-0 left-0 right-0 z-40 glass"
        initial={{ y: -100 }}
        animate={{ y: 0 }}
        transition={{ duration: 0.5 }}
      >
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-20 items-center">
            <Link href="/">
              <Logo />
            </Link>
            <div className="hidden md:flex items-center space-x-8">
              <Link href="/services" className="text-slate-300 hover:text-primary-light transition-colors">Services</Link>
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
      <section className="relative min-h-screen flex items-center justify-center overflow-hidden pt-20">
        <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-primary-dark/20 via-background to-background"></div>
        <div className="absolute inset-0">
          <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-primary/10 rounded-full blur-3xl animate-pulse-slow"></div>
          <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-primary-light/10 rounded-full blur-3xl animate-pulse-slow animate-delay-500"></div>
        </div>
        
        <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <motion.div
            variants={staggerContainer}
            initial="initial"
            animate="animate"
          >
            <motion.div 
              variants={fadeInUp}
              className="inline-flex items-center space-x-2 bg-primary/10 border border-primary/30 rounded-full px-4 py-2 mb-8"
            >
              <span className="w-2 h-2 rounded-full bg-primary animate-pulse"></span>
              <span className="text-primary-light text-sm font-medium">Now with AI-powered design</span>
            </motion.div>

            <motion.h1 
              variants={fadeInUp}
              className="text-5xl md:text-7xl font-bold text-white mb-6 leading-tight"
            >
              Build & Sell Websites
              <span className="block text-gradient mt-2">with Confidence</span>
            </motion.h1>
            
            <motion.p 
              variants={fadeInUp}
              className="text-xl text-slate-400 max-w-2xl mx-auto mb-10 leading-relaxed"
            >
              Discover local businesses without websites, generate stunning sites with AI, 
              and close deals—all in one beautifully crafted platform.
            </motion.p>
            
            <motion.div 
              variants={fadeInUp}
              className="flex justify-center space-x-4"
            >
              <MagneticButton strength={0.2}>
                <Link href="/contact" className="bg-primary text-white text-lg px-8 py-4 rounded-lg font-semibold hover:bg-primary-dark transition-all shadow-lg hover:shadow-primary/50 flex items-center space-x-2 group">
                  <span>Start Building</span>
                  <ArrowRight className="h-5 w-5 group-hover:translate-x-1 transition-transform" />
                </Link>
              </MagneticButton>
              <MagneticButton strength={0.2}>
                <Link href="/portfolio" className="border-2 border-slate-600 text-white text-lg px-8 py-4 rounded-lg font-semibold hover:border-primary hover:text-primary transition-all">
                  View Work
                </Link>
              </MagneticButton>
            </motion.div>
          </motion.div>
        </div>

        <motion.div 
          className="absolute bottom-10 left-1/2 -translate-x-1/2"
          animate={{ y: [0, 10, 0] }}
          transition={{ duration: 2, repeat: Infinity }}
        >
          <ChevronDown className="h-8 w-8 text-slate-500" />
        </motion.div>
      </section>

      {/* Stats Section */}
      <section className="py-24 bg-surface">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <motion.div 
            className="grid grid-cols-2 md:grid-cols-4 gap-8"
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.5 }}
          >
            {[
              { value: 3, suffix: '', label: 'Years Experience' },
              { value: 47, suffix: '', label: 'Websites Built' },
              { value: 94, suffix: '%', label: 'Client Retention' },
              { value: 12, suffix: '', label: 'Days Average Delivery' },
            ].map((stat, i) => (
              <TiltCard key={i} tiltAmount={5}>
                <div className="text-center p-6">
                  <div className="text-4xl md:text-5xl font-bold text-gradient mb-2">
                    <Counter end={stat.value} suffix={stat.suffix} />
                  </div>
                  <p className="text-slate-400">{stat.label}</p>
                </div>
              </TiltCard>
            ))}
          </motion.div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-24 bg-background">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <motion.div 
            className="text-center mb-16"
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
          >
            <span className="text-primary font-semibold tracking-wider uppercase text-sm">Features</span>
            <h2 className="text-4xl font-bold text-white mt-4">Everything You Need</h2>
            <p className="text-slate-400 mt-4 max-w-2xl mx-auto">
              A complete platform for website creation and sales
            </p>
          </motion.div>

          <div className="grid md:grid-cols-3 gap-8">
            {[
              { icon: Globe, title: 'Prospect Discovery', desc: 'Find local businesses without websites automatically using our intelligent search.' },
              { icon: Zap, title: 'AI Generation', desc: 'Generate professional websites in minutes with our cutting-edge AI technology.' },
              { icon: Shield, title: 'Easy Deployment', desc: 'One-click deployment to Vercel with custom domains and SSL included.' },
            ].map((feature, i) => (
              <motion.div
                key={i}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: i * 0.1 }}
              >
                <SpotlightCard className="h-full">
                  <div className="bg-surface border border-slate-700 rounded-2xl p-8 h-full hover:border-primary/50 transition-colors">
                    <div className="w-14 h-14 rounded-xl bg-primary/10 flex items-center justify-center mb-6">
                      <feature.icon className="h-7 w-7 text-primary" />
                    </div>
                    <h3 className="text-xl font-semibold text-white mb-3">{feature.title}</h3>
                    <p className="text-slate-400 leading-relaxed">{feature.desc}</p>
                  </div>
                </SpotlightCard>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-24 bg-surface">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6 }}
          >
            <h2 className="text-4xl md:text-5xl font-bold text-white mb-6">
              Ready to Start Your Journey?
            </h2>
            <p className="text-xl text-slate-400 mb-10 leading-relaxed">
              Join thousands of creators building beautiful websites and growing their businesses.
            </p>
            <MagneticButton>
              <Link href="/contact" className="bg-primary text-white text-lg px-10 py-4 rounded-lg font-semibold hover:bg-primary-dark transition-all shadow-lg hover:shadow-primary/50 inline-flex items-center space-x-2 group">
                <span>Create Free Account</span>
                <ArrowRight className="h-5 w-5 group-hover:translate-x-1 transition-transform" />
              </Link>
            </MagneticButton>
          </motion.div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-background border-t border-slate-800 py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid md:grid-cols-4 gap-12 mb-12">
            <div className="col-span-2">
              <Logo className="mb-4" />
              <p className="text-slate-400 max-w-sm">
                Building beautiful websites for local businesses with cutting-edge AI technology.
              </p>
            </div>
            <div>
              <h4 className="font-semibold text-white mb-4">Product</h4>
              <ul className="space-y-3 text-slate-400">
                <li><Link href="/services" className="hover:text-primary transition-colors">Services</Link></li>
                <li><Link href="/portfolio" className="hover:text-primary transition-colors">Portfolio</Link></li>
                <li><Link href="/pricing" className="hover:text-primary transition-colors">Pricing</Link></li>
              </ul>
            </div>
            <div>
              <h4 className="font-semibold text-white mb-4">Company</h4>
              <ul className="space-y-3 text-slate-400">
                <li><Link href="/about" className="hover:text-primary transition-colors">About</Link></li>
                <li><Link href="/contact" className="hover:text-primary transition-colors">Contact</Link></li>
              </ul>
            </div>
          </div>
          <div className="border-t border-slate-800 pt-8 flex flex-col md:flex-row justify-between items-center">
            <p className="text-slate-500 text-sm">2024 WebMaker AI. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  );
}

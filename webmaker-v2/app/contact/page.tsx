'use client';

import { useState } from 'react';
import { motion } from 'framer-motion';
import Link from 'next/link';
import { ArrowRight, MapPin, Phone, Mail, Clock, Send } from 'lucide-react';
import ScrollProgress from '@/components/animations/ScrollProgress';
import MagneticButton from '@/components/animations/MagneticButton';
import Logo from '@/components/Logo';

export default function ContactPage() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone: '',
    business: '',
    message: '',
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // Handle form submission
    console.log(formData);
  };

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
            <span className="text-primary font-semibold tracking-wider uppercase text-sm">Contact</span>
            <h1 className="text-5xl md:text-6xl font-bold text-white mt-4 mb-6">
              Get in Touch
            </h1>
            <p className="text-xl text-slate-400">
              Have a project in mind? We would love to hear from you. Send us a message 
              and we will respond as soon as possible.
            </p>
          </motion.div>
        </div>
      </section>

      {/* Contact Section */}
      <section className="py-24 bg-surface">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid lg:grid-cols-2 gap-16">
            {/* Contact Info */}
            <motion.div
              initial={{ opacity: 0, x: -30 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true }}
            >
              <h2 className="text-3xl font-bold text-white mb-6">Contact Information</h2>
              <p className="text-slate-400 mb-8">
                Fill out the form and our team will get back to you within 24 hours.
              </p>
              <div className="space-y-6">
                <div className="flex items-center space-x-4">
                  <div className="w-12 h-12 rounded-xl bg-primary/10 flex items-center justify-center">
                    <Phone className="h-5 w-5 text-primary" />
                  </div>
                  <div>
                    <p className="text-slate-400 text-sm">Phone</p>
                    <p className="text-white font-semibold">603 678 0701</p>
                  </div>
                </div>
                <div className="flex items-center space-x-4">
                  <div className="w-12 h-12 rounded-xl bg-primary/10 flex items-center justify-center">
                    <Mail className="h-5 w-5 text-primary" />
                  </div>
                  <div>
                    <p className="text-slate-400 text-sm">Email</p>
                    <p className="text-white font-semibold">studio.aureum.reachout@gmail.com</p>
                  </div>
                </div>
                <div className="flex items-center space-x-4">
                  <div className="w-12 h-12 rounded-xl bg-primary/10 flex items-center justify-center">
                    <MapPin className="h-5 w-5 text-primary" />
                  </div>
                  <div>
                    <p className="text-slate-400 text-sm">Address</p>
                    <p className="text-white font-semibold">123 Summer Street, Boston, MA 02110</p>
                  </div>
                </div>
                <div className="flex items-center space-x-4">
                  <div className="w-12 h-12 rounded-xl bg-primary/10 flex items-center justify-center">
                    <Clock className="h-5 w-5 text-primary" />
                  </div>
                  <div>
                    <p className="text-slate-400 text-sm">Hours</p>
                    <p className="text-white font-semibold">Mon-Fri: 9AM - 6PM EST</p>
                  </div>
                </div>
              </div>
            </motion.div>

            {/* Contact Form */}
            <motion.div
              initial={{ opacity: 0, x: 30 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true }}
            >
              <form onSubmit={handleSubmit} className="bg-background border border-slate-700 rounded-2xl p-8">
                <h3 className="text-2xl font-bold text-white mb-6">Send us a Message</h3>
                <div className="space-y-4">
                  <div>
                    <label className="block text-slate-400 text-sm mb-2">Your Name</label>
                    <input
                      type="text"
                      value={formData.name}
                      onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                      className="w-full px-4 py-3 rounded-lg bg-surface border border-slate-700 text-white focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition-all"
                      placeholder="John Doe"
                      required
                    />
                  </div>
                  <div>
                    <label className="block text-slate-400 text-sm mb-2">Email Address</label>
                    <input
                      type="email"
                      value={formData.email}
                      onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                      className="w-full px-4 py-3 rounded-lg bg-surface border border-slate-700 text-white focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition-all"
                      placeholder="john@example.com"
                      required
                    />
                  </div>
                  <div>
                    <label className="block text-slate-400 text-sm mb-2">Phone Number</label>
                    <input
                      type="tel"
                      value={formData.phone}
                      onChange={(e) => setFormData({ ...formData, phone: e.target.value })}
                      className="w-full px-4 py-3 rounded-lg bg-surface border border-slate-700 text-white focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition-all"
                      placeholder="603 678 0701"
                    />
                  </div>
                  <div>
                    <label className="block text-slate-400 text-sm mb-2">Business Name</label>
                    <input
                      type="text"
                      value={formData.business}
                      onChange={(e) => setFormData({ ...formData, business: e.target.value })}
                      className="w-full px-4 py-3 rounded-lg bg-surface border border-slate-700 text-white focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition-all"
                      placeholder="Your Business"
                    />
                  </div>
                  <div>
                    <label className="block text-slate-400 text-sm mb-2">Message</label>
                    <textarea
                      value={formData.message}
                      onChange={(e) => setFormData({ ...formData, message: e.target.value })}
                      rows={4}
                      className="w-full px-4 py-3 rounded-lg bg-surface border border-slate-700 text-white focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition-all resize-none"
                      placeholder="Tell us about your project..."
                      required
                    />
                  </div>
                  <MagneticButton>
                    <button
                      type="submit"
                      className="w-full bg-primary text-white py-4 rounded-lg font-semibold hover:bg-primary-dark transition-all flex items-center justify-center space-x-2 group"
                    >
                      <span>Send Message</span>
                      <Send className="h-5 w-5 group-hover:translate-x-1 transition-transform" />
                    </button>
                  </MagneticButton>
                </div>
              </form>
            </motion.div>
          </div>
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

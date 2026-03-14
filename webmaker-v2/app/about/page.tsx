'use client';

import { motion } from 'framer-motion';
import Link from 'next/link';
import { ArrowRight, Sparkles, Target, Heart, Zap, Users } from 'lucide-react';
import ScrollProgress from '@/components/animations/ScrollProgress';
import MagneticButton from '@/components/animations/MagneticButton';
import Counter from '@/components/animations/Counter';
import TiltCard from '@/components/animations/TiltCard';

const values = [
  { icon: Target, title: 'Results Driven', desc: 'We measure success by your business growth, not just pretty pixels.' },
  { icon: Heart, title: 'Client First', desc: 'Your goals are our goals. We listen, adapt, and deliver beyond expectations.' },
  { icon: Zap, title: 'Fast Delivery', desc: 'Time is money. Our streamlined process gets you online in 10 days.' },
  { icon: Users, title: 'Partnership', desc: 'We are not just vendors, we are your long-term digital partners.' },
];

const team = [
  { name: 'Andy Zhang', role: 'Founder & Lead Developer', bio: 'Full-stack developer with 8+ years of experience building web applications.' },
  { name: 'Sarah Chen', role: 'UI/UX Designer', bio: 'Award-winning designer passionate about creating intuitive user experiences.' },
  { name: 'Mike Torres', role: 'SEO Specialist', bio: 'Digital marketing expert helping businesses rank higher on Google.' },
];

export default function AboutPage() {
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
              <Link href="/pricing" className="text-slate-300 hover:text-primary-light transition-colors">Pricing</Link>
              <Link href="/about" className="text-primary-light">About</Link>
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
            <span className="text-primary font-semibold tracking-wider uppercase text-sm">About Us</span>
            <h1 className="text-5xl md:text-6xl font-bold text-white mt-4 mb-6">
              Our Story
            </h1>
            <p className="text-xl text-slate-400">
              We are a team of developers, designers, and digital strategists passionate about 
              helping local businesses succeed online.
            </p>
          </motion.div>
        </div>
      </section>

      {/* Mission */}
      <section className="py-24 bg-surface">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid lg:grid-cols-2 gap-16 items-center">
            <motion.div
              initial={{ opacity: 0, x: -30 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true }}
            >
              <h2 className="text-4xl font-bold text-white mb-6">Our Mission</h2>
              <p className="text-slate-400 text-lg leading-relaxed mb-6">
                We believe every local business deserves a professional online presence. 
                In todays digital world, your website is often the first impression customers 
                have of your business. We are here to make sure it is a great one.
              </p>
              <p className="text-slate-400 text-lg leading-relaxed">
                Founded in 2021, WebMaker AI has helped dozens of businesses across Boston 
                and beyond establish their digital footprint. We combine cutting-edge technology 
                with old-fashioned customer service to deliver websites that not only look great 
                but drive real business results.
              </p>
            </motion.div>
            <motion.div
              initial={{ opacity: 0, x: 30 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true }}
              className="grid grid-cols-2 gap-6"
            >
              <div className="bg-background p-6 rounded-2xl text-center">
                <div className="text-4xl font-bold text-gradient mb-2">
                  <Counter end={3} />
                </div>
                <p className="text-slate-400">Years in Business</p>
              </div>
              <div className="bg-background p-6 rounded-2xl text-center">
                <div className="text-4xl font-bold text-gradient mb-2">
                  <Counter end={47} />
                </div>
                <p className="text-slate-400">Websites Built</p>
              </div>
              <div className="bg-background p-6 rounded-2xl text-center">
                <div className="text-4xl font-bold text-gradient mb-2">
                  <Counter end={12} />
                </div>
                <p className="text-slate-400">Industries Served</p>
              </div>
              <div className="bg-background p-6 rounded-2xl text-center">
                <div className="text-4xl font-bold text-gradient mb-2">
                  <Counter end={94} suffix="%" />
                </div>
                <p className="text-slate-400">Client Retention</p>
              </div>
            </motion.div>
          </div>
        </div>
      </section>

      {/* Values */}
      <section className="py-24 bg-background">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <motion.div 
            className="text-center mb-16"
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
          >
            <span className="text-primary font-semibold tracking-wider uppercase text-sm">Our Values</span>
            <h2 className="text-4xl font-bold text-white mt-4">What We Stand For</h2>
          </motion.div>
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
            {values.map((value, i) => (
              <motion.div
                key={i}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: i * 0.1 }}
              >
                <TiltCard tiltAmount={5}>
                  <div className="bg-surface border border-slate-700 rounded-2xl p-8 h-full hover:border-primary/50 transition-colors">
                    <div className="w-14 h-14 rounded-xl bg-primary/10 flex items-center justify-center mb-6">
                      <value.icon className="h-7 w-7 text-primary" />
                    </div>
                    <h3 className="text-xl font-semibold text-white mb-3">{value.title}</h3>
                    <p className="text-slate-400">{value.desc}</p>
                  </div>
                </TiltCard>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Team */}
      <section className="py-24 bg-surface">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <motion.div 
            className="text-center mb-16"
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
          >
            <span className="text-primary font-semibold tracking-wider uppercase text-sm">Our Team</span>
            <h2 className="text-4xl font-bold text-white mt-4">Meet the People Behind the Magic</h2>
          </motion.div>
          <div className="grid md:grid-cols-3 gap-8">
            {team.map((member, i) => (
              <motion.div
                key={i}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: i * 0.1 }}
                className="text-center"
              >
                <div className="w-32 h-32 mx-auto rounded-full bg-gradient-to-br from-primary to-primary-light mb-6"></div>
                <h3 className="text-xl font-semibold text-white">{member.name}</h3>
                <p className="text-primary mb-2">{member.role}</p>
                <p className="text-slate-400">{member.bio}</p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="py-24 bg-background">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
          >
            <h2 className="text-4xl font-bold text-white mb-6">Ready to Work Together?</h2>
            <p className="text-xl text-slate-400 mb-10">Lets build something amazing for your business.</p>
            <MagneticButton>
              <Link href="/contact" className="bg-primary text-white text-lg px-10 py-4 rounded-lg font-semibold hover:bg-primary-dark transition-all inline-flex items-center space-x-2 group">
                <span>Get in Touch</span>
                <ArrowRight className="h-5 w-5 group-hover:translate-x-1 transition-transform" />
              </Link>
            </MagneticButton>
          </motion.div>
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

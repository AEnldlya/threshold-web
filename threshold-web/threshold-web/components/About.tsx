'use client'

import { motion } from 'framer-motion'

const benefits = [
  { icon: '🎯', title: 'Conversion-Focused', text: 'Every element designed to drive action.' },
  { icon: '⚡', title: 'High Performance', text: 'Optimized for speed, built for scale.' },
  { icon: '♿', title: 'Accessible', text: 'WCAG AA compliant from day one.' },
  { icon: '🔍', title: 'SEO-Ready', text: 'Structured data and semantic HTML.' },
  { icon: '📱', title: 'Mobile First', text: 'Perfect on every device, every time.' },
  { icon: '🛡️', title: 'Secure & Safe', text: 'HTTPS, backups, and security best practices.' }
]

const testimonials = [
  {
    quote: 'They delivered a professional website in 10 days. It\'s exactly what we needed to grow.',
    author: 'Sarah Mitchell',
    role: 'Salon Owner',
    rating: 5
  },
  {
    quote: 'The attention to detail and speed of delivery set them apart. Highly recommended.',
    author: 'James Chen',
    role: 'Restaurant Manager',
    rating: 5
  },
  {
    quote: 'Finally, an agency that understands local business needs. Worth every penny.',
    author: 'Maria Rodriguez',
    role: 'Plumbing Service Owner',
    rating: 5
  }
]

export default function About() {
  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        staggerChildren: 0.1,
        delayChildren: 0.2,
      },
    },
  }

  const itemVariants = {
    hidden: { opacity: 0, y: 20 },
    visible: {
      opacity: 1,
      y: 0,
      transition: { duration: 0.6, ease: 'easeOut' },
    },
  }

  return (
    <section id="about" className="section-padding bg-white relative overflow-hidden">
      {/* Background decoration */}
      <div className="absolute top-0 left-0 w-96 h-96 bg-blue-100/20 rounded-full filter blur-3xl -z-10 -translate-x-1/2 -translate-y-1/2"></div>
      <div className="absolute bottom-0 right-0 w-96 h-96 bg-cyan-100/20 rounded-full filter blur-3xl -z-10 translate-x-1/2 translate-y-1/2"></div>

      <div className="container-max">
        {/* Header */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: '0px 0px -200px 0px' }}
          transition={{ duration: 0.8 }}
          className="text-center mb-16 md:mb-20"
        >
          <span className="inline-block px-4 py-2 rounded-full bg-blue-100/80 text-blue-700 text-sm font-medium mb-6 border border-blue-200/50">
            Why Choose Us
          </span>
          <h2 className="text-3xl md:text-4xl lg:text-5xl font-bold text-slate-900 mb-6">
            More Than Just a Website
            <span className="block text-slate-400">A Partnership Built to Grow</span>
          </h2>
        </motion.div>

        {/* Two column layout */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-16 mb-20">
          {/* Left: Why us */}
          <motion.div
            initial={{ opacity: 0, x: -40 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true, margin: '0px 0px -150px 0px' }}
            transition={{ duration: 0.8 }}
            className="space-y-6"
          >
            <h3 className="text-2xl md:text-3xl font-bold text-slate-900">
              We Build Websites That Convert
            </h3>
            <p className="text-lg text-slate-600 leading-relaxed">
              Every website we create is a strategic tool designed to help your business grow. We don't just build pretty sites—we build sites that turn visitors into customers.
            </p>

            <div className="space-y-4 py-6">
              <p className="text-slate-600 leading-relaxed">
                From your first call to launch day and beyond, we're invested in your success. Here's what makes us different:
              </p>
              <ul className="space-y-3">
                {[
                  'No templates or cookie-cutter designs',
                  'Custom design built specifically for your business',
                  'Proven performance metrics guaranteed',
                  'Full WCAG AA accessibility compliance',
                  'SEO-optimized from the ground up',
                  '30-day support included post-launch',
                  'Money-back guarantee if unsatisfied'
                ].map((item, index) => (
                  <motion.li
                    key={index}
                    initial={{ opacity: 0, x: -20 }}
                    whileInView={{ opacity: 1, x: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.5, delay: index * 0.05 }}
                    className="flex items-start gap-3"
                  >
                    <span className="text-blue-600 font-bold mt-1">✓</span>
                    <span className="text-slate-600">{item}</span>
                  </motion.li>
                ))}
              </ul>
            </div>

            <button
              onClick={() => document.getElementById('contact')?.scrollIntoView({ behavior: 'smooth' })}
              className="btn-primary w-full sm:w-auto mt-8"
            >
              Schedule Your Consultation →
            </button>
          </motion.div>

          {/* Right: Benefits grid */}
          <motion.div
            variants={containerVariants}
            initial="hidden"
            whileInView="visible"
            viewport={{ once: true, margin: '0px 0px -150px 0px' }}
            className="grid grid-cols-1 md:grid-cols-2 gap-6"
          >
            {benefits.map((benefit, index) => (
              <motion.div
                key={index}
                variants={itemVariants}
                whileHover={{ y: -4 }}
                className="group p-6 rounded-xl bg-gradient-to-br from-slate-50 to-slate-100/50 border border-slate-200/50 hover:border-blue-300/50 hover:shadow-lg transition-all duration-300"
              >
                <div className="text-4xl mb-3 group-hover:scale-110 transition-transform duration-300">
                  {benefit.icon}
                </div>
                <h4 className="font-bold text-slate-900 mb-2">{benefit.title}</h4>
                <p className="text-sm text-slate-600">{benefit.text}</p>
              </motion.div>
            ))}
          </motion.div>
        </div>

        {/* Testimonials section */}
        <motion.div
          initial={{ opacity: 0, y: 40 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: '0px 0px -200px 0px' }}
          transition={{ duration: 0.8 }}
          className="my-20 pt-20 border-t border-slate-200"
        >
          <div className="text-center mb-12">
            <h3 className="text-3xl md:text-4xl font-bold text-slate-900 mb-4">
              Loved by Local Businesses
            </h3>
            <p className="text-lg text-slate-600">
              See what our clients have to say
            </p>
          </div>

          <motion.div
            variants={containerVariants}
            initial="hidden"
            whileInView="visible"
            viewport={{ once: true, margin: '0px 0px -150px 0px' }}
            className="grid grid-cols-1 md:grid-cols-3 gap-8"
          >
            {testimonials.map((testimonial, index) => (
              <motion.div
                key={index}
                variants={itemVariants}
                whileHover={{ y: -6 }}
                className="group relative p-8 rounded-2xl bg-white border border-slate-200/50 hover:border-blue-300/50 hover:shadow-xl transition-all duration-300"
              >
                {/* Stars */}
                <div className="flex gap-1 mb-4">
                  {[...Array(testimonial.rating)].map((_, i) => (
                    <span key={i} className="text-xl">⭐</span>
                  ))}
                </div>

                {/* Quote */}
                <p className="text-slate-700 leading-relaxed mb-6">
                  "{testimonial.quote}"
                </p>

                {/* Author */}
                <div className="border-t border-slate-200 pt-4">
                  <p className="font-semibold text-slate-900">{testimonial.author}</p>
                  <p className="text-sm text-slate-600">{testimonial.role}</p>
                </div>

                {/* Hover effect */}
                <div className="absolute inset-0 rounded-2xl bg-gradient-to-br from-blue-500/5 to-cyan-500/5 opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none"></div>
              </motion.div>
            ))}
          </motion.div>
        </motion.div>

        {/* Stats section */}
        <motion.div
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true, margin: '0px 0px -150px 0px' }}
          transition={{ duration: 0.8 }}
          className="grid grid-cols-1 md:grid-cols-4 gap-8 py-12"
        >
          {[
            { number: '50+', label: 'Websites Delivered' },
            { number: '95+', label: 'Avg Lighthouse Score' },
            { number: '10', label: 'Days to Launch' },
            { number: '100%', label: 'Client Satisfaction' }
          ].map((stat, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6, delay: index * 0.1 }}
              className="text-center"
            >
              <div className="text-4xl md:text-5xl font-bold text-transparent bg-gradient-to-r from-blue-600 to-cyan-600 bg-clip-text mb-2">
                {stat.number}
              </div>
              <p className="text-slate-600 font-medium">{stat.label}</p>
            </motion.div>
          ))}
        </motion.div>
      </div>
    </section>
  )
}

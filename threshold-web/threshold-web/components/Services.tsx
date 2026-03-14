'use client'

import { motion } from 'framer-motion'

const services = [
  {
    icon: '⚡',
    title: 'High Performance',
    description: 'Lighthouse 95+ scores out of the box. Lightning-fast load times optimized for conversion.',
    features: ['<2s load time', 'Mobile optimized', 'Core Web Vitals ready']
  },
  {
    icon: '🎨',
    title: 'Custom Design',
    description: 'Bespoke, modern design tailored to your business. No templates, no compromises.',
    features: ['Brand-aligned', 'Conversion-focused', 'Timeless aesthetics']
  },
  {
    icon: '♿',
    title: 'Accessibility First',
    description: 'WCAG AA compliant. Keyboard navigation, screen readers, perfect contrast.',
    features: ['Full compliance', 'Keyboard nav', 'Screen reader ready']
  },
  {
    icon: '📱',
    title: 'Mobile Perfect',
    description: 'Responsive design built mobile-first. Perfect on phones, tablets, and desktops.',
    features: ['Responsive grid', '48px+ touch targets', 'Readable fonts']
  },
  {
    icon: '🔍',
    title: 'SEO Ready',
    description: 'Structured data, meta tags, semantic HTML. Built to rank from day one.',
    features: ['Schema markup', 'Meta optimization', 'Sitemap included']
  },
  {
    icon: '🚀',
    title: 'Fast Delivery',
    description: '10-day timeline from kickoff to launch. No lengthy projects or surprises.',
    features: ['Fixed timeline', 'Flat pricing', 'Full transparency']
  }
]

export default function Services() {
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
    <section id="services" className="section-padding bg-white relative overflow-hidden">
      {/* Background decoration */}
      <div className="absolute top-20 -left-40 w-80 h-80 bg-blue-100/20 rounded-full filter blur-3xl -z-10"></div>
      <div className="absolute -bottom-40 right-0 w-96 h-96 bg-cyan-100/20 rounded-full filter blur-3xl -z-10"></div>

      <div className="container-max">
        {/* Section header */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: '0px 0px -200px 0px' }}
          transition={{ duration: 0.8 }}
          className="text-center mb-16 md:mb-20"
        >
          <span className="inline-block px-4 py-2 rounded-full bg-blue-100/80 text-blue-700 text-sm font-medium mb-6 border border-blue-200/50">
            What We Deliver
          </span>
          <h2 className="text-3xl md:text-4xl lg:text-5xl font-bold text-slate-900 mb-6">
            Everything You Need
            <span className="block text-slate-400">to Stand Out Online</span>
          </h2>
          <p className="text-lg text-slate-600 max-w-2xl mx-auto leading-relaxed">
            Every website comes with professional design, high performance, and full accessibility. All for one fixed price.
          </p>
        </motion.div>

        {/* Service cards */}
        <motion.div
          variants={containerVariants}
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true, margin: '0px 0px -150px 0px' }}
          className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-16"
        >
          {services.map((service, index) => (
            <motion.div
              key={index}
              variants={itemVariants}
              whileHover={{ y: -8, transition: { duration: 0.3 } }}
              className="group relative p-8 rounded-2xl border border-slate-200/50 bg-white/50 backdrop-blur-sm hover:border-blue-300/50 hover:shadow-xl hover:shadow-blue-500/10 transition-all duration-300"
            >
              {/* Icon */}
              <div className="text-5xl mb-4 group-hover:scale-110 transition-transform duration-300">
                {service.icon}
              </div>

              {/* Content */}
              <h3 className="text-xl font-bold text-slate-900 mb-3">
                {service.title}
              </h3>
              <p className="text-slate-600 mb-6 leading-relaxed">
                {service.description}
              </p>

              {/* Features */}
              <ul className="space-y-2">
                {service.features.map((feature, idx) => (
                  <li key={idx} className="flex items-center gap-2 text-sm text-slate-600">
                    <span className="w-1.5 h-1.5 rounded-full bg-gradient-to-r from-blue-500 to-cyan-500"></span>
                    {feature}
                  </li>
                ))}
              </ul>

              {/* Hover effect */}
              <div className="absolute inset-0 rounded-2xl bg-gradient-to-br from-blue-500/5 to-cyan-500/5 opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none"></div>
            </motion.div>
          ))}
        </motion.div>

        {/* Pricing and timeline section */}
        <motion.div
          initial={{ opacity: 0, y: 40 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: '0px 0px -150px 0px' }}
          transition={{ duration: 0.8, delay: 0.2 }}
          className="bg-gradient-to-r from-slate-900 via-blue-900 to-slate-900 rounded-3xl p-8 md:p-12 text-white overflow-hidden relative"
        >
          {/* Background decoration */}
          <div className="absolute inset-0 bg-grid-white/10 -z-10"></div>

          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            {/* Pricing */}
            <motion.div
              initial={{ opacity: 0, x: -40 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.8, delay: 0.3 }}
            >
              <h3 className="text-3xl md:text-4xl font-bold mb-4">Simple Pricing</h3>
              <p className="text-xl text-blue-100 mb-8">
                One fixed price. No hidden fees. No surprises.
              </p>
              <div className="text-5xl md:text-6xl font-bold mb-4">
                $2,500
                <span className="text-lg text-blue-200 font-normal block mt-2">per website</span>
              </div>
              <p className="text-sm text-blue-200">
                ✓ Full design & development<br/>
                ✓ 10-day delivery<br/>
                ✓ Performance guarantee<br/>
                ✓ 30-day support
              </p>
            </motion.div>

            {/* Timeline */}
            <motion.div
              initial={{ opacity: 0, x: 40 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.8, delay: 0.3 }}
            >
              <h3 className="text-2xl font-bold mb-8">The 10-Day Timeline</h3>
              <div className="space-y-4">
                {[
                  { day: '1-2', phase: 'Discovery & Design', icon: '📋' },
                  { day: '3-5', phase: 'Development', icon: '💻' },
                  { day: '6-7', phase: 'Optimization', icon: '⚡' },
                  { day: '8-9', phase: 'Testing & Review', icon: '✅' },
                  { day: '10', phase: 'Launch', icon: '🚀' },
                ].map((item, idx) => (
                  <motion.div
                    key={idx}
                    initial={{ opacity: 0, x: 20 }}
                    whileInView={{ opacity: 1, x: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.5, delay: 0.4 + idx * 0.1 }}
                    className="flex items-center gap-4 pb-4 border-b border-blue-400/20 last:border-b-0"
                  >
                    <div className="text-2xl">{item.icon}</div>
                    <div>
                      <div className="font-semibold text-blue-300">{item.day}</div>
                      <div className="text-sm text-blue-100">{item.phase}</div>
                    </div>
                  </motion.div>
                ))}
              </div>
            </motion.div>
          </div>
        </motion.div>
      </div>
    </section>
  )
}

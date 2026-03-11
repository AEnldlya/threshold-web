'use client'

import { motion } from 'framer-motion'

const services = [
  {
    icon: '🎨',
    title: 'Custom Design',
    description: 'Bespoke design tailored to your business. Professional, modern, and conversion-focused.'
  },
  {
    icon: '⚡',
    title: 'High Performance',
    description: 'Lighthouse 95+ score. Lightning-fast load times. Optimized for mobile and desktop.'
  },
  {
    icon: '♿',
    title: 'Accessibility First',
    description: 'WCAG AA compliant. Your site works for everyone, everywhere.'
  },
  {
    icon: '📱',
    title: 'Fully Responsive',
    description: 'Perfect on mobile, tablet, and desktop. Built mobile-first from the ground up.'
  },
  {
    icon: '🔍',
    title: 'SEO Optimized',
    description: 'Structured data, meta tags, and semantic HTML. Built to rank.'
  },
  {
    icon: '🚀',
    title: 'Fast Delivery',
    description: '10-day timeline from kickoff to launch. No lengthy projects.'
  }
]

export default function Services() {
  return (
    <section id="services" className="py-20 px-6 bg-white">
      <div className="max-w-6xl mx-auto">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          viewport={{ once: true }}
          className="text-center mb-16"
        >
          <h2 className="heading-2 mb-4">What We Deliver</h2>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            Every website comes with professional design, high performance, and full accessibility.
          </p>
          <div className="mt-6 text-4xl font-bold text-amber-500">
            $2,500
            <span className="text-lg text-gray-600 font-normal ml-2">per website</span>
          </div>
        </motion.div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {services.map((service, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: index * 0.1 }}
              viewport={{ once: true }}
              whileHover={{ y: -5 }}
              className="p-8 border border-gray-200 rounded-lg hover:border-amber-500 hover:shadow-lg transition-all"
            >
              <div className="text-5xl mb-4">{service.icon}</div>
              <h3 className="text-xl font-bold text-navy mb-3">{service.title}</h3>
              <p className="text-gray-600 leading-relaxed">{service.description}</p>
            </motion.div>
          ))}
        </div>

        <motion.div
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          transition={{ duration: 0.8, delay: 0.3 }}
          viewport={{ once: true }}
          className="mt-16 bg-navy rounded-lg p-8 text-white"
        >
          <h3 className="text-2xl font-bold mb-4">The 10-Day Timeline</h3>
          <div className="grid grid-cols-1 md:grid-cols-5 gap-4">
            <div className="text-center">
              <div className="text-2xl font-bold text-amber-500 mb-2">1-2</div>
              <div className="text-sm">Discovery & Design</div>
            </div>
            <div className="text-center">
              <div className="text-2xl font-bold text-amber-500 mb-2">3-5</div>
              <div className="text-sm">Development</div>
            </div>
            <div className="text-center">
              <div className="text-2xl font-bold text-amber-500 mb-2">6-7</div>
              <div className="text-sm">Refinement</div>
            </div>
            <div className="text-center">
              <div className="text-2xl font-bold text-amber-500 mb-2">8-9</div>
              <div className="text-sm">Staging & Review</div>
            </div>
            <div className="text-center">
              <div className="text-2xl font-bold text-amber-500 mb-2">10</div>
              <div className="text-sm">Launch</div>
            </div>
          </div>
        </motion.div>
      </div>
    </section>
  )
}

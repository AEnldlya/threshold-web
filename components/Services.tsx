'use client'

import { motion } from 'framer-motion'

const services = [
  {
    icon: 'https://images.unsplash.com/photo-1561070791-2526d30994b5?w=500&h=500&fit=crop',
    title: 'Custom Design',
    description: 'Bespoke design tailored to your business. Professional, modern, and conversion-focused.'
  },
  {
    icon: 'https://images.unsplash.com/photo-1552664730-d307ca884978?w=500&h=500&fit=crop',
    title: 'High Performance',
    description: 'Lighthouse 95+ score. Lightning-fast load times. Optimized for mobile and desktop.'
  },
  {
    icon: 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=500&h=500&fit=crop',
    title: 'Accessibility First',
    description: 'WCAG AA compliant. Your site works for everyone, everywhere.'
  },
  {
    icon: 'https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=500&h=500&fit=crop',
    title: 'Fully Responsive',
    description: 'Perfect on mobile, tablet, and desktop. Built mobile-first from the ground up.'
  },
  {
    icon: 'https://images.unsplash.com/photo-1579403849066-db86b482c04f?w=500&h=500&fit=crop',
    title: 'SEO Optimized',
    description: 'Structured data, meta tags, and semantic HTML. Built to rank.'
  },
  {
    icon: 'https://images.unsplash.com/photo-1495521821757-a1efb6729352?w=500&h=500&fit=crop',
    title: 'Fast Delivery',
    description: '10-day timeline from kickoff to launch. No lengthy projects.'
  }
]

export default function Services() {
  return (
    <section id="services" className="py-20 px-6 bg-black">
      <div className="max-w-6xl mx-auto">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          viewport={{ once: true }}
          className="text-center mb-16"
        >
          <h2 className="text-4xl md:text-5xl font-bold text-white mb-4">What We Deliver</h2>
          <p className="text-xl text-gray-300 max-w-2xl mx-auto">
            Every website comes with professional design, high performance, and full accessibility.
          </p>
          <div className="mt-6 text-4xl font-bold text-yellow-400">
            $2,500
            <span className="text-lg text-gray-300 font-normal ml-2">per website</span>
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
              className="p-8 border border-gray-700 rounded-lg hover:border-yellow-400 hover:shadow-lg hover:shadow-yellow-400/20 transition-all bg-gray-900"
            >
              <img 
                src={service.icon} 
                alt={service.title}
                className="w-24 h-24 object-cover rounded-lg mb-4"
              />
              <h3 className="text-xl font-bold text-white mb-3">{service.title}</h3>
              <p className="text-gray-400 leading-relaxed">{service.description}</p>
            </motion.div>
          ))}
        </div>

        <motion.div
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          transition={{ duration: 0.8, delay: 0.3 }}
          viewport={{ once: true }}
          className="mt-16 bg-gray-900 rounded-lg p-8 text-white border border-gray-700"
        >
          <h3 className="text-2xl font-bold mb-4 text-yellow-400">The 10-Day Timeline</h3>
          <div className="grid grid-cols-1 md:grid-cols-5 gap-4">
            <div className="text-center">
              <div className="text-2xl font-bold text-yellow-400 mb-2">1-2</div>
              <div className="text-sm text-gray-300">Discovery & Design</div>
            </div>
            <div className="text-center">
              <div className="text-2xl font-bold text-yellow-400 mb-2">3-5</div>
              <div className="text-sm text-gray-300">Development</div>
            </div>
            <div className="text-center">
              <div className="text-2xl font-bold text-yellow-400 mb-2">6-7</div>
              <div className="text-sm text-gray-300">Refinement</div>
            </div>
            <div className="text-center">
              <div className="text-2xl font-bold text-yellow-400 mb-2">8-9</div>
              <div className="text-sm text-gray-300">Staging & Review</div>
            </div>
            <div className="text-center">
              <div className="text-2xl font-bold text-yellow-400 mb-2">10</div>
              <div className="text-sm text-gray-300">Launch</div>
            </div>
          </div>
        </motion.div>
      </div>
    </section>
  )
}

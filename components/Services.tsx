'use client'

import { motion } from 'framer-motion'

const services = [
  {
    image: 'https://images.pexels.com/photos/3194519/pexels-photo-3194519.jpeg?auto=compress&cs=tinysrgb&w=600',
    title: 'Custom Design',
    description: 'Bespoke design tailored to your business. Professional, modern, and conversion-focused.'
  },
  {
    image: 'https://images.pexels.com/photos/3182812/pexels-photo-3182812.jpeg?auto=compress&cs=tinysrgb&w=600',
    title: 'High Performance',
    description: 'Lighthouse 95+ score. Lightning-fast load times. Optimized for mobile and desktop.'
  },
  {
    image: 'https://images.pexels.com/photos/3944387/pexels-photo-3944387.jpeg?auto=compress&cs=tinysrgb&w=600',
    title: 'Accessibility First',
    description: 'WCAG AA compliant. Your site works for everyone, everywhere.'
  },
  {
    image: 'https://images.pexels.com/photos/788946/pexels-photo-788946.jpeg?auto=compress&cs=tinysrgb&w=600',
    title: 'Fully Responsive',
    description: 'Perfect on mobile, tablet, and desktop. Built mobile-first from the ground up.'
  },
  {
    image: 'https://images.pexels.com/photos/3945704/pexels-photo-3945704.jpeg?auto=compress&cs=tinysrgb&w=600',
    title: 'SEO Optimized',
    description: 'Structured data, meta tags, and semantic HTML. Built to rank.'
  },
  {
    image: 'https://images.pexels.com/photos/5632399/pexels-photo-5632399.jpeg?auto=compress&cs=tinysrgb&w=600',
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
              className="p-8 border border-gray-700 hover:border-yellow-400 hover:shadow-lg hover:shadow-yellow-400/20 transition-all bg-gray-900"
            >
              <img 
                src={service.image} 
                alt={service.title}
                className="w-full h-32 object-cover mb-6 border border-gray-600"
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
          className="mt-16 bg-gray-900 p-8 text-white border border-gray-700"
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

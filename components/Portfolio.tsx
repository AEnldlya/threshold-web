'use client'

import { motion } from 'framer-motion'

const projects = [
  {
    name: 'Summer Street Hair Studio',
    category: 'Salon',
    description: 'Professional hair salon website with booking system, service gallery, and team profiles.',
    metrics: {
      lighthouse: 96,
      performance: '2.1s LCP',
      accessibility: 'AA'
    }
  },
  {
    name: 'Example Plumbing Co.',
    category: 'Plumbing',
    description: 'Local plumbing service site with service overview, emergency callout, and testimonials.',
    metrics: {
      lighthouse: 94,
      performance: '1.8s LCP',
      accessibility: 'AA'
    }
  },
  {
    name: 'Local Restaurant',
    category: 'Restaurant',
    description: 'Restaurant site with menu, reservations, location, and online ordering integration.',
    metrics: {
      lighthouse: 95,
      performance: '2.2s LCP',
      accessibility: 'AA'
    }
  }
]

export default function Portfolio() {
  return (
    <section id="portfolio" className="py-20 px-6 bg-black">
      <div className="max-w-6xl mx-auto">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          viewport={{ once: true }}
          className="text-center mb-16"
        >
          <h2 className="text-4xl md:text-5xl font-bold text-white mb-4">Our Work</h2>
          <p className="text-xl text-gray-300 max-w-2xl mx-auto">
            Professional websites that deliver results. Every project meets our high standards for performance and accessibility.
          </p>
        </motion.div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {projects.map((project, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: index * 0.1 }}
              viewport={{ once: true }}
              className="bg-gray-900 rounded-lg overflow-hidden border border-gray-700 hover:shadow-xl hover:shadow-yellow-400/20 transition-shadow"
            >
              <div className="h-48 bg-gradient-to-br from-yellow-400 to-yellow-600 flex items-center justify-center">
                <div className="text-center text-black">
                  <div className="text-5xl mb-2">🌐</div>
                  <div className="text-lg font-bold">{project.name}</div>
                </div>
              </div>
              
              <div className="p-6">
                <div className="inline-block px-3 py-1 bg-yellow-400/20 text-yellow-400 rounded-full text-sm font-semibold mb-3">
                  {project.category}
                </div>
                <p className="text-gray-300 mb-4">{project.description}</p>
                
                <div className="space-y-2 text-sm">
                  <div className="flex justify-between items-center">
                    <span className="text-gray-400">Lighthouse Score</span>
                    <span className="font-bold text-yellow-400">{project.metrics.lighthouse}</span>
                  </div>
                  <div className="flex justify-between items-center">
                    <span className="text-gray-400">Performance</span>
                    <span className="font-bold text-yellow-400">{project.metrics.performance}</span>
                  </div>
                  <div className="flex justify-between items-center">
                    <span className="text-gray-400">Accessibility</span>
                    <span className="font-bold text-yellow-400">WCAG {project.metrics.accessibility}</span>
                  </div>
                </div>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  )
}

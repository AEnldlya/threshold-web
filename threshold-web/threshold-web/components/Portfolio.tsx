'use client'

import { motion } from 'framer-motion'

const projects = [
  {
    id: 1,
    name: 'Summer Street Hair Studio',
    category: 'Salon & Spa',
    tagline: 'Online booking & service showcase',
    description: 'Professional hair salon website with integrated booking system, service gallery, staff profiles, and customer testimonials.',
    image: '💇‍♀️',
    color: 'from-pink-500 to-rose-500',
    metrics: {
      lighthouse: 96,
      performance: '1.9s',
      accessibility: 'AA',
      users: '500+/mo'
    }
  },
  {
    id: 2,
    name: 'Example Plumbing Co.',
    category: 'Service',
    tagline: 'Emergency callout & service info',
    description: 'Local plumbing service site with service overview, emergency hotline, testimonials, and service area map.',
    image: '🔧',
    color: 'from-blue-500 to-cyan-500',
    metrics: {
      lighthouse: 95,
      performance: '1.8s',
      accessibility: 'AA',
      users: '300+/mo'
    }
  },
  {
    id: 3,
    name: 'Local Restaurant Group',
    category: 'Food & Beverage',
    tagline: 'Menu, reservations & ordering',
    description: 'Restaurant website with menu showcase, table reservations, location info, and integration with online ordering platforms.',
    image: '🍽️',
    color: 'from-orange-500 to-amber-500',
    metrics: {
      lighthouse: 94,
      performance: '2.1s',
      accessibility: 'AA',
      users: '800+/mo'
    }
  }
]

export default function Portfolio() {
  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        staggerChildren: 0.2,
        delayChildren: 0.1,
      },
    },
  }

  const itemVariants = {
    hidden: { opacity: 0, y: 40 },
    visible: {
      opacity: 1,
      y: 0,
      transition: { duration: 0.8, ease: 'easeOut' },
    },
  }

  return (
    <section id="portfolio" className="section-padding bg-gradient-to-b from-white via-blue-50/30 to-white relative overflow-hidden">
      {/* Background elements */}
      <div className="absolute top-40 right-0 w-96 h-96 bg-cyan-100/20 rounded-full filter blur-3xl -z-10"></div>
      <div className="absolute -bottom-40 left-10 w-80 h-80 bg-blue-100/20 rounded-full filter blur-3xl -z-10"></div>

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
            Our Portfolio
          </span>
          <h2 className="text-3xl md:text-4xl lg:text-5xl font-bold text-slate-900 mb-6">
            Professional Work
            <span className="block text-slate-400">That Delivers Results</span>
          </h2>
          <p className="text-lg text-slate-600 max-w-2xl mx-auto leading-relaxed">
            Every project meets our high standards for performance, accessibility, and user experience. Built to convert and built to last.
          </p>
        </motion.div>

        {/* Project cards */}
        <motion.div
          variants={containerVariants}
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true, margin: '0px 0px -200px 0px' }}
          className="space-y-12 mb-16"
        >
          {projects.map((project, index) => (
            <motion.div
              key={project.id}
              variants={itemVariants}
              className="group"
            >
              <div className={`grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-12 items-center ${index % 2 === 1 ? 'lg:grid-cols-2 lg:[&>*:nth-child(2)]:order-first' : ''}`}>
                {/* Content */}
                <motion.div
                  initial={{ opacity: 0, x: index % 2 === 0 ? -40 : 40 }}
                  whileInView={{ opacity: 1, x: 0 }}
                  viewport={{ once: true }}
                  transition={{ duration: 0.8 }}
                  className="space-y-6"
                >
                  <div>
                    <span className={`inline-block px-3 py-1 rounded-full bg-gradient-to-r ${project.color} text-white text-xs font-semibold mb-4`}>
                      {project.category}
                    </span>
                    <h3 className="text-3xl md:text-4xl font-bold text-slate-900 mb-2">
                      {project.name}
                    </h3>
                    <p className="text-lg text-slate-500 font-medium">
                      {project.tagline}
                    </p>
                  </div>

                  <p className="text-lg text-slate-600 leading-relaxed">
                    {project.description}
                  </p>

                  {/* Metrics grid */}
                  <div className="grid grid-cols-2 gap-4 pt-4">
                    <motion.div
                      whileHover={{ y: -4 }}
                      className="bg-white/80 backdrop-blur-sm p-4 rounded-xl border border-slate-200/50 hover:shadow-lg transition-all"
                    >
                      <div className={`text-3xl font-bold bg-gradient-to-r ${project.color} bg-clip-text text-transparent`}>
                        {project.metrics.lighthouse}
                      </div>
                      <div className="text-sm text-slate-600 font-medium mt-1">Lighthouse Score</div>
                    </motion.div>
                    <motion.div
                      whileHover={{ y: -4 }}
                      className="bg-white/80 backdrop-blur-sm p-4 rounded-xl border border-slate-200/50 hover:shadow-lg transition-all"
                    >
                      <div className={`text-3xl font-bold bg-gradient-to-r ${project.color} bg-clip-text text-transparent`}>
                        {project.metrics.performance}
                      </div>
                      <div className="text-sm text-slate-600 font-medium mt-1">Load Time</div>
                    </motion.div>
                    <motion.div
                      whileHover={{ y: -4 }}
                      className="bg-white/80 backdrop-blur-sm p-4 rounded-xl border border-slate-200/50 hover:shadow-lg transition-all"
                    >
                      <div className={`text-3xl font-bold bg-gradient-to-r ${project.color} bg-clip-text text-transparent`}>
                        WCAG {project.metrics.accessibility}
                      </div>
                      <div className="text-sm text-slate-600 font-medium mt-1">Accessibility</div>
                    </motion.div>
                    <motion.div
                      whileHover={{ y: -4 }}
                      className="bg-white/80 backdrop-blur-sm p-4 rounded-xl border border-slate-200/50 hover:shadow-lg transition-all"
                    >
                      <div className={`text-3xl font-bold bg-gradient-to-r ${project.color} bg-clip-text text-transparent`}>
                        {project.metrics.users}
                      </div>
                      <div className="text-sm text-slate-600 font-medium mt-1">Monthly Users</div>
                    </motion.div>
                  </div>

                  <motion.button
                    whileHover={{ x: 4 }}
                    className="inline-flex items-center gap-2 text-blue-600 font-semibold hover:text-blue-700 transition-colors pt-4"
                  >
                    View case study →
                  </motion.button>
                </motion.div>

                {/* Visual */}
                <motion.div
                  initial={{ opacity: 0, scale: 0.9 }}
                  whileInView={{ opacity: 1, scale: 1 }}
                  viewport={{ once: true }}
                  transition={{ duration: 0.8, delay: 0.2 }}
                  whileHover={{ scale: 1.05 }}
                  className="relative h-80 rounded-2xl overflow-hidden group/card"
                >
                  <div className={`absolute inset-0 bg-gradient-to-br ${project.color} opacity-90`}></div>
                  <div className="absolute inset-0 flex items-center justify-center text-8xl group-hover/card:scale-110 transition-transform duration-300">
                    {project.image}
                  </div>
                  
                  {/* Overlay info */}
                  <div className="absolute inset-0 bg-gradient-to-t from-black/30 to-transparent opacity-0 group-hover/card:opacity-100 transition-opacity duration-300 flex items-end p-6">
                    <div className="text-white">
                      <p className="text-sm font-medium text-blue-100 mb-2">Delivered on timeline</p>
                      <p className="text-lg font-bold">All metrics exceeded</p>
                    </div>
                  </div>
                </motion.div>
              </div>

              {/* Divider */}
              {index < projects.length - 1 && (
                <div className="mt-16 border-t border-slate-200/50"></div>
              )}
            </motion.div>
          ))}
        </motion.div>

        {/* CTA */}
        <motion.div
          initial={{ opacity: 0, y: 40 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: '0px 0px -150px 0px' }}
          transition={{ duration: 0.8 }}
          className="text-center bg-gradient-to-r from-blue-500 to-cyan-500 rounded-3xl p-12 text-white"
        >
          <h3 className="text-3xl md:text-4xl font-bold mb-4">Ready to Join Them?</h3>
          <p className="text-lg text-blue-100 mb-8 max-w-2xl mx-auto">
            Your business deserves a professional website. Let's build something great in 10 days.
          </p>
          <button
            onClick={() => document.getElementById('contact')?.scrollIntoView({ behavior: 'smooth' })}
            className="px-8 py-4 bg-white text-blue-600 font-bold rounded-lg hover:shadow-xl hover:scale-105 transition-all duration-200"
          >
            Start Your Project Today →
          </button>
        </motion.div>
      </div>
    </section>
  )
}

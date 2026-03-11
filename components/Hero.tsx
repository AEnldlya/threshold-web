'use client'

import { motion } from 'framer-motion'

export default function Hero() {
  return (
    <section className="pt-32 pb-20 px-6 bg-gradient-to-b from-navy via-navy to-gray-50">
      <div className="max-w-5xl mx-auto text-center">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
        >
          <h1 className="text-5xl md:text-6xl font-bold text-white mb-6">
            Professional Websites
            <br />
            <span className="text-amber-500">Made Simple</span>
          </h1>

          <p className="text-xl text-gray-100 mb-8 max-w-2xl mx-auto leading-relaxed">
            High-performance, beautifully designed websites built specifically for local businesses. 
            Lighthouse 95+, WCAG AA compliant, and delivered in just 10 days.
          </p>

          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <motion.button
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
              className="px-8 py-4 bg-amber-500 text-white font-bold rounded-lg hover:bg-amber-600 transition-colors text-lg"
              onClick={() => document.getElementById('contact')?.scrollIntoView({ behavior: 'smooth' })}
            >
              Start Your Project
            </motion.button>
            <motion.button
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
              className="px-8 py-4 border-2 border-white text-white font-bold rounded-lg hover:bg-white hover:text-navy transition-colors text-lg"
              onClick={() => document.getElementById('services')?.scrollIntoView({ behavior: 'smooth' })}
            >
              View Our Services
            </motion.button>
          </div>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 40 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.2 }}
          className="mt-20 grid grid-cols-1 md:grid-cols-3 gap-8"
        >
          <div className="bg-white/10 backdrop-blur-sm p-6 rounded-lg border border-white/20">
            <div className="text-4xl font-bold text-amber-500 mb-2">95+</div>
            <div className="text-white font-semibold">Lighthouse Score</div>
          </div>
          <div className="bg-white/10 backdrop-blur-sm p-6 rounded-lg border border-white/20">
            <div className="text-4xl font-bold text-amber-500 mb-2">10</div>
            <div className="text-white font-semibold">Days to Launch</div>
          </div>
          <div className="bg-white/10 backdrop-blur-sm p-6 rounded-lg border border-white/20">
            <div className="text-4xl font-bold text-amber-500 mb-2">100%</div>
            <div className="text-white font-semibold">WCAG Compliant</div>
          </div>
        </motion.div>
      </div>
    </section>
  )
}

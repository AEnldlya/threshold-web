'use client'

import { motion } from 'framer-motion'

export default function About() {
  return (
    <section id="about" className="py-20 px-6 bg-black">
      <div className="max-w-4xl mx-auto">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          viewport={{ once: true }}
          className="text-center mb-12"
        >
          <h2 className="text-4xl md:text-5xl font-bold text-white mb-4">Why Threshold Web?</h2>
        </motion.div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-12">
          <motion.div
            initial={{ opacity: 0, x: -30 }}
            whileInView={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.8 }}
            viewport={{ once: true }}
          >
            <h3 className="text-2xl font-bold text-yellow-400 mb-6">We Build Websites That Convert</h3>
            <p className="text-gray-300 mb-4 leading-relaxed">
              Every website we build is designed with your business goals in mind. We don't just create pretty sites—we create sites that drive results.
            </p>
            <p className="text-gray-300 mb-4 leading-relaxed">
              From initial discovery to launch, we handle every detail. You get a professional, high-performance website that ranks well and keeps visitors engaged.
            </p>
            <ul className="space-y-3">
              <li className="flex items-center gap-3">
                <span className="text-yellow-400 font-bold">✓</span>
                <span className="text-gray-300">No templates or cookie-cutter designs</span>
              </li>
              <li className="flex items-center gap-3">
                <span className="text-yellow-400 font-bold">✓</span>
                <span className="text-gray-300">Professional, modern design</span>
              </li>
              <li className="flex items-center gap-3">
                <span className="text-yellow-400 font-bold">✓</span>
                <span className="text-gray-300">Complete optimization for performance</span>
              </li>
              <li className="flex items-center gap-3">
                <span className="text-yellow-400 font-bold">✓</span>
                <span className="text-gray-300">Full accessibility compliance</span>
              </li>
              <li className="flex items-center gap-3">
                <span className="text-yellow-400 font-bold">✓</span>
                <span className="text-gray-300">SEO-ready from day one</span>
              </li>
            </ul>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, x: 30 }}
            whileInView={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.8 }}
            viewport={{ once: true }}
            className="bg-gray-900 rounded-lg p-8 text-white border border-gray-700"
          >
            <h3 className="text-2xl font-bold mb-6 text-yellow-400">Our Approach</h3>
            <div className="space-y-6">
              <div>
                <div className="text-yellow-400 font-bold mb-2">Discovery</div>
                <p className="text-gray-300">We learn about your business, goals, and target audience.</p>
              </div>
              <div>
                <div className="text-yellow-400 font-bold mb-2">Design</div>
                <p className="text-gray-300">Professional mockups in Figma for your approval before any coding.</p>
              </div>
              <div>
                <div className="text-yellow-400 font-bold mb-2">Development</div>
                <p className="text-gray-300">Modern, clean code built with Next.js and TypeScript.</p>
              </div>
              <div>
                <div className="text-yellow-400 font-bold mb-2">Optimization</div>
                <p className="text-gray-300">Performance, accessibility, and SEO audits before launch.</p>
              </div>
              <div>
                <div className="text-yellow-400 font-bold mb-2">Launch</div>
                <p className="text-gray-300">Deployed and ready to work for your business.</p>
              </div>
            </div>
          </motion.div>
        </div>
      </div>
    </section>
  )
}

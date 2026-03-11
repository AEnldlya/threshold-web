'use client'

import { motion } from 'framer-motion'

export default function Footer() {
  const currentYear = new Date().getFullYear()

  return (
    <footer className="bg-black text-white py-16 px-6 border-t border-gray-800">
      <div className="max-w-6xl mx-auto">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8 mb-12">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
            viewport={{ once: true }}
          >
            <div className="text-2xl font-bold mb-4">
              <span className="text-yellow-400">Threshold</span> Web
            </div>
            <p className="text-gray-300">
              Professional websites built for local businesses.
            </p>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.1 }}
            viewport={{ once: true }}
          >
            <h4 className="font-bold mb-4 text-yellow-400">Quick Links</h4>
            <ul className="space-y-2 text-gray-300">
              <li><a href="#services" className="hover:text-yellow-400 transition-colors">Services</a></li>
              <li><a href="#portfolio" className="hover:text-yellow-400 transition-colors">Portfolio</a></li>
              <li><a href="#about" className="hover:text-yellow-400 transition-colors">About</a></li>
              <li><a href="#contact" className="hover:text-yellow-400 transition-colors">Contact</a></li>
            </ul>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.2 }}
            viewport={{ once: true }}
          >
            <h4 className="font-bold mb-4 text-yellow-400">Services</h4>
            <ul className="space-y-2 text-gray-300">
              <li><a href="#services" className="hover:text-yellow-400 transition-colors">Web Design</a></li>
              <li><a href="#services" className="hover:text-yellow-400 transition-colors">Development</a></li>
              <li><a href="#services" className="hover:text-yellow-400 transition-colors">SEO Optimization</a></li>
              <li><a href="#services" className="hover:text-yellow-400 transition-colors">Accessibility</a></li>
            </ul>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.3 }}
            viewport={{ once: true }}
          >
            <h4 className="font-bold mb-4 text-yellow-400">Contact</h4>
            <ul className="space-y-2 text-gray-300">
              <li><a href="tel:6033067508" className="hover:text-yellow-400 transition-colors">603-306-7508</a></li>
              <li className="text-sm">
                <span className="text-yellow-400">Email</span><br />
                hello@thresholdweb.com
              </li>
            </ul>
          </motion.div>
        </div>

        <motion.div
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          transition={{ duration: 0.6, delay: 0.4 }}
          viewport={{ once: true }}
          className="border-t border-gray-700 pt-8"
        >
          <div className="text-center text-gray-400">
            <p>&copy; {currentYear} Threshold Web. All rights reserved.</p>
            <p className="text-sm mt-2">High-performance websites for local businesses.</p>
          </div>
        </motion.div>
      </div>
    </footer>
  )
}

'use client'

import { motion } from 'framer-motion'

export default function Header() {
  return (
    <header className="bg-black text-white py-4 sticky top-0 z-50 shadow-lg border-b border-gray-800">
      <div className="max-w-6xl mx-auto px-4 flex justify-between items-center">
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.5 }}
          className="text-2xl font-bold"
        >
          <span className="text-yellow-400">Threshold</span> Web
        </motion.div>
        <nav className="hidden md:flex space-x-8">
          <a href="#services" className="hover:text-yellow-400 transition">Services</a>
          <a href="#portfolio" className="hover:text-yellow-400 transition">Portfolio</a>
          <a href="#about" className="hover:text-yellow-400 transition">About</a>
          <a href="#contact" className="hover:text-yellow-400 transition">Contact</a>
        </nav>
      </div>
    </header>
  )
}

'use client'

import { motion } from 'framer-motion'

export default function Header() {
  return (
    <header className="bg-slate-900 text-white py-4 sticky top-0 z-50 shadow-lg">
      <div className="max-w-6xl mx-auto px-4 flex justify-between items-center">
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.5 }}
          className="text-2xl font-bold"
        >
          Threshold Web
        </motion.div>
        <nav className="hidden md:flex space-x-8">
          <a href="#services" className="hover:text-yellow-500 transition">Services</a>
          <a href="#portfolio" className="hover:text-yellow-500 transition">Portfolio</a>
          <a href="#about" className="hover:text-yellow-500 transition">About</a>
          <a href="#contact" className="hover:text-yellow-500 transition">Contact</a>
        </nav>
      </div>
    </header>
  )
}

'use client'

import Link from 'next/link'
import { motion } from 'framer-motion'

export default function Header() {
  return (
    <header className="fixed w-full top-0 z-50 bg-white border-b border-gray-100">
      <nav className="max-w-6xl mx-auto px-6 py-4 flex items-center justify-between">
        <motion.div
          initial={{ opacity: 0, x: -20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.5 }}
          className="text-2xl font-bold"
        >
          <span className="text-navy">Threshold</span>
          <span className="text-amber-500"> Web</span>
        </motion.div>

        <motion.ul
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.5, delay: 0.1 }}
          className="hidden md:flex gap-8 text-gray-700"
        >
          <li>
            <a href="#services" className="hover:text-amber-500 transition-colors font-medium">
              Services
            </a>
          </li>
          <li>
            <a href="#portfolio" className="hover:text-amber-500 transition-colors font-medium">
              Portfolio
            </a>
          </li>
          <li>
            <a href="#about" className="hover:text-amber-500 transition-colors font-medium">
              About
            </a>
          </li>
          <li>
            <a href="#contact" className="hover:text-amber-500 transition-colors font-medium">
              Contact
            </a>
          </li>
        </motion.ul>

        <motion.button
          initial={{ opacity: 0, x: 20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.5 }}
          className="btn-primary"
          onClick={() => document.getElementById('contact')?.scrollIntoView({ behavior: 'smooth' })}
        >
          Get Started
        </motion.button>
      </nav>
    </header>
  )
}

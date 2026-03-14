'use client'

import { motion } from 'framer-motion'

export default function Footer() {
  const currentYear = new Date().getFullYear()

  const footerLinks = [
    {
      title: 'Company',
      links: [
        { label: 'Home', href: '#' },
        { label: 'Services', href: '#services' },
        { label: 'Portfolio', href: '#portfolio' },
        { label: 'About', href: '#about' },
      ]
    },
    {
      title: 'Resources',
      links: [
        { label: 'Blog', href: '#' },
        { label: 'Guides', href: '#' },
        { label: 'Case Studies', href: '#portfolio' },
        { label: 'FAQ', href: '#' },
      ]
    },
    {
      title: 'Legal',
      links: [
        { label: 'Privacy Policy', href: '#' },
        { label: 'Terms of Service', href: '#' },
        { label: 'Contact', href: '#contact' },
        { label: 'Support', href: '#contact' },
      ]
    },
  ]

  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        staggerChildren: 0.1,
        delayChildren: 0.1,
      },
    },
  }

  const itemVariants = {
    hidden: { opacity: 0, y: 20 },
    visible: {
      opacity: 1,
      y: 0,
      transition: { duration: 0.6 },
    },
  }

  return (
    <footer className="bg-slate-900 text-white py-16 md:py-24">
      {/* Main footer content */}
      <div className="container-max mb-16">
        <motion.div
          variants={containerVariants}
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true, margin: '0px 0px -100px 0px' }}
          className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-12 mb-12 pb-12 border-b border-slate-800"
        >
          {/* Brand */}
          <motion.div variants={itemVariants} className="lg:col-span-1">
            <div className="flex items-center gap-3 mb-4">
              <div className="w-10 h-10 rounded-lg bg-gradient-to-br from-blue-500 to-cyan-500 flex items-center justify-center">
                <span className="text-white font-bold text-lg">T</span>
              </div>
              <div>
                <div className="font-bold text-white">Threshold Web</div>
                <div className="text-xs text-blue-300">Professional Websites</div>
              </div>
            </div>
            <p className="text-slate-400 text-sm mb-6">
              Premium websites for local businesses. Built in 10 days. Performance guaranteed.
            </p>
            <div className="flex gap-4">
              {[
                { icon: '𝕏', href: 'https://twitter.com' },
                { icon: '📘', href: 'https://facebook.com' },
                { icon: '💼', href: 'https://linkedin.com' },
              ].map((social, idx) => (
                <a
                  key={idx}
                  href={social.href}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="w-9 h-9 rounded-lg bg-slate-800 hover:bg-blue-500 flex items-center justify-center text-white transition-all duration-200 hover:scale-110"
                  aria-label="Social media link"
                >
                  {social.icon}
                </a>
              ))}
            </div>
          </motion.div>

          {/* Link sections */}
          {footerLinks.map((section) => (
            <motion.div key={section.title} variants={itemVariants} className="lg:col-span-1">
              <h3 className="font-semibold text-white mb-6">{section.title}</h3>
              <ul className="space-y-4">
                {section.links.map((link) => (
                  <li key={link.label}>
                    <a
                      href={link.href}
                      className="text-slate-400 hover:text-blue-400 transition-colors duration-200 text-sm font-medium"
                    >
                      {link.label}
                    </a>
                  </li>
                ))}
              </ul>
            </motion.div>
          ))}

          {/* Contact CTA */}
          <motion.div variants={itemVariants} className="lg:col-span-1">
            <h3 className="font-semibold text-white mb-6">Get in Touch</h3>
            <div className="space-y-4">
              <div>
                <p className="text-slate-400 text-sm mb-2">Phone</p>
                <a
                  href="tel:6033067508"
                  className="text-blue-400 hover:text-blue-300 font-semibold transition-colors"
                >
                  603-306-7508
                </a>
              </div>
              <div>
                <p className="text-slate-400 text-sm mb-2">Email</p>
                <a
                  href="mailto:hello@thresholdweb.com"
                  className="text-blue-400 hover:text-blue-300 font-semibold transition-colors break-all"
                >
                  hello@thresholdweb.com
                </a>
              </div>
              <button
                onClick={() => document.getElementById('contact')?.scrollIntoView({ behavior: 'smooth' })}
                className="w-full mt-4 px-4 py-2 bg-gradient-to-r from-blue-600 to-cyan-600 text-white rounded-lg hover:shadow-lg hover:shadow-blue-500/30 transition-all duration-200 text-sm font-semibold"
              >
                Start Project →
              </button>
            </div>
          </motion.div>
        </motion.div>

        {/* Bottom bar */}
        <motion.div
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8, delay: 0.3 }}
          className="flex flex-col md:flex-row items-center justify-between gap-4 text-slate-400 text-sm"
        >
          <div>
            <p>
              © {currentYear} Threshold Web. All rights reserved. |{' '}
              <a href="#" className="text-blue-400 hover:text-blue-300 transition-colors">
                Privacy
              </a>
              {' '} •{' '}
              <a href="#" className="text-blue-400 hover:text-blue-300 transition-colors">
                Terms
              </a>
            </p>
          </div>
          <div className="text-center md:text-right">
            <p>
              Proudly built with{' '}
              <span className="text-red-500">♥</span> in{' '}
              <span className="font-semibold text-white">Boston, MA</span>
            </p>
          </div>
        </motion.div>
      </div>

      {/* Floating CTA bar for mobile */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true }}
        transition={{ duration: 0.6, delay: 0.4 }}
        className="fixed bottom-0 left-0 right-0 bg-gradient-to-r from-blue-600 to-cyan-600 text-white py-3 px-4 shadow-2xl md:hidden z-40"
      >
        <button
          onClick={() => document.getElementById('contact')?.scrollIntoView({ behavior: 'smooth' })}
          className="w-full font-bold text-center hover:opacity-90 transition-opacity"
        >
          Ready? Start Your Website Today →
        </button>
      </motion.div>
    </footer>
  )
}

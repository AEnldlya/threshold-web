'use client'

import { motion } from 'framer-motion'

export default function Hero() {
  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        staggerChildren: 0.15,
        delayChildren: 0.2,
      },
    },
  }

  const itemVariants = {
    hidden: { opacity: 0, y: 30 },
    visible: {
      opacity: 1,
      y: 0,
      transition: { duration: 0.8, ease: 'easeOut' },
    },
  }

  return (
    <section className="relative overflow-hidden pt-20 md:pt-32 pb-16 md:pb-24">
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-slate-50 via-blue-50/30 to-slate-50 -z-10"></div>
      
      {/* Animated background blobs */}
      <div className="absolute top-20 left-10 w-80 h-80 bg-blue-200/20 rounded-full filter blur-3xl opacity-70 -z-10 animate-pulse-slow"></div>
      <div className="absolute bottom-10 right-10 w-96 h-96 bg-cyan-200/20 rounded-full filter blur-3xl opacity-70 -z-10 animate-pulse-slow" style={{ animationDelay: '2s' }}></div>

      <div className="container-max">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-16 items-center">
          {/* Left content */}
          <motion.div
            variants={containerVariants}
            initial="hidden"
            animate="visible"
            className="space-y-8"
          >
            {/* Badges */}
            <motion.div variants={itemVariants} className="flex flex-wrap gap-3">
              <span className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-blue-100/80 text-blue-700 text-sm font-medium border border-blue-200/50">
                <span className="relative flex h-2 w-2">
                  <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-blue-500 opacity-75"></span>
                  <span className="relative inline-flex rounded-full h-2 w-2 bg-blue-500"></span>
                </span>
                Now Launching in Your City
              </span>
            </motion.div>

            {/* Main headline */}
            <motion.h1 variants={itemVariants} className="text-4xl md:text-5xl lg:text-6xl font-bold tracking-tight">
              <span className="block text-slate-900">Professional Websites</span>
              <span className="block bg-gradient-to-r from-blue-600 to-cyan-600 bg-clip-text text-transparent">Built in 10 Days</span>
            </motion.h1>

            {/* Subheading */}
            <motion.p
              variants={itemVariants}
              className="text-lg md:text-xl text-slate-600 leading-relaxed max-w-xl"
            >
              High-performance, beautifully designed websites built specifically for local businesses. Lighthouse 95+, WCAG AA compliant, conversion-focused.
            </motion.p>

            {/* Stats */}
            <motion.div variants={itemVariants} className="grid grid-cols-3 gap-4 py-6">
              <div className="bg-white/80 backdrop-blur-sm p-4 rounded-xl border border-slate-200/50 hover:shadow-lg transition-all">
                <div className="text-2xl md:text-3xl font-bold text-blue-600">95+</div>
                <div className="text-xs md:text-sm text-slate-600 font-medium mt-1">Lighthouse Score</div>
              </div>
              <div className="bg-white/80 backdrop-blur-sm p-4 rounded-xl border border-slate-200/50 hover:shadow-lg transition-all">
                <div className="text-2xl md:text-3xl font-bold text-cyan-600">10</div>
                <div className="text-xs md:text-sm text-slate-600 font-medium mt-1">Days to Launch</div>
              </div>
              <div className="bg-white/80 backdrop-blur-sm p-4 rounded-xl border border-slate-200/50 hover:shadow-lg transition-all">
                <div className="text-2xl md:text-3xl font-bold text-blue-600">$2.5K</div>
                <div className="text-xs md:text-sm text-slate-600 font-medium mt-1">Fixed Price</div>
              </div>
            </motion.div>

            {/* CTAs */}
            <motion.div variants={itemVariants} className="flex flex-col sm:flex-row gap-4 pt-4">
              <button
                onClick={() => document.getElementById('contact')?.scrollIntoView({ behavior: 'smooth' })}
                className="btn-primary w-full sm:w-auto"
              >
                Start Your Project →
              </button>
              <button
                onClick={() => document.getElementById('portfolio')?.scrollIntoView({ behavior: 'smooth' })}
                className="btn-secondary w-full sm:w-auto"
              >
                See Our Work
              </button>
            </motion.div>

            {/* Trust statement */}
            <motion.p variants={itemVariants} className="text-sm text-slate-500 pt-4">
              ✓ No hidden fees • ✓ Full support • ✓ Money-back guarantee
            </motion.p>
          </motion.div>

          {/* Right visual */}
          <motion.div
            initial={{ opacity: 0, scale: 0.95, y: 40 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            transition={{ duration: 1, delay: 0.3, ease: 'easeOut' }}
            className="relative h-80 md:h-96 lg:h-full"
          >
            {/* Floating card 1 */}
            <motion.div
              animate={{ y: [0, -20, 0] }}
              transition={{ duration: 4, repeat: Infinity, ease: 'easeInOut' }}
              className="absolute top-0 right-0 w-72 bg-white/80 backdrop-blur-xl rounded-2xl border border-slate-200/50 p-6 shadow-xl hover:shadow-2xl transition-shadow"
            >
              <div className="flex items-center gap-3 mb-4">
                <div className="w-10 h-10 rounded-lg bg-gradient-to-br from-blue-500 to-cyan-500 flex items-center justify-center text-white font-bold">
                  ⚡
                </div>
                <span className="font-semibold text-slate-900">Lightning Fast</span>
              </div>
              <p className="text-sm text-slate-600">
                Average load time under 2 seconds. Optimized images, lazy loading, CDN-ready.
              </p>
            </motion.div>

            {/* Floating card 2 */}
            <motion.div
              animate={{ y: [0, 20, 0] }}
              transition={{ duration: 4.5, repeat: Infinity, ease: 'easeInOut', delay: 1 }}
              className="absolute bottom-10 left-0 w-72 bg-white/80 backdrop-blur-xl rounded-2xl border border-slate-200/50 p-6 shadow-xl hover:shadow-2xl transition-shadow"
            >
              <div className="flex items-center gap-3 mb-4">
                <div className="w-10 h-10 rounded-lg bg-gradient-to-br from-green-500 to-emerald-500 flex items-center justify-center text-white font-bold">
                  ♿
                </div>
                <span className="font-semibold text-slate-900">Fully Accessible</span>
              </div>
              <p className="text-sm text-slate-600">
                WCAG AA compliant. Keyboard navigation, screen readers, perfect contrast ratios.
              </p>
            </motion.div>

            {/* Background decoration */}
            <div className="absolute inset-0 bg-gradient-to-br from-blue-400/10 to-cyan-400/10 rounded-3xl"></div>
          </motion.div>
        </div>

        {/* Scroll indicator */}
        <motion.div
          animate={{ y: [0, 8, 0] }}
          transition={{ duration: 2, repeat: Infinity }}
          className="flex justify-center mt-16 md:mt-24"
        >
          <div className="flex flex-col items-center gap-2 text-slate-400">
            <span className="text-sm font-medium">Scroll to explore</span>
            <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 14l-7 7m0 0l-7-7m7 7V3" />
            </svg>
          </div>
        </motion.div>
      </div>
    </section>
  )
}

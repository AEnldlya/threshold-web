'use client'

import { useEffect, useRef, useCallback } from 'react'
import { motion, useScroll, useSpring, useMotionValue, useMotionTemplate } from 'framer-motion'
import Link from 'next/link'

// Spotlight effect component
function SpotlightEffect({ mouseX, mouseY }: { mouseX: ReturnType<typeof useMotionValue<number>>, mouseY: ReturnType<typeof useMotionValue<number>> }) {
  const spotlightX = useMotionTemplate`${mouseX}px`
  const spotlightY = useMotionTemplate`${mouseY}px`
  
  return (
    <motion.div
      className="pointer-events-none fixed inset-0 z-30 opacity-0 transition-opacity duration-300 lg:opacity-100"
      style={{
        background: useMotionTemplate`radial-gradient(600px circle at ${spotlightX} ${spotlightY}, rgba(245, 158, 11, 0.15), transparent 40%)`,
      }}
    />
  )
}

// Floating particle component
function FloatingParticle({ delay, x, y }: { delay: number; x: string; y: string }) {
  return (
    <motion.div
      className="absolute w-2 h-2 rounded-full bg-amber-500/30"
      style={{ left: x, top: y }}
      animate={{
        y: [0, -30, 0],
        opacity: [0.3, 0.8, 0.3],
        scale: [1, 1.2, 1],
      }}
      transition={{
        duration: 4,
        delay,
        repeat: Infinity,
        ease: "easeInOut",
      }}
    />
  )
}

// Magnetic button component
function MagneticButton({ 
  children, 
  variant = 'primary',
  href
}: { 
  children: React.ReactNode
  variant?: 'primary' | 'secondary'
  href: string
}) {
  const ref = useRef<HTMLButtonElement>(null)
  const x = useMotionValue(0)
  const y = useMotionValue(0)

  const handleMouseMove = useCallback((e: React.MouseEvent<HTMLButtonElement>) => {
    if (!ref.current) return
    const rect = ref.current.getBoundingClientRect()
    const centerX = rect.left + rect.width / 2
    const centerY = rect.top + rect.height / 2
    const distX = e.clientX - centerX
    const distY = e.clientY - centerY
    
    x.set(distX * 0.3)
    y.set(distY * 0.3)
  }, [x, y])

  const handleMouseLeave = useCallback(() => {
    x.set(0)
    y.set(0)
  }, [x, y])

  const springConfig = { damping: 20, stiffness: 300 }
  const springX = useSpring(x, springConfig)
  const springY = useSpring(y, springConfig)

  const baseClasses = variant === 'primary'
    ? "px-8 py-4 bg-amber-500 text-navy font-bold hover:bg-amber-400 transition-colors text-lg"
    : "px-8 py-4 border-2 border-amber-500 text-amber-500 font-bold hover:bg-amber-500 hover:text-navy transition-colors text-lg"

  return (
    <Link href={href}>
      <motion.button
        ref={ref}
        onMouseMove={handleMouseMove}
        onMouseLeave={handleMouseLeave}
        style={{ x: springX, y: springY }}
        whileTap={{ scale: 0.95 }}
        className={baseClasses}
      >
        {children}
      </motion.button>
    </Link>
  )
}

// 3D Tilt card component
function TiltCard({ children, className }: { children: React.ReactNode; className?: string }) {
  const ref = useRef<HTMLDivElement>(null)
  const rotateX = useMotionValue(0)
  const rotateY = useMotionValue(0)

  const handleMouseMove = useCallback((e: React.MouseEvent<HTMLDivElement>) => {
    if (!ref.current) return
    const rect = ref.current.getBoundingClientRect()
    const centerX = rect.left + rect.width / 2
    const centerY = rect.top + rect.height / 2
    const mouseX = e.clientX - centerX
    const mouseY = e.clientY - centerY
    
    rotateY.set(mouseX / 10)
    rotateX.set(-mouseY / 10)
  }, [rotateX, rotateY])

  const handleMouseLeave = useCallback(() => {
    rotateX.set(0)
    rotateY.set(0)
  }, [rotateX, rotateY])

  const springConfig = { damping: 30, stiffness: 200 }
  const springRotateX = useSpring(rotateX, springConfig)
  const springRotateY = useSpring(rotateY, springConfig)

  return (
    <motion.div
      ref={ref}
      onMouseMove={handleMouseMove}
      onMouseLeave={handleMouseLeave}
      style={{
        rotateX: springRotateX,
        rotateY: springRotateY,
        transformStyle: 'preserve-3d',
      }}
      className={className}
    >
      {children}
    </motion.div>
  )
}

// Scroll progress bar
function ScrollProgressBar() {
  const { scrollYProgress } = useScroll()
  const scaleX = useSpring(scrollYProgress, {
    stiffness: 100,
    damping: 30,
    restDelta: 0.001,
  })

  return (
    <motion.div
      className="fixed top-0 left-0 right-0 h-1 bg-amber-500 origin-left z-50"
      style={{ scaleX }}
    />
  )
}

// Text reveal animation component
function TextReveal({ text, className, delay = 0 }: { text: string; className?: string; delay?: number }) {
  const words = text.split(' ')

  const container = {
    hidden: { opacity: 0 },
    visible: () => ({
      opacity: 1,
      transition: { staggerChildren: 0.12, delayChildren: delay },
    }),
  }

  const child = {
    visible: {
      opacity: 1,
      y: 0,
      transition: {
        type: "spring",
        damping: 12,
        stiffness: 100,
      },
    },
    hidden: {
      opacity: 0,
      y: 20,
    },
  }

  return (
    <motion.span
      className={`inline-flex flex-wrap justify-center ${className}`}
      variants={container}
      initial="hidden"
      animate="visible"
    >
      {words.map((word, index) => (
        <motion.span variants={child} key={index} className="mr-2">
          {word}
        </motion.span>
      ))}
    </motion.span>
  )
}

// Main hero component
export default function HeroAceternity() {
  const containerRef = useRef<HTMLDivElement>(null)
  const mouseX = useMotionValue(0)
  const mouseY = useMotionValue(0)

  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      mouseX.set(e.clientX)
      mouseY.set(e.clientY)
    }

    window.addEventListener('mousemove', handleMouseMove)
    return () => window.removeEventListener('mousemove', handleMouseMove)
  }, [mouseX, mouseY])

  // Generate random particles
  const particles = [
    { x: '10%', y: '20%', delay: 0 },
    { x: '85%', y: '15%', delay: 0.5 },
    { x: '75%', y: '70%', delay: 1 },
    { x: '15%', y: '80%', delay: 1.5 },
    { x: '50%', y: '10%', delay: 0.8 },
    { x: '90%', y: '50%', delay: 1.2 },
    { x: '5%', y: '50%', delay: 0.3 },
    { x: '60%', y: '85%', delay: 1.8 },
  ]

  return (
    <>
      <ScrollProgressBar />
      <section 
        ref={containerRef}
        className="relative min-h-screen pt-32 pb-20 px-6 bg-navy overflow-hidden"
      >
        {/* Spotlight effect */}
        <SpotlightEffect mouseX={mouseX} mouseY={mouseY} />

        {/* Floating particles */}
        <div className="absolute inset-0 pointer-events-none">
          {particles.map((p, i) => (
            <FloatingParticle key={i} {...p} />
          ))}
        </div>

        {/* Content */}
        <div className="relative z-10 max-w-5xl mx-auto text-center">
          <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.8, ease: 'easeOut' }}
          >
            {/* Main headline with text reveal */}
            <h1 className="text-5xl md:text-6xl font-bold text-white mb-6">
              <TextReveal text="Professional Websites" className="block" delay={0} />
              <br className="hidden md:block" />
              <span className="text-amber-500">
                <TextReveal text="Made Simple" className="block" delay={0.4} />
              </span>
            </h1>

            {/* Subtitle */}
            <motion.p
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.8, delay: 0.6 }}
              className="text-xl text-gray-300 mb-8 max-w-2xl mx-auto leading-relaxed"
            >
              High-performance, beautifully designed websites built specifically for local businesses. 
              Lighthouse 95+, WCAG AA compliant, and delivered in just 10 days.
            </motion.p>

            {/* Magnetic buttons */}
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.8, delay: 0.8 }}
              className="flex flex-col sm:flex-row gap-4 justify-center"
            >
              <MagneticButton href="/contact">
                Start Your Project
              </MagneticButton>
              <MagneticButton href="/services" variant="secondary">
                View Our Services
              </MagneticButton>
            </motion.div>
          </motion.div>

          {/* Stats with 3D tilt */}
          <motion.div
            initial={{ opacity: 0, y: 40 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 1 }}
            className="mt-20 grid grid-cols-1 md:grid-cols-3 gap-8"
          >
            <TiltCard className="h-full">
              <div className="bg-gray-900/50 backdrop-blur-sm p-6 rounded-lg border border-amber-500/30 h-full">
                <motion.div
                  initial={{ scale: 0 }}
                  animate={{ scale: 1 }}
                  transition={{ type: "spring", stiffness: 200, delay: 1.2 }}
                  className="text-4xl font-bold text-amber-500 mb-2"
                >
                  95+
                </motion.div>
                <div className="text-white font-semibold">Lighthouse Score</div>
              </div>
            </TiltCard>

            <TiltCard className="h-full">
              <div className="bg-gray-900/50 backdrop-blur-sm p-6 rounded-lg border border-amber-500/30 h-full">
                <motion.div
                  initial={{ scale: 0 }}
                  animate={{ scale: 1 }}
                  transition={{ type: "spring", stiffness: 200, delay: 1.4 }}
                  className="text-4xl font-bold text-amber-500 mb-2"
                >
                  10
                </motion.div>
                <div className="text-white font-semibold">Days to Launch</div>
              </div>
            </TiltCard>

            <TiltCard className="h-full">
              <div className="bg-gray-900/50 backdrop-blur-sm p-6 rounded-lg border border-amber-500/30 h-full">
                <motion.div
                  initial={{ scale: 0 }}
                  animate={{ scale: 1 }}
                  transition={{ type: "spring", stiffness: 200, delay: 1.6 }}
                  className="text-4xl font-bold text-amber-500 mb-2"
                >
                  100%
                </motion.div>
                <div className="text-white font-semibold">WCAG Compliant</div>
              </div>
            </TiltCard>
          </motion.div>
        </div>

        {/* Bottom gradient fade */}
        <div className="absolute bottom-0 left-0 right-0 h-32 bg-gradient-to-t from-navy to-transparent pointer-events-none" />
      </section>
    </>
  )
}

'use client';

import { useRef } from 'react';
import { motion, useScroll, useTransform } from 'framer-motion';
import Link from 'next/link';

// Animation variants
const fadeInUp = {
  hidden: { opacity: 0, y: 40 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.6, ease: [0.22, 1, 0.36, 1] } }
};

const staggerContainer = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: { staggerChildren: 0.1, delayChildren: 0.2 }
  }
};

export default function Home() {
  const containerRef = useRef<HTMLDivElement>(null);
  const { scrollYProgress } = useScroll({
    target: containerRef,
    offset: ["start start", "end end"]
  });

  const heroY = useTransform(scrollYProgress, [0, 0.5], [0, 100]);
  const heroOpacity = useTransform(scrollYProgress, [0, 0.3], [1, 0]);

  const services = [
    {
      title: 'Riding Lessons',
      description: 'Private and group lessons for all ages and skill levels.',
      price: 'From $75',
      image: '/images/outlook-farm/dressage.png'
    },
    {
      title: 'Trail Rides',
      description: 'Guided rides through the Vermont countryside.',
      price: 'From $95',
      image: '/images/outlook-farm/view-of-barn.png'
    },
    {
      title: 'Boarding',
      description: 'Full-service horse boarding with indoor arena and pastures.',
      price: 'From $650/mo',
      image: '/images/outlook-farm/barn.png'
    }
  ];

  return (
    <main ref={containerRef} className="bg-cream text-black overflow-x-hidden">
      {/* Hero Section */}
      <section className="relative h-screen overflow-hidden bg-black">
        <motion.div
          style={{ y: heroY, opacity: heroOpacity }}
          className="absolute inset-0"
        >
          <div className="relative w-full h-full">
            <img
              src="/images/outlook-farm/view-of-barn.png"
              alt="Outlook Farm"
              className="object-cover w-full h-full"
            />
            <div className="absolute inset-0 bg-gradient-to-b from-black/40 via-black/20 to-black/60" />
          </div>
        </motion.div>

        {/* Hero Content */}
        <div className="relative z-10 h-full flex items-end pb-24 md:pb-32 px-6 lg:px-12">
          <div className="max-w-7xl mx-auto w-full">
            <motion.div
              variants={staggerContainer}
              initial="hidden"
              animate="visible"
            >
              <motion.p variants={fadeInUp} className="text-white/60 text-sm tracking-wider uppercase mb-4">
                Norwich, Vermont
              </motion.p>
              <motion.h1 variants={fadeInUp} className="text-white text-5xl md:text-7xl lg:text-8xl font-light tracking-tight leading-none mb-8">
                Outlook Farm
              </motion.h1>
              <motion.p variants={fadeInUp} className="text-white/80 text-xl md:text-2xl max-w-xl mb-8">
                Horseback riding lessons, trail rides, and boarding since 1998.
              </motion.p>
              
              <motion.div variants={fadeInUp} className="flex flex-col sm:flex-row gap-4">
                <Link 
                  href="/contact"
                  className="inline-flex items-center justify-center gap-3 px-8 py-4 bg-white text-black text-sm tracking-wide hover:bg-cream transition-all duration-300"
                >
                  Book a visit
                  <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M17 8l4 4m0 0l-4 4m4-4H3" />
                  </svg>
                </Link>
                <Link 
                  href="/services"
                  className="inline-flex items-center justify-center gap-3 px-8 py-4 border border-white/30 text-white text-sm tracking-wide hover:bg-white/10 transition-all duration-300"
                >
                  See services
                </Link>
              </motion.div>
            </motion.div>
          </div>
        </div>
      </section>

      {/* Introduction Section */}
      <section className="py-20 md:py-28 px-6 lg:px-12 bg-cream">
        <div className="max-w-7xl mx-auto">
          <div className="grid lg:grid-cols-2 gap-12 lg:gap-24 items-center">
            <motion.div
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6 }}
            >
              <p className="text-pasture-green text-sm tracking-wider uppercase mb-4">Est. 1998</p>
              <h2 className="text-3xl md:text-4xl lg:text-5xl font-light tracking-tight leading-tight mb-6">
                25 years of riding lessons in Norwich
              </h2>
              <p className="text-stone-dark text-lg leading-relaxed mb-6">
                Outlook Farm has been teaching people to ride for over two decades. 
                We started with three horses and a small barn, and now we have 50 acres 
                where riders of all levels come to learn.
              </p>
              <Link 
                href="/about"
                className="inline-flex items-center gap-2 text-black text-sm tracking-wide border-b border-pasture-green pb-1 hover:text-pasture-green transition-colors"
              >
                Read our story
                <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M17 8l4 4m0 0l-4 4m4-4H3" />
                </svg>
              </Link>
            </motion.div>

            <motion.div
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6, delay: 0.1 }}
              className="relative"
            >
              <div className="relative aspect-[4/5] overflow-hidden">
                <img
                  src="/images/outlook-farm/jumping.png"
                  alt="Horse jumping at Outlook Farm"
                  className="object-cover w-full h-full"
                />
              </div>
            </motion.div>
          </div>
        </div>
      </section>

      {/* Services Section */}
      <section className="py-20 md:py-28 px-6 lg:px-12 bg-pasture-green/5">
        <div className="max-w-7xl mx-auto">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="mb-12"
          >
            <p className="text-pasture-green text-sm tracking-wider uppercase mb-4">What we offer</p>
            <h2 className="text-3xl md:text-4xl font-light tracking-tight">Services</h2>
          </motion.div>

          <div className="grid md:grid-cols-3 gap-8">
            {services.map((service, index) => (
              <motion.div
                key={service.title}
                initial={{ opacity: 0, y: 30 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.5, delay: index * 0.1 }}
              >
                <Link href="/services" className="group block">
                  <div className="relative aspect-[4/3] mb-4 overflow-hidden">
                    <img
                      src={service.image}
                      alt={service.title}
                      className="object-cover w-full h-full transition-transform duration-500 group-hover:scale-105"
                    />
                  </div>
                  
                  <div className="flex justify-between items-start mb-2">
                    <h3 className="text-xl font-normal tracking-tight group-hover:text-pasture-green transition-colors">{service.title}</h3>
                    <span className="text-pasture-green text-sm font-medium">{service.price}</span>
                  </div>
                  <p className="text-stone-dark leading-relaxed">{service.description}</p>
                </Link>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Feature Image */}
      <section className="py-20 md:py-28 px-6 lg:px-12 bg-cream">
        <div className="max-w-7xl mx-auto">
          <motion.div
            initial={{ opacity: 0 }}
            whileInView={{ opacity: 1 }}
            viewport={{ once: true }}
            transition={{ duration: 0.8 }}
            className="relative"
          >
            <div className="relative aspect-[21/9] overflow-hidden">
              <img
                src="/images/outlook-farm/barn.png"
                alt="Outlook Farm barn"
                className="object-cover w-full h-full"
              />
            </div>
            <div className="absolute bottom-0 left-0 right-0 p-6 md:p-8 bg-gradient-to-t from-black/70 to-transparent">
              <p className="text-white/80 text-sm tracking-wider uppercase mb-2">Facilities</p>
              <p className="text-white text-xl md:text-2xl font-light">Indoor arena, pastures, and 50 acres of land</p>
            </div>
          </motion.div>
        </div>
      </section>

      {/* Pastures Section */}
      <section className="py-20 md:py-28 px-6 lg:px-12 bg-pasture-green text-white">
        <div className="max-w-7xl mx-auto">
          <div className="grid lg:grid-cols-2 gap-12 lg:gap-24 items-center">
            <motion.div
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6 }}
            >
              <p className="text-white/60 text-sm tracking-wider uppercase mb-4">The Land</p>
              <h2 className="text-3xl md:text-4xl lg:text-5xl font-light tracking-tight leading-tight mb-6">
                Room to roam
              </h2>
              <p className="text-white/80 text-lg leading-relaxed mb-6">
                Our horses spend their days in fenced pastures with plenty of grass 
                and fresh air. We have 50 acres of Vermont countryside with 12 
                separate paddocks for turnout.
              </p>
              <div className="grid grid-cols-2 gap-6">
                <div>
                  <p className="text-4xl font-light text-white mb-1">50</p>
                  <p className="text-white/60 text-sm">Acres</p>
                </div>
                <div>
                  <p className="text-4xl font-light text-white mb-1">12</p>
                  <p className="text-white/60 text-sm">Paddocks</p>
                </div>
              </div>
            </motion.div>

            <motion.div
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6, delay: 0.1 }}
              className="relative"
            >
              <div className="aspect-[4/3] bg-white/10 rounded-lg overflow-hidden">
                <img
                  src="/images/outlook-farm/view-of-barn.png"
                  alt="Outlook Farm pastures"
                  className="object-cover w-full h-full"
                />
              </div>
            </motion.div>
          </div>
        </div>
      </section>

      {/* Contact CTA */}
      <section className="py-20 md:py-28 px-6 lg:px-12 bg-black text-white">
        <div className="max-w-4xl mx-auto text-center">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6 }}
          >
            <h2 className="text-3xl md:text-4xl lg:text-5xl font-light tracking-tight mb-6">
              Come ride with us
            </h2>
            <p className="text-white/60 text-lg mb-10 max-w-2xl mx-auto">
              Whether you&apos;ve never been on a horse or you&apos;re looking to improve your skills, 
              we&apos;d love to have you visit.
            </p>
            <Link 
              href="/contact"
              className="inline-flex items-center justify-center gap-3 px-10 py-4 bg-pasture-green text-white text-sm tracking-wide hover:bg-pasture-green-dark transition-all duration-300"
            >
              Get in touch
              <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M17 8l4 4m0 0l-4 4m4-4H3" />
              </svg>
            </Link>
          </motion.div>
        </div>
      </section>

    </main>
  );
}

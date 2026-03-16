'use client';

import Link from 'next/link';
import { useRef } from 'react';
import { motion, useScroll, useTransform, useInView } from 'framer-motion';
import { Star, Clock, MapPin, ArrowRight, Phone, Calendar, Award, Scissors } from 'lucide-react';
import Navigation from '@/components/Navigation';
import Image from 'next/image';

export default function HomePage() {
  const containerRef = useRef<HTMLDivElement>(null);
  const heroRef = useRef<HTMLDivElement>(null);
  const isHeroInView = useInView(heroRef, { once: true });
  
  const { scrollYProgress } = useScroll({ target: containerRef, offset: ["start start", "end end"] });
  const heroY = useTransform(scrollYProgress, [0, 0.3], [0, -50]);
  const heroOpacity = useTransform(scrollYProgress, [0, 0.2], [1, 0]);

  const services = [
    { name: 'Classic Haircut', price: '$35', duration: '30 min', description: 'A solid cut that works for you' },
    { name: 'Fade / Taper', price: '$40', duration: '35 min', description: 'Clean fade with sharp lines' },
    { name: 'Beard Trim', price: '$20', duration: '15 min', description: 'Keep your beard looking sharp' },
    { name: 'Haircut & Beard', price: '$50', duration: '45 min', description: 'The full package' },
  ];

  const reviews = [
    { name: 'Rusty S.', rating: 5, text: 'Brook listens to me, rather than merely doing the same thing every time. She\'s always good-humored, and respectful of schedules.', date: 'Dec 2024' },
    { name: 'T. N.', rating: 5, text: 'Brooke is great! She\'s pretty skilled with a pair of scissors and a razor for a men\'s haircut. Highly recommend!', date: 'Jul 2024' },
    { name: 'Susan Henderson', rating: 5, text: 'Great haircuts by Brooke. Have been there many times and always happy with how my hair is cut.', date: 'Jul 2024' },
    { name: 'Lynne Weaver', rating: 5, text: 'Thank you Brooke for taking the time to get my color and style just perfect!! I absolutely love it!', date: 'May 2024' },
    { name: 'Meredith Erickson', rating: 5, text: 'Stylist was friendly, haircut was exactly what I requested, salon was super clean and welcoming.', date: 'Feb 2024' },
    { name: 'Reagan Quinn', rating: 5, text: 'Brooke is super friendly, and the salon is very nice and clean! Wonderful job cutting and styling.', date: 'Feb 2024' },
  ];

  const features = [
    { icon: Award, title: '20+ Years Experience', desc: 'Brooke knows her stuff' },
    { icon: MapPin, title: 'Downtown Hanover', desc: '53 S. Main St' },
    { icon: Calendar, title: 'Easy Booking', desc: 'Book online anytime' },
    { icon: Phone, title: 'Walk-ins Welcome', desc: 'When there\'s room' },
  ];

  return (
    <main ref={containerRef} className="min-h-screen bg-white overflow-x-hidden">
      <Navigation />

      {/* Hero Section */}
      <section ref={heroRef} className="relative min-h-screen pt-32 pb-20 lg:pt-40 lg:pb-32 bg-black overflow-hidden">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative">
          <div className="grid lg:grid-cols-2 gap-12 lg:gap-20 items-center">
            <motion.div style={{ y: heroY, opacity: heroOpacity }} className="relative z-10">
              <motion.span 
                initial={{ opacity: 0, y: 20 }} 
                animate={isHeroInView ? { opacity: 1, y: 0 } : {}} 
                transition={{ duration: 0.6, delay: 0.2 }}
                className="inline-block text-gold text-sm tracking-wider uppercase mb-6"
              >
                Barber Shop in Hanover, NH
              </motion.span>
              
              <motion.h1
                initial={{ opacity: 0, y: 30 }}
                animate={isHeroInView ? { opacity: 1, y: 0 } : {}}
                transition={{ duration: 0.8, delay: 0.3 }}
                className="text-5xl md:text-6xl lg:text-7xl font-bold text-white leading-tight mb-6"
              >
                Good haircuts.<br />
                <span className="text-gold">Done right.</span>
              </motion.h1>
              
              <motion.p 
                initial={{ opacity: 0, y: 20 }} 
                animate={isHeroInView ? { opacity: 1, y: 0 } : {}} 
                transition={{ duration: 0.6, delay: 0.5 }}
                className="text-xl text-grey-300 mb-10 max-w-lg leading-relaxed"
              >
                Brooke has been cutting hair in the Upper Valley for 20+ years. 
                She listens, she\'s skilled, and she respects your time.
              </motion.p>
              
              <motion.div 
                initial={{ opacity: 0, y: 20 }} 
                animate={isHeroInView ? { opacity: 1, y: 0 } : {}} 
                transition={{ duration: 0.6, delay: 0.6 }} 
                className="flex flex-wrap gap-4"
              >
                <a 
                  href="https://bookoapp.com/book/twisted-scissors" 
                  target="_blank" 
                  rel="noopener noreferrer"
                  className="inline-flex items-center gap-2 px-8 py-4 bg-gold text-black font-semibold text-lg hover:bg-gold-light transition-all"
                >
                  Book Now
                  <ArrowRight size={20} />
                </a>
                <Link 
                  href="/services" 
                  className="inline-flex items-center gap-2 px-8 py-4 border-2 border-white/30 text-white font-semibold text-lg hover:bg-white/10 transition-all"
                >
                  See Services
                </Link>
              </motion.div>
            </motion.div>
            
            <motion.div 
              initial={{ opacity: 0, x: 50 }} 
              animate={isHeroInView ? { opacity: 1, x: 0 } : {}} 
              transition={{ duration: 0.8, delay: 0.4 }} 
              className="relative"
            >
              <div className="relative aspect-square overflow-hidden bg-grey-900 flex items-center justify-center p-12">
                <Image 
                  src="/images/logo.png" 
                  alt="Twisted Scissors Logo" 
                  width={350} 
                  height={350} 
                  className="object-contain" 
                  priority 
                />
              </div>
              
              <div className="absolute -bottom-4 -left-4 bg-gold text-black px-6 py-4">
                <div className="text-3xl font-bold">5.0</div>
                <div className="text-sm flex items-center gap-1">
                  <Star className="w-4 h-4 fill-current" /> Google Rating
                </div>
              </div>
            </motion.div>
          </div>
        </div>
      </section>

      {/* Features Bar */}
      <section className="bg-grey-100 border-y border-grey-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-8">
            {features.map((feature) => (
              <div key={feature.title} className="flex items-center gap-4">
                <div className="w-12 h-12 bg-gold/10 rounded-full flex items-center justify-center flex-shrink-0">
                  <feature.icon className="text-gold" size={24} />
                </div>
                <div>
                  <div className="font-bold text-black">{feature.title}</div>
                  <div className="text-grey-600 text-sm">{feature.desc}</div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Services Section */}
      <section className="py-20 lg:py-28">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-4xl md:text-5xl font-bold text-black mb-4">What We Do</h2>
            <p className="text-grey-600 text-lg max-w-2xl mx-auto">
              Straightforward pricing. Quality work. No surprises.
            </p>
          </div>
          
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            {services.map((service) => (
              <div 
                key={service.name} 
                className="bg-white p-6 border border-grey-200 hover:border-gold transition-colors"
              >
                <Scissors className="text-gold mb-4" size={24} />
                <h3 className="text-xl font-bold text-black mb-2">{service.name}</h3>
                <p className="text-grey-600 text-sm mb-4">{service.description}</p>
                <div className="flex items-center gap-4 text-grey-500 text-sm mb-4">
                  <span className="flex items-center gap-1">
                    <Clock size={14} /> {service.duration}
                  </span>
                </div>
                <div className="text-3xl font-bold text-gold">{service.price}</div>
              </div>
            ))}
          </div>
          
          <div className="text-center mt-12">
            <Link 
              href="/services" 
              className="inline-flex items-center gap-2 px-8 py-4 bg-black text-white font-semibold hover:bg-grey-800 transition-all"
            >
              All Services <ArrowRight size={20} />
            </Link>
          </div>
        </div>
      </section>

      {/* About Section */}
      <section className="py-20 lg:py-28 bg-black">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid lg:grid-cols-2 gap-16 items-center">
            <div>
              <span className="text-gold text-sm tracking-wider uppercase mb-4 block">About</span>
              <h2 className="text-4xl md:text-5xl font-bold text-white mb-6">
                Local barber.<br />Real experience.
              </h2>
              <div className="space-y-4 text-lg text-grey-300 leading-relaxed">
                <p>
                  Brooke has been cutting hair in Hanover for 18 years. She opened Twisted Scissors 
                  at 53 S. Main Street to give the Upper Valley a no-nonsense place to get a great haircut.
                </p>
                <p>
                  She listens to what you want, respects your time, and knows her way around 
                  both scissors and clippers. Men, women, kids—she does it all.
                </p>
              </div>
              <div className="grid grid-cols-3 gap-8 mt-10 pt-10 border-t border-white/10">
                <div>
                  <div className="text-4xl font-bold text-gold">18+</div>
                  <div className="text-grey-400 text-sm mt-1">Years in Hanover</div>
                </div>
                <div>
                  <div className="text-4xl font-bold text-gold">20+</div>
                  <div className="text-grey-400 text-sm mt-1">Years cutting hair</div>
                </div>
                <div>
                  <div className="text-4xl font-bold text-gold">5.0</div>
                  <div className="text-grey-400 text-sm mt-1">Google rating</div>
                </div>
              </div>
            </div>
            <div className="relative">
              <div className="relative aspect-[4/3] overflow-hidden">
                <Image 
                  src="/images/insideview.png" 
                  alt="Inside Twisted Scissors" 
                  fill 
                  className="object-cover" 
                />
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Reviews Section */}
      <section className="py-20 lg:py-28 bg-grey-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-4xl md:text-5xl font-bold text-black mb-4">What People Say</h2>
            <p className="text-grey-600 text-lg">Real reviews from real clients.</p>
          </div>
          
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            {reviews.map((review, index) => (
              <div 
                key={index} 
                className="bg-white p-6 shadow-sm border-t-4 border-gold"
              >
                <div className="flex gap-1 mb-4">
                  {[...Array(review.rating)].map((_, i) => (
                    <Star key={i} className="text-gold fill-gold" size={18} />
                  ))}
                </div>
                <p className="text-grey-600 mb-4 leading-relaxed">&ldquo;{review.text}&rdquo;</p>
                <div className="flex justify-between items-center pt-4 border-t border-grey-100">
                  <div className="font-bold text-black">{review.name}</div>
                  <div className="text-grey-400 text-sm">{review.date}</div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Hours & Location */}
      <section className="py-20 lg:py-28 bg-black">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid lg:grid-cols-2 gap-16">
            <div>
              <span className="text-gold text-sm tracking-wider uppercase mb-4 block">Hours</span>
              <h2 className="text-3xl md:text-4xl font-bold text-white mb-8">When We&apos;re Open</h2>
              <div className="space-y-3">
                {[
                  { day: 'Monday', hours: 'Closed' },
                  { day: 'Tuesday', hours: 'Closed' },
                  { day: 'Wednesday', hours: '9AM - 5PM' },
                  { day: 'Thursday', hours: '9AM - 5PM' },
                  { day: 'Friday', hours: '9AM - 5PM' },
                  { day: 'Saturday', hours: '9AM - 12:30PM' },
                  { day: 'Sunday', hours: 'Closed' }
                ].map((item) => (
                  <div 
                    key={item.day} 
                    className="flex justify-between items-center py-3 border-b border-white/10"
                  >
                    <span className="text-white">{item.day}</span>
                    <span className={item.hours === 'Closed' ? 'text-grey-500' : 'text-gold'}>
                      {item.hours}
                    </span>
                  </div>
                ))}
              </div>
            </div>
            
            <div>
              <span className="text-gold text-sm tracking-wider uppercase mb-4 block">Location</span>
              <h2 className="text-3xl md:text-4xl font-bold text-white mb-8">Find Us</h2>
              <div className="bg-white/5 p-6 border border-white/10">
                <div className="flex items-start gap-4 mb-4">
                  <MapPin className="text-gold mt-1" size={24} />
                  <div>
                    <div className="text-xl font-bold text-white mb-1">Twisted Scissors</div>
                    <div className="text-grey-300">53 S. Main Street</div>
                    <div className="text-grey-300">Hanover, NH 03755</div>
                  </div>
                </div>
                <div className="flex items-center gap-4">
                  <Phone className="text-gold" size={24} />
                  <a href="tel:6032779842" className="text-grey-300 hover:text-gold transition-colors text-lg">
                    (603) 277-9842
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-16 bg-gold">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h2 className="text-3xl md:text-4xl font-bold text-black mb-4">Need a haircut?</h2>
          <p className="text-lg text-black/80 mb-8">Book online or give us a call.</p>
          <a 
            href="https://bookoapp.com/book/twisted-scissors" 
            target="_blank" 
            rel="noopener noreferrer" 
            className="inline-flex items-center gap-2 px-10 py-4 bg-black text-gold font-bold text-lg hover:bg-grey-900 transition-all"
          >
            Book Now <ArrowRight size={24} />
          </a>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-black text-white py-12">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid md:grid-cols-4 gap-8">
            <div>
              <div className="flex items-center gap-2 mb-4">
                <div className="relative w-8 h-8">
                  <Image src="/images/logo.png" alt="Twisted Scissors" fill className="object-contain" />
                </div>
                <span className="font-bold text-xl">Twisted Scissors</span>
              </div>
              <p className="text-grey-400 text-sm">Barber shop in Hanover, NH</p>
            </div>
            <div>
              <h4 className="font-bold text-lg mb-4">Hours</h4>
              <ul className="space-y-2 text-grey-400 text-sm">
                <li>Wed-Fri: 9am - 5pm</li>
                <li>Saturday: 9am - 12:30pm</li>
                <li>Sun-Tue: Closed</li>
              </ul>
            </div>
            <div>
              <h4 className="font-bold text-lg mb-4">Contact</h4>
              <ul className="space-y-2 text-grey-400 text-sm">
                <li>(603) 277-9842</li>
                <li>53 S. Main St, Hanover, NH</li>
              </ul>
            </div>
            <div>
              <h4 className="font-bold text-lg mb-4">Book</h4>
              <a 
                href="https://bookoapp.com/book/twisted-scissors" 
                target="_blank" 
                rel="noopener noreferrer" 
                className="inline-flex items-center gap-2 px-6 py-3 bg-gold text-black font-semibold hover:bg-gold-light transition-all"
              >
                Schedule Online
              </a>
            </div>
          </div>
          <div className="border-t border-white/10 mt-10 pt-8 text-center text-grey-500 text-sm">
            &copy; {new Date().getFullYear()} Twisted Scissors. All rights reserved.
          </div>
        </div>
      </footer>
    </main>
  );
}

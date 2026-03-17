'use client';

import { useEffect, useRef, useState } from 'react';
import { motion, useScroll, useTransform, AnimatePresence } from 'framer-motion';
import { ArrowRight, Trophy, Users, Zap, ChevronDown, Play, Pause } from 'lucide-react';
import Link from 'next/link';

// Glitch text effect component
function GlitchText({ text, className }: { text: string; className?: string }) {
  return (
    <span className={`relative inline-block ${className}`}>
      <span className="relative z-10">{text}</span>
      <span className="absolute top-0 left-0 -z-10 translate-x-[2px] text-[#FF006E] opacity-70 animate-pulse">
        {text}
      </span>
      <span className="absolute top-0 left-0 -z-10 -translate-x-[2px] text-[#00FF88] opacity-70 animate-pulse delay-75">
        {text}
      </span>
    </span>
  );
}

// Counter animation component
function AnimatedCounter({ target, suffix = '' }: { target: number; suffix?: string }) {
  const [count, setCount] = useState(0);
  const ref = useRef<HTMLSpanElement>(null);
  
  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          const duration = 2000;
          const steps = 60;
          const increment = target / steps;
          let current = 0;
          
          const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
              setCount(target);
              clearInterval(timer);
            } else {
              setCount(Math.floor(current));
            }
          }, duration / steps);
          
          observer.disconnect();
        }
      },
      { threshold: 0.5 }
    );
    
    if (ref.current) observer.observe(ref.current);
    return () => observer.disconnect();
  }, [target]);
  
  return <span ref={ref}>{count}{suffix}</span>;
}

export default function HomePage() {
  const containerRef = useRef<HTMLDivElement>(null);
  const videoRef = useRef<HTMLVideoElement>(null);
  const [isPlaying, setIsPlaying] = useState(true);
  const { scrollYProgress } = useScroll({
    target: containerRef,
    offset: ["start start", "end start"]
  });
  
  const heroY = useTransform(scrollYProgress, [0, 0.5], [0, 150]);
  const heroOpacity = useTransform(scrollYProgress, [0, 0.3], [1, 0]);
  const videoScale = useTransform(scrollYProgress, [0, 0.5], [1, 1.1]);

  const toggleVideo = () => {
    if (videoRef.current) {
      if (isPlaying) {
        videoRef.current.pause();
      } else {
        videoRef.current.play();
      }
      setIsPlaying(!isPlaying);
    }
  };

  const teamMembers = [
    { name: 'Andy Zhang', role: 'Lead Builder' },
    { name: 'Owen Osterberg', role: 'Programming' },
    { name: 'Ben Pastel', role: 'Driver' },
    { name: 'Kastner Anderson', role: 'Engineering' },
    { name: 'Elizabeth Anderson', role: 'Outreach' },
    { name: 'Jacob Hannan', role: 'Design' },
    { name: 'Grayson Lyall', role: 'Strategy' },
    { name: 'Alan Zhang', role: 'Research' },
  ];

  return (
    <main ref={containerRef} className="bg-[#060608] text-[#F0F0F5]">
      {/* Navigation */}
      <nav className="fixed top-0 left-0 right-0 z-50 px-6 lg:px-12 py-6">
        <div className="max-w-[1600px] mx-auto flex items-center justify-between">
          <Link href="/" className="font-display text-2xl font-bold tracking-tight">
            <GlitchText text="HapLink" />
          </Link>
          
          <div className="hidden md:flex items-center gap-8">
            <Link href="#team" className="text-sm font-medium text-[#6B6B7B] hover:text-[#00FF88] transition-colors">
              Team
            </Link>
            <Link href="#robot" className="text-sm font-medium text-[#6B6B7B] hover:text-[#00FF88] transition-colors">
              Robot
            </Link>
            <Link href="#seasons" className="text-sm font-medium text-[#6B6B7B] hover:text-[#00FF88] transition-colors">
              Seasons
            </Link>
          </div>
          
          <Link 
            href="#contact" 
            className="px-6 py-2.5 bg-[#00FF88] text-[#060608] font-semibold text-sm rounded-full hover:glow-accent transition-all duration-300"
          >
            Support Us
          </Link>
        </div>
      </nav>

      {/* Hero Section - Full viewport with video background */}
      <section className="relative min-h-screen flex items-center justify-center overflow-hidden">
        {/* Video Background */}
        <motion.div 
          className="absolute inset-0 z-0"
          style={{ scale: videoScale }}
        >
          <video
            ref={videoRef}
            autoPlay
            muted
            loop
            playsInline
            className="w-full h-full object-cover opacity-40"
          >
            <source src="/images/robot-2025.mp4" type="video/mp4" />
          </video>
          <div className="absolute inset-0 bg-gradient-to-b from-[#060608] via-transparent to-[#060608]" />
          <div className="absolute inset-0 bg-gradient-to-r from-[#060608] via-transparent to-[#060608]" />
        </motion.div>

        {/* Hero Content */}
        <motion.div 
          className="relative z-10 max-w-[1600px] mx-auto px-6 lg:px-12 text-center"
          style={{ y: heroY, opacity: heroOpacity }}
        >
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, ease: [0.16, 1, 0.3, 1] }}
          >
            <span className="inline-block px-4 py-2 bg-[#12121A] border border-[#00FF88]/30 rounded-full text-[#00FF88] text-xs font-mono tracking-[0.3em] uppercase mb-8">
              FIRST Tech Challenge 2024-2025
            </span>
          </motion.div>

          <motion.h1
            initial={{ opacity: 0, y: 50 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 1, delay: 0.2, ease: [0.16, 1, 0.3, 1] }}
            className="font-display text-7xl md:text-8xl lg:text-[10rem] font-bold leading-[0.85] tracking-tight mb-6"
          >
            <span className="block">TEAM</span>
            <span className="block text-gradient">26532</span>
          </motion.h1>

          <motion.p
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.4, ease: [0.16, 1, 0.3, 1] }}
            className="text-xl md:text-2xl text-[#6B6B7B] max-w-2xl mx-auto mb-12 font-body"
          >
            Happy Haptic Doctors. Eight students. One robot. Infinite innovation.
          </motion.p>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.6, ease: [0.16, 1, 0.3, 1] }}
            className="flex flex-wrap items-center justify-center gap-4"
          >
            <Link 
              href="#robot"
              className="group inline-flex items-center gap-3 px-8 py-4 bg-[#00FF88] text-[#060608] font-semibold rounded-full hover:glow-accent-strong transition-all duration-300"
            >
              Meet the Robot
              <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
            </Link>
            
            <button 
              onClick={toggleVideo}
              className="inline-flex items-center gap-3 px-8 py-4 border border-[#6B6B7B] text-[#F0F0F5] font-semibold rounded-full hover:border-[#00FF88] hover:text-[#00FF88] transition-all duration-300"
            >
              {isPlaying ? <Pause className="w-5 h-5" /> : <Play className="w-5 h-5" />}
              {isPlaying ? 'Pause Video' : 'Play Video'}
            </button>
          </motion.div>
        </motion.div>

        {/* Scroll indicator */}
        <motion.div 
          className="absolute bottom-12 left-1/2 -translate-x-1/2 z-10"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 1.2 }}
        >
          <motion.div
            animate={{ y: [0, 10, 0] }}
            transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
            className="flex flex-col items-center gap-2 text-[#6B6B7B]"
          >
            <span className="text-xs font-mono tracking-widest uppercase">Scroll</span>
            <ChevronDown className="w-5 h-5" />
          </motion.div>
        </motion.div>
      </section>

      {/* Stats Section */}
      <section className="py-24 px-6 lg:px-12 border-y border-[#12121A]">
        <div className="max-w-[1600px] mx-auto">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-8 md:gap-12">
            {[
              { value: 8, suffix: '', label: 'Team Members' },
              { value: 3, suffix: '', label: 'Years Competing' },
              { value: 2, suffix: '', label: 'World Championships' },
              { value: 26532, suffix: '', label: 'Team Number' },
            ].map((stat, i) => (
              <motion.div
                key={stat.label}
                initial={{ opacity: 0, y: 30 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.6, delay: i * 0.1 }}
                viewport={{ once: true }}
                className="text-center"
              >
                <div className="font-display text-5xl md:text-6xl font-bold text-[#00FF88] mb-2">
                  <AnimatedCounter target={stat.value} suffix={stat.suffix} />
                </div>
                <div className="text-sm text-[#6B6B7B] font-medium tracking-wider uppercase">
                  {stat.label}
                </div>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Robot Section */}
      <section id="robot" className="py-32 px-6 lg:px-12">
        <div className="max-w-[1600px] mx-auto">
          <div className="grid lg:grid-cols-2 gap-16 items-center">
            <motion.div
              initial={{ opacity: 0, x: -50 }}
              whileInView={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.8 }}
              viewport={{ once: true }}
            >
              <span className="inline-block px-4 py-2 bg-[#12121A] border border-[#FF006E]/30 rounded-full text-[#FF006E] text-xs font-mono tracking-[0.3em] uppercase mb-6">
                2026 Season
              </span>
              
              <h2 className="font-display text-5xl md:text-6xl font-bold mb-6 leading-tight">
                Meet Our <br />
                <span className="text-gradient">2026 Robot</span>
              </h2>
              
              <p className="text-lg text-[#6B6B7B] mb-8 leading-relaxed">
                Built for speed, precision, and reliability. Our 2026 robot features omni-wheel drive, 
                a precision flywheel mechanism, and an advanced intake system designed to dominate 
                the competition.
              </p>

              <div className="grid grid-cols-2 gap-6 mb-8">
                {[
                  { icon: Zap, label: 'Drive System', value: 'Omni-Wheel 4WD' },
                  { icon: Trophy, label: 'Scoring', value: 'Flywheel Precision' },
                ].map((spec) => (
                  <div key={spec.label} className="p-4 bg-[#0A0A0F] border border-[#12121A] rounded-xl">
                    <spec.icon className="w-6 h-6 text-[#00FF88] mb-3" />
                    <div className="text-sm text-[#6B6B7B] mb-1">{spec.label}</div>
                    <div className="font-semibold">{spec.value}</div>
                  </div>
                ))}
              </div>

              <Link 
                href="/robot"
                className="group inline-flex items-center gap-3 text-[#00FF88] font-semibold hover:gap-4 transition-all"
              >
                Full Robot Specs
                <ArrowRight className="w-5 h-5" />
              </Link>
            </motion.div>

            <motion.div
              initial={{ opacity: 0, x: 50 }}
              whileInView={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.8 }}
              viewport={{ once: true }}
              className="relative"
            >
              <div className="relative aspect-square rounded-2xl overflow-hidden bg-[#0A0A0F] border border-[#12121A]">
                <img 
                  src="/images/robot-2026.jpg" 
                  alt="2026 Robot"
                  className="w-full h-full object-cover"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-[#060608] via-transparent to-transparent" />
              </div>
              
              {/* Floating badge */}
              <motion.div 
                className="absolute -bottom-6 -left-6 px-6 py-4 bg-[#12121A] border border-[#00FF88]/30 rounded-xl"
                animate={{ y: [0, -10, 0] }}
                transition={{ duration: 4, repeat: Infinity, ease: "easeInOut" }}
              >
                <div className="text-3xl font-display font-bold text-[#00FF88]">2026</div>
                <div className="text-sm text-[#6B6B7B]">Competition Ready</div>
              </motion.div>
            </motion.div>
          </div>
        </div>
      </section>

      {/* Team Section */}
      <section id="team" className="py-32 px-6 lg:px-12 bg-[#0A0A0F]">
        <div className="max-w-[1600px] mx-auto">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
            viewport={{ once: true }}
            className="text-center mb-16"
          >
            <span className="inline-block px-4 py-2 bg-[#12121A] border border-[#00FF88]/30 rounded-full text-[#00FF88] text-xs font-mono tracking-[0.3em] uppercase mb-6">
              The Squad
            </span>
            <h2 className="font-display text-5xl md:text-6xl font-bold mb-6">
              Meet the <span className="text-gradient">Team</span>
            </h2>
            <p className="text-lg text-[#6B6B7B] max-w-2xl mx-auto">
              Eight students from Hanover, NH, united by a passion for robotics and innovation.
            </p>
          </motion.div>

          <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
            {teamMembers.map((member, i) => (
              <motion.div
                key={member.name}
                initial={{ opacity: 0, y: 30 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5, delay: i * 0.1 }}
                viewport={{ once: true }}
                className="group p-6 bg-[#060608] border border-[#12121A] rounded-2xl hover:border-[#00FF88]/50 transition-all duration-300"
              >
                <div className="w-16 h-16 mb-4 rounded-full bg-gradient-to-br from-[#00FF88]/20 to-[#FF006E]/20 flex items-center justify-center">
                  <Users className="w-8 h-8 text-[#00FF88]" />
                </div>
                <h3 className="font-display text-xl font-bold mb-1 group-hover:text-[#00FF88] transition-colors">
                  {member.name}
                </h3>
                <p className="text-sm text-[#6B6B7B]">{member.role}</p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Seasons Timeline */}
      <section id="seasons" className="py-32 px-6 lg:px-12">
        <div className="max-w-[1600px] mx-auto">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
            viewport={{ once: true }}
            className="text-center mb-16"
          >
            <span className="inline-block px-4 py-2 bg-[#12121A] border border-[#FF006E]/30 rounded-full text-[#FF006E] text-xs font-mono tracking-[0.3em] uppercase mb-6">
              Our Journey
            </span>
            <h2 className="font-display text-5xl md:text-6xl font-bold mb-6">
              Season <span className="text-gradient">History</span>
            </h2>
          </motion.div>

          <div className="space-y-8">
            {[
              { year: '2023-24', title: 'FLL Worlds', desc: 'First Lego League World Championship competitors', highlight: 'Houston, TX' },
              { year: '2024-25', title: 'FTC Rookie Year', desc: 'Transitioned to FIRST Tech Challenge', highlight: 'Into the Deep' },
              { year: '2025-26', title: 'Veteran Status', desc: 'Second year FTC with refined strategy', highlight: 'Current Season' },
            ].map((season, i) => (
              <motion.div
                key={season.year}
                initial={{ opacity: 0, x: i % 2 === 0 ? -50 : 50 }}
                whileInView={{ opacity: 1, x: 0 }}
                transition={{ duration: 0.6 }}
                viewport={{ once: true }}
                className="flex flex-col md:flex-row items-center gap-8 p-8 bg-[#0A0A0F] border border-[#12121A] rounded-2xl hover:border-[#00FF88]/30 transition-colors"
              >
                <div className="md:w-32 text-center md:text-left">
                  <div className="font-display text-3xl font-bold text-[#00FF88]">{season.year}</div>
                </div>
                <div className="flex-1 text-center md:text-left">
                  <h3 className="font-display text-2xl font-bold mb-2">{season.title}</h3>
                  <p className="text-[#6B6B7B]">{season.desc}</p>
                </div>
                <div className="px-4 py-2 bg-[#12121A] rounded-full text-sm font-mono text-[#FF006E]">
                  {season.highlight}
                </div>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section id="contact" className="py-32 px-6 lg:px-12">
        <div className="max-w-[1600px] mx-auto">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
            viewport={{ once: true }}
            className="relative p-12 md:p-20 bg-gradient-to-br from-[#0A0A0F] to-[#12121A] border border-[#12121A] rounded-3xl overflow-hidden"
          >
            {/* Background glow */}
            <div className="absolute top-0 right-0 w-96 h-96 bg-[#00FF88]/10 rounded-full blur-[128px]" />
            <div className="absolute bottom-0 left-0 w-96 h-96 bg-[#FF006E]/10 rounded-full blur-[128px]" />
            
            <div className="relative z-10 text-center">
              <h2 className="font-display text-4xl md:text-6xl font-bold mb-6">
                Support <span className="text-gradient">Team 26532</span>
              </h2>
              <p className="text-lg text-[#6B6B7B] max-w-2xl mx-auto mb-10">
                Your donation helps us purchase materials, attend competitions, and continue 
                pushing the boundaries of what&apos;s possible in robotics.
              </p>
              
              <div className="flex flex-wrap items-center justify-center gap-4">
                <Link 
                  href="/donate"
                  className="inline-flex items-center gap-3 px-10 py-5 bg-[#00FF88] text-[#060608] font-bold text-lg rounded-full hover:glow-accent-strong transition-all duration-300"
                >
                  Donate Now
                  <ArrowRight className="w-6 h-6" />
                </Link>
                
                <Link 
                  href="/contact"
                  className="inline-flex items-center gap-3 px-10 py-5 border border-[#6B6B7B] text-[#F0F0F5] font-semibold rounded-full hover:border-[#00FF88] hover:text-[#00FF88] transition-all duration-300"
                >
                  Contact Us
                </Link>
              </div>
            </div>
          </motion.div>
        </div>
      </section>

      {/* Footer */}
      <footer className="py-12 px-6 lg:px-12 border-t border-[#12121A]">
        <div className="max-w-[1600px] mx-auto flex flex-col md:flex-row items-center justify-between gap-6">
          <div className="font-display text-2xl font-bold">
            <GlitchText text="HapLink" />
          </div>
          
          <div className="text-sm text-[#6B6B7B]">
            Team 26532 • Happy Haptic Doctors • Hanover, NH
          </div>
          
          <div className="flex items-center gap-6">
            <Link href="https://github.com/AEnldlya/haplink-robotics" className="text-[#6B6B7B] hover:text-[#00FF88] transition-colors">
              GitHub
            </Link>
            <Link href="/donate" className="text-[#6B6B7B] hover:text-[#00FF88] transition-colors">
              Donate
            </Link>
          </div>
        </div>
      </footer>
    </main>
  );
}

'use client';

import Link from 'next/link';
import { useState } from 'react';
import { Menu, X, Phone } from 'lucide-react';
import Image from 'next/image';

export default function Navigation() {
  const [isOpen, setIsOpen] = useState(false);

  const navLinks = [
    { href: '/services', label: 'Services' },
    { href: '/about', label: 'About' },
    { href: '/reviews', label: 'Reviews' },
    { href: '/contact', label: 'Contact' },
  ];

  return (
    <nav className="fixed top-0 left-0 right-0 z-50 bg-black/95 backdrop-blur-md border-b border-white/10">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-20">
          {/* Logo */}
          <Link href="/" className="flex items-center gap-3">
            <div className="relative w-10 h-10">
              <Image src="/images/logo.png" alt="Twisted Scissors" fill className="object-contain" />
            </div>
            <span className="font-display text-2xl font-bold text-white tracking-wide">
              TWISTED <span className="text-gold">SCISSORS</span>
            </span>
          </Link>

          {/* Desktop Nav */}
          <div className="hidden md:flex items-center gap-8">
            {navLinks.map((link) => (
              <Link key={link.href} href={link.href} className="text-white/80 hover:text-gold transition-colors font-medium">
                {link.label}
              </Link>
            ))}
            <a href="tel:6032779842" className="flex items-center gap-2 text-gold hover:text-white transition-colors">
              <Phone size={18} />
              <span className="font-medium">(603) 277-9842</span>
            </a>
            <a href="https://bookoapp.com/book/twisted-scissors" target="_blank" rel="noopener noreferrer"
              className="px-6 py-3 bg-gold text-white font-semibold hover:bg-blue-700 transition-all">
              Book Now
            </a>
          </div>

          {/* Mobile Menu Button */}
          <button onClick={() => setIsOpen(!isOpen)} className="md:hidden text-white p-2">
            {isOpen ? <X size={28} /> : <Menu size={28} />}
          </button>
        </div>
      </div>

      {/* Mobile Menu */}
      {isOpen && (
        <div className="md:hidden bg-black border-t border-white/10">
          <div className="px-4 py-6 space-y-4">
            {navLinks.map((link) => (
              <Link key={link.href} href={link.href} onClick={() => setIsOpen(false)} className="block text-white/80 hover:text-gold transition-colors font-medium text-lg">
                {link.label}
              </Link>
            ))}
            <a href="tel:6032779842" className="flex items-center gap-2 text-gold py-2">
              <Phone size={18} />
              <span>(603) 277-9842</span>
            </a>
            <a href="https://bookoapp.com/book/twisted-scissors" target="_blank" rel="noopener noreferrer"
              className="block w-full text-center px-8 py-4 bg-gold text-white font-semibold mt-4" onClick={() => setIsOpen(false)}>
              Book Now
            </a>
          </div>
        </div>
      )}
    </nav>
  );
}

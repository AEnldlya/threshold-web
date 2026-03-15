'use client';

import React from 'react';

interface LogoProps {
  className?: string;
  size?: number;
  showText?: boolean;
}

export default function Logo({ className = '', size = 40, showText = true }: LogoProps) {
  return (
    <div className={`flex items-center space-x-2 ${className}`}>
      <svg
        width={size}
        height={size}
        viewBox="0 0 40 40"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
        className="flex-shrink-0"
      >
        <defs>
          <linearGradient id="logoGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stopColor="#14b8a6" />
            <stop offset="100%" stopColor="#0d9488" />
          </linearGradient>
          <linearGradient id="logoGradientLight" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stopColor="#5eead4" />
            <stop offset="100%" stopColor="#14b8a6" />
          </linearGradient>
        </defs>
        
        {/* Background rounded square */}
        <rect
          x="2"
          y="2"
          width="36"
          height="36"
          rx="8"
          fill="url(#logoGradient)"
        />
        
        {/* Inner highlight */}
        <rect
          x="2"
          y="2"
          width="36"
          height="36"
          rx="8"
          fill="url(#logoGradientLight)"
          opacity="0.3"
        />
        
        {/* W letter */}
        <path
          d="M8 12L12 28L16 18L20 28L24 18L28 28L32 12"
          stroke="white"
          strokeWidth="2.5"
          strokeLinecap="round"
          strokeLinejoin="round"
          fill="none"
        />
        
        {/* M letter overlay (subtle) */}
        <path
          d="M10 12L14 22L18 12"
          stroke="white"
          strokeWidth="2"
          strokeLinecap="round"
          strokeLinejoin="round"
          fill="none"
          opacity="0.6"
        />
      </svg>
      
      {showText && (
        <span className="text-xl font-bold text-white tracking-tight">
          WebMaker
        </span>
      )}
    </div>
  );
}

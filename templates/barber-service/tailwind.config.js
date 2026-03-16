/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      fontFamily: {
        display: ['var(--font-oswald)', 'system-ui', 'sans-serif'],
        sans: ['var(--font-inter)', 'system-ui', 'sans-serif'],
        accent: ['var(--font-playfair)', 'serif'],
      },
      colors: {
        black: '#0A0A0A',
        white: '#FFFFFF',
        grey: {
          100: '#F5F5F5',
          200: '#E5E5E5',
          300: '#D4D4D4',
          400: '#A3A3A3',
          500: '#737373',
          600: '#525252',
          700: '#404040',
          800: '#262626',
          900: '#171717',
        },
        gold: '#D4AF37',
        'gold-light': '#F4D03F',
        'gold-dark': '#B8860B',
        cream: '#F5F5F0',
      },
    },
  },
  plugins: [],
}

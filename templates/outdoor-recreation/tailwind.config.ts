/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        // Logo-inspired palette
        cream: {
          DEFAULT: '#faf9f6',
          warm: '#f5f3ef',
        },
        warm: {
          gray: '#e8e4de',
          light: '#d4cfc7',
        },
        stone: {
          DEFAULT: '#9a958d',
          light: '#d4cfc7',
          dark: '#6b665e',
          50: '#fafaf9',
          100: '#f5f5f4',
          200: '#e7e5e4',
          300: '#d6d3d1',
          400: '#a8a29e',
          500: '#78716c',
          600: '#57534e',
          700: '#44403c',
          800: '#292524',
          900: '#1c1917',
        },
        charcoal: '#3d3a36',
        black: '#1a1917',
        accent: {
          warm: '#c4a77d',
          gold: '#b8956a',
        },
        // Pasture green - for green pastures
        'pasture-green': {
          DEFAULT: '#4a6741',
          light: '#6b8f5e',
          dark: '#354d2e',
        },
      },
      fontFamily: {
        sans: ['Inter', '-apple-system', 'BlinkMacSystemFont', 'sans-serif'],
      },
      spacing: {
        '18': '4.5rem',
        '88': '22rem',
      },
    },
  },
  plugins: [],
}

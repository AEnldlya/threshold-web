/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './app/**/*.{js,ts,jsx,tsx,mdx}',
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        // Retro Color Palette
        retro: {
          olive: '#6B6556',      // Dark olive green
          red: '#FF3300',        // Bright retro red
          mint: '#6BC4A6',       // Mint green
          yellow: '#FFE082',     // Soft yellow
          cream: '#FFFACD',      // Cream yellow
        }
      }
    },
  },
  plugins: [],
}

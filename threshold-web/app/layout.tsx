import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'Threshold Web - Professional Websites',
  description: 'High-performance websites built for local businesses. Professional design, optimized performance, delivered in 10 days.',
  metadataBase: new URL('https://thresholdweb.com'),
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className="scroll-smooth">
      <body className="bg-white text-gray-900">
        {children}
      </body>
    </html>
  )
}

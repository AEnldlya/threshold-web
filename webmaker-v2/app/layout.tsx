import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'WebMaker AI - Professional Websites Built for Local Businesses',
  description: 'We build stunning, high-converting websites for local businesses. 10-day delivery, $2,500 starting price.',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}

import './globals.css'
import type { Metadata } from 'next'
import Header from './components/Header'

export const metadata: Metadata = {
  title: 'TechPick',
  description: 'Technology recommendation based on project descriptions',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>
        <Header />
        <div className="min-h-main bg-background">
          {children}
        </div>
      </body>
    </html>
  )
}

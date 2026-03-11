import { NextRequest, NextResponse } from 'next/server'

export async function POST(request: NextRequest) {
  try {
    const data = await request.json()
    
    // Log the form data
    console.log('Contact form submission:', data)
    
    // In production, you would:
    // 1. Send email via SendGrid, Mailgun, etc.
    // 2. Save to database
    // 3. Send confirmation email to user
    
    // For now, just return success
    return NextResponse.json(
      { success: true, message: 'Thank you for reaching out! We will contact you soon.' },
      { status: 200 }
    )
  } catch (error) {
    console.error('Form submission error:', error)
    return NextResponse.json(
      { success: false, message: 'Error submitting form' },
      { status: 500 }
    )
  }
}

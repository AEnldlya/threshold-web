#!/usr/bin/env python3

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

def send_pen_email():
    """Send the pen return demand email"""
    
    sender_email = "Andy.li.zhang2010@gmail.com"
    recipient_email = "liamglenny@hanovernorwichschools.org"
    app_password = "Ljnzy@Nov16"
    
    # Email details
    subject = "Yo, give me my pen back"
    body = """Liam,

Still waiting on that pen. Not sure what you're doing with it, but it's mine. Return it before I send the authorities.

Thanks,
Andy"""
    
    try:
        # Gmail SMTP setup
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        
        # Create message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        # Send
        print(f"📧 Sending email to {recipient_email}...")
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.send_message(msg)
        
        print(f"✓ Email sent successfully!")
        print(f"\nFrom: {sender_email}")
        print(f"To: {recipient_email}")
        print(f"Subject: {subject}")
        print(f"Sent at: {datetime.now().isoformat()}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error sending email: {str(e)}")
        return False

if __name__ == "__main__":
    send_pen_email()

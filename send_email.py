import os
import smtplib
from email.message import EmailMessage

# Set up the email content
msg = EmailMessage()
msg["Subject"] = "Subject of the email"
msg["From"] = os.getenv("EMAIL_ADDRESS")  # Using environment variable for email address
msg["To"] = "mate@e.email"  # Replace with the recipient's email address
msg.set_content("Body of the email goes here.")

# Connect to the SMTP server
with smtplib.SMTP(os.getenv("SMTP_SERVER"), os.getenv("SMTP_PORT")) as smtp:
    smtp.starttls()  # Start TLS encryption
    smtp.login(
        os.getenv("EMAIL_ADDRESS"), os.getenv("EMAIL_PASSWORD")
    )  # Using environment variables for credentials
    smtp.send_message(msg)

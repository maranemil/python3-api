import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_registration(receiver_email):
    # Email configuration
    sender_email = 'your_email@gmail.com'
    receiver_email = 'recipient_email@example.com'
    subject = 'Registration'
    body = """Hi (receiver_email),

Click the following link to activate your account: _____

Please note that this link expires after 3 days. If you wait
longer, you'll have to request another registration link.

Best regards,
Company"""

    # Create the MIME object
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Attach the body to the email
    message.attach(MIMEText(body, 'plain'))

    # SMTP server configuration
    smtp_server = 'smtp.my.server'
    smtp_port = 587
    smtp_username = 'your_email@'
    smtp_password = 'your_email_password'

    # Create the SMTP connection
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        # Start the TLS connection (for security)
        server.starttls()

        # Login to the email server
        server.login(smtp_username, smtp_password)

        # Send the email
        server.sendmail(sender_email, receiver_email, message.as_string())


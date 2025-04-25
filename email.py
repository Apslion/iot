import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Gmail credentials
sender_email = 'your_email@gmail.com'
receiver_email = 'receiver_email@example.com'
password = 'your_app_password'  # This is your generated App Password

# Email subject and body
subject = 'Test Email from Python'
body = 'This is a test email sent using Python and Gmail SMTP server.'

# Create the email message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Set up the Gmail SMTP server and send the email
try:
    # Connect to the Gmail SMTP server (using TLS encryption)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # Start TLS encryption
    
    # Log in to the Gmail account
    server.login(sender_email, password)
    
    # Send the email
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    print('Email sent successfully!')
    
except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the connection to the SMTP server
    server.quit()
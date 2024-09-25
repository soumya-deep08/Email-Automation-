import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_emails):
    # Your email credentials
    gmail_user = 'amodkarsneha@gmail.com'
    gmail_password = 'fpsg pqmm jjwl navy'

    # Create a secure SSL context
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    try:
        # Connect to the Gmail SMTP server
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
            server.login(gmail_user, gmail_password)
            
            # Send email to each recipient
            for to_email in to_emails:
                msg = MIMEMultipart()
                msg['From'] = gmail_user
                msg['Subject'] = subject
                
                # Attach the body to the email
                msg.attach(MIMEText(body, 'plain'))
                
                server.sendmail(gmail_user, to_email, msg.as_string())
                print(f'Email sent to {to_email} successfully!')
                
        print('All emails sent successfully!')
    except Exception as e:
        print(f'Error occurred: {e}')

# Example usage
subject = 'Test Email'
body = 'Hello, this is a test email.'
to_emails = ['srivastavaanushka878@gmail.com','soumaydeep2022@gmail.com']
send_email(subject, body, to_emails)
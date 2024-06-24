import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_notification_to_user(user_id, message):
    """
    Send an email notification to the user using Brevo SMTP.
    """
    user_email = get_user_email(user_id)
    
    if not user_email:
        print(f"User {user_id} does not have a valid email address.")
        return False

    try:
        # Brevo SMTP configuration
        smtp_server = "smtp-relay.brevo.com"
        smtp_port = 587
        smtp_user = "774177001@smtp-brevo.com"
        smtp_password = os.getenv('BREVO_SMTP_PASSWORD')
        from_email = os.getenv('FROM_EMAIL', 'no-reply@yourservice.com')
        from_name = os.getenv('FROM_NAME', 'Your Service Name')

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = f"{from_name} <{from_email}>"
        msg['To'] = user_email
        msg['Subject'] = 'Notification from Your Service'

        # Add the message body
        msg.attach(MIMEText(message, 'plain'))

        # Connect to Brevo SMTP and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(from_email, user_email, msg.as_string())

        print(f"Notification sent to user {user_id} at {user_email}.")
        return True
    except Exception as e:
        print(f"Failed to send notification to user {user_id}: {e}")
        return False

def get_user_email(user_id):
    """
    Fetch the user's email address from the database.
    This is a placeholder function. Replace it with actual database logic.
    """
    # Placeholder email addresses for demonstration purposes
    user_emails = {
        1: 'user1@example.com',
        2: 'user2@example.com',
        3: 'user3@example.com'
    }
    return user_emails.get(user_id)

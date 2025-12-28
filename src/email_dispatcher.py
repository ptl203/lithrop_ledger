import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

class EmailDispatcher:
    """
    This module handles the secure sending of the generated HTML newsletter via SMTP.
    """
    def __init__(self, smtp_host, smtp_port, username, password):
        """
        Initializes the SMTP connection details.
        """
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, to_emails: list, subject: str, html_content: str):
        """
        Establishes a secure connection to the SMTP server (e.g., `smtp.gmail.com:587`) using `smtplib`.
        Authenticates using the provided credentials (specifically, a Gmail App Password).
        Constructs a `MIMEMultipart` email message, setting the body to the provided HTML content and ensuring the `Content-Type` is `text/html`.
        Sends the email to the specified recipient(s).
        """
        if not to_emails:
            logging.warning("No recipients specified. Skipping email dispatch.")
            return

        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = self.username
        msg['To'] = ", ".join(to_emails)

        # Attach the HTML content
        part = MIMEText(html_content, 'html')
        msg.attach(part)

        try:
            with smtplib.SMTP(self.smtp_host, self.smtp_port) as server:
                server.starttls()
                server.login(self.username, self.password)
                server.send_message(msg)
                logging.info(f"Email sent successfully to: {', '.join(to_emails)}")
        except Exception as e:
            logging.error(f"Failed to send email: {e}")

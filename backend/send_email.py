import smtplib
import os
from email.mime.text import MIMEText

EMAIL = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("EMAIL_APP_PASSWORD")

def send_email(to_email, subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL
    msg["To"] = to_email

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)

if __name__ == "__main__":
    send_email(
        "test@email.com",
        "Quick question",
        "Hey — wanted to reach out about helping you get more clients."
    )

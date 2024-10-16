import os
from email.message import EmailMessage
import smtplib

from dotenv import load_dotenv
_ = load_dotenv()


def send_email(subject, content):
    account = os.environ.get("ACCOUNT")
    password = os.environ.get("PASSWORD")

    message = EmailMessage()
    message["To"] = os.environ.get("CONTACT")
    message["From"] = ""
    message["Subject"] = subject
    message.set_content(content)

    # Send email.
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(account, password)
        smtp.send_message(message)


if __name__ == "__main__":
    send_email("Test", "Le super test fonctionne bien dis donc.")
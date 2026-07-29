import smtplib
from email.mime.text import MIMEText

SENDER_EMAIL = "varunkumarguntireddi@gmail.com"
APP_PASSWORD = "qkyqslnhmhxomove"
print("EMAIL SENDER FILE LOADED")

def send_email(receiver, subject, body):

    try:

        msg = MIMEText(body)

        msg["Subject"] = subject
        msg["From"] = SENDER_EMAIL
        msg["To"] = receiver

        smtp = smtplib.SMTP("smtp.gmail.com", 587)

        smtp.starttls()

        smtp.login(SENDER_EMAIL, APP_PASSWORD)

        smtp.send_message(msg)

        smtp.quit()

        return True

    except Exception as e:
       print(type(e))
       print(e)
       return f"{type(e).__name__}: {e}"
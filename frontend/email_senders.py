import smtplib
from email.mime.text import MIMEText

SENDER_EMAIL = "varunkumarguntireddi@gmail.com"
APP_PASSWORD = "qkyqslnhmhxomove"

print("EMAIL SENDER FILE LOADED")


def send_email(receiver, subject, body):

    smtp = None

    try:
        print("=" * 50)
        print("Starting Email Sending")
        print("Receiver :", receiver)
        print("Subject  :", subject)

        msg = MIMEText(body, "plain", "utf-8")
        msg["Subject"] = subject
        msg["From"] = SENDER_EMAIL
        msg["To"] = receiver

        smtp = smtplib.SMTP("smtp.gmail.com", 587, timeout=20)

        # Show SMTP conversation in terminal
        smtp.set_debuglevel(1)

        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(SENDER_EMAIL, APP_PASSWORD)

        smtp.send_message(msg)

        print("Email Sent Successfully")
        print("=" * 50)

        return True

    except Exception as e:
        print("=" * 50)
        print("EMAIL ERROR")
        print(type(e).__name__)
        print(e)
        print("=" * 50)

        return f"{type(e).__name__}: {e}"

    finally:
        if smtp:
            try:
                smtp.quit()
            except:
                pass
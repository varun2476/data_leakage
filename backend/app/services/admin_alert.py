import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


ADMIN_EMAIL = "varunkumarguntireddi@gmail.com"

SMTP_EMAIL = "varunkumarguntireddi@gmail.com"
SMTP_PASSWORD = "qkyqslnhmhxomove"


def send_admin_alert(
        employee_id,
        receiver_email,
        risk_level,
        sender_email,
        detected_data,
        message
):

    subject = "🚨 Data Leakage Attempt Detected"

    body = f"""
    Hello BOSS,

    A possible data leakage attempt has been detected.

    Employee ID:
    {employee_id}

    Sender Email:
    {sender_email}

    Receiver Email:
    {receiver_email}

    Risk Level:
    {risk_level}

    Sensitive Data Detected:
    {detected_data}

    Message:
    {message}

    Action Taken:
    Transmission Blocked

    Regards,
    AI Secure Data Scanner
    """

    msg = MIMEMultipart()

    msg["From"] = SMTP_EMAIL
    msg["To"] = ADMIN_EMAIL
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))


    try:

        server = smtplib.SMTP(
            "smtp.gmail.com",
            587
        )

        server.starttls()

        server.login(
            SMTP_EMAIL,
            SMTP_PASSWORD
        )

        server.send_message(msg)

        server.quit()

        return True


    except Exception as e:

        print("Admin email error:", e)

        return False
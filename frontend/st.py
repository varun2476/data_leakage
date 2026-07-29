import smtplib

sender = "varunkumarguntireddi@gmail.com"
app_password = "qkyqslnhmhxomove"  # no spaces

try:
    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(sender, app_password)
    print("✅ Login successful")
    smtp.quit()
except Exception as e:
    print("❌ Login failed:", e)

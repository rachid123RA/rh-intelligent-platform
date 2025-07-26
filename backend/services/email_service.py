import smtplib
from email.mime.text import MIMEText

def send_email(to, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'tonmail@domaine.com'
    msg['To'] = to

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('tonmail@domaine.com', 'ton_password')
        server.send_message(msg)

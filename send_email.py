import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "zemka.kit@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "zemka.kit@gmail.com"
    content = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=content) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

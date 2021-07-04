import os
import smtplib, ssl


def send_email(name, subject, email, msg):
    port = 587  # For starttls
    smtp_server = os.getenv("SMTP")
    sender_email = os.getenv("SENDER")
    admins = ["NrdyBhu1@gmail.com", "nalinangrish2005@gmail.com", "cindysongh@gmail.com"]
    password = os.getenv("PSSWD")
    message = f"""
    Subject: {subject}
    From: {name}
    Email: {email}
    {msg}
    """
    
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        for addr in admins:
            server.sendmail(sender_email, addr, message)
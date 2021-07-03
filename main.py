from flask import Flask, request, jsonify, redirect
import smtplib, ssl
from dotenv import load_dotenv
import os

app = Flask(__name__)

false = False
true = True

load_dotenv()  # take environment variables from .env.

def send_email(name, subject, email, msg):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "unityusr@gmail.com"
    nrdybhu1_mail = "NrdyBhu1@gmail.com"
    nalin_mail = "nalinangrish2005@gmail.com"
    cindy_mail = "cindysongh@gmail.com"
    password = os.environ["PSSWD"]
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
        server.sendmail(sender_email, nrdybhu1_email, message)
        server.sendmail(sender_email, nalin_email, message)
        server.sendmail(sender_email, cindy_email, message)


@app.route("/contact" , methods=["GET", "POST"])
def send():
    if request.method == "POST":
        data = request.get_json()
        try:
            send_email(name=data['name'], subject=data['subject'], email=data['email'], msg=data['msg'])
            return jsonify({"success":true, "message": "Mail Sent!"})
        except Exception as e:
            return jsonify({"success":false, "message": f"Error: {e}"})
    if request.method == "GET":
        return "<h1>You should not use GET, use POST</h1>"


@app.route("/")
def home():
    return redirect("https://wwf-jr.netlify.app/", code=302)


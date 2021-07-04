from flask import Flask, request, jsonify, redirect
from dotenv import load_dotenv
from lib import *

app = Flask(__name__)

false = False
true = True

load_dotenv()  # take environment variables from .env.



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


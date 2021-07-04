from flask import Flask, request, jsonify, redirect
from dotenv import load_dotenv
from markupsafe import escape
from lib import send_email, get_conts, get_cont_info

# Create flask app
app = Flask(__name__)

false = False
true = True

load_dotenv()  # take environment variables from .env.


# interacts with contact post from frontend
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


# redirect to frontend instead of plain text
@app.route("/")
def home():
    return redirect("https://wwf-jr.netlify.app/", code=302)


# fetches a list of continents
@app.route("/fetch_cont")
def fetch_cont():
    try:
        return jsonify({"success":true, "conts":get_conts()})
    except Exception as e:
        return jsonify({"success":false, "error":e})
    
# fetches info of a continent
@app.route("/<string:cont>")
def fetch_cont_info(cont):
    try:
        if cont in get_conts():
            return jsonify({"success":true, "cont":escape(cont), "info":get_cont_info(escape(cont))})
        else:
            return jsonify({"success":false, "error": "No such continent!!"})
    except Exception as e:
        return jsonify({"success":false, "error":e})

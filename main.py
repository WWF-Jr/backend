from flask import Flask, request, jsonify, redirect
from dotenv import load_dotenv
from markupsafe import escape
from flask_cors import CORS, cross_origin
from lib import *

# Create flask app
app = Flask(__name__)
CORS(app)

false = False
true = True

load_dotenv()  # take environment variables from .env.


# interacts with contact post from frontend
@app.route("/contact" , methods=["GET", "POST"])
@cross_origin()
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
@cross_origin()
def home():
    return redirect("https://wwf-jr.netlify.app/", code=302)


# fetches a list of continents
@app.route("/fetch_cont")
@cross_origin()
def fetch_cont():
    try:
        return jsonify({"success":true, "conts":get_conts()})
    except Exception as e:
        return jsonify({"success":false, "error":e})
    
# fetches info of a continent
@app.route("/<string:cont>")
@cross_origin()
def fetch_cont_info(cont):
    cont = cont.lower()
    try:
        if cont in get_conts():
            return jsonify({"success":true, "cont":escape(cont), "info":get_cont_info(escape(cont)), "animals":get_animals_of_cont(escape(cont))})
        else:
            return jsonify({"success":false, "error": "No such continent!!"})
    except Exception as e:
        return jsonify({"success":false, "error":e})

    
# fetches info of a animal
@app.route("/<string:cont>/info/<string:animal>")
@cross_origin()
def fetch_cont_animal_info(cont, animal):
    cont = cont.lower()
    animal = animal.lower()
    try:
        if cont in get_conts() and animal in get_animals_of_cont(escape(cont)):
            return jsonify({"success":true, "cont":escape(cont), "animal":escape(animal), "info":get_animal_info(escape(cont), escape(animal))})
        else:
            return jsonify({"success":false, "error": "No such continent or animal!!"})
    except Exception as e:
        return jsonify({"success":false, "error":e}) 

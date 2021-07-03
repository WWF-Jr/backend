from flask import Flask
# import os

app = Flask(__name__)

false = False
true = True


@app.route("/")
def hello_world():
    return "Hello, World!"


# if os.environ["PORT"]:
#     port = int(os.environ["PORT"])
# else:
#     port = 8000


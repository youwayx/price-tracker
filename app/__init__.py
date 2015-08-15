from flask import Flask
from amazon import models

app = Flask(__name__)

@app.route("/")
def hello():
    return "hi"

models.init()

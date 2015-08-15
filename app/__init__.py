from flask import Flask
import models

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')

@app.route("/")
def hello():
    return "hi"

models.init()

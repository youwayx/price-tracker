from flask import Flask
import scraping

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/track")
def track_price():
    return "hello"


if __name__ == "__main__":
    app.run()

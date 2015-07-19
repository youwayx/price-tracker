from flask import Flask

app = Flask(__name__)
app._static_folder = 'app/static'
app.config.from_object('config')

from app import views

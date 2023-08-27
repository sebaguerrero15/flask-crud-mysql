from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return 'hola, mundo'

@app.route("/new")
def add_contact():
    return 'contacto guardado!'


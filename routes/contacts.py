

@app.route("/")
def home():
    return 'hola, mundo'

@app.route("/new")
def add_contact():
    return 'contacto guardado!'
from flask import Flask

app = Flask(__name__)

# Ruta raiz
@app.route("/")
def index():
    return "Hello World!"

# Ruta con parámetro string
@app.route("/user/<string:user>")
def user(user):
    return "Hola " + user


# Ruta con parámetro entero
@app.route("/numero/<int:numero>")
def numero(numero):
    return "Número {}".format(numero)


# Ruta con parámetros combinados
@app.route("/user/<int:id>/<string:username>")
def users(id , username):
    return "Id {} usuario {}".format(id, username)


# Ruta con parámetro float
@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return "El resultado de la suma es {}".format(n1 + n2)


# Ruta con valor por default
@app.route("/default/")
@app.route("/default/<string:dft>")
def default(dft="(no especificado)"):
    return "El valor por default es " + dft


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

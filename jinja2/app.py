from flask import Flask, render_template

app = Flask(__name__)

# Ruta raiz
@app.route("/")
def index():
    titulo = "Ay qué lindo!"
    lista = ["footer", "header", "info"]
    return render_template("index.html", titulo=titulo, lista=lista)



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

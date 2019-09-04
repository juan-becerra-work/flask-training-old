from flask import Flask
import json


# Construye la aplicación Flask
app = Flask(__name__)


#Declara la ruta raiz
@app.route("/", methods=["GET", "POST"])
def dockertest():

    # Abre el archivo JSON con la respuesta de la API
    with open('apiResponse.json') as json_data:

        # Carga el archivo JSON a una variable
        jsonResponse = json.load(json_data)

        # Cierra el archivo
        json_data.close()

    # Devuelve la respuesta de la URL ( http://localhost:5000)
    return (jsonResponse)


# INICIO DE LA APLICACIÓN
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

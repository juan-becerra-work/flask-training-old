from flask import Flask
import json


# Construye la aplicación Flask
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def dockertest():
    with open('apiResponse.json') as json_data:
        jsonResponse = json.load(json_data)
        json_data.close()
    return (jsonResponse)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

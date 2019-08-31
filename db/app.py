from flask import Flask, render_template
#import dbGADI
import test
import GADI_lib_file
import getpass

# ----------------------------------------------
# CONNECT TO DATABASE
# ----------------------------------------------
def ConnectToDatabase():
    global conn
    global dbUser
    global ACDParameters

    # GADI_lib_file.GetParametersFromFile()
    ACDParameters = GADI_lib_file.GetParametersFromFile()

    # Ask for database user password
    InputMessage = "Enter password for user " + ACDParameters.get("dbUser") + \
        " in the database " + ACDParameters.get("dbName") + "(" + \
        ACDParameters.get("dbServer") + "): "
    dbPassword = getpass.getpass(InputMessage)

    # Connect to a SQLServer database
    conn = test.db_connect_MSSQLSERVER(
           ACDParameters.get("dbServer"),
           ACDParameters.get("dbUser"),
           dbPassword, 
           ACDParameters.get("dbName"))
    # ----------------------------------------------
# ----------------------------------------------


app = Flask(__name__)

# Ruta raiz
@app.route("/")
def index():
    titulo = "Ay qué lindo esto!"
    lista = ["footer", "header", "info"]
    return render_template("index.html", titulo=titulo, lista=lista)


# Ruta raiz
@app.route("/query")
def query():
    cu = conn.cursor
    lst = cu.execute('select * from RUL_Rule')
    print("list of columns:")
    print(cu.fieldnames[0])
    print('rowcount=' + str(cu.rowcount))
    titulo = "Tirando query!"
    lista = [cu.fieldnames[0], cu.fieldnames[1], cu.fieldnames[2], cu.fieldnames[3]]
    return render_template("index.html", titulo=titulo, lista=lista)


if __name__ == "__main__":
    ConnectToDatabase()
    app.run(debug=True, host="0.0.0.0")

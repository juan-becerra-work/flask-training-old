from flask import Flask, render_template
import dbGADI
import ValueChainQueries

app = Flask(__name__)

# Ruta raiz
@app.route("/")
def index():
    titulo = "Ay qué lindo esto!"
    lista = ["footer", "header", "info"]
    return render_template("index.html", titulo=titulo, lista=lista)


# Ruta query test
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

@app.route("/q")
def anotherquery():
    titulo = "OOOOOOTRO query!"
    lista = ValueChainQueries.getDataComponents(conn)
    return render_template("index.html", titulo=titulo, lista=lista)


if __name__ == "__main__":

    conn = dbGADI.ConnectToDatabase()
    if conn == None:
        print ('Connection to database failed. Appllication will end.')
        exit

    app.run(debug=True, host="0.0.0.0")

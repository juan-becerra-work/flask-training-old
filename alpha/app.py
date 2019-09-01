from flask import Flask, render_template
import dbGADI
import ValueChainQueries

app = Flask(__name__)

# Ruta raiz
@app.route("/")
def index():
    titulo = "Lista de entidades"
    menuEntidades = ValueChainQueries.getEntityComponents_all(conn, 'id')
    listaComponentes = ValueChainQueries.getDataComponents_all(conn)
    #return render_template("alpha.html", titulo=titulo, menuEntidades=menuEntidades, listaComponentes=listaComponentes)
    return render_template("index1.html", titulo=titulo, menuEntidades=menuEntidades)



if __name__ == "__main__":

    conn = dbGADI.ConnectToDatabase()
    if conn == None:
        print ('Connection to database failed. Appllication will end.')
        exit

    app.run(debug=True, host="0.0.0.0")

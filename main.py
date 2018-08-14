from Database import *
from Class_Categoria import Categorias
from Class_Pelicula import Peliculas
from Class_Personas import Autores, Actores, Productores
from Class_Reviews import Reviews
from flask import Flask, render_template
import datetime
from Funciones import *

data = Database()

data.setConnection("127.0.0.1", "root", "alumno", "TPPYTHON")

app = Flask(__name__)

tablas = nombreTablas()

@app.route("/")
def inicio():

    return render_template("inicio.html", urls = tablas)

@app.route("/<tabla>")
def tabla(tabla):
        clase = globals()[tabla]
        var = clase()
        varauxinicial = clase()
        aux = Database().run("Select * FROM %s" % tabla)
        listaAux = []
        for item in aux:
            varauxfinal = varauxinicial.cargar(item[nombreID(tabla)])
            listaAux.append(varauxfinal)
        longitud = len(listaAux)

        return render_template("Tabla.html", name = tabla, select = Database().run("Select * FROM %s" % tabla),
                               row = Database().run("Select * FROM %s" % tabla).fetchall()[1],
                               variable = var, lista = listaAux, lenLista = longitud)
if __name__ == "__main__":
    app.run(debug=True)

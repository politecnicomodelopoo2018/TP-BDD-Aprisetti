from Database import *
from Class_Categoria import Categoria
from Class_Pelicula import Pelicula
from Class_Personas import Autores, Actores, Productores
from Class_Reviews import Reviews
from flask import Flask, render_template
import datetime
from Funciones import *

data = Database()

data.setConnection("127.0.0.1", "root", "alumno", "TPPYTHON")

app = Flask(__name__)

tablas = nombreTablas()

info = Database().run("Select * FROM Peliculas")
for item in info:
    for meti in item.values():
        print (meti)

@app.route("/")
def inicio():

    return render_template("inicio.html", urls = tablas)

@app.route("/<tabla>")
def tabla(tabla):
        return render_template("Tabla.html", name = tabla, db = Database().run("Select * FROM %s" % tabla),
                               row = Database().run("Select * FROM %s" % tabla).fetchall()[0])

if __name__ == "__main__":
    app.run(debug=True)

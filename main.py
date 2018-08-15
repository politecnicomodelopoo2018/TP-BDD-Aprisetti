from Database import *
from Class_Categoria import Categorias
from Class_Pelicula import Peliculas
from Class_Personas import Autores, Actores, Productores
from Class_Reviews import Reviews
from flask import request, jsonify, render_template, Flask
from flask_jsglue import JSGlue
import json
import datetime
import sys
from Funciones import *

data = Database()

data.setConnection("127.0.0.1", "root", "alumno", "TPPYTHON")

app = Flask(__name__)
jsglue = JSGlue(app)

tablas = nombreTablas()

@app.route("/")
def inicio():

    return render_template("inicio.html", urls = tablas)

@app.route("/<tabla>", methods = ["GET", "POST"])

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

@app.route("/borrar", methods = ["GET", "POST"])
def borrar():
    if request.method == "POST":

        clase = globals()[request.get_json()['tabla']]
        objetoinicial = clase()
        objetofinal = objetoinicial.cargar(int(request.get_json()['id']))
        objetofinal.baja()

        print(data, file=sys.stderr)

        return jsonify(data)

    else:

        return render_template("Tabla.html")



@app.route("/<tabla>ingresar")
def ingresar(tabla):

    clase = globals()[tabla]
    var = clase()
    varauxinicial = clase()
    aux = Database().run("Select * FROM %s" % tabla)
    listaAux = []
    for item in aux:
        varauxfinal = varauxinicial.cargar(item[nombreID(tabla)])
        listaAux.append(varauxfinal)
    longitud = len(listaAux)

    return render_template("ingresar.html", name=tabla, select=Database().run("Select * FROM %s" % tabla),
                           row=Database().run("Select * FROM %s" % tabla).fetchall()[1],
                           variable=var, lista=listaAux, lenLista=longitud)

if __name__ == "__main__":
    app.run(debug=True)

'''
function delete(id){
             {% for cosa in range(lenLista)%}
                if (id == {{cosa}}){
                        {{ lista[cosa].baja() }}
                    }
             {% endfor %}
        }
'''
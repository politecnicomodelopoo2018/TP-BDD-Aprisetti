from Database import *
from Class_Pelicula import Peliculas

class Categorias(object):

    idCategoria = None
    nombre = None

    @staticmethod
    def cargar(id):

        info = Database().run("Select * FROM Categorias")

        categoria = Categorias()

        for item in info:
            if id == item["idCategoria"]:
                categoria.idCategoria = item["idCategoria"]
                categoria.nombre = item["nombre"]

        return categoria


    def alta(self):

        Database().run("INSERT INTO Categorias Values (NULL, '%s')" %self.nombre)

    def baja(self):
        print(self.idCategoria)
        infoAux = Database().run("Select idPelicula FROM Peliculas WHERE idCategoria = %s" % self.idCategoria)

        for item in infoAux:
            pelicula = Peliculas.cargar(item["idPelicula"])
            pelicula.baja()

        Database().run("DELETE FROM Categorias WHERE idCategoria = '%s'" %(self.idCategoria))


    def modificacion(self):

        Database().run(("UPDATE Categorias SET nombre = '%s' WHERE idCategoria = '%s'"
                             %(self.nombre,self.idCategoria)))
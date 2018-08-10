from Database import *
from datetime import datetime
from Class_Reviews import Reviews

class Pelicula(object):

    idPelicula = None
    titulo = None
    duracion = None
    fechaLanzamiento = None
    presupuesto = None
    ganancia = None
    sinopsis = None
    idAutor = None
    idProductor = None
    idCategoria = None

    @staticmethod
    def cargar(id):

        info = Database().run("Select * FROM Peliculas where idPelicula = '%s'" %(id))

        pelicula = Pelicula()

        for item in info:

            if id == item["idPelicula"]:

                pelicula.idPelicula = item["idPelicula"]
                pelicula.titulo = item["titulo"]
                pelicula.duracion = item["duracion"]
                pelicula.fechaLanzamiento = item["fechaLanzamiento"]
                pelicula.presupuesto = item["presupuesto"]
                pelicula.ganancia = item["ganancia"]
                pelicula.sinopsis = item["sinopsis"]
                pelicula.idAutor = item["idAutor"]
                pelicula.idProductor = item["idProductor"]
                pelicula.idCategoria = item["idCategoria"]

        return pelicula

    def alta(self):

        Database().run("INSERT INTO Peliculas Values (NULL, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"
                      % (self.titulo, self.duracion, self.fechaLanzamiento, self.presupuesto, self.ganancia,
                         self.sinopsis, self.idAutor, self.idProductor, self.idCategoria))

    def baja(self):

        infoAuxRev = Database().run("Select idReview FROM Reviews WHERE idPelicula = %s" % self.idPelicula)
        for item in infoAuxRev:
            revAux = Reviews.cargar(item["idReview"])
            revAux.baja()

        Database().run("DELETE From Peliculas_has_Actores where idPelicula = '%s'" % (self.idPelicula))

        Database().run("DELETE FROM Peliculas WHERE idPelicula = '%s'" % (self.idPelicula))

    def modificacion(self):

        Database().run(("UPDATE Peliculas SET titulo = '%s', duracion = '%s', fechaLanzamiento = '%s',"
                       "presupuesto = '%s', ganancia = '%s', sinopsis = '%s',"
                       "idAutor = '%s', idProductor = '%s', idCategoria = '%s'"
                       "WHERE idPelicula = %s" % (self.titulo, self.duracion, self.fechaLanzamiento,
                                                     self.presupuesto, self.ganancia, self.sinopsis,
                                                     self.idAutor, self.idProductor, self.idCategoria,
                                                     self.idPelicula)))


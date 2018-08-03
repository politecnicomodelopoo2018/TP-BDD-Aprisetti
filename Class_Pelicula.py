from Database import *
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

    __db = Database()

    def cargar(self, id):

        info = self.__db.run("Select * FROM Peliculas")

        for item in info:

            if id == item["idPelicula"]:

                self.idPelicula = item["idPelicula"]
                self.titulo = item["titulo"]
                self.duracion = item["duracion"]
                self.fechaLanzamiento = item["fechaLanzamiento"]
                self.presupuesto = item["presupuesto"]
                self.ganancia = item["ganancia"]
                self.sinopsis = item["sinopsis"]
                self.idAutor = item["idAutor"]
                self.idProductor = item["idProductor"]
                self.idCategoria = item["idCategoria"]

    def alta(self):

        self.__db.run("INSERT INTO Peliculas Values (NULL, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"
                      % (self.titulo, self.duracion, self.fechaLanzamiento, self.presupuesto, self.ganancia,
                         self.sinopsis, self.idAutor, self.idProductor, self.idCategoria))

    def baja(self):

        idRev = self.__db.run("Select idReview From Reviews where idPelicula = '%s'" %(self.idPelicula))

        reviewAux = Reviews()

        for item in idRev:

            print(item["idReview"])
            reviewAux.cargar(item["idReview"])
            reviewAux.baja()

        self.__db.run("DELETE FROM Peliculas WHERE idPelicula = '%s'" % (self.idPelicula))

    def modificacion(self):

        self.__db.run(("UPDATE Peliculas SET titulo = '%s', duracion = '%s', fechaLanzamiento = '%s',"
                       "presupuesto = '%s', ganancia = '%s', sinopsis = '%s',"
                       "idAutor = '%s', idProductor = '%s', idCategoria = '%s'"
                       "WHERE idPelicula = %s" % (self.titulo, self.duracion, self.fechaLanzamiento,
                                                     self.presupuesto, self.ganancia, self.sinopsis,
                                                     self.idAutor, self.idProductor, self.idCategoria,
                                                     self.idPelicula)))


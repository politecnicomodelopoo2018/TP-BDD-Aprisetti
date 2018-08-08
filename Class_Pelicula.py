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


    @staticmethod
    def cargar(id):

        info = Database().run("Select * FROM Peliculas where idPelicula = '%s'" %(id))
        pepe = Pelicula()
        for item in info:

            if id == item["idPelicula"]:

                pepe.idPelicula = item["idPelicula"]
                pepe.titulo = item["titulo"]
                pepe.duracion = item["duracion"]
                pepe.fechaLanzamiento = item["fechaLanzamiento"]
                pepe.presupuesto = item["presupuesto"]
                pepe.ganancia = item["ganancia"]
                pepe.sinopsis = item["sinopsis"]
                pepe.idAutor = item["idAutor"]
                pepe.idProductor = item["idProductor"]
                pepe.idCategoria = item["idCategoria"]
        return pepe
    def alta(self):

        self.__db.run("INSERT INTO Peliculas Values (NULL, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"
                      % (self.titulo, self.duracion, self.fechaLanzamiento, self.presupuesto, self.ganancia,
                         self.sinopsis, self.idAutor, self.idProductor, self.idCategoria))

    def baja(self):

        self.__db.run("DELETE From Reviews where idPelicula = '%s'" %(self.idPelicula))
        self.__db.run("DELETE From Peliculas_has_Actores where idPelicula = '%s'" % (self.idPelicula))
        self.__db.run("DELETE FROM Peliculas WHERE idPelicula = '%s'" % (self.idPelicula))

    def modificacion(self):

        self.__db.run(("UPDATE Peliculas SET titulo = '%s', duracion = '%s', fechaLanzamiento = '%s',"
                       "presupuesto = '%s', ganancia = '%s', sinopsis = '%s',"
                       "idAutor = '%s', idProductor = '%s', idCategoria = '%s'"
                       "WHERE idPelicula = %s" % (self.titulo, self.duracion, self.fechaLanzamiento,
                                                     self.presupuesto, self.ganancia, self.sinopsis,
                                                     self.idAutor, self.idProductor, self.idCategoria,
                                                     self.idPelicula)))


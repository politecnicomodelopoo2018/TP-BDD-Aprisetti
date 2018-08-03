class Peliculas_has_Actores(object):

    idPelicula = None
    idActor = None

    def cargar(self):

        info = self.__db.run("Select * FROM Peliculas_has_Actores")

        for item in info:

            self.idPelicula = item["idPelicula"]
            self.idActor = item["idActor"]

    def alta(self):

        self.__db.run("INSERT INTO Peliculas_has_Actores Values (%s, %s)" % (self.idPelicula, self.idActor))

    def baja(self):

        self.__db.run("DELETE FROM Peliculas_has_Actores WHERE idPeliculas = %s AND idActor = %s" % (self.idPelicula,
                                                                                                     self.idActor))
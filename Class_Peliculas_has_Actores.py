from Database import *

class Peliculas_has_Actores(object):

    idPelicula = None
    idActor = None

    @staticmethod
    def cargar(idPel, idAut):

        info = Database().run("Select * FROM Peliculas_has_Actores where idPelicula = '%s' AND idActor = %s"
                              %(idPel, idAut))

        elim = Peliculas_has_Actores()

        for item in info:

            elim.idPelicula = item["idPelicula"]
            elim.idActor = item["idActor"]

    def alta(self):

        self.Database().run("INSERT INTO Peliculas_has_Actores Values (%s, %s)" % (self.idPelicula, self.idActor))

    def baja(self):

        self.Database().run("DELETE FROM Peliculas_has_Actores WHERE idPeliculas = %s AND idActor = %s"
                            % (self.idPelicula, self.idActor))
from Database import *
from Class_Pelicula import *

class Persona(object):

    def __init__(self, nombre = None, apellido = None, fechaNac = None):

        self.nombre = nombre
        self.apellido = apellido
        self.fechaNac = fechaNac
        self.__db = Database()


class Autores (Persona):

    def __init__(self, idAutor = None, nombre = None, apellido = None, fechaNac = None, ratingPromedio = None):
        Persona.__init__(self, nombre, apellido, fechaNac)

        self.idAutor = idAutor
        self.ratingPromedio = ratingPromedio

    @staticmethod
    def cargar(id):

        info = Database().run("Select * FROM Autores where idAutor = '%s'" %(id))
        autor = Autores()
        for item in info:
            if id == item["idAutor"]:
                autor.idAutor = item["idAutor"]
                autor.nombre = item["nombre"]
                autor.apellido = item["apellido"]
                autor.fechaNac = item["fechaNac"]
                autor.ratingPromedio = item["ratingPromedio"]

        return autor
    def alta(self):

        Database().run("INSERT INTO Autores Values (NULL, '%s', '%s', '%s', '%s')" % (self.nombre, self.apellido,
                                                                                           self.fechaNac,
                                                                                           self.ratingPromedio))

    def baja(self):
        info = Database().run("Select idPelicula FROM Peliculas where idAutor = '%s'" %(self.idAutor))
        for item in info:
            auxiliar = Peliculas().cargar(item["idPelicula"])
        auxiliar.baja()

        Database().run("DELETE FROM Autores WHERE idAutor = '%s'" % (self.idAutor))

    def modificacion(self):

        Database().run("UPDATE Autores SET nombre = '%s', apellido = '%s', fechaNac = '%s', ratingPromedio = '%s'"
                       "WHERE idAutor = %s" %
                      (self.nombre, self.apellido, self.fechaNac, self.ratingPromedio, self.idAutor))

class Actores(Persona):

    def __init__(self, idActor = None,  nombre = None, apellido = None, fechaNac = None, cantidadDePeliculas = None):
        Persona.__init__(self, nombre, apellido, fechaNac)

        self.idActor = idActor
        self.cantidadDePeliculas = cantidadDePeliculas

    @staticmethod
    def cargar(id):

        info = Database().run("Select * FROM Actores")
        actor = Actores()
        for item in info:

            if id == item["idActor"]:
                actor.idActor = item["idActor"]
                actor.nombre = item["nombre"]
                actor.apellido = item["apellido"]
                actor.fechaNac = item["fechaNac"]
                actor.cantidadDePeliculas = item["cantidadDePeliculas"]
        return actor

    def alta(self):
        print(("INSERT INTO Actores Values (NULL, '%s', '%s', '%s', '%s')"
               % (self.nombre, self.apellido, self.fechaNac, self.cantidadDePeliculas)))
        Database().run("INSERT INTO Actores Values (NULL, '%s', '%s', '%s', '%s')"
                       % (self.nombre, self.apellido, self.fechaNac, self.cantidadDePeliculas))

    def baja(self):

        Database().run("DELETE FROM Actores WHERE idActor = '%s'" % (self.idActor))

    def modificacion(self):

        Database().run("UPDATE Actores SET nombre = '%s', apellido = '%s', fechaNac = '%s', cantidadDePeliculas = '%s'"
                       "WHERE idActor = %s"
                       % (self.nombre, self.apellido, self.fechaNac, self.cantidadDePeliculas, self.idActor))

class Productores(Persona):

    def __init__(self,  idProductor = None, nombre = None, apellido = None, fechaNac = None, añosDeExperiencia = None):
        Persona.__init__(self, nombre, apellido, fechaNac)

        self.idProductor = idProductor
        self.añosDeExperiencia = añosDeExperiencia

    @staticmethod
    def cargar(id):

        info = Database().run("Select * FROM Productores")
        productor = Productores()
        for item in info:

            if id == item["idProductor"]:
                productor.idProductor = item["idProductor"]
                productor.nombre = item["nombre"]
                productor.apellido = item["apellido"]
                productor.fechaNac = item["fechaNac"]
                productor.añosDeExperiencia = item["añosDeExperiencia"]
        return productor

    def alta(self):

        Database().run("INSERT INTO Productores Values (NULL, '%s', '%s', '%s', '%s')" % (self.nombre, self.apellido,
                                                                                           self.fechaNac,
                                                                                           self.añosDeExperiencia))

    def baja(self):

        Database().run("DELETE FROM Productores WHERE idProductor = '%s'" % (self.idProductor))

    def modificacion(self):

        Database().run("UPDATE Productores SET nombre = '%s', apellido = '%s', fechaNac = '%s', añosDeExperiencia = '%s'"
                       "Where idProductor = %s"
                      % (self.nombre, self.apellido, self.fechaNac, self.añosDeExperiencia, self.idProductor))
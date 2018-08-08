from Database import *

class Persona(object):

    def __init__(self, nombre = None, apellido = None, fechaNac = None):

        self.nombre = nombre
        self.apellido = apellido
        self.fechaNac = fechaNac

        self.__db = Database()


class Autores (Persona):

    def __init__(self, idAutor = None, nombre = None, apellido = None, fechaNac = None, ratingPromedio = None):
        Persona.__init__(self, nombre, apellido, fechaNac)

        self.__db = Database()
        self.idAutor = idAutor
        self.ratingPromedio = ratingPromedio

    @staticmethod
    def cargar(id):

        info = Database().run("Select * FROM Autores where idAutor = '%s'" %(id))
        pepe = Autores()
        for item in info:
            if id == item["idAutor"]:
                pepe.idAutor = item["idAutor"]
                pepe.nombre = item["nombre"]
                pepe.apellido = item["apellido"]
                pepe.fechaNac = item["fechaNac"]
                pepe.ratingPromedio = item["ratingPromedio"]

        return pepe
    def alta(self):

        self.__db.run("INSERT INTO Autores Values (NULL, '%s', '%s', '%s', '%s')" % (self.nombre, self.apellido,
                                                                                           self.fechaNac,
                                                                                           self.ratingPromedio))

    def baja(self):
        self.__db.run("DELETE FROM Autores WHERE idAutor = '%s'" % (self.idAutor))

    def modificacion(self):

        self.__db.run("UPDATE Autores SET nombre = '%s', apellido = '%s', fechaNac = '%s', ratingPromedio = '%s'" %
                      (self.nombre, self.apellido, self.fechaNac, self.ratingPromedio))

class Actores(Persona):

    def __init__(self, idActor = None,  nombre = None, apellido = None, fechaNac = None, cantidadDePeliculas = None):
        Persona.__init__(self, nombre, apellido, fechaNac)

        self.__db = Database()
        self.idActor = idActor
        self.cantidadDePeliculas = cantidadDePeliculas

    def cargar(self, id):

        info = self.__db.run("Select * FROM Actores")

        for item in info:

            if id == item["idActor"]:
                self.idActor = item["idActor"]
                self.nombre = item["nombre"]
                self.apellido = item["apellido"]
                self.fechaNac = item["fechaNac"]
                self.cantidadDePeliculas = item["cantidadDePeliculas"]

    def alta(self):
        print(("INSERT INTO Actores Values (NULL, '%s', '%s', '%s', '%s')" % (self.nombre, self.apellido, self.fechaNac, self.cantidadDePeliculas)))
        self.__db.run("INSERT INTO Actores Values (NULL, '%s', '%s', '%s', '%s')" % (self.nombre, self.apellido, self.fechaNac, self.cantidadDePeliculas))

    def baja(self):

        self.__db.run("DELETE FROM Actores WHERE idActor = '%s'" % (self.idActor))

    def modificacion(self):

        self.__db.run("UPDATE Actores SET nombre = '%s', apellido = '%s', fechaNac = '%s', cantidadDePeliculas = '%s'" %
                      (self.nombre, self.apellido, self.fechaNac, self.cantidadDePeliculas))

class Productores(Persona):

    def __init__(self,  idProductor = None, nombre = None, apellido = None, fechaNac = None, añosDeExperiencia = None):
        Persona.__init__(self, nombre, apellido, fechaNac)

        self.__db = Database()
        self.idProductor = idProductor
        self.añosDeExperiencia = añosDeExperiencia

    def cargar(self, id):

        info = self.__db.run("Select * FROM Productores")

        for item in info:

            if id == item["idProductor"]:
                self.idProductor = item["idProductor"]
                self.nombre = item["nombre"]
                self.apellido = item["apellido"]
                self.fechaNac = item["fechaNac"]
                self.añosDeExperiencia = item["añosDeExperiencia"]

    def alta(self):

        self.__db.run("INSERT INTO Productores Values (NULL, '%s', '%s', '%s', '%s')" % (self.nombre, self.apellido,
                                                                                           self.fechaNac,
                                                                                           self.añosDeExperiencia))

    def baja(self):

        self.__db.run("DELETE FROM Productores WHERE idProductor = '%s'" % (self.idProductor))

    def modificacion(self):

        self.__db.run("UPDATE Productores SET nombre = '%s', apellido = '%s', fechaNac = '%s', añosDeExperiencia = '%s'"
                      % (self.nombre, self.apellido, self.fechaNac, self.añosDeExperiencia))
from Database import *

class Categoria(object):

    __idCategoria = None
    __nombre = None
    __db = Database()


    def cargar(self, id):

        info = self.__db.run("Select * FROM Categorias")


        for item in info:
            if id == item["idCategoria"]:
                self.__idCategoria = item["idCategoria"]
                self.__nombre = item["nombre"]


    def alta(self):

        self.__db.run("INSERT INTO Categorias Values (NULL, '%s')" %self.__nombre)

    def baja(self):

        self.__db.run("DELETE FROM Categorias WHERE idCategoria = '%s'" %(self.__idCategoria))


    def modificacion(self, newNombre):

        self.__db.run(("UPDATE Categorias SET nombre = '%s' WHERE idCategoria = '%s'" %(newNombre, self.__idCategoria)))

        self.__nombre = newNombre
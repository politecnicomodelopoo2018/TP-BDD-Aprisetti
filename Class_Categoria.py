import pymysql.cursors
from Database import *

class Categoria(object):

    __idCategoria = None
    __nombre = None
    __db = Database()

    def cargar(self):

        self.__db.createDict()

        self.__idCategoria = info["idCategoria"]
        self.__nombre = info["nombre"]




    def setNombre(self, newNombre):

        auxCursor = self.__db.run()
        update = auxCursor.cursor(pymysql.cursors.DictCursor)
        update.execute("UPDATE Categorias SET Nombre = %s WHERE idCategoria = %s" %(newNombre, self.__idCategoria))

        self.__nombre = newNombre


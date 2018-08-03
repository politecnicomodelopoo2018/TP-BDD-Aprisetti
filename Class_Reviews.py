from Database import *

class Reviews(object):

    idReview = None
    critico = None
    descripcion = None
    puntaje = None
    __db = Database()

    def cargar(self, id):

        info = self.__db.run("Select * FROM Reviews")

        for item in info:
            if item["idReview"] == id:

                self.idReview = item["idReview"]
                self.critico = item["critico"]
                self.descripcion = item["descripcion"]
                self.puntaje = item["puntaje"]

    def alta(self):

        self.__db.run("INSERT INTO Reviews Values (NULL, '%s', '%s', '%s')" %(self.critico, self.puntaje, self.puntaje))

    def baja(self):

        self.__db.run("DELETE FROM Reviews Where idReview = '%s'" % self.idReview)

    def modificacion(self):

        self.__db.run("UPDATE Reviews Set critico = '%s', descripcion = '%s', puntaje = '%s'" % (self.critico,
                                                                                           self.descripcion,
                                                                                           self.puntaje))
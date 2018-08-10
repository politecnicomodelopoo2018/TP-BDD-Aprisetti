from Database import *

class Reviews(object):

    idReview = None
    critico = None
    descripcion = None
    puntaje = None
    idPelicula = None
    Database()

    @staticmethod
    def cargar(id):

        info = Database().run("Select * FROM Reviews")
        review = Reviews()
        for item in info:
            if item["idReview"] == id:
                review.idReview = item["idReview"]
                review.critico = item["critico"]
                review.descripcion = item["descripcion"]
                review.puntaje = item["puntaje"]
                review.idPelicula = item["idPelicula"]
        return review
    def alta(self):

        Database().run("INSERT INTO Reviews Values (NULL, '%s', '%s', '%s', '%s')" %(self.critico, self.descripcion,
                                                                                      self.puntaje, self.idPelicula))

    def baja(self):

        Database().run("DELETE FROM Reviews Where idReview = '%s'" % self.idReview)

    def modificacion(self):

        Database().run("UPDATE Reviews Set critico = '%s', descripcion = '%s', puntaje = '%s' WHERE idReview = %s"
                       % (self.critico, self.descripcion, self.puntaje, self.idReview))
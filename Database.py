import pymysql.cursors

class Database(object):
    __instance = None
    __host = None
    __user = None
    __passwd = None
    __db = None

    def __new__(cls, *args, **kwargs):
        if Database.__instance is None:
            Database.__instance = object.__new__(cls)
        return Database.__instance

    def setConnection(self, host, user, passwd, db):
        self.__host = host
        self.__user = user
        self.__passwd = passwd
        self.__db = db


    def run(self, query):
        db = pymysql.connect(host = self.__host,
                             user = self.__user,
                             passwd = self.__passwd,
                             db = self.__db,
                             autocommit = True
                            )


        '''select_cursor = db.cursor(pymysql.cursors.DictCursor)

        select_cursor.execute("Select * From Peliculas")
        for item in select_cursor:
            print("%d / %s / %s / %s / %s / %s / %s / %s / %s / %s"
                  %(item["idPelicula"], item["titulo"], item["duracion"], item["fechaLanzamiento"],
                    item["presupuesto"], item["ganancia"], item["sinopsis"], item["idAutor"],
                    item["idProductor"], item["idCategoria"]))'''
        cursor = db.cursor(pymysql.cursors.DictCursor) #CURSOR:SIRVE PARA EJECUTAR LOS QUERIES, DictCursor:Cursor a Dict

        cursor.execute(query)

        db.close()

        return cursor
            
        

    def createDict(self):

        select = self.run().cursor(pymysql.cursors.DictCursor)

        return select


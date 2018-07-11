from Database import *
from Class_Categoria import Categoria


data = Database()

data.setConnection("127.0.0.1", "root", "alumno", "TPPYTHON")
data.run()

c = Categoria()



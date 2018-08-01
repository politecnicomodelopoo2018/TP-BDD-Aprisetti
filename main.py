from Database import *
from Class_Categoria import Categoria
from Class_Pelicula import Pelicula


data = Database()

data.setConnection("127.0.0.1", "root", "alumno", "TPPYTHON")

c = Categoria()
p = Pelicula()

c.cargar(2)

c.modificacion("JAJA")

c.cargar(2)

c.alta()

p.cargar(1)

p.titulo = "HOLA"

p.modificacion()

p.cargar(3)

p.alta()



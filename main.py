from Database import *
from Class_Categoria import Categoria
from Class_Pelicula import Pelicula
from Class_Personas import Autores, Actores, Productores

data = Database()

data.setConnection("127.0.0.1", "root", "alumno", "TPPYTHON")

c = Categoria()
p = Pelicula()
a1 = Actores()
a2 = Autores()
a3 = Productores()

c.cargar(2)

c.modificacion("JAJA")

c.cargar(2)

c.alta()

p.cargar(1)

p.titulo = "HOLA"

p.modificacion()

p.cargar(3)

p.alta()

p.baja()

a1.cargar(1)
a2.cargar(2)
a3.cargar(3)

a1.alta()
a2.alta()
a3.alta()

a1.nombre = "Jose"
a2.nombre = "Jose"
a3.nombre = "Jose"

a1.modificacion()
a2.modificacion()
a3.modificacion()

a1.baja()
a2.baja()
a3.baja()
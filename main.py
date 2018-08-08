from Database import *
from Class_Categoria import Categoria
from Class_Pelicula import Pelicula
from Class_Personas import Autores, Actores, Productores
import datetime
data = Database()

data.setConnection("127.0.0.1", "root", "alumno", "TPPYTHON")

c = Categoria()
p = Pelicula()
a1 = Actores()
a2 = Autores()
a3 = Productores()

'''''''''
p.cargar(3)

p.alta()

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

c.cargar(2)

c.modificacion("JAJA")

c.cargar(2)

c.alta()

p.cargar(1)


p.titulo = "jose"
p.idPelicula = 1
p.duracion = 122
p.fechaLanzamiento = datetime.date(2008, 11, 22)
p.presupuesto = 56666
p.ganancia = 1234567
p.sinopsis = "josefino erta un nene normal"
p.idAutor = 1
p.idProductor = 2
p.idCategoria = 3

p.alta()


'''''
pee = Pelicula()
jose = pee.cargar(2)
print(jose.duracion)
from Database import *
from Class_Categoria import Categoria
from Class_Pelicula import Pelicula
from Class_Personas import Autores, Actores, Productores
from Class_Reviews import Reviews
from datetime import *
data = Database()

data.setConnection("127.0.0.1", "root", "alumno", "TPPYTHON")

def menu():

    print("BIENVENIDO A LA BASE DE DATOS SOBRE PELICULAS")

    print("¿Sobra que tabla desea trabajar?")
    print("1-Peliculas")
    print("2-Categorias")
    print("3-Actores")
    print("4-Autores")
    print("5-Productos")
    print("6-Peliculas tienen actores")
    print("7-Reviews")

    tabla = int(input())

    print("¿Que desea hacer?")
    print("1-Ingresar")
    print("2-Eliminar")
    if tabla != 6:
        print("3-Modificar")

    accion = int(input())

    if tabla == 1:

        if accion == 1:

            pelicula = Pelicula()
            print("Ingrese los valores que desea ingresar en peliculas")
            print("Titulo: "); pelicula.titulo = input()
            print("Duracion: "); pelicula.duracion = int(input())
            print("Fecha de lanzamiento "); pelicula.fechaLanzamiento = datetime.strptime(input(), "%Y/%m/%d")
            print("Presupuesto: "); pelicula.presupuesto = int(input())
            print("Ganancia: "); pelicula.ganancia = int(input())
            print("Sinopsis: "); pelicula.sinopsis = input()
            print("Identificador del autor: "); pelicula.idAutor = int(input())
            print("Identificador del productor: "); pelicula.idProductor = int(input())
            print("Identificador de la categoria"); pelicula.idCategoria = int(input())
            pelicula.alta()

        if accion == 2:

            print("¿Que pelicula desea borrar?")
            pelicula = Pelicula.cargar((int(input())))
            pelicula.baja()

        if accion == 3:

            print("¿Que pelicula desea modificar?")
            pelicula = Pelicula.cargar((int(input())))
            print("Ingrese los valores que desea ingresar en la pelicula")
            print("Titulo: "); pelicula.titulo = input()
            print("Duracion: "); pelicula.duracion = int(input())
            print("Fecha de lanzamiento "); pelicula.fechaLanzamiento = datetime.strptime(input(), "%Y/%m/%d")
            print("Presupuesto: "); pelicula.presupuesto = int(input())
            print("Ganancia: "); pelicula.ganancia = int(input())
            print("Sinopsis: "); pelicula.sinopsis = input()
            print("Identificador del autor: "); pelicula.idAutor = int(input())
            print("Identificador del productor: "); pelicula.idProductor = int(input())
            print("Identificador de la categoria"); pelicula.idCategoria = int(input())
            pelicula.modificacion()

    if tabla == 2:

        if accion == 1:

            categoria = Categoria()
            print("Ingrese los valores en categoria")
            print("Ingrese nombre de la categoria"); categoria.nombre = input()
            categoria.alta()

        if accion == 2:

            print("¿Que categoria desea borrar?")
            categoria = Categoria.cargar(int(input()))
            categoria.baja()

        if accion == 3:

            print("¿Que categoria desea modificar?")
            categoria = Categoria.cargar(int(input()))
            print("Ingrese los valores en categoria")
            print("Ingrese nombre de la categoria"); categoria.nombre = input()
            categoria.modificacion()

    if tabla == 3:

         if accion == 1:

             actor = Actores()


menu()
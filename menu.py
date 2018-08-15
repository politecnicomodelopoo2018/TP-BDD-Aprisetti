from Database import *
from Class_Categoria import Categorias
from Class_Pelicula import Peliculas
from Class_Personas import Autores, Actores, Productores
from Class_Reviews import Reviews
from Class_Peliculas_has_Actores import  Peliculas_has_Actores
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
    print("5-Productores")
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

            pelicula = Peliculas()
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

        elif accion == 2:

            print("¿Que pelicula desea borrar?")
            pelicula = Peliculas.cargar((int(input())))
            pelicula.baja()

        elif accion == 3:

            print("¿Que pelicula desea modificar?")
            pelicula = Peliculas.cargar((int(input())))
            print("Ingrese los valores que desea ingresar en la pelicula")
            print("Titulo: "); pelicula.titulo = input()
            print("Duracion: "); pelicula.duracion = int(input())
            print("Fecha de lanzamiento: "); pelicula.fechaLanzamiento = datetime.strptime(input(), "%Y/%m/%d")
            print("Presupuesto: "); pelicula.presupuesto = int(input())
            print("Ganancia: "); pelicula.ganancia = int(input())
            print("Sinopsis: "); pelicula.sinopsis = input()
            print("Identificador del autor: "); pelicula.idAutor = int(input())
            print("Identificador del productor: "); pelicula.idProductor = int(input())
            print("Identificador de la categoria"); pelicula.idCategoria = int(input())
            pelicula.modificacion()

    elif tabla == 2:

        if accion == 1:

            categoria = Categorias()
            print("Ingrese los valores en categoria")
            print("Ingrese nombre de la categoria"); categoria.nombre = input()
            categoria.alta()

        elif accion == 2:

            print("¿Que categoria desea borrar?")
            categoria = Categorias.cargar(int(input()))
            categoria.baja()

        elif accion == 3:

            print("¿Que categoria desea modificar?")
            categoria = Categorias.cargar(int(input()))
            print("Ingrese los valores en categoria")
            print("Ingrese nombre de la categoria"); categoria.nombre = input()
            categoria.modificacion()

    elif tabla == 3:

         if accion == 1:

            actor = Actores()
            print("Ingrese los valores que desea ingresar en Actores")
            print("Nombre: "); actor.nombre = input()
            print("Apellido: "); actor.apellido = input()
            print("Fecha de nacimiento: "); actor.fechaNac = datetime.strptime(input(), "%Y/%m/%d")
            print("Cantidad de peliculas : "); actor.cantidadDePeliculas = int(input())
            actor.alta()

         elif accion == 2:

             print("¿Que actor desea borrar?")
             actor = Actores.cargar((int(input())))
             actor.baja()

         elif accion == 3:

             print("¿Que actor desea modificar?")
             actor = Autores.cargar((int(input())))
             print("Ingrese los valores que desea ingresar en el actor")
             print("Nombre: "); actor.nombre = input()
             print("Apellido: "); actor.apellido = input()
             print("Fecha de nacimiento: "); actor.fechaNac = datetime.strptime(input(), "%Y/%m/%d")
             print("Cantidad de peliculas: "); actor.cantidadDePeliculas = datetime.strptime(input(), "%Y/%m/%d")


    elif tabla == 4:

        if accion == 1:

            autor = Autores()
            print("Ingrese los valores que desea ingresar en Autores")
            print("Nombre: "); autor.nombre = input()
            print("Apellido: "); autor.apellido = input()
            print("Fecha de nacimiento: "); autor.fechaNac = datetime.strptime(input(), "%Y/%m/%d")
            print("Rating promedio: "); autor.ratingPromedio = int(input())
            autor.alta()

        elif accion == 2:

            print("¿Que autor desea borrar?")
            autor = Autores.cargar((int(input())))
            autor.baja()

        elif accion == 3:

            print("¿Que actor desea modificar?")
            autor = Autores.cargar((int(input())))
            print("Ingrese los valores que desea ingresar en el actor")
            print("Nombre: "); autor.nombre = input()
            print("Apellido: "); autor.apellido = input()
            print("Fecha de nacimiento: "); autor.fechaNac = datetime.strptime(input(), "%Y/%m/%d")
            print("Rating promedio: "); autor.ratingPromedio = datetime.strptime(input(), "%Y/%m/%d")

    elif tabla == 5:

        if accion == 1:

            productor = Productores()
            print("Ingrese los valores que desea ingresar en Autores")
            print("Nombre: "); productor.nombre = input()
            print("Apellido: "); productor.apellido = input()
            print("Fecha de nacimiento: "); productor.fechaNac = datetime.strptime(input(), "%Y/%m/%d")
            print("Rating promedio: "); productor.añosDeExperiencia = int(input())
            productor.alta()

        elif accion == 2:

            print("¿Que autor desea borrar?")
            productor = Productores.cargar((int(input())))
            productor.baja()

        elif accion == 3:

            print("¿Que actor desea modificar?")
            productor = Productores.cargar((int(input())))
            print("Ingrese los valores que desea ingresar en el actor")
            print("Nombre: "); productor.nombre = input()
            print("Apellido: "); productor.apellido = input()
            print("Fecha de nacimiento: "); productor.fechaNac = datetime.strptime(input(), "%Y/%m/%d")
            print("Rating promedio: "); productor.añosDeExperiencia = datetime.strptime(input(), "%Y/%m/%d")

    elif tabla == 6:

        if accion == 1:

            pelAct = Peliculas_has_Actores()
            print("Ingrese los valores de peliculas y actores que desea relacionar")
            print("idPelicula: "); pelAct.idPelicula = int(input())
            print("idActor: "); pelAct.idActor = int(input())
            pelAct.alta()

        elif accion == 2:

            print("¿Que relacion entre pelicula y actor desea borrar?")
            pelAct = Peliculas_has_Actores.cargar((int(input())), (int(input())))
            pelAct.baja()

    elif tabla == 7:

        if accion == 1:

            review = Reviews()
            print("Ingrese los valores que desea ingresar en Reviews")
            print("Nombre del critico: "); review.critico = input()
            print("Descripcion: "); review.descripcion = input()
            print("Puntaje: "); review.puntaje = int(input())
            print("idPelicula: "); review.idPelicula = int(input())
            review.alta()

        elif accion == 2:

            print("¿Que review desea borrar?")
            review = Reviews.cargar((int(input())))
            review.baja()

        elif accion == 3:

            print("¿Que review desea modificar?")
            review = Reviews.cargar((int(input())))
            print("Ingrese los valores que desea ingresar en el actor")
            print("Nombre del critico: "); review.critico = input()
            print("Descripcion: "); review.descripcion = input()
            print("Puntaje: "); review.puntaje = int(input())
            print("idPelicula: "); review.idPelicula = int(input())
            review.modificacion()

menu()
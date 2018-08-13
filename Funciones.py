def nombreTablas():

    listaAux = ['Peliculas', 'Categorias', 'Actores', 'Autores', 'Productores', 'Reviews']

    return listaAux

def nombreID(tabla):

    listaAux = ["idPelicula", "idCategoria", 'idActor', 'idAutor', 'idProductor', 'idReview']

    if tabla == "Peliculas":
        return listaAux[0]

    elif tabla == "Categorias":
        return listaAux[1]

    elif tabla == "Actores":
        return listaAux[2]

    elif tabla == "Autores":
        return listaAux[3]

    elif tabla == "Productores":
        return listaAux[4]

    elif tabla == "Reviews":
        return listaAux[5]



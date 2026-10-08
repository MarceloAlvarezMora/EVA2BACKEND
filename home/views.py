from django.shortcuts import render


def inicio(request):
    return render(request, 'home/inicio.html')


def accion(request):
    peliculas = [
        {
            "nombre": "The Avengers: Los Vengadores",
            "anio": 2012,
            "imagen": "images/avengers.png",
        },
        {
            "nombre": "The Dark Knight",
            "anio": 2008,
            "imagen": "images/darknight.png",
        },
        {
            "nombre": "Gladiator",
            "anio": 2000,
            "imagen": "images/gladiator.png",
        },
        {
            "nombre": "John Wick",
            "anio": 2014,
            "imagen": "images/johnwick.png",
        },
        {
            "nombre": "Terminator 2",
            "anio": 1991,
            "imagen": "images/terminator.png",
        },
        {
            "nombre": "Bullet Train",
            "anio": 2022,
            "imagen": "images/bullettrain.png",
        },
        {
            "nombre": "The Matrix",
            "anio": 1999,
            "imagen": "images/matrix.png",
        },
        {
            "nombre": "Heat",
            "anio": 1995,
            "imagen": "images/heat.png",
        },
        {
            "nombre": "El Furor del Dragón",
            "anio": 1972,
            "imagen": "images/el_furor_del_dragon.png",
        },
        {
            "nombre": "El Profesional (León)",
            "anio": 1994,
            "imagen": "images/el_profesional.png",
        },
    ]

    return render(request, 'home/accion.html', {
        'peliculas': peliculas,
    })


def terror(request):
    peliculas = [
        {
            "nombre": "El Exorcista",
            "anio": 1973,
            "imagen": "images/exorcist.png",
        },
        {
            "nombre": "El silencio de los inocentes",
            "anio": 1991,
            "imagen": "images/el_silencio_de_los_inocentes.png",
        },
        {
            "nombre": "Hereditary",
            "anio": 2018,
            "imagen": "images/hereditary.png",
        },
        {
            "nombre": "The Conjuring",
            "anio": 2013,
            "imagen": "images/conjuring.png",
        },
        {
            "nombre": "Texas Chainsaw Massacre",
            "anio": 1974,
            "imagen": "images/chainsaw.png",
        },
        {
            "nombre": "The Thing",
            "anio": 1982,
            "imagen": "images/the_thing.png",
        },
        {
            "nombre": "Halloween",
            "anio": 1978,
            "imagen": "images/halloween.png",
        },
        {
            "nombre": "The Wicker Man",
            "anio": 1973,
            "imagen": "images/the_wicker_man.png",
        },
        {
            "nombre": "The Witch",
            "anio": 2015,
            "imagen": "images/the_witch.png",
        },
        {
            "nombre": "It",
            "anio": 2017,
            "imagen": "images/it.png",
        },
    ]

    return render(request, 'home/terror.html', {
        'peliculas': peliculas,
    })
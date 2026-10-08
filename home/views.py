from django.shortcuts import render


def inicio(request):
    return render(request, 'home/inicio.html')


def accion(request):
    peliculas = [
        {"nombre": "The Avengers: Los Vengadores", "anio": 2012, "imagen": "images/avengers.png"},
        {"nombre": "The Dark Knight", "anio": 2008, "imagen": "images/darknight.png"},
        {"nombre": "Gladiator", "anio": 2000, "imagen": "images/gladiator.png"},
        {"nombre": "John Wick", "anio": 2014, "imagen": "images/johnwick.png"},
        {"nombre": "Terminator 2", "anio": 1991, "imagen": "images/terminator.png"},
        {"nombre": "Bullet Train", "anio": 2022, "imagen": "images/bullettrain.png"},
        {"nombre": "The Matrix", "anio": 1999,  "imagen": "images/matrix.png"},
        {"nombre": "Heat", "anio": 1995, "imagen": "images/heat.png"},
        {"nombre": "El Furor del Dragón", "anio": 1972, "imagen": "images/el_furor_del_dragon.png"},
        {"nombre": "El Profesional (León)", "anio": 1994, "imagen": "images/el_profesional.png"},
    ]

    return render(request, 'home/accion.html', {
        'peliculas': peliculas
    })
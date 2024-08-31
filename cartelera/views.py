from django.shortcuts import render
from django.http import HttpResponse
from boleteria.views import PELICULAS

def mostrar_estrenos(request):
    respuesta = "<html><body><h1>Próximos Estrenos</h1></body></html>"
    for pelicula in PELICULAS:
        for horario in pelicula["horarios"]:
            respuesta += f"<p>{pelicula['titulo']} - Sala {pelicula['sala']} - Horario {horario}</p>"


    return HttpResponse(respuesta)


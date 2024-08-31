from django.shortcuts import render
from django.http import HttpResponse
from boleteria.views import boletos_reservados 

# Create your views here.

def mostrar_reservas(request):
    respuesta = "<html><body><h1>Reservas Actuales</h1></body></html>"
    for boleto in boletos_reservados:
        pelicula_titulo = boleto['pelicula']['titulo']
        pelicula_sala = boleto['pelicula']['sala']
        respuesta += f"""
        <p>
        Rut: {boleto['rut']} <br>
        Nombre: {boleto['nombre']}<br>
        Asiento: {boleto['asiento']}<br>
        Película: {pelicula_titulo} - {pelicula_sala}<br>
        Horario: {boleto['horario']}
        </p>
        """
    
    return HttpResponse(respuesta)
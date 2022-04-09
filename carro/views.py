from django.shortcuts import render
from .carro import Carro
from AppCoder.models import Juego
from django.shortcuts import redirect


# Create your views here.

def agregar_juego(request, juego_id):

    carro=Carro(request)
    juego= Juego.objects.get(id=juego_id)

    carro.agregar(juego=juego)

    return redirect ("Juegos")

def eliminar_juego(request, juego_id):
    
    carro=Carro(request)
    juego= Juego.objects.get(id=juego_id)

    carro.eliminar(juego=juego)

    return redirect ("Juegos")

def restar_juego(request, juego_id):
    
    carro=Carro(request)
    juego= Juego.objects.get(id=juego_id)

    carro.restar_producto(juego=juego)

    return redirect ("Carro")

def limpiar_carro(request):
    
    carro=Carro(request)
    carro.limpiar_carro()

    return redirect ("Carro")


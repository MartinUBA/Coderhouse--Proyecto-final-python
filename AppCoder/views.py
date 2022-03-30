from ast import Return
from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Categoria, Clientes,Juego, Servicio
from AppCoder.forms import JuegoFormulario, ClientesFormulario, ServiciosFormulario
from django.views.generic import ListView

# Create your views here.




def inicio(request):

      return render(request, "AppCoder/inicio.html")

def contacto(request):
    
      return render(request, "AppCoder/contacto.html")



def juegos(request):

      juegos=Juego.objects.all()
      return render(request, "AppCoder/juegos.html", {"juegos": juegos})


def servicios(request):
      servicios=Servicio.objects.all()
      return render(request, "AppCoder/servicios.html",{"nombre": servicios})


def juegoFormulario(request):
    
      if request.method == "POST":

            miFormulario = JuegoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  juego = Juego(nombre=informacion["nombre"], precio=informacion["precio"], stock=informacion["stock"], imagen=informacion["imagen"])
                  juego.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = JuegoFormulario()

      return render(request, "AppCoder/juegoFormulario.html", {"miFormulario": miFormulario})




def clientesFormulario(request):

      if request.method == 'POST':

            miFormulario = ClientesFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  cliente = Clientes(nombre=informacion['nombre'],apellido=informacion['apellido'],email=informacion['email'],
                  direccion=informacion['direccion'],edad=informacion['edad'], fechaDeEntrega=informacion['fechaDeEntrega'],entregado=informacion['entregado'] )
                  

                  cliente.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= ClientesFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/clientesFormulario.html", {"miFormulario":miFormulario})

def serviciosFormulario(request):
    
      if request.method == 'POST':

            miFormulario = ServiciosFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  servicio = Servicio (servicio=informacion['servicio'],precio=informacion['precio'])
                  

                  servicio.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= ServiciosFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/serviciosFormulario.html", {"miFormulario":miFormulario})



def busquedaJuego(request):
      return render(request, "AppCoder/busquedaJuego.html")



def buscar(request):
      if request.GET ['nombre']:    
            #respuesta = f"Estoy buscando el juego: {request.GET['nombre'] }" 
            nombre = request.GET['nombre'] 
            nombre = Juego.objects.filter(nombre__icontains=nombre)

            return render(request, "AppCoder/resultadosPorBusqueda.html", {"nombre":nombre})

      else: 

	      respuesta = "No enviaste datos"

      #No olvidar from django.http import HttpResponse
      return HttpResponse(respuesta)

def leerJuegos(request):
    
      juegos = Juego.objects.all() #trae todos los juegos

      contexto= {"juegos":juegos} 

      return render(request, "AppCoder/leerJuegos.html",contexto)


def eliminarJuego(request, juego_nombre):
    
    juego = Juego.objects.get(nombre=juego_nombre)
    juego.delete()

    # vuelvo al menú
    juegos = Juego.objects.all()  # trae todos los juegos

    contexto = {"juegos": juegos}

    return render(request, "AppCoder/leerJuegos.html", contexto)

def editarJuego(request, juego_nombre):
      # Recibe el nombre del juego que vamos a modificar
  juego = Juego.objects.get(nombre=juego_nombre)
  # Si es metodo POST hago lo mismo que el agregar
  if request.method == 'POST':
    # aquí mellega toda la información del html
    miFormulario = JuegoFormulario(request.POST)
    print(miFormulario)
    if miFormulario.is_valid: # Si pasó la validación de Django
      informacion = miFormulario.cleaned_data
      juego.nombre = informacion['nombre']
      juego.precio = informacion['precio']
      juego.stock = informacion['stock']
      juego.imagen = informacion['imagen']
      juego.save()
      # Vuelvo al inicio o a donde quieran
      return render(request, "AppCoder/inicio.html")
  # En caso que no sea post
  else:
    # Creo el formulario con los datos que voy a modificar
    miFormulario = JuegoFormulario(initial={'nombre': juego.nombre, 'precio': juego.precio,
                          'stock': juego.stock, 'imagen': juego.imagen})
  # Voy al html que me permite editar
  return render(request, "AppCoder/editarJuego.html", {"miFormulario": miFormulario, "juego_nombre": juego_nombre})

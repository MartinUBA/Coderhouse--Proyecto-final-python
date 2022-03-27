from ast import Return
from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Categoria,Juego
from AppCoder.forms import tiendaFormulario, ProfesorFormulario

# Create your views here.

def categoria(request):

      categoria =  Categoria(nombre="Acción", año="1989")
      categoria.save()
      documentoDeTexto = f"--->Categoria: {categoria.nombre}   Año: {categoria.año}"


      return HttpResponse(documentoDeTexto)


def inicio(request):

      return render(request, "AppCoder/inicio.html")

def contacto(request):
    
      return render(request, "AppCoder/contacto.html")



def juegos(request):

      return render(request, "AppCoder/juegos.html")


def reservas(request):

      return render(request, "AppCoder/reservas.html")


def tienda(request):

      if request.method == 'POST':

            miFormulario = tiendaFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  tienda = Juego (nombre=informacion['nombre'], precio=informacion['precio']) 

                  tienda.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= tiendaFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/juegos.html", {"miFormulario":miFormulario})




#def profesores(request):

      if request.method == 'POST':

            miFormulario = ProfesorFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  profesor = Profesor (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   email=informacion['email'], profesion=informacion['profesion']) 

                  profesor.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= ProfesorFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/profesores.html", {"miFormulario":miFormulario})






def buscar(request):

      if  request.GET["nombre"]:

	      #respuesta = f"Estoy buscando la camada nro: {request.GET['nombre'] }" 
            nombre = request.GET['nombre'] 
            nombre = Juego.objects.filter(nombre__icontains=nombre)

            return render(request, "AppCoder/inicio.html", {"nombre":nombre})

      else: 

	      respuesta = "No enviaste datos"

      #No olvidar from django.http import HttpResponse
      return HttpResponse(respuesta)
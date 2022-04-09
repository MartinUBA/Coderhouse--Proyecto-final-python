from ast import Return
from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Categoria, Clientes,Juego, Servicio
from AppCoder.forms import JuegoFormulario, ClientesFormulario, ServiciosFormulario, UserRegisterForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from AppCoder.forms import UserRegisterForm, UserEditForm
from django.db import models
from .models import Avatar



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
      return render(request, "AppCoder/servicios.html",{"servicios": servicios})


def juegoFormulario(request):
    
      if request.method == "POST":

            miFormulario = JuegoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  juego = Juego(nombre=informacion["nombre"], precio=informacion["precio"], stock=informacion["stock"], imagen=informacion['imagen'])
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

                  servicio = Servicio (servicio=informacion['servicio'],precio=informacion['precio'], imagen=informacion['imagen'])
                  

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


class ServicioList(ListView):
    
    model = Servicio
    template_name = "AppCoder/servicios_list.html"

class ServicioDetalle(DetailView):
    
    model = Servicio
    template_name = "AppCoder/servicios_detalle.html"


class ServicioCreacion(CreateView):
    
    model = Servicio
    success_url = "/AppCoder/servicio/list"
    fields = ['servicio', 'precio', 'imagen']

class ServicioUpdate(UpdateView):
    
    model = Servicio
    success_url = "/AppCoder/servicio/list"
    fields = ['servicio', 'precio', 'imagen']

class ServicioDelete(DeleteView):
    
    model = Servicio
    success_url = "/AppCoder/servicio/list"

def login_request(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "AppCoder/logincorrecto.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppCoder/loginincorrecto.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "AppCoder/loginincorrecto.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "AppCoder/login.html", {"form": form})

def register(request):
    
      if request.method == 'POST':

            form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppCoder/inicio.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"AppCoder/registro.html" ,  {"form":form})

#DECORADOR!
@login_required
def inicio(request):

      avatares= Avatar.objects.filter(user=request.user.id)

      return render(request, "AppCoder/inicio.html", {"url":avatares[0].imagen.url})


# Vista de editar el perfil
@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "AppCoder/inicio.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "AppCoder/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})


def carro(request):
    
      return render(request,"AppCoder/carro.html")

def quienessomos(request):
    
      return render(request,"AppCoder/quienessomos.html")
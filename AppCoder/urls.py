from django.urls import path

from AppCoder import views
from django.conf import settings 
from django.conf.urls.static import static 



urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    #path('cursos', views.cursos, name="Cursos"),
    #path('profesores', views.profesores, name="Profesores"),
    path('juegos', views.juegos, name="Juegos"),
    path('servicios', views.servicios, name="Servicios"),
    path('juegoFormulario', views.juegoFormulario, name="JuegoFormulario"),
    path('clientesFormulario', views.clientesFormulario, name="ClientesFormulario"),
    path('serviciosFormulario', views.serviciosFormulario, name="ServiciosFormulario"),
    path('contacto', views.contacto, name="Contacto"),
    #path('profesorFormulario', views.profesorFormulario, name="ProfesorFormulario"),
    path('busquedaJuego',  views.busquedaJuego, name="BusquedaJuego"),
    path('buscar/', views.buscar),
   
]
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



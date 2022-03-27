from django.urls import path

from AppCoder import views





urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    #path('cursos', views.cursos, name="Cursos"),
    #path('profesores', views.profesores, name="Profesores"),
    path('juegos', views.juegos, name="Juegos"),
    path('reservas', views.reservas, name="Reservas"),
    path('tiendaFormulario', views.tiendaFormulario, name="tiendaFormulario"),
    path('contacto', views.contacto, name="Contacto"),
    #path('profesorFormulario', views.profesorFormulario, name="ProfesorFormulario"),
    #path('busquedaCamada',  views.busquedaCamada, name="BusquedaCamada"),
    path('buscar/', views.buscar),
   
]


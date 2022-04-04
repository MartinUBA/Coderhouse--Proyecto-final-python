from django.urls import path, re_path

from AppCoder import views
from django.conf import settings 
from django.conf.urls.static import static 
from django.contrib.auth.views import LogoutView


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
    path('leerJuegos', views.leerJuegos, name = "LeerJuegos"),
    path('eliminarJuego/<juego_nombre>/', views.eliminarJuego, name="EliminarJuego"),
    path('editarJuego/<juego_nombre>/', views.editarJuego, name="EditarJuego"),
    path('servicio/list', views.ServicioList.as_view(), name='List'),
    re_path(r'^(?P<pk>\d*)$', views.ServicioDetalle.as_view(), name='Detail'),
    re_path(r'^nuevo$', views.ServicioCreacion.as_view(), name='New'),
    re_path(r'^editar/(?P<pk>\d*)$', views.ServicioUpdate.as_view(), name='Edit'),
    re_path(r'^borrar/(?P<pk>\d*)$', views.ServicioDelete.as_view(), name='Delete'),
    path('login', views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),

   
]
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



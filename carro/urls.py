from django.urls import path

from .import views

app_name="carro"

urlpatterns= [

    path("agregar/<int:juego_id>/", views.agregar_juego, name="agregar"),
    path("eliminar/<int:juego_id>/", views.eliminar_juego, name="eliminar"),
    path("restar/<int:juego_id>/", views.restar_juego, name="restar"),
    path("limpiar/", views.limpiar_carro, name="limpiar"),

]
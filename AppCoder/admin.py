from django.contrib import admin
from  .models import * #importamos el archivo models

# Register your models here.
#registramos los modelos

admin.site.register(Juego)

admin.site.register(Categoria)

admin.site.register(Empresa)

admin.site.register(Reservas)

from django.db import models

# Create your models here.
class Categoria(models.Model):

    nombre=models.CharField(max_length=40)
    año = models.IntegerField()


class Juego(models.Model):
    nombre= models.CharField(max_length=30)
    precio= models.FloatField(max_length=30)
    stock= models.IntegerField()

    class Meta:
        verbose_name='juego'
        verbose_name_plural='juegos'
    

    def __str__(self):
        return f"Nombre: {self.nombre} - Precio {self.precio} - Stock {self.stock}"

class Empresa(models.Model):
    nombre= models.CharField(max_length=30)
    email= models.EmailField()
    

class Clientes(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email=models.EmailField()
    direccion=models.CharField(max_length=50)
    edad=models.IntegerField()
    fechaDeEntrega = models.DateField()  
    entregado = models.BooleanField()

class Servicio(models.Model):
    servicio= models.CharField(max_length=40)
    precio=models.IntegerField()




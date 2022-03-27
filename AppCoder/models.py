from django.db import models

# Create your models here.
class Categoria(models.Model):

    nombre=models.CharField(max_length=40)
    año = models.IntegerField()


class Juego(models.Model):
    nombre= models.CharField(max_length=30)
    precio= models.FloatField(max_length=30)


class Empresa(models.Model):
    nombre= models.CharField(max_length=30)
    email= models.EmailField()
    

class Reservas(models.Model):
    nombre= models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()  
    entregado = models.BooleanField()

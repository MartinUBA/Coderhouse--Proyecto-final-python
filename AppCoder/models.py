from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Categoria(models.Model):

    nombre=models.CharField(max_length=40)
    año = models.IntegerField()


class Juego(models.Model):
    nombre= models.CharField(max_length=30)
    precio= models.FloatField(max_length=30)
    stock= models.IntegerField()
    imagen= models.ImageField(upload_to='juegos', null=True, blank= True)

    class Meta:
        verbose_name='juego'
        verbose_name_plural='juegos'
    

    def __str__(self):
        return f"Nombre: {self.nombre} - Precio:   {self.precio} $- Stock:   {self.stock} uni."
    
    

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

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido:   {self.apellido} - Email:   {self.email} - direccion:   {self.direccion} - edad:   {self.edad} - Fecha de entrega:   {self.fechaDeEntrega} - Entregado:   {self.entregado}"

class Servicio(models.Model):
    servicio= models.CharField(max_length=40)
    precio=models.IntegerField()
    imagen=models.ImageField(upload_to='servicios', null=True, blank= True)


    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'
    

    def __str__(self):
        return f"Nombre: {self.servicio} - Precio:   {self.precio} $"

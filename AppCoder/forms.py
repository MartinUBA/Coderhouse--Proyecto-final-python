from django import forms


class JuegoFormulario(forms.Form):

    nombre = forms.CharField()
    precio = forms.IntegerField()
    stock= forms.IntegerField()

class ClientesFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    direccion=forms.CharField(max_length=50)
    edad=forms.IntegerField()
    fechaDeEntrega= forms.DateField()
    entregado=forms.BooleanField()

class ServiciosFormulario(forms.Form):
    servicio= forms.CharField(max_length=30)
    precio= forms.IntegerField()

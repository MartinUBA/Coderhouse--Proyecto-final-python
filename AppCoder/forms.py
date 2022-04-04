from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class JuegoFormulario(forms.Form):

    nombre = forms.CharField()
    precio = forms.IntegerField()
    stock= forms.IntegerField()
    imagen= forms.ImageField()

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
    imagen=forms.ImageField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

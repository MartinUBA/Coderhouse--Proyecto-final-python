from django import forms


class tiendaFormulario(forms.Form):

    #Especificar los campos
    nombre = forms.CharField()
    precio = forms.FloatField()


class ProfesorFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)
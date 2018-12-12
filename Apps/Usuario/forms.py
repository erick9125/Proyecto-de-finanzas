from django import forms
from .models import Usuarios, Lista
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

#Importando para formulario de mantenedor

class ClienteForm(UserCreationForm):

    class Meta:
        model = User
        
        fields = [
            'first_name',
            'last_name',
            'email',
            'password1',
            
            
        ]

        labels = {
            
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Email',
            'password1':'Ingrese Clave',
            
        }

        widgets = {
            
    		'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
    		'email': forms.TextInput(attrs={'class':'form-control'}),
    		'password1': forms.PasswordInput(attrs={'class':'form-control'}),
            
            
        }

class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Ingrese Nombre'       
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Ingrese Clave'

#Formulario para Mantenedor 

class ListaForm(forms.ModelForm):
    nombrelista = forms.CharField(required=True, label='Nombre de la lista')
    class Meta:
        model = Lista
        fields = ('nombrelista',)
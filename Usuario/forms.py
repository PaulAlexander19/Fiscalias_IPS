from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Usuario

class UsuarioForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Constraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Constraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = Usuario
        fields = [
          "username",
          "email",
          "password1",
          "password2",
          #"first_name",
          #"last_name",
          #"Direccion",
          #"Departamento",
          #"Provincia",
        ]

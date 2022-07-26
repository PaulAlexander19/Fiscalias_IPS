from django import forms
from .models import Usuario

class Form(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields = [
          "Nombre",
          "Apellidos",
          "Usuario",
          "Contraseña",
          "Dirección",
          "Departamento",
          "Provincia",
        ]

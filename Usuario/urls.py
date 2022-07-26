from django.urls import path
from .views import (
  UsuarioRegister,
)

urlpatterns = [
    path("registro", UsuarioRegister, name="usuario-register"),
]

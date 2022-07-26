from django.urls import path
from .views import (
  UsuarioRegister,
  UsuarioLogin,
)

urlpatterns = [
    path("registro/", UsuarioRegister, name="usuario-register"),
    path("login/", UsuarioLogin, name="usuario-login"),
]

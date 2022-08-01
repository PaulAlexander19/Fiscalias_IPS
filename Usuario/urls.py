from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
  UsuarioRegister,
  UsuarioLogin,
)

urlpatterns = [
    path("perfil/", views.UsuarioPerfil, name="usuario-perfil"),
    path("registro/", views.UsuarioRegister, name="usuario-register"),
    path("login/", LoginView.as_view(template_name='Usuario/login.html'), name="usuario-login"),
    path("logout/", LogoutView.as_view(template_name='Usuario/logout.html'), name="usuario-logout"),
]

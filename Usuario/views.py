from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Usuario
from .forms import UsuarioForm

# Create your views here.
def UsuarioRegister(request):
  form = UsuarioForm(request.POST or None)
  if (form.is_valid()):
    form.save()
    return redirect('../')


  context = {
    'form': form 
  }
  return render(request, 'Usuario/usuarioRegister.html', context)

def UsuarioLogin(request):
  username = request.POST['username']
  password = request.POST['password']
  user = authenticate(request, username=username, password=password)
  if user is not None:
    login(request, user)
  else:
    pass
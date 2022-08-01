from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import *
from .forms import UsuarioForm
from django.contrib import messages

# Create your views here.
def UsuarioRegister(request):
  if request.method == 'POST':
    form = UsuarioForm(request.POST or None)
    if (form.is_valid()):
      form.save()
      #return redirect('/fiscalias/')
      username = form.cleaned_data['username']
      messages.success(request, f'Usuario {username} creado')
  else:
    form = UsuarioForm() 

  context = {'form': form }
  return render(request, 'Usuario/usuarioRegister.html', context)


def UsuarioLogin(request):
  username = request.POST.get('username')
  password = request.POST.get('password')
  user = authenticate(request, username=username, password=password)
  if user is not None:
    login(request, user)
  else:
    pass

  

def UsuarioPerfil(request):
  return render(request, 'Usuario/usuarioRegister.html', {'user':user, 'posts':posts})

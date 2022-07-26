from django.shortcuts import render
from .models import Usuario
from .forms import UsuarioForm

# Create your views here.
def UsuarioRegister(request):
  form = UsuarioForm(request.POST or None)
  if (form.is_valid()):
    form.save()
    form = UsuarioForm()

  context = (
    'form': form 
  )
  return render(request, '', context)
from django.shortcuts import render
from django.views.generic import (
  ListView,
  DetailView,
)
from .models import Fiscalias

# Create your views here.
class FiscaliaListView(ListView):
  model = Fiscalias

class FiscaliaDetailView(DetailView):
  model = Fiscalias
from django.http import HttpResponse
from django.shortcuts import render
from httplib2 import Http

# Create your views here.
## aquil es la logica
def mainView(request, *args, **kwargs):
    
    return render(request, 'fiscaliaApp/MainSearch.html')

def fiscaliaView(request, *args, **kwargs):
    return render(request, 'fiscaliaApp/FiscaliaPage.html')

def testView(request, *args, **kwargs):
    ## retorna un h1
    return HttpResponse('<h1>Hola mundo</h1>') 
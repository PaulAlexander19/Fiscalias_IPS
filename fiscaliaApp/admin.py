from django.contrib import admin

# Register your models here.
from .models import Consultas, Fiscalia, FiscaliaDet, Historial, Usuario

admin.site.register(Consultas)
admin.site.register(Fiscalia)
admin.site.register(FiscaliaDet)
admin.site.register(Historial)
admin.site.register(Usuario)

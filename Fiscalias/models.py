from django.db import models
from Usuario.models import Usuario
class Fiscalias(models.Model):
    FisID = models.AutoField(primary_key=True)
    CodSiga = models.CharField(max_length=10, blank=True, null=True)
    Nombre = models.CharField(max_length=255, blank=True, null=True)
    Distrito = models.CharField(max_length=100, blank=True, null=True)
    Especialidad = models.CharField(max_length=100, blank=True, null=True)
    Tipo = models.CharField(max_length=100, blank=True, null=True)
    Situacion = models.CharField(max_length=100, blank=True, null=True)
    Provincia = models.CharField(max_length=100, blank=True, null=True)
    Departamento = models.CharField(max_length=100, blank=True, null=True)
    Direccion = models.CharField(max_length=255, blank=True, null=True)
    Correo = models.EmailField(max_length=255, blank=True, null=True)
    Telefono = models.TextField(blank=True, null=True) # Separar mas de un telef. con un "|"

    def __str__(self):
        return self.Nombre

class Consulta(models.Model):
    ConID = models.AutoField(primary_key=True)
    UserID = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True, null=True) # UserID es un Objeto
    FisID = models.ForeignKey(Fiscalias, on_delete=models.CASCADE, blank=True, null=True)
    Fecha = models.DateField(blank=True, null=True, auto_now_add=True)
    
    def __str__(self):
        return str(self.ConID) + " -> " + self.UserID.first_name + " - " + self.FisID.Nombre        


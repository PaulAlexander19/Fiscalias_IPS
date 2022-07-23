from django.db import models

class Fiscalias:
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
    Correo = models.CharField(max_length=255, blank=True, null=True)
    Telefono = models.CharField(max_length=255, blank=True, null=True)

class Consulta:
    ConID = models.AutoField(primary_key=True)
    UserID = models.ForeignKey('Usuario', models.DO_NOTHING, blank=True, null=True)
    Fecha = models.DateField(blank=True, null=True)
    FisID = models.ForeignKey('Fiscalias', models.DO_NOTHING, blank=True, null=True)


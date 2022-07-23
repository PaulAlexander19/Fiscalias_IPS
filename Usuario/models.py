from tkinter import PhotoImage
from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    PhotoImage = models.ImageField(upload_to='usuarios/%y/%m/%d', blank=True, null=True)
    Direccion = models.CharField(max_length=255, blank=True, null=True)
    Departamento = models.CharField(max_length=100, blank=True, null=True)
    Provincia = models.CharField(max_length=100, blank=True, null=True)

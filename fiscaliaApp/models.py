# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Consultas(models.Model):
    idconsultas = models.IntegerField(db_column='idConsultas', primary_key=True)  # Field name made lowercase.
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='idUsuario', blank=True, null=True)  # Field name made lowercase.
    idfiscalia = models.ForeignKey('Fiscalia', models.DO_NOTHING, db_column='idFiscalia', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Consultas'


class Fiscalia(models.Model):
    idfiscalia = models.OneToOneField('FiscaliaDet', models.DO_NOTHING, db_column='idFiscalia', primary_key=True)  # Field name made lowercase.
    fisdepartamento = models.CharField(db_column='FisDepartamento', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fisprovincia = models.CharField(db_column='FisProvincia', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fisdistrito = models.CharField(db_column='FisDistrito', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fisnombre = models.CharField(db_column='FisNombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fisespecialidad = models.CharField(db_column='FisEspecialidad', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fistipo = models.CharField(db_column='FisTipo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fissituación = models.CharField(db_column='FisSituación', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Fiscalia'


class FiscaliaDet(models.Model):
    idfiscaliadet = models.IntegerField(db_column='idFiscaliaDet', primary_key=True)  # Field name made lowercase.
    fisdetcorreo = models.CharField(db_column='FisDetCorreo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fisdetdireccion = models.CharField(db_column='FisDetDireccion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fisdetencargado = models.CharField(db_column='FisDetEncargado', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fiscalia_detcol = models.CharField(db_column='Fiscalia_detcol', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Fiscalia_det'


class Historial(models.Model):
    idhistorial = models.IntegerField(db_column='idHistorial', primary_key=True)  # Field name made lowercase.
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='idUsuario', blank=True, null=True)  # Field name made lowercase.
    consultas = models.IntegerField(db_column='Consultas')  # Field name made lowercase.

    class Meta:
        db_table = 'Historial'
        unique_together = (('idhistorial', 'consultas'),)


class Usuario(models.Model):
    idusuario = models.IntegerField(db_column='idUsuario', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    constraseña = models.CharField(db_column='Constraseña', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dirección = models.CharField(db_column='Dirección', max_length=45, blank=True, null=True)  # Field name made lowercase.
    usuariocol = models.CharField(db_column='Usuariocol', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Usuario'

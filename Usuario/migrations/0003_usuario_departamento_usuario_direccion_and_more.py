# Generated by Django 4.0.6 on 2022-07-23 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0002_alter_usuario_photoimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='Departamento',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='Direccion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='Provincia',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

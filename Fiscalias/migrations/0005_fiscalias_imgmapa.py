# Generated by Django 3.2.7 on 2022-07-27 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fiscalias', '0004_alter_consulta_fisid_alter_consulta_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='fiscalias',
            name='ImgMapa',
            field=models.ImageField(blank=True, null=True, upload_to='fiscalias'),
        ),
    ]
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Clase1(models.Model):
    titulo=models.CharField(max_length=100, verbose_name="Titulo")


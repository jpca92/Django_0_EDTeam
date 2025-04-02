from django.db import models

class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    imagen = models.CharField(max_length=255)
    autor = models.CharField(max_length=150)

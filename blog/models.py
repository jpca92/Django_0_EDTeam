from django.db import models

class Articulo(models.Model):
    titulo = models.Charfield(max_length=200)
    imagen = models.Charfield(max_length=255)
    autor = models.CharField(max_length=150)

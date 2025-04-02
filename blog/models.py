from django.db import models
from django.contrib.auth.models import User

class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='articulos')
    # autor = models.CharField(max_length=150)
    autor = models.ForeignKey(User, on_delete=models.RESTRICT)


    def __str__(self):
        return self.titulo

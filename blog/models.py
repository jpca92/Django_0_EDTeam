from datetime import date
from django.db import models
from django.contrib.auth.models import User

class Articulo(models.Model):

    CATEGORIA_CHOICES = (
        ('general', 'General'),
        ('diseño_web', 'Diseño Web'),
        ('desarrollo_web' , 'Desarrollo Web'),
    )
    titulo = models.CharField(max_length=200)
    contenido = models.TextField(default= '')
    duracion = models.IntegerField(default=0)
    fecha_registro = models.DateField(default=date.today)
    categoria = models.CharField(max_length = 50, default='general',choices=CATEGORIA_CHOICES)
    imagen = models.ImageField(upload_to='articulos')
    # autor = models.CharField(max_length=150)
    autor = models.ForeignKey(User, on_delete=models.RESTRICT)


    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.RESTRICT)
    texto = models.TextField(default='')
    autor = models.CharField(max_length=60, default='anonimo')

    def __str__(self):
        return self.autor
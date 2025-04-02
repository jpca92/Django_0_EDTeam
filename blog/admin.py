from django.contrib import admin
from .models import Articulo

# Register your models here.
# admin.site.register(Articulo)

# Para mostrar campos en el panel de admin
@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'imagen', 'autor')

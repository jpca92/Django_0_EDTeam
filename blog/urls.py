from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('contenido/<int:articulo_id>',views.contenido, name='contenido'),


]
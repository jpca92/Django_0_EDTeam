from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from cursos.views import cursos, cursosAPI, saludo, suma, operations, show_form

from django.conf import settings
from django.conf.urls.static import static


def holamundo(request):
    # Para reisar el header
    # print(request.headers)
    return HttpResponse('<h1> Hola Mundo </h1>')

urlpatterns = [
    path('holamundo/', holamundo),
    path('cursos/', cursos),
    path('cursosapi/', cursosAPI),
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('suma/<int:n1>/<int:n2>',suma),
    path('operations/<int:n1>/<int:n2>/<str:operation>',operations),
    path('form', show_form),
    path('', include('blog.urls')),
    path('cursos_index/', include('cursos.urls')),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

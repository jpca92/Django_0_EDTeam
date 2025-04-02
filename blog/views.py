from django.shortcuts import render

from .models import Articulo

# Create your views here.
def index(request):
    listaArticulos= Articulo.objects.all()
    print(listaArticulos)
    context = {
        "articulos":listaArticulos
    }
    
    return render(request,'blog/index.html',context)

def contenido (request, articulo_id):
    objArticulo = Articulo.objects.get(pk=articulo_id)
    context= {
        'articulo':objArticulo
    }
    return render (request, 'blog/articulo.html',context)
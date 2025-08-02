

from django.shortcuts import render

from articulos.models import Articulo

def Home(request):       
    
    ultimos_articulos = Articulo.objects.order_by('-creado')[:3]  # Los 3 más recientes
    
    return render(request, 'home.html', {'ultimos_articulos': ultimos_articulos})




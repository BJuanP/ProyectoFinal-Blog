
from django.shortcuts import render
from django.views.generic.detail import DetailView    #Esto es una vista preparada para mostrar el detalle de un proyecto
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Articulo            #Esto es necesario para traer lo que está en la clase Producto
from .forms import FormularioCrearArticulo


#VISTA BASADA EN FUNCIONES
def Listar_Articulos(request):
    
    #ORM = SELECT * FROM PRODUCTO
    todos = Articulo.objects.all()    #Acá le digo que me traiga todos los objetos de la tabla productos
    

    return render(request, 'articulos/listar.html', {'articulos': todos})       #Esto es para pasarle todos los productos al template. Es una lista



class Crear_Articulo(CreateView):     
    
    model = Articulo
    template_name = 'articulos/crear.html'
    form_class = FormularioCrearArticulo
    success_url = reverse_lazy('articulos:path_listar_articulos')
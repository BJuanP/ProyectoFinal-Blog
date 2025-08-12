
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



#VISTA BASADA EN CLASES
class Detalle_Articulo(DetailView):
    
    template_name = 'articulos/detalle.html'
    model = Articulo
    context_object_name = 'articulo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orden = self.request.GET.get('orden', 'reciente')  # valor por defecto 'reciente'
        
        # Obtener los comentarios ordenados - corregimos esta parte
        comentarios = self.object.MisComentarios.all()  # Asegúrate que MisComentarios es el related_name correcto
        
        # Aplicamos el orden
        if orden == 'antiguo':
            comentarios = comentarios.order_by('creado')
        else:
            comentarios = comentarios.order_by('-creado')
        
        context['comentarios'] = comentarios
        return context


class Crear_Articulo(CreateView):     
    
    model = Articulo
    template_name = 'articulos/crear.html'
    form_class = FormularioCrearArticulo
    success_url = reverse_lazy('articulos:path_listar_articulos')
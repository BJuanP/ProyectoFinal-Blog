
from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.contrib import messages


from .models import Articulo
from .forms import FormularioCrearArticulo
from apps.categorias.models import Categoria





class soloMod(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.groups.filter(name='Moderador').exists()

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            raise PermissionDenied  # Si está logueado pero no es moderador → 403
        return super().handle_no_permission()  # Si no está logueado → lo lleva a login



def Listar_Articulos(request):
    categoria_id = request.GET.get('categoria')
    orden = request.GET.get('orden', 'reciente')  # 'reciente' por defecto

    categorias = Categoria.objects.all()
    categoria_seleccionada = None

    if categoria_id:
        queryset = Articulo.objects.filter(categoria_id=categoria_id)
        categoria_seleccionada = Categoria.objects.filter(id=categoria_id).first()
    else:
        queryset = Articulo.objects.all()

    # Ordenar por fecha
    if orden == 'antiguo':
        queryset = queryset.order_by('fecha_publicacion')
    else:
        queryset = queryset.order_by('-fecha_publicacion')

    paginator = Paginator(queryset, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'articulos/listar.html', {
        'articulos': page_obj.object_list,
        'page_obj': page_obj,
        'categorias': categorias,
        'categoria_seleccionada': categoria_seleccionada,
        'orden': orden,
    })



#VISTA BASADA EN CLASES
class Detalle_Articulo(DetailView):
    
    template_name = 'articulos/detalle.html'
    model = Articulo
    context_object_name = 'articulo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orden = self.request.GET.get('orden', 'reciente')  # valor por defecto 'reciente'
        
        # Obtener los comentarios ordenados - corregimos esta parte
        comentarios = self.object.MisComentarios()  # Asegúrate que MisComentarios es el related_name correcto
        
        # Aplicamos el orden
        if orden == 'antiguo':
            comentarios = comentarios.order_by('creado')
        else:
            comentarios = comentarios.order_by('-creado')
        
        context['comentarios'] = comentarios
        context['es_moderador'] = (
            self.request.user.is_authenticated
            and self.request.user.groups.filter(name='Moderador').exists()
        )
        return context



class Crear_Articulo(soloMod, CreateView):
    model = Articulo
    template_name = 'articulos/crear.html'
    form_class = FormularioCrearArticulo
    success_url = reverse_lazy('articulos:path_listar_articulos')
    


class EditarArticuloView(UpdateView):
    model = Articulo
    form_class = FormularioCrearArticulo
    template_name = 'articulos/editar.html'

    def get_success_url(self):
        return reverse('articulos:path_detalle_articulo', kwargs={'pk': self.object.pk})
    
    



class EliminarArticuloView(DeleteView):
    model = Articulo
    template_name = 'articulos/eliminar.html'
    success_url = reverse_lazy('articulos:path_listar_articulos')
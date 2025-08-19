from django.shortcuts import render
from .models import Categoria
from apps.articulos.models import Articulo
<<<<<<< HEAD
=======
from django.core.paginator import Paginator
>>>>>>> db86a01 (Finalizado)


def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/listar.html', {'categorias': categorias})


def listar_articulos_por_categoria(request, categoria_slug):
    categorias = Categoria.objects.all()
    categoria = Categoria.objects.get(slug=categoria_slug)
<<<<<<< HEAD
    articulos = Articulo.objects.filter(categoria=categoria)
    return render(request, 'articulos/listar.html', {
        'categorias': categorias,
        'articulos': articulos,
        'categoria_actual': categoria
=======
    
    # Obtener parámetro de orden
    orden = request.GET.get('orden', 'reciente')  # 'reciente' por defecto
    
    # Filtrar por categoría
    queryset = Articulo.objects.filter(categoria=categoria)
    
    # Aplicar orden
    if orden == 'antiguo':
        queryset = queryset.order_by('fecha_publicacion')
    else:  # reciente (default)
        queryset = queryset.order_by('-fecha_publicacion')
    
    # Paginación
    paginator = Paginator(queryset, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'articulos/listar.html', {
        'categorias': categorias,
        'articulos': page_obj.object_list,
        'page_obj': page_obj,
        'categoria_seleccionada': categoria,
        'orden': orden,
>>>>>>> db86a01 (Finalizado)
    })

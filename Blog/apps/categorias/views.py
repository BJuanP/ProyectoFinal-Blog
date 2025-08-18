from django.shortcuts import render
from .models import Categoria
from apps.articulos.models import Articulo


def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/listar.html', {'categorias': categorias})


def listar_articulos_por_categoria(request, categoria_slug):
    categorias = Categoria.objects.all()
    categoria = Categoria.objects.get(slug=categoria_slug)
    articulos = Articulo.objects.filter(categoria=categoria)
    return render(request, 'articulos/listar.html', {
        'categorias': categorias,
        'articulos': articulos,
        'categoria_actual': categoria
    })

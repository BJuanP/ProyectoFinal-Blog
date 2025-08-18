from django.urls import path
from . import views

app_name = 'categorias'

urlpatterns = [
    path('listar/', views.listar_categorias, name='listar_categorias'),
    path('<slug:categoria_slug>/articulos/', views.listar_articulos_por_categoria, name='listar_articulos_por_categoria'),
]

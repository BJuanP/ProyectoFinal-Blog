
from django.urls import path
from . import views

app_name = "articulos"

urlpatterns = [
    
    path('Listar', views.Listar_Articulos, name = 'path_listar_articulos'),
    
    path('Crear/', views.Crear_Articulo.as_view(), name = 'path_crear_articulo'),   #Esto es una opcion para crear articulos
    

]
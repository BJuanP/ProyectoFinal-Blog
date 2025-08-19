from django.urls import path
from . import views

app_name = "apps.comentarios"

urlpatterns = [
    path('Agregar/<int:pk>/',views.Comentar, name='path_comentar'),

    path('Eliminar/<int:pk>/',views.Eliminar, name='path_eliminar'),
    path('Confirmar_eliminar/<int:pk>/<int:articulo_pk>/',views.ConfirmarEliminar, name='path_confirmar_eliminar'),
    
    path('Editar/<int:pk>/',views.Editar, name='path_editar'),
    path('Confirmar_editar/<int:pk>/',views.ConfirmarEditar, name='path_confirmar_editar'),
  
]
from django.urls import path
from . import views

app_name = "comentarios"

urlpatterns = [
    path('Agregar/<int:pk>/',views.Comentar, name='path_comentar'),
    path('Eliminar/<int:pk>/',views.Eliminar, name='path_eliminar'),
    path('Confirmar_eliminar/<int:pk>/<int:articulo_pk>/',views.ConfirmarEliminar, name='path_confirmar_eliminar'),
]

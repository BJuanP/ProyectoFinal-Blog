from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Comentario
from articulos.models import Articulo

#@login_required
def Comentar(request, pk):
    articulo = Articulo.objects.get(pk = pk)
    usuario = request.user
    comentario = request.POST.get('comentario', None)

    Comentario.objects.create(texto = comentario, articulo = articulo, usuario = usuario)

    return HttpResponseRedirect(reverse_lazy('articulos:path_detalle_articulo', kwargs={'pk':pk}))


def ConfirmarEliminar(request, pk, articulo_pk):
    comentario = get_object_or_404(Comentario, pk=pk)

    if request.user == comentario.usuario or request.user.is_staff:
        #articulo = comentario.articulo.pk
        comentario.delete()
        messages.success(request, "Comentario eliminado correctamente.")
    else:
        return HttpResponseForbidden("No tienes permiso para eliminar este comentario.")
    
    return HttpResponseRedirect(reverse_lazy('articulos:path_detalle_articulo', kwargs={'pk':articulo_pk}))


#@login_required
def Eliminar(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)

    if request.user != comentario.usuario and not request.user.is_staff:
            #articulo = comentario.articulo.pk
        return HttpResponseForbidden("No tienes permiso para eliminar este comentario.")
         
    return render(request, "comentarios/confirmar_eliminar.html", {'comentario': comentario})

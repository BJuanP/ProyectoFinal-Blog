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


###         CREAR UN COMENTARIO         ###

#@login_required
def Comentar(request, pk):
    articulo = Articulo.objects.get(pk = pk)
    usuario = request.user
    comentario = request.POST.get('comentario', None)
    orden = request.GET.get('orden', '')
    
    Comentario.objects.create(texto = comentario, articulo = articulo, usuario = usuario)

    redirect_url = reverse_lazy('articulos:path_detalle_articulo', kwargs={'pk':pk})
    if orden:
        return HttpResponseRedirect(f'{redirect_url}?orden={orden}')
    return HttpResponseRedirect(redirect_url)


<<<<<<< HEAD
###         ELIMINAR Y CONFIRMAR ELIMINAR           ###


=======

###         ELIMINAR Y CONFIRMAR ELIMINAR           ###


#@login_required
>>>>>>> 584c2698955b2d42985241307c9f5f56030b5796
def ConfirmarEliminar(request, pk, articulo_pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    orden = request.GET.get('orden', '')

    if request.method == 'POST':
        if request.user == comentario.usuario or request.user.is_staff:
            #articulo = comentario.articulo.pk
            comentario.delete()
            messages.success(request, "Comentario eliminado correctamente.")
            redirect_url = reverse_lazy('articulos:path_detalle_articulo', kwargs={'pk':articulo_pk})
            if orden:
                return HttpResponseRedirect(f'{redirect_url}?orden={orden}')
            return HttpResponseRedirect(redirect_url)
        else:
            return HttpResponseForbidden("No tienes permiso para eliminar este comentario.")

		
#@login_required
def Eliminar(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    orden = request.GET.get('orden', '')

    if request.user != comentario.usuario and not request.user.is_staff:
            #articulo = comentario.articulo.pk
        return HttpResponseForbidden("No tienes permiso para eliminar este comentario.")
    contexto = {
        'comentario': comentario, 
        'orden': orden
        }
    return render(request, "comentarios/confirmar_eliminar.html", contexto)



###        EDITAR Y CONFIRMAR EDICIÓN       ###

#@login_required
def Editar (request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    orden = request.GET.get('orden', '')

    if request.user != comentario.usuario and not request.user.is_staff:
        return HttpResponseForbidden("No tienes permiso para editar este comentario.")
    contexto = {
        'comentario': comentario,
        'orden': orden
    }
    return render(request, 'comentarios/confirmar_edicion.html',contexto)

#@login_required
def ConfirmarEditar (request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    orden = request.GET.get('orden', '')
    articulo_pk = comentario.articulo.pk

    if request.user != comentario.usuario and not request.user.is_staff:
        return HttpResponseForbidden("No tienes permiso para editar este comentario.")
    
    if request.method == 'POST':
        nuevo_texto = request.POST.get('comentario', None)
        if nuevo_texto:
            comentario.texto = nuevo_texto
            comentario.save()
            messages.success(request, "Comentario actualizado correctamente.")
            redirect_url = reverse_lazy('articulos:path_detalle_articulo', kwargs={'pk':articulo_pk})
            if orden:
                return HttpResponseRedirect(f'{redirect_url}?orden={orden}')
            return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseForbidden("No tienes permiso para eliminar este comentario.")

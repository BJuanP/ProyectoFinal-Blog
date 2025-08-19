from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .models import Comentario
from apps.articulos.models import Articulo
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponseForbidden
from django.contrib import messages

# Función auxiliar para verificar si es moderador
def es_moderador(user):
    return user.groups.filter(name='Moderador').exists()

@login_required
def Comentar(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    usuario = request.user
    comentario = request.POST.get('comentario', None)
    orden = request.GET.get('orden', '')

    if comentario:  # Evitamos guardar vacío
        Comentario.objects.create(texto=comentario, articulo=articulo, usuario=usuario)

    redirect_url = reverse_lazy('articulos:path_detalle_articulo', kwargs={'pk': pk})
    if orden:
        return HttpResponseRedirect(f'{redirect_url}?orden={orden}')
    return HttpResponseRedirect(redirect_url)

@login_required
def ConfirmarEliminar(request, pk, articulo_pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    orden = request.GET.get('orden', '')

    if request.method == 'POST':
        if request.user == comentario.usuario or es_moderador(request.user):
            comentario.delete()
            messages.success(request, "Comentario eliminado correctamente.")
            redirect_url = reverse_lazy('articulos:path_detalle_articulo', kwargs={'pk': articulo_pk})
            if orden:
                return HttpResponseRedirect(f'{redirect_url}?orden={orden}')
            return HttpResponseRedirect(redirect_url)
        else:
            return HttpResponseForbidden("No tienes permiso para eliminar este comentario. <a href='javascript:window.history.back();'>Volver</a>")

@login_required
def Eliminar(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    orden = request.GET.get('orden', '')

    if request.user != comentario.usuario and not es_moderador(request.user):
        return HttpResponseForbidden("No tienes permiso para eliminar este comentario. <a href='javascript:window.history.back();'>Volver</a>")

    contexto = {
        'comentario': comentario,
        'orden': orden,
    }
    return render(request, "comentarios/confirmar_eliminar.html", contexto)

@login_required
def Editar(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    orden = request.GET.get('orden', '')

    if request.user != comentario.usuario and not es_moderador(request.user):
        return HttpResponseForbidden("No tienes permiso para editar este comentario. <a href='javascript:window.history.back();'>Volver</a>")

    contexto = {
        'comentario': comentario,
        'orden': orden,
    }
    return render(request, 'comentarios/confirmar_edicion.html', contexto)

@login_required
def ConfirmarEditar(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    orden = request.GET.get('orden', '')
    articulo_pk = comentario.articulo.pk

    if request.user != comentario.usuario and not es_moderador(request.user):
        return HttpResponseForbidden("No tienes permiso para editar este comentario. <a href='javascript:window.history.back();'>Volver</a>")

    if request.method == 'POST':
        nuevo_texto = request.POST.get('comentario', None)
        if nuevo_texto:
            comentario.texto = nuevo_texto
            comentario.save()
            messages.success(request, "Comentario actualizado correctamente.")
            redirect_url = reverse_lazy('articulos:path_detalle_articulo', kwargs={'pk': articulo_pk})
            if orden:
                return HttpResponseRedirect(f'{redirect_url}?orden={orden}')
            return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseForbidden("No tienes permiso para editar este comentario. <a href='javascript:window.history.back();'>Volver</a>")

from django.shortcuts import render, HttpResponseRedirect
from .models import Comentario
from articulos.models import Articulo
from django.urls import reverse_lazy

def Comentar(request, pk):
    articulo = Articulo.objects.get(pk = pk)
    usuario = request.user
    comentario = request.POST.get('comentario', None)

    Comentario.objects.create(texto = comentario, articulo = articulo, usuario = usuario)

    return HttpResponseRedirect(reverse_lazy('articulos:path_detalle_articulo', kwargs={'pk':pk}))




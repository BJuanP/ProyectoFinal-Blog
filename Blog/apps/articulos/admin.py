
from django.contrib import admin

from .models import Articulo

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ("nombre", "creado", "destacado")
    list_filter = ("destacado", "creado")
    search_fields = ("nombre", "descripcion")
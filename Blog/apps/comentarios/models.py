from django.db import models
from articulos.models import Articulo
from django.contrib.auth.models import User


class Comentario(models.Model):
    creado = models.DateTimeField(auto_now_add= True)
    modificado = models.DateTimeField(auto_now=True)
    texto = models.TextField(max_length=600)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.usuario} comentó en {self.articulo}."
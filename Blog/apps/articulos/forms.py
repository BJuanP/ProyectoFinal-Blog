
from django import forms 

from .models import Articulo


class FormularioCrearArticulo(forms.ModelForm): 
    
    class Meta: 
        model = Articulo                #Este sería el modelo. Se lo pasamos
        fields = ('nombre','descripcion','imagen')         #Acá le decimos qué campos queremos que aparezcan
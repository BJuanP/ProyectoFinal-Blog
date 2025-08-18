
from django import forms 

from .models import Articulo


class FormularioCrearArticulo(forms.ModelForm): 
    
    class Meta: 
        model = Articulo                #Este sería el modelo. Se lo pasamos
        fields = ('nombre', 'categoria', 'resumen', 'cuerpo', 'imagen')         # Campos a mostrar en el formulario
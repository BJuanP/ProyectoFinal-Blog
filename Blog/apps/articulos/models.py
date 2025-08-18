from django.db import models
from apps.categorias.models import Categoria
from apps.usuario.models import Usuario

# Create your models here.

class Articulo(models.Model):    #Son clases en Python que se van a relacionar con las tablas.
    
    creado = models.DateTimeField(
        auto_now_add=True
    )
    
    modificado = models.DateTimeField(     #Estos son 2 atributos que van a actualizar la fecha cada vez que se crea y se modifica algo     
        auto_now_add=True
    )
    
    #Djgango me crea por defecto una clave primaria, a menos que nosotros querramos crearla.
    nombre = models.CharField(max_length=100)   #En este tipo de dato es obligatorio poner la longitud máxima
    resumen = models.CharField(max_length=500, null=True, help_text="Resumen breve que se mostrará en los listados.")
    cuerpo = models.TextField(max_length=4000, null=True, help_text="Cuerpo completo del artículo, solo visible en el detalle.")
    imagen = models.ImageField(upload_to = 'articulos')     #Esto significa que las imagenes van a estar en una carpeta llamada articulos
    autor = models.ForeignKey(Usuario, on_delete=models.SET_DEFAULT, default=1)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_DEFAULT, default=1) #ID 1 crearemos categoria "general"
    
    destacado = models.BooleanField(
        default=False,
        help_text="Marcar esta casilla para que el articulo sea el destacado en el home."
    )
    
    def __str__(self):   #Esto es para que cuando yo vea un producto, lo vea a través del nombre
        
        return self.nombre
    
    def MisComentarios(self):
        return self.comentario_set.all()
    
    
    def save(self, *args, **kwargs):
        super_guardar = super().save
        if self.destacado:
            Articulo.objects.exclude(pk=self.pk).update(destacado=False)
        super_guardar(*args, **kwargs)
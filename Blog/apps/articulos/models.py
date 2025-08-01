
from django.db import models

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
    descripcion = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to = 'articulos')     #Esto significa que las imagenes van a estar en una carpeta llamada articulos
    
    def __str__(self):   #Esto es para que cuando yo vea un producto, lo vea a través del nombre
        
        return self.nombre
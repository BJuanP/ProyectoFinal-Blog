


from django.contrib import admin
from django.urls import path, include

from . import views

from django.conf.urls.static import static     #Estas 2 importaciones son para poder ver las imágenes
from django.conf import settings

from django.contrib.auth import views as auth



urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.Home, name = "path_home"),
    
    path('Articulos/', include('articulos.urls')), 
    path('Comentarios/', include('comentarios.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   


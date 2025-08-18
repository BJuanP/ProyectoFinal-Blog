# /var/www/.../mysite_wsgi.py   (o el WSGI file que te muestra PythonAnywhere)
import os, sys

# 1) Ruta al directorio raíz del proyecto (donde está manage.py)
project_root = '/home/BJuanP/ProyectoFinal-Blog/Blog'      # <-- CAMBIÁ esto si tu carpeta difiere
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# 2) (Opcional) Agregar también el parent si hace falta
parent = '/home/BJuanP/ProyectoFinal-Blog'                 # <-- CAMBIÁ si difiere
if parent not in sys.path:
    sys.path.insert(0, parent)

# 3) Módulo de settings correcto para producción
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Blog.settings.production')

# 4) Crear la aplicación WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

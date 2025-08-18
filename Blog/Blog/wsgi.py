import os
import sys

path = '/home/carrito/carrito' #Donde esta el manage.py
if path not in sys.path:
    sys.path.insert(0, path)

#Configuracion de modulo settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings.production')

#Cargamos la app WSGI

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

application = StaticFilesHandler(get_wsgi_application())
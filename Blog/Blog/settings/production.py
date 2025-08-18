from .base import *

DEBUG = False

ALLOWED_HOSTS = ['<BJuanP>.pythonanywhere.com']

CSRF_TRUSTED_ORIGINS = ['https://<BJuanP>.pythonanywhere.com']



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'usuario$basedatos',
        'USER': 'usuario',
        'PASSWORD': 'contraseña',
        'HOST': 'usuario.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}
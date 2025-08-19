<<<<<<< HEAD


from .base import *
import os

DEBUG = False

ALLOWED_HOSTS = ['BJuanP.pythonanywhere.com']
CSRF_TRUSTED_ORIGINS = ['https://BJuanP.pythonanywhere.com']


DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.mysql',
         'NAME': 'BJuanP$blogdb',
         'USER': 'BJuanP',
         'PASSWORD': '***',
         'HOST': 'BJuanP.mysql.pythonanywhere-services.com',
         'PORT': '3306',
         'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"},
     }
 }

# Email real si lo necesitás (sino, dejá consola)
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# DEFAULT_FROM_EMAIL = "no-reply@tudominio"
=======
from .base import * 

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR_STR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR_STR, 'media')

DEBUG = False

ALLOWED_HOSTS = ['inforgrupo4.pythonanywhere.com']

SECRET_KEY = ''


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'inforgrupo4$infogrupo4', 
        'USER': 'inforgrupo4',
        'PASSWORD': 'Proyecto.Blog4',
        'HOST': 'inforgrupo4.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}
>>>>>>> db86a01 (Finalizado)

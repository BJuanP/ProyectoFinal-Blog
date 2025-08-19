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

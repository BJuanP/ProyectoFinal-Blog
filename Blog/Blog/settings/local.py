from .base import *

DEBUG = True
SECRET_KEY = 'django-insecure-7)!m2=bj#@&w_k0te_8+lpr8j6o44uf1+*cws3vkgvzvg%$g0q'
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


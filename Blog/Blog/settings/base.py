<<<<<<< HEAD

from pathlib import Path
import sys, os

# Si este archivo está en Blog/settings/base.py:
BASE_DIR = Path(__file__).resolve().parent.parent.parent  # apunta a carpeta Blog (donde está manage.py)

# Que tus apps estén importables como 'apps.*'
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'insegura-dev-solo-local')

DEBUG = False  # por defecto OFF; cada entorno lo ajusta

ALLOWED_HOSTS = []  # cada entorno lo ajusta

AUTH_USER_MODEL = 'usuario.Usuario'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'

=======
from pathlib import Path
import sys
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
BASE_DIR_STR = str(BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))


AUTH_USER_MODEL = 'usuario.Usuario'

LOGIN_REDIRECT_URL = '/'
# Redirección al formulario de login
LOGIN_URL = '/login/'




# Application definition

>>>>>>> db86a01 (Finalizado)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'apps.usuario',
    'apps.articulos',
    'apps.comentarios',
    'apps.categorias',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
<<<<<<< HEAD
        'DIRS': [BASE_DIR / 'templates'],
=======
        'DIRS': [BASE_DIR / 'templates'],  # plantillas globales
>>>>>>> db86a01 (Finalizado)
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.categorias.context_processors.categorias_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'Blog.wsgi.application'

<<<<<<< HEAD
# Base de datos: que cada entorno la defina; aquí un default mínimo
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'es-ar'
TIME_ZONE = 'America/Argentina/Buenos_Aires'
USE_I18N = True
USE_TZ = True

# Estáticos y media
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'   # destino de collectstatic en producción
STATICFILES_DIRS = [BASE_DIR / 'static'] # solo si existe esa carpeta

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email (por defecto consola; prod lo puede sobrescribir)
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FROM_EMAIL = "no-reply@example.local"
CONTACT_RECIPIENT_EMAIL = "informacion@example.tld"
=======

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# -----------------------
# INTERNACIONALIZACIÓN
# -----------------------

LANGUAGE_CODE = 'es-ar'
TIME_ZONE = 'America/Argentina/Buenos_Aires'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# -----------------------
# ARCHIVOS ESTÁTICOS Y MEDIA
# -----------------------

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR_STR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR_STR, 'media')



# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FROM_EMAIL = "no-reply@techvision.local"
CONTACT_RECIPIENT_EMAIL = "informacion@untitled.tld"
>>>>>>> db86a01 (Finalizado)

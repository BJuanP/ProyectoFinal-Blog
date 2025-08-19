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
        'DIRS': [BASE_DIR / 'templates'],  # plantillas globales
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

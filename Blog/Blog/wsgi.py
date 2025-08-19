import sys
import os

path = '/home/inforgrupo4/ProyectoFinal-Blog-main/Blog'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'Blog.settings.production'


from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler


application = StaticFilesHandler(get_wsgi_application())

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'react_django_web_33425.settings')

application = get_wsgi_application()

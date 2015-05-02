import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webconf.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

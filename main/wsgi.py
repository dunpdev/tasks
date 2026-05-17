"""
WSGI config for main project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Use production settings if RAILWAY_ENVIRONMENT_NAME or PRODUCTION_ENV is set
if os.environ.get("RAILWAY_ENVIRONMENT_NAME") or os.environ.get("PRODUCTION_ENV"):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings_prod")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")

application = get_wsgi_application()

"""
WSGI config for enterprise_dev project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'enterprise_dev.settings')
profile = os.environ.get("DJANGO_SETTINGS_MODULE", "develop")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"enterprise_dev.setting.{profile}")

application = get_wsgi_application()

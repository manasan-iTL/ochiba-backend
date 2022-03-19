"""
WSGI config for BookmarkShareApp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

#.envから環境変数を読み込む
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BookmarkShareApp.settings.development')

application = get_wsgi_application()

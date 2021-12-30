"""
ASGI config for BookmarkShareApp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
import dotenv

from django.core.asgi import get_asgi_application

#.envから環境変数を読み込む
dotenv.load_dotenv()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BookmarkShareApp.settings.development')

application = get_asgi_application()

from .base import *
import os

DEBUG = True

SECRET_KEY = 'django-insecure-j#pug!n(u6@qh#t1pdh-b-*g5emnw_^j(lw!o)i*mh!^s1+*0e'

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# デフォルトのメール送信元を設定
DEFAULT_FROM_EMAIL = 'admin@example.com'
#コンソール上にメッセージを表示
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

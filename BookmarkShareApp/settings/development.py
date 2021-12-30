from .base import *
import os

DEBUG = True

SECRET_KEY = 'django-insecure-j#pug!n(u6@qh#t1pdh-b-*g5emnw_^j(lw!o)i*mh!^s1+*0e'

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bookmarkshares',
        'USER': 'postgres',
        'PASSWORD': '1531',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# デフォルトのメール送信元を設定
DEFAULT_FROM_EMAIL = 'admin@example.com'
#コンソール上にメッセージを表示
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

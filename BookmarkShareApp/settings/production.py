from BookmarkShareApp.settings.development import DEBUG
from .base import *
import os

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'name',
        'USER': 'user',
        'PASSWORD': '',
        'HOST': 'host',
        'PORT': '',
    }
}

# メール送信の設定 Gmailを使う。
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'ochiba.customer@gmail.com'
EMAIL_HOST_PASSWORD = 'ggyhexmgtcdhvdzg'
EMAIL_USE_TLS = True
from BookmarkShareApp.settings.development import DEBUG
from .base import *
import os

DEBUG = True

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd5effl8gu4qdrl',
        'USER': 'tjugxvgxgcfork',
        'PASSWORD': '809340a085bb778e2b12b22bc597e1ad8448d0bca981c2ce6035aaa0d1e188ed',
        'HOST': 'ec2-3-218-158-102.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

# メール送信の設定 Gmailを使う。
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'ochiba.customer@gmail.com'
EMAIL_HOST_PASSWORD = 'ggyhexmgtcdhvdzg'
EMAIL_USE_TLS = True



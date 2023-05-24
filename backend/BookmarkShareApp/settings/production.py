from .base import *
import os
import dj_database_url

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['ochiba.fly.dev']
CSRF_TRUSTED_ORIGINS = ['https://ochiba.fly.dev', 'http://ochiba.fly.dev'] 

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
'default': dj_database_url.config()
}

# メール送信の設定 Gmailを使う。
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_SENDER = f"ブックマークシェアアプリochiba {EMAIL_HOST_USER}>"
EMAIL_USE_TLS = True


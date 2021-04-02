from .base import *
from decouple import config

ALLOWED_HOST = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '3jo',
        'USER': '3jo',
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': '192.168.99.100',
        'PORT': '33066'
    }
}
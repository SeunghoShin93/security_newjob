from .base import *

ALLOWED_HOST = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'root',
        'PASSWORD': 'passwd',
        'HOST': 'db',
        'PORT': '3306'
    }
}
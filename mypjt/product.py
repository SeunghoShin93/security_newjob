from .settings import *

ALLOWED_HOST = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'root',
        'PASSWORD': 'django',
        'PORT': '3306',
        'HOST': 'localhost'
    }
}
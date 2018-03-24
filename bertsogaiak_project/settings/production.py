from .base import *

DEBUG = False
ALLOWED_HOSTS = ['bertsogaiak.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'PORT': '',
    }
}

STATIC_URL = 'https://bertsogaiak.herokuapp.com/static/'
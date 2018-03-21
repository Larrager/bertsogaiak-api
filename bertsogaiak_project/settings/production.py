from .base import *

DEBUG = False
ALLOWED_HOSTS = ['dfb-bloga.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_URL = 'https://dfb-bloga.herokuapp.com/static/'
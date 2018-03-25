from .base import *
import dj_database_url

DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES['default'] = dj_database_url.parse(os.environ.get('DATABASE_URL'))

STATIC_URL = '/static/'

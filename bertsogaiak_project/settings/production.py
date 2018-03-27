from .base import *
import dj_database_url

DEBUG = False
ALLOWED_HOSTS = ['bertsogaiak.herokuapp.com']

DATABASES['default'] = dj_database_url.parse(os.environ.get('DATABASE_URL'))

STATIC_URL = 'https://bertsogaiak.herokuapp.com/static/'

CORS_ORIGIN_ALLOW_ALL = True
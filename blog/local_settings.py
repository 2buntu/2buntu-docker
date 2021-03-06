"""
Local settings for 2buntu are automatically gathered from environment variables
set by Docker when the container is linked with others.
"""

from os import environ, makedirs, path
from uuid import uuid4

# Assume DEBUG & READ_ONLY are False unless told otherwise
DEBUG = TEMPLATE_DEBUG = bool(environ.get('DEBUG', False))
READ_ONLY = bool(environ.get('READ_ONLY', False))

# Assign environment variables to really short names to simplify the code
psqlh = environ.get('POSTGRES_PORT_5432_TCP_ADDR', None)
psqlp = environ.get('POSTGRES_PORT_5432_TCP_PORT', None)
pfh = environ.get('POSTFIX_PORT_25_TCP_ADDR', None)
pfp = environ.get('POSTFIX_PORT_25_TCP_PORT', None)
redish = environ.get('REDIS_PORT_6379_TCP_ADDR', None)
redisp = environ.get('REDIS_PORT_6379_TCP_PORT', None)

# Use PostgreSQL info if provided, otherwise use an in-memory SQLite database
if psqlh and psqlp:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'postgres',
            'USER': 'postgres',
            'HOST': psqlh,
            'PORT': psqlp,
        },
    }
else:
    # Ensure that /data/db exists
    if not path.exists('/data/db'):
        makedirs('/data/db')
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': '/data/db/twobuntu.sqlite3',
        }
    }

# Use SMTP settings if provided, otherwise, use the console
if pfh and pfp:
    EMAIL_HOST = pfh
    EMAIL_PORT = pfp
else:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Activate the Redis cache if the appropriate settings were provided
if redish and redisp:
    CACHES = {
        'default': {
            'BACKEND': 'redis_cache.cache.RedisCache',
            'LOCATION': '%s:%s:0' % (redish, redisp),
        },
    }

MEDIA_URL = '/media/'
STATIC_URL = '/static/'

# These are stored on a separate volume
MEDIA_ROOT = '/data/www/media'
STATIC_ROOT = '/data/www/static'

RECAPTCHA_SITE_KEY = environ.get('RECAPTCHA_SITE_KEY', '')
RECAPTCHA_SECRET_KEY = environ.get('RECAPTCHA_SECRET_KEY', '')

# If you are using Twitter integration, then you will need to supply values for these settings
TWITTER = {
    'token': environ.get('TWITTER_TOKEN', ''),
    'token_secret': environ.get('TWITTER_TOKEN_SECRET', ''),
    'consumer_key': environ.get('TWITTER_CONSUMER_KEY', ''),
    'consumer_secret': environ.get('TWITTER_CONSUMER_SECRET', ''),
}

# Generate a secret key if one was not provided
SECRET_KEY = environ.get('SECRET_KEY', uuid4().hex)

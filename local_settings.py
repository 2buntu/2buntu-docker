"""
Local settings for 2buntu are automatically gathered from environment variables
set by Docker when the container is linked with others.
"""

from os import environ, makedirs, path
from uuid import uuid4

# Assume production unless told otherwise
DEBUG = TEMPLATE_DEBUG = bool(environ.get('DEBUG', False))
SERVER_EMAIL = DEFAULT_FROM_EMAIL = '2buntu <donotreply@2buntu.com>'

# Assign environment variables to really short names to simplify the code
psqlh = environ.get('POSTGRES_PORT_5432_TCP_ADDR', None)
psqlp = environ.get('POSTGRES_PORT_5432_TCP_PORT', None)
redish = environ.get('REDIS_PORT_6379_TCP_ADDR', None)
redisp = environ.get('REDIS_PORT_6379_TCP_PORT', None)

# Ensure that /data/db exists
# (normally a race condition, but doesn't matter in this case)
if not path.exists('/data/db'):
    makedirs('/data/db')

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
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': '/data/db/twobuntu.sqlite3',
        }
    }

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

RECAPTCHA_PUBLIC_KEY = environ.get('RECAPTCHA_PUBLIC_KEY', '')
RECAPTCHA_PRIVATE_KEY = environ.get('RECAPTCHA_PRIVATE_KEY', '')

# If you are using Twitter integration, then you will need to supply values for these settings
TWITTER = {
    'token': environ.get('TWITTER_TOKEN', ''),
    'token_secret': environ.get('TWITTER_TOKEN_SECRET', ''),
    'consumer_key': environ.get('TWITTER_CONSUMER_KEY', ''),
    'consumer_secret': environ.get('TWITTER_CONSUMER_SECRET', ''),
}

# Generate a secret key if one was not provided
SECRET_KEY = environ.get('SECRET_KEY', uuid4().hex)

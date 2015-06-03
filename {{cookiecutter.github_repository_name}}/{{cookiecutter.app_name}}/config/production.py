import os
import urlparse
from .common import Common
from configurations import values


class Production(Common):

    # Honor the 'X-Forwarded-Proto' header for request.is_secure()
    # https://devcenter.heroku.com/articles/getting-started-with-django
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    INSTALLED_APPS = Common.INSTALLED_APPS
    SECRET_KEY = values.SecretValue()

    # django-secure
    # http://django-secure.readthedocs.org/en/v0.1.2/settings.html
    INSTALLED_APPS += ("djangosecure", )

    SECURE_HSTS_SECONDS = 60
    SECURE_HSTS_INCLUDE_SUBDOMAINS = values.BooleanValue(True)
    SECURE_FRAME_DENY = values.BooleanValue(True)
    SECURE_CONTENT_TYPE_NOSNIFF = values.BooleanValue(True)
    SECURE_BROWSER_XSS_FILTER = values.BooleanValue(True)
    SESSION_COOKIE_SECURE = values.BooleanValue(False)
    SESSION_COOKIE_HTTPONLY = values.BooleanValue(True)
    SECURE_SSL_REDIRECT = values.BooleanValue(True)

    # Site
    # https://docs.djangoproject.com/en/1.6/ref/settings/#allowed-hosts
    ALLOWED_HOSTS = ["*"]

    INSTALLED_APPS += ("gunicorn", )

    # Template
    # https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )),
    )

    # Caching
    redis_url = urlparse.urlparse(os.environ.get('REDISTOGO_URL', 'redis://localhost:6379'))

    CACHES = {
        'default': {
            'BACKEND': 'redis_cache.RedisCache',
            'LOCATION': '{}:{}'.format(redis_url.hostname, redis_url.port),
            'OPTIONS': {
                'DB': 0,
                'PASSWORD': redis_url.password,
                'PARSER_CLASS': 'redis.connection.HiredisParser',
                'CONNECTION_POOL_CLASS': 'redis.BlockingConnectionPool',
                'CONNECTION_POOL_CLASS_KWARGS': {
                    'max_connections': 50,
                    'timeout': 20,
                }
            }
        }
    }

    # Django RQ production settings
    RQ_QUEUES = {
        'default': {
            'URL': os.getenv('REDISTOGO_URL', 'redis://localhost:6379'),
            'DB': 0,
            'DEFAULT_TIMEOUT': 500,
        },
    }

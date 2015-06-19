import os
from .common import Common
from configurations import values


class Local(Common):

    DEBUG = values.BooleanValue(True)
    TEMPLATE_DEBUG = DEBUG

    # Testing
    INSTALLED_APPS = Common.INSTALLED_APPS
    INSTALLED_APPS += ('django_nose',)
    TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
    NOSE_ARGS = [
        '{{cookiecutter.app_name}}',
        '--logging-clear-handlers',
        '--with-coverage',
        '--with-progressive',
        '--cover-package={{cookiecutter.app_name}}'
    ]

    # Mail
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025
    EMAIL_BACKEND = values.Value('django.core.mail.backends.console.EmailBackend')

    # Django RQ local settings
    RQ_QUEUES = {
        'default': {
            'URL': os.getenv('REDISTOGO_URL', 'redis://localhost:6379'),
            'DB': 0,
            'DEFAULT_TIMEOUT': 500,
        },
    }

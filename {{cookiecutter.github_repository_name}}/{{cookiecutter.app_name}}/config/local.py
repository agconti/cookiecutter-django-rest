import os
from .common import Common
from configurations import values

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Local(Common):

    DEBUG = values.BooleanValue(True)
    for config in Common.TEMPLATES:
        config['OPTIONS']['debug'] = DEBUG

    # Testing
    INSTALLED_APPS = Common.INSTALLED_APPS
    INSTALLED_APPS += ('django_nose',)
    TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
    NOSE_ARGS = [
        BASE_DIR,
        '-s',
        '--nologcapture',
        '--with-coverage',
        '--with-progressive',
        '--cover-package={}'.format(BASE_DIR)
    ]

    # Mail
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025
    EMAIL_BACKEND = values.Value('django.core.mail.backends.console.EmailBackend')

    # Vesitle Image Field settings
    VERSATILEIMAGEFIELD_SETTINGS = Common.VERSATILEIMAGEFIELD_SETTINGS
    VERSATILEIMAGEFIELD_SETTINGS['create_images_on_demand'] = True

    # Django RQ local settings
    RQ_QUEUES = {
        'default': {
            'URL': os.getenv('REDISTOGO_URL', 'redis://localhost:6379'),
            'DB': 0,
            'DEFAULT_TIMEOUT': 500,
        },
    }

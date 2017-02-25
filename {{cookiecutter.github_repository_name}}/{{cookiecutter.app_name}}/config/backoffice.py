 
from .common import Common
 
from .common import Common
from .local import Local

class Backoffice(Common):

    INSTALLED_APPS = Common.INSTALLED_APPS
    MIDDLEWARE = Common.MIDDLEWARE
    DEBUG = Local.DEBUG
    RQ_QUEUES = Local.RQ_QUEUES

    INSTALLED_APPS += (
        'django.contrib.admin',
        'django.contrib.sessions',
        'django.contrib.messages',
    )



    MIDDLEWARE += (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    )

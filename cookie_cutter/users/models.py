from __future__ import unicode_literals

# from django.db import models
# from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def __unicode__(self):
        return self.username

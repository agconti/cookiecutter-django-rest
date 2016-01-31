from __future__ import unicode_literals

# from django.db import models
# from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractUser


@python_2_unicode_compatible
class User(AbstractUser):

    def __str__(self):
        return self.username

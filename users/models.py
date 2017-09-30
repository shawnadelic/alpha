# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Placeholder for a custom user model.

    If not included in initial migration of database, will
    be more difficult to change from the default user model
    later.
    """
    pass

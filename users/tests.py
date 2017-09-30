# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from users.models import User


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(
            username='Einstein',
            email='alberteinstein@gmail.com',
            password='jdflkk32$@#42k3j',
            first_name='Albert',
            last_name='Einstein'
        )

    def test_users_exist(self):
        assert User.objects.first().username == 'Einstein'

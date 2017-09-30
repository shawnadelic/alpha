# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from pages.models import Page


class PageTestCase(TestCase):
    def setUp(self):
        Page.objects.create(
            path='0002',
            depth=1,
            slug='home',
            title='Home Page',
        )

    def test_page_exists(self):
        assert Page.objects.first().title == 'Home Page'

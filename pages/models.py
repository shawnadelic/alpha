# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from wagtail.wagtailcore.models import Page as WagtailPage
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel


class Page(WagtailPage):
    body = RichTextField(blank=True)

    content_panels = WagtailPage.content_panels + [
        FieldPanel('body', classname='full')
    ]

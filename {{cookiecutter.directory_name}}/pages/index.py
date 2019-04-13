# -*- coding: utf-8 -*-
from optimus.pages.views.base import PageViewBase
from optimus.conf.registry import settings


class Index(PageViewBase):
    """
    Default index page
    """
    title = "My project"
    template_name = "index.html"
    destination = "index_{language_code}.html"

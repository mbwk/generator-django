# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'', include('harlo.urls', namespace='blop')),
    # Root URL
    url(r'^/?$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^account/', include('accounts.urls', namespace='account')),
)

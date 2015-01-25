# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^m/', include('cvpvcBlog.apps.mini_url.urls', namespace='miniurl')),
    url(r'^', include('cvpvcBlog.apps.article.urls', namespace='blog')),
)
# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from fests.views import IndexView, ContentView, Post1View, Post2View, YouView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',IndexView.as_view(), name='home'),
    url(r'^content/',ContentView.as_view(),name='content'),
    url(r'^post1/', Post1View.as_view(),name='post1'),
    url(r'^post2/', Post2View.as_view(),name='post2'),
    url(r'^you/', YouView.as_view(),name='you'),
]
# -*- coding: UTF-8 -*-
__author__ = 'bespontoff'

from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.JokeListView.as_view(), name='index'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^vote/(?P<joke_id>[0-9]+)/(?P<grade>[1-5])/$', views.vote, name='vote'),
    url(r'^loadjokes/$', views.load_jokes, name='loadjokes'),
    url(r'^login/$', auth_views.login),

]
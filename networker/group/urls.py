""" user app URL Configuration """

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.listing_group, name='listing_group'),
]

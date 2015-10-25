""" user app URL Configuration """

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.listing_group, name='listing_group'),
    url(r'^test/', 'group.views.listing_user_groups', name='listing_user_groups'),
]

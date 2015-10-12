from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.user_listing, name='user_listing'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.user_list, name='user_list'),
    url(r'^profile', views.user_new, name='user_new'),
    url(r'^profile/(?P<pk>[0-9]+)/edit/$', views.user_edit, name='user_edit')
]
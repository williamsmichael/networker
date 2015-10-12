from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.user_listing, name='user_listing'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.user_detail, name='user_detail'),
    url(r'^detail/main/(?P<pk>[0-9]+)/$', views.user_detail_main, name='user_detail_main'),
    # url(r'^detail/main/(?P<pk>[0-9]+)/edit/$', views.user_detail_main_edit, name='user_detail_main_edit'),


    url(r'^profile', views.user_new, name='user_new'),
    url(r'^profile/(?P<pk>[0-9]+)/edit/$', views.user_edit, name='user_edit')
]
from django.conf.urls import patterns, url

from . import views

urlpatterns = [
    # url(r'^$', views.user_listing, name='user_listing'),
    # url(r'^detail/(?P<pk>[0-9]+)/$', views.user_detail, name='user_detail'),
    # url(r'^edit/(?P<pk>\d+)/$', views.UpdateContactView.as_view(),
    # 	name='contacts-edit',),
    # url(r'^detail/main/(?P<pk>[0-9]+)/$', views.user_detail_main, name='user_detail_main'),
    # url(r'^detail/main/(?P<pk>[0-9]+)/edit/$', views.user_detail_main_edit, name='user_detail_main_edit'),

    url(r'^$', views.UserListing.as_view(), name='listing'),
    url(r'^create/', views.UserCreate.as_view(), name='create'),
    # url(r'^(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/$', views.UserDetail, name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.UserUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.UserDelete.as_view(), name='delete'),


    url(r'^profile', views.user_new, name='user_new'),
    url(r'^profile/(?P<pk>[0-9]+)/edit/$', views.user_edit, name='user_edit')
]
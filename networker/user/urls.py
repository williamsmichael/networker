from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.user_list, name='user_list'),
    url(r'^profile', views.user_profile, name='user_profile'),
]
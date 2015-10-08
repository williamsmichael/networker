from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.user_list, name='user_list'),
    url(r'^register/$', views.register, name='register'),
    # url(r'email/(?P<pk>\d+)/$', views.email_list),
]
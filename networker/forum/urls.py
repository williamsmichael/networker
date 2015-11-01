""" group app URL Configuration """

from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [

	# ----------------------------------------------------------------listview
    # url(r'^$', 'forum.views.forum', name='forum'),
    # # url(r'^(\d+)/$', 'forum'),
    # # url(r'^thread/(\d+)/$', 'thread'),

	url(r'^$', 'forum.views.forum_list', name='forum_list'),
	url(r'^(\d+)/$', views.thread_list, name='thread_list'),
	url(r'^thread/(\d+)/$', views.thread, name='thread'),

]
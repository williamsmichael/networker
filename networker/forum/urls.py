""" group app URL Configuration """

from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [

	# ----------------------------------------------------------------listview
    # url(r'^$', 'forum.views.forum', name='forum'),
    # # url(r'^(\d+)/$', 'forum'),
    # # url(r'^thread/(\d+)/$', 'thread'),

	url(r'^$', 'forum.views.main', name='main'),
	# url(r'^forum/(\d+)/$', forum.views.forum, name='forum'),
	# url(r'^thread/(\d+)/$', forum.views.thread, 'thread'),

]
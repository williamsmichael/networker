""" group app URL Configuration """

from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [

    # --------------------------------------------------------------updateview
    url(r'^(?P<forum>[-\w]+)/(?P<thread>[-\w]+)/update$', login_required(views.ThreadUpdate.as_view(
        template_name='forum/create_update_form.html')), name='update_thread'),

	# ----------------------------------------------------------------listview
	url(r'^$', 'forum.views.forum_list', name='forum_list'),
	url(r'^(?P<thread>[-\w]+)/(?P<post>[-\w]+)', 'forum.views.post_list', name='post_list'),
	url(r'^(?P<thread>[-\w]+)/', 'forum.views.thread_list', name='thread_list'),

    # --------------------------------------------------------------createview
    # url(r'^(\d+)/create$', login_required(views.CreateThread.as_view(
        # template_name='forum/thread_form.html')), name='create_thread'),


    # ------------------------------------------------------------------unused
	# url(r'^post/(new_thread|reply)/(\d+)/$', views.post, name='post'),
	# url(r'^new_thread/(\d+)/$', views.new_thread, name='new_thread'),
	# url(r'^reply/(\d+)/$', views.reply, name='reply'),
	# url(r'^(?P<pk>[0-9]+)/topic', login_required(views.ThreadListing.as_view(template_name='forum/thread_list.html')), name='thread_list'),
	# url(r'^(?P<pk>[0-9]+)/topics', views.thread_list, name='thread_list'),
	# url(r'^(?P<pk>[0-9]+)/topic/(?P<thread>[0-9]+)/posts', views.post_list, name='post_list'),
    # url(r'^$', 'forum.views.forum', name='forum'),
    # # url(r'^(\d+)/$', 'forum'),
    # # url(r'^thread/(\d+)/$', 'thread'),
	# url(r'^(?P<pk>[0-9]+)/topic/(?P<thread>[0-9]+)/post', login_required(views.PostListing.as_view(template_name='forum/post_list.html')), name='post_list'),


]